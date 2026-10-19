#!/usr/bin/env python3
"""Validate authored catalogue assessments and generate their browsing view; owns no ratings."""
import argparse
import collections
import datetime
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / "docs/result/catalogue"
ASPECTS = ("creativity", "current_usefulness", "expected_usefulness", "impl_progress", "presentability")
ROUTES = ("creativity", "usefulness", "substantial_work")
CONFIDENCE = {"low", "medium", "high"}
VERDICTS = ("showcase_candidate", "repair", "incubate", "undecided", "remove_candidate")
TEXT_FIELDS = ("path", "parent_pin", "state_limits", "description", "scope_audience", "confidence", "verification", "contribution", "alternatives_question", "reason", "next_step", "observation_time", "parent_revision")


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def registry():
    rows = git("config", "-f", ".gitmodules", "--get-regexp", r"^submodule\..*\.path$").splitlines()
    paths = [row.split(" ", 1)[1] for row in rows]
    if len(paths) != len(set(paths)):
        raise ValueError("duplicate .gitmodules path")
    return set(paths)


def validate(records, expected, check_files=True):
    errors = []
    paths = [a.get("path") for a in records]
    counts = collections.Counter(paths)
    for path, count in counts.items():
        if count != 1:
            errors.append(f"{path}: duplicate assessment")
    missing = expected - set(paths)
    extras = set(paths) - expected
    if missing or extras:
        errors.append(f"coverage missing={sorted(missing)} extra={sorted(extras, key=str)}")
    for a in records:
        path = a.get("path", "<missing>")
        def fail(message):
            errors.append(f"{path}: {message}")
        for field in TEXT_FIELDS:
            if not isinstance(a.get(field), str) or not a[field].strip():
                fail(f"missing/non-text {field}")
        if a.get("confidence") not in CONFIDENCE:
            fail("invalid confidence")
        if "child_head" not in a:
            fail("missing child_head (use null if unavailable)")
        for field in ("parent_pin", "child_head", "parent_revision"):
            if field == "child_head" and a.get(field) is None:
                continue
            if not re.fullmatch(r"[0-9a-f]{40,64}", str(a.get(field, ""))):
                fail(f"invalid revision {field}")
        try:
            if datetime.datetime.fromisoformat(a.get("observation_time", "")).tzinfo is None:
                fail("observation_time lacks timezone")
        except ValueError:
            fail("invalid observation_time")
        scores = a.get("scores", {})
        if not isinstance(scores, dict) or set(scores) != set(ASPECTS):
            fail("invalid score aspects")
            scores = {}
        for aspect, rating in scores.items():
            if not isinstance(rating, dict):
                fail(f"invalid {aspect} rating")
                continue
            value = rating.get("value")
            if "value" not in rating or (value is not None and (type(value) is not int or value not in range(5))):
                fail(f"invalid {aspect} value")
            if not isinstance(rating.get("reason"), str) or not rating["reason"].strip() or rating.get("confidence") not in CONFIDENCE:
                fail(f"invalid {aspect} evidence judgement")
        routes = a.get("routes", {})
        if not isinstance(routes, dict) or set(routes) != set(ROUTES) or any(r not in {"supported", "unsupported", "unknown"} for r in routes.values()):
            fail("invalid routes")
            routes = {}
        verdict = a.get("verdict")
        if verdict not in VERDICTS:
            fail("invalid verdict")
        if verdict in {"undecided", "remove_candidate"} and "supported" in routes.values():
            fail("supported route cannot mean undecided/removal")
        if verdict in {"showcase_candidate", "repair", "incubate"} and "supported" not in routes.values():
            fail("retain verdict requires a supported route")
        if verdict == "remove_candidate" and set(routes.values()) != {"unsupported"}:
            fail("removal requires all routes unsupported")
        if a.get("child_head") is None and (verdict != "undecided" or set(routes.values()) != {"unknown"} or any(r.get("value") is not None for r in scores.values())):
            fail("unavailable child cannot carry scores or supported/unsupported routes")
        likelihood = a.get("delivery_likelihood", {})
        if not isinstance(likelihood, dict) or likelihood.get("status") not in {"evidenced", "uncertain", "blocked"} or not isinstance(likelihood.get("reason"), str) or not likelihood["reason"].strip():
            fail("invalid delivery_likelihood")
        producer = a.get("producer", {})
        if not isinstance(producer, dict) or not producer.get("model") or not producer.get("role") or not producer.get("reference"):
            fail("missing assessment producer")
        evidence = a.get("evidence")
        if not isinstance(evidence, list):
            fail("missing evidence list")
            evidence = []
        if "supported" in routes.values() and not evidence:
            fail("supported route lacks inspectable evidence")
        for item in evidence:
            if not isinstance(item, dict) or not isinstance(item.get("path"), str) or not isinstance(item.get("locator"), str) or not item["locator"].strip():
                fail("invalid evidence item")
                continue
            p = Path(item["path"])
            if p.is_absolute() or ".." in p.parts:
                fail("evidence path must stay repo-relative")
            elif check_files and not (ROOT / p).is_file():
                fail(f"missing evidence file {p}")
        if check_files and path in expected:
            try:
                pin = git("ls-files", "--stage", "--", path).split()[1]
                if pin != a.get("parent_pin"):
                    fail("assessment pin differs from current parent gitlink; reassess")
                child_root = Path(git("-C", path, "rev-parse", "--show-toplevel")).resolve()
                if child_root != (ROOT / path).resolve():
                    raise subprocess.CalledProcessError(1, "child root check")
                head = git("-C", path, "rev-parse", "HEAD")
                if head != a.get("child_head"):
                    fail("assessment child HEAD is stale; reassess")
            except (subprocess.CalledProcessError, IndexError):
                if a.get("child_head") is not None or verdict != "undecided" or set(routes.values()) != {"unknown"} or any(r.get("value") is not None for r in scores.values()):
                    fail("unavailable child must have null HEAD/scores and unknown routes, not invented evidence")
    if errors:
        raise ValueError("\n".join(errors))


def load():
    records = []
    for file in sorted(HOME.glob("*.json")):
        record = json.loads(file.read_text())
        if file.name != record.get("path", "") + ".json":
            raise ValueError(f"{file}: name/path mismatch")
        records.append(record)
    validate(records, registry())
    return records


def text(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def render(records):
    counts = collections.Counter(a["verdict"] for a in records)
    retained = sum(counts[v] for v in ("showcase_candidate", "repair", "incubate"))
    lines = ["<!-- Generated by scripts/catalogue.py from authored *.json assessments; edit those sources, not this view. -->", "# Project catalogue", "The evidence-backed assessment of every declared submodule; this catalogue is not the parent README or an approved showcase.", "[Rubric](../../method/catalogue.md) · [Public comparisons](../catalogue-comparison.md)", f"Coverage: **{len(records)} projects**; **{retained} retain**, **{counts['undecided']} undecided**, **{counts['remove_candidate']} remove candidates**.", "Scores are ordinal 0–4; ? means unknown, not zero. Expected usefulness is conditional on completing the stated scope; delivery likelihood is separate.", "These are source-inspected judgements, not fresh runtime, visual, security or experimental verification. Showcase candidates are a verification queue, not approved public features. Private projects are represented only by sanitized structural summaries.", "Click an assessment to read score reasons, confidence, revision-bound evidence, OR-route decisions and the next decisive step. No average score decides membership."]
    for verdict in VERDICTS:
        group = sorted((a for a in records if a["verdict"] == verdict), key=lambda a: a["path"].lower())
        if not group:
            continue
        lines += ["## " + verdict.replace("_", " ").capitalize(), "| Project / assessment | Description | Creativity | Current usefulness | Expected usefulness | Impl progress | Presentability |", "|---|---|---:|---:|---:|---:|---:|"]
        for a in group:
            values = ["?" if a["scores"][key]["value"] is None else str(a["scores"][key]["value"]) for key in ASPECTS]
            lines.append("| " + " | ".join([f"[{a['path']}]({a['path']}.json)", text(a["description"]), *values]) + " |")
    lines += ["## Validation and regeneration", "Run `python3 scripts/catalogue.py --check` from the parent root to check coverage, schema, current pins/HEADs, local evidence-file existence and generated consistency.", "Run `python3 scripts/catalogue.py --render` after editing assessment sources to regenerate this view; `--self-test` exercises safe failing fixtures without touching real records.", "Mechanical checks do not establish that a locator supports a claim, that code works, or that a comparison is exhaustive. Parent inspection supplies bounded semantic calibration; no independent acceptance is claimed."]
    return "\n".join(lines) + "\n"


def self_test():
    records = load()
    def rejects(label, change, check_files=False):
        sample = json.loads(json.dumps(records))
        change(sample)
        try:
            validate(sample, registry(), check_files=check_files)
        except ValueError:
            return label
        raise AssertionError(f"negative control was accepted: {label}")
    tests = [rejects("missing project", lambda a: a.pop()), rejects("duplicate project", lambda a: a.append(a[0])), rejects("bad score", lambda a: a[0]["scores"]["creativity"].update(value=5)), rejects("boolean score", lambda a: a[0]["scores"]["creativity"].update(value=True)), rejects("unsafe removal", lambda a: a[0].update(verdict="remove_candidate")), rejects("unsafe evidence path", lambda a: a[0]["evidence"].append({"path": "../outside", "locator": "unsafe"})), rejects("missing evidence file", lambda a: a[0]["evidence"].append({"path": "docs/result/catalogue/__missing_fixture__", "locator": "negative control"}), check_files=True), rejects("stale pin", lambda a: a[0].update(parent_pin="0" * 40), check_files=True)]
    sample = json.loads(json.dumps(records))
    sample[0]["scores"]["creativity"]["value"] = None
    validate(sample, registry(), check_files=False)
    print("PASS negative controls: " + ", ".join(tests) + "; unknown accepted")


def import_handoffs(directory):
    """Adopt authored investigator records once; never overwrite an assessment source."""
    drafts = []
    for file in sorted(Path(directory).glob("*.json")):
        handoff = json.loads(file.read_text())
        for record in handoff["assessments"]:
            record["kind"] = "authored_assessment"
            record["observation_time"] = handoff["observation_time"]
            record["parent_revision"] = handoff["parent_revision"]
            record["producer"] = {"model": "github_copilot/gpt-6-luna:high", "role": "scout; parent-integrated source-inspection judgement", "reference": "workflow d7f2894e-ccc7-4a2f-aa85-b798dbb5939b, lane " + handoff["lane"]}
            record["inspection_limits"] = handoff["limits"]
            likelihood = record["delivery_likelihood"]
            if isinstance(likelihood, str):
                status, _, reason = likelihood.partition(" — ")
                likelihood = {"status": status, "reason": reason}
            elif "value" in likelihood:
                likelihood = {"status": likelihood["value"], "reason": likelihood["reason"]}
            record["delivery_likelihood"] = likelihood
            verification = record["verification"]
            if isinstance(verification, dict):
                record["verification"] = verification["inspected"] + "; executed=" + str(verification["executed"]).lower() + "; " + verification["limits"]
            path = record["path"]
            if path not in registry() or "/" in path or "\\\\" in path:
                raise ValueError(f"invalid import path: {path}")
            output = HOME / (path + ".json")
            if output.exists():
                raise ValueError(f"refusing to overwrite authored assessment: {output}")
            drafts.append((output, record))
    if len({p for p, _ in drafts}) != len(drafts) or {a["path"] for _, a in drafts} != registry():
        raise ValueError("handoff coverage is incomplete or duplicated")
    HOME.mkdir(parents=True, exist_ok=True)
    for output, record in drafts:
        output.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
    print(f"Imported {len(drafts)} authored drafts; parent calibration and --check are still required")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--render", action="store_true")
    mode.add_argument("--self-test", action="store_true")
    mode.add_argument("--import-handoffs", metavar="DIRECTORY")
    args = parser.parse_args()
    if args.import_handoffs:
        import_handoffs(args.import_handoffs)
        return
    if args.self_test:
        self_test()
        return
    records = load()
    output = HOME / "README.md"
    expected = render(records)
    if args.render:
        output.write_text(expected)
    elif not output.is_file() or output.read_text() != expected:
        raise ValueError("catalogue browsing view is missing or stale; run --render")
    digest = hashlib.sha256()
    sources = [ROOT / ".gitmodules", Path(__file__), ROOT / "docs/method/catalogue.md", ROOT / "docs/product/catalogue.md", ROOT / "docs/result/catalogue-comparison.md", *sorted(HOME.glob("*.json"))]
    for source in sources:
        digest.update(str(source.relative_to(ROOT)).encode() + b"\0" + source.read_bytes() + b"\0")
    digest.update(expected.encode())
    print(f"PASS {len(records)} assessments: exact coverage, schema, current pins/HEADs, evidence files, generated view")
    print("Assessment/rubric/producer/view sha256: " + digest.hexdigest())


if __name__ == "__main__":
    main()
