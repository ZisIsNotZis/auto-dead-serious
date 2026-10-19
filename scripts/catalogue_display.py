#!/usr/bin/env python3
"""Fill each project's display text and apply an audit re-score, in the authored source file.

`--derive` writes the display block for any project that lacks one, composed only from facts
already in assessments.json. `--apply FILE` folds an audit JSON in: it replaces the numeric
judgements it covers and appends a dated-by-cause line to the rating trajectory. Both are
idempotent enough to re-run; --apply keeps the previous estimate in the trajectory.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs/result/catalogue-redesign/assessments.json"
PRIVATE = {"colleague_private", "tutor_private", "resume_private"}
MATURITY_STATE = {"usable": "working", "complete": "delivered-once", "partial": "prototype", "idea": "design-only", "unknown": "unclear"}

PROJECT = ("current_product_value", "future_product_value", "technical_feasibility", "delivery_feasibility")
CONTRIB = ("non_obviousness", "depth_of_thought", "transferability", "current_contribution_value", "future_contribution_value")


def set_est(judgement, value, rationale, basis):
    judgement.update({"status": "estimated", "estimate": value, "scale": "ordinal_0_10",
                      "rationale": rationale, "confidence": judgement.get("confidence", "medium"), "basis": basis})


def short(text, words=14):
    parts = re.split(r"(?<=[.;])\s", text.strip())
    return " ".join(parts[0].split()[:words]).rstrip(".,;")


def derive(a):
    p = a["project"]["judgements"]
    m = a["metadata"]
    best = max(a["contributions"], key=lambda c: (c["judgements"]["current_contribution_value"]["estimate"], c["judgements"]["depth_of_thought"]["estimate"]), default=None)
    private = a["path"] in PRIVATE
    state = "private" if private else MATURITY_STATE.get(m.get("maturity"), "unclear")
    delivery = p["delivery_feasibility"]["estimate"]
    if private:
        gate, reason = 0, "private payload: not shareable and deliberately not inspected"
    elif not a["contributions"] and m.get("maturity") != "complete":
        gate, reason = 0, "no reusable artefact or method inside: nothing to show a stranger"
    else:
        gate, reason = 1, "a stranger can open it and see something: the caveats are already priced in delivery"
    see = [m.get("delivery_form", "")] if m.get("delivery_form") else []
    for e in a["evidence"][:3]:
        see.append(f"{e['source']} — {e['claim']}")
    if a.get("source_pin"):
        see.append(f"everything above is pinned at {a['source_pin'][:12]}")
    if best:
        j = best["judgements"]
        idea = {k: j[k]["estimate"] for k in ("non_obviousness", "depth_of_thought", "transferability")}
        asset = short(best["description"], 14)
        why_idea = (f"mean of {idea['non_obviousness']}/{idea['depth_of_thought']}/{idea['transferability']} for "
                    f"`{best['id'].split(':', 1)[-1]}`, the strongest currently valuable asset: "
                    + j["non_obviousness"]["rationale"])
        inside_now, inside_next = j["current_contribution_value"]["estimate"], j["future_contribution_value"]["estimate"]
    else:
        idea = {k: 0 for k in ("non_obviousness", "depth_of_thought", "transferability")}
        asset, inside_now, inside_next = "", 0, 0
        why_idea = "no contribution card was identified, so no idea score exists: recorded as zero identified value, not as an assertion that nothing was thought"
    now, nxt, tech, deliveryv = (p[k]["estimate"] for k in PROJECT)
    why_realized = f"max(product now {now}, best inside {inside_now}) = {max(now, inside_now)}: " + p["current_product_value"]["rationale"]
    why_upside = (f"max(product if done {nxt}, inside if done {inside_next}) × (technical {tech} + delivery {deliveryv})/20 "
                  f"= {max(nxt, inside_next) * (tech + deliveryv) / 20:.1f}: " + p["future_product_value"]["rationale"])
    return {
        "what": a["project"]["description"],
        "for": m.get("audience", ""),
        "state": state,
        "asset": asset,
        "showability": {"gate": gate, "reason": reason},
        "see": [s for s in see if s],
        "why": {"idea": why_idea, "realized": why_realized, "upside": why_upside, "delivery": p["delivery_feasibility"]["rationale"]},
        "idea": idea,
        "trajectory": ["practical estimate from the existing project packet; no new research, run or measurement"],
    }


def apply_audit(a, record):
    """Replace the numbers the audit covers and record both sides of the change."""
    p = a["project"]["judgements"]
    before = {k: p[k]["estimate"] for k in PROJECT}
    after = record["project"]
    basis = "audit re-score: idea judged blind to delivery state, integer 0–10 estimate, not a measurement"
    for key in PROJECT:
        if key in after:
            set_est(p[key], after[key], record["project_evidence"].get({"current_product_value": "current", "future_product_value": "future", "technical_feasibility": "technical", "delivery_feasibility": "delivery"}[key], ""), basis)
    old_idea = a["display"].get("idea") if a.get("display") else None
    a.setdefault("display", {})["idea"] = record["idea"]
    a["display"]["state"] = record.get("state", a["display"].get("state"))
    if record.get("asset"):
        a["display"]["asset"] = record["asset"]
    if record.get("showability"):
        audited = record["showability"]
        gate = 0 if audited["gate"] == 0 else 1
        note = "" if audited["gate"] == 1 else " (audit called it a caveat, which delivery already prices; a caveat is not a zero)"
        a["display"]["showability"] = {"gate": gate, "reason": audited["reason"] + note}
    if record.get("note"):
        a["display"]["hook"] = record["note"]
    by_id = {c["id"]: c for c in record.get("contributions", [])}
    for c in a["contributions"]:
        if c["id"] in by_id:
            scored = by_id[c["id"]]
            for key in CONTRIB:
                set_est(c["judgements"][key], scored["scores"][key], scored.get("reason", ""), basis)
    delta = ", ".join(f"{k.split('_')[0]} {before[k]}→{after.get(k, before[k])}" for k in PROJECT if after.get(k) != before[k]) or "project scores unchanged"
    idea_txt = f"idea {old_idea}→{record['idea']}" if old_idea and old_idea != record["idea"] else "idea confirmed"
    a["display"].setdefault("trajectory", []).append(
        f"audit re-score ({record.get('state', 'state unknown')}): {delta}; {idea_txt}. " + (record.get("note") or ""))
    if record.get("fused"):
        a["display"]["fused_idea"] = record.get("fused_note", "the three idea dimensions could not be separated on the available evidence")


def main():
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--derive", action="store_true")
    parser.add_argument("--apply", nargs="+")
    args = parser.parse_args()
    data = json.loads(SOURCE.read_text())
    by_path = {a["path"]: a for a in data["assessments"]}
    if args.apply:
        seen = set()
        for file in args.apply:
            payload = json.loads(Path(file).read_text())
            for record in payload.get("projects", payload if isinstance(payload, list) else []):
                assert record["path"] in by_path, record["path"]
                assert record["path"] not in seen, f"duplicate audit record {record['path']}"
                seen.add(record["path"])
                if "display" not in by_path[record["path"]]:
                    by_path[record["path"]]["display"] = derive(by_path[record["path"]])
                apply_audit(by_path[record["path"]], record)
        print(f"applied audit to {len(seen)} projects")
    if args.derive or args.apply:
        missing = [a["path"] for a in data["assessments"] if "display" not in a]
        for path in missing:
            by_path[path]["display"] = derive(by_path[path])
        data["contract_version"] = "practical-estimates-v2-showcase"
        data["display_method"] = ("showcase = gate × idea^0.40 × (realized+0.5)^0.35 × (upside+0.5)^0.25, where idea is the mean of the three "
                                 "contribution idea dimensions, realized = max(product now, best inside now), upside = max(product if done, inside if done) × (technical+delivery)/20. "
                                 "Derived at render time by scripts/catalogue_final.py; the gate is 1 showable, 0.5 caveat, 0 not showable. "
                                 "Display text is composed from the authored facts in this file; no effort hours or observations were invented.")
        SOURCE.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
        print(f"derived display for {len(missing)} projects; every project now has display text")
    else:
        parser.error("choose --derive or --apply FILE")


if __name__ == "__main__":
    main()
