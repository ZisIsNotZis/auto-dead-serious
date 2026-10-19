#!/usr/bin/env python3
"""Integrate and project the approved nine-judgement catalogue without owning ratings."""
import argparse
import copy
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import catalogue

RESULT_DIR = ROOT / "docs/result/catalogue-redesign"
ASSESSMENTS = RESULT_DIR / "assessments.json"
VIEW = RESULT_DIR / "README.md"
CONTRACT = catalogue.REDESIGN_CONTRACT


def contract_data():
    checked = catalogue.validate_redesign_contract()
    contract = checked["contract"]
    wp1 = contract["x_wp1"]
    pins = {entry["path"]: entry["source_pin"] for entry in wp1["registry_pins"]}
    return contract, wp1["root_source_revision"], pins, sorted(pins), checked["lanes"]


def validate_handoff(data, lane, pins, root_revision):
    if not isinstance(data, dict) or set(data) != {"contract_version", "lane", "root_source_revision", "assessments"}:
        raise ValueError(f"{lane}: handoff fields differ from the WP2 contract")
    if data["contract_version"] != 1 or data["lane"] != lane["key"]:
        raise ValueError(f"{lane['key']}: wrong contract version or lane")
    if data["root_source_revision"] != root_revision:
        raise ValueError(f"{lane['key']}: root source revision differs from the contract")
    records = data["assessments"]
    if not isinstance(records, list) or any(not isinstance(item, dict) for item in records) or [item.get("path") for item in records] != lane["paths"]:
        raise ValueError(f"{lane['key']}: handoff coverage/order differs from the contract")
    for record in records:
        catalogue.validate_assessment(record, pins[record["path"]])
    return records


def validate_dataset(data, context=None):
    _, root_revision, pins, paths, _ = context or contract_data()
    if not isinstance(data, dict) or set(data) != {"contract_version", "root_source_revision", "assessments"}:
        raise ValueError("integrated dataset fields differ from the integration contract")
    if data["contract_version"] != 1 or data["root_source_revision"] != root_revision:
        raise ValueError("integrated dataset contract version or root revision is wrong")
    records = data["assessments"]
    if not isinstance(records, list) or any(not isinstance(item, dict) for item in records):
        raise ValueError("integrated assessments must be a list of project objects")
    actual_paths = [item.get("path") for item in records]
    if actual_paths != paths:
        raise ValueError("integrated project coverage must match the root-pinned registry exactly once in lexical order")
    contribution_ids = set()
    for record in records:
        catalogue.validate_assessment(record, pins[record["path"]])
        for contribution in record["contributions"]:
            if contribution["id"] in contribution_ids:
                raise ValueError(f"duplicate integrated contribution id: {contribution['id']}")
            contribution_ids.add(contribution["id"])
    return records


def integrate_calibration_evidence(records):
    by_path = {item["path"]: item for item in records}
    hyper = by_path["hyperframaker"]
    if not any(item["provenance"] == "owner_testimony" for item in hyper["evidence"]):
        hyper["evidence"].append({
            "id": "owner-calibration",
            "provenance": "owner_testimony",
            "claim": "The owner places hyperframaker at most around APS and likely lower in underlying thought despite finding the output fun; this is calibration testimony, not an implementation or value finding.",
            "source": "docs/product/catalogue-calibration.md",
            "locator": "User-stated judgement; Calibration examples and limits",
            "revision": "f623cb650c30fe619880610a9bc1666332b644a8",
        })
    agentic = by_path["agentic-animation"]
    if not any(item["id"] == "documented-story-pipeline" for item in agentic["evidence"]):
        agentic["evidence"].append({
            "id": "documented-story-pipeline",
            "provenance": "independent_observation",
            "claim": "At the contract-pinned source, the README and pipeline document specify a structured story/YAML pipeline, asset preparation, calls at dramatic/audio boundaries, audio-authoritative timing, compilation checks and sampled visual/audio QA. This establishes the documented method, not successful execution or the owner's broader async/pre/post claims.",
            "source": "agentic-animation/README.md and docs/PIPELINE.md at the contract-pinned revision",
            "locator": "README: Canonical YAML pipeline; docs/PIPELINE.md: steps 1–6 and Operating rule",
            "revision": agentic["source_pin"],
        })
    if not any(item["id"] == "agentic-animation:documented-story-pipeline" for item in agentic["contributions"]):
        agentic["contributions"].append({
            "id": "agentic-animation:documented-story-pipeline",
            "kind": "transferable_practice_insight",
            "description": "A documented assets-first authoring workflow inventories story needs, prepares and checks assets, authors validated YAML calls at dramatic/audio boundaries, builds timing from measured audio, compiles to immutable performance IR, and reviews sampled visual/audio output. The inspected documents describe the method; this card does not claim the full workflow was executed or that the owner's asynchronous/pre/post claims were independently confirmed.",
            "reuse_scope": "Potentially reusable in authored narrated animation where story structure, assets, audio timing, compilation constraints, and sampled output review must stay aligned; transfer outside this project has not been observed.",
            "judgements": {
                "non_obviousness": {"status": "estimated", "estimate": 4, "plausible_range": [3, 5], "rationale": "The documented workflow links story, assets, audio timing, compiler constraints, and QA, while adjacent public sources establish many component primitives and the bounded comparison does not prove a unique integration.", "evidence_refs": ["documented-story-pipeline", "public-calibration"]},
                "depth_of_thought": {"status": "estimated", "estimate": 6, "plausible_range": [5, 7], "rationale": "The pinned pipeline specifies interacting stage contracts, failure conditions, and perceptual QA boundaries rather than relying on a successful render alone; it documents a systematic method but does not establish end-to-end execution quality.", "evidence_refs": ["documented-story-pipeline"]},
                "transferability": {"status": "estimated", "estimate": 5, "plausible_range": [4, 6], "rationale": "The stage boundaries can be adapted to another authored narrated-animation pipeline, but this method is domain-specific and no external reuse is documented.", "evidence_refs": ["documented-story-pipeline"]},
                "current_contribution_value": {"status": "estimated", "estimate": 4, "plausible_range": [3, 5], "rationale": "A detailed current workflow and its failure/inspection criteria are documented; no independent reuse or complete workflow exercise was established in this integration.", "evidence_refs": ["documented-story-pipeline"]},
                "future_contribution_value": {"status": "estimated", "estimate": 4, "plausible_range": [3, 5], "rationale": "If the documented authoring and QA sequence remains executable across new episodes, it could offer a bounded reusable practice; generalization and transfer are not yet demonstrated.", "evidence_refs": ["documented-story-pipeline", "owner-calibration"]},
            },
        })
        agentic["project"]["inside_value_refs"].append("agentic-animation:documented-story-pipeline")


def integrate(handoff_dir):
    _, root_revision, pins, paths, lanes = contract_data()
    records = []
    for lane in lanes:
        file = Path(handoff_dir) / (lane["key"] + ".json")
        handoff = json.loads(file.read_text(encoding="utf-8"))
        records.extend(validate_handoff(handoff, lane, pins, root_revision))
    records.sort(key=lambda record: record["path"])
    integrate_calibration_evidence(records)
    data = {"contract_version": 1, "root_source_revision": root_revision, "assessments": records}
    validate_dataset(data, (None, root_revision, pins, paths, lanes))
    RESULT_DIR.mkdir(parents=True, exist_ok=True)
    ASSESSMENTS.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Integrated {len(records)} projects from {len(lanes)} validated lanes at root revision {root_revision}")


def fmt_rating(value):
    if value["status"] == "unknown":
        return "unknown"
    if value["status"] == "range":
        low, high = value["probability_range"]
        return f"subjective {low:g}–{high:g}; horizon: {value['horizon']}"
    low, high = value["plausible_range"]
    return f"{value['estimate']} ({low}–{high})"


def value_summary(value):
    if value["status"] == "unknown":
        return "unknown"
    low, high = value["plausible_range"]
    return f"{value['estimate']} ({low}–{high})"


def anchor(path):
    slug = re.sub(r"[^a-z0-9-]+", "-", path.lower()).strip("-")
    return "project-" + slug


def render(data):
    records = validate_dataset(data)
    lines = [
        "<!-- Generated by scripts/catalogue_redesign.py from assessments.json; edit the JSON source, not this view. -->",
        "# Catalogue redesign — integrated draft",
        "",
        "> **Not M1 acceptance.** Public-A evidence remains incomplete, public-B is blocked, and the fresh independent review is pending.",
        "",
        "This view is a projection of the nine-judgement assessments at [assessments.json](assessments.json), bound to root source revision `" + data["root_source_revision"] + "`. Every project occurs once. Project judgements and linked contribution judgements have separate homes within each project record; no aggregate or tie-break is used.",
        "",
        "The older 0–4 records at `../catalogue/` remain disputed legacy evidence and are not current replacement scores. Bounded public evidence: [public-A, incomplete](../catalogue-redesign-public-calibration.md) · [public-B, blocked](../catalogue-redesign-public-other.md).",
        "",
        f"Coverage: **{len(records)} of {len(records)} root-pinned projects**. Feasibility remains unknown unless a justified constrained probability range exists.",
        "",
        "## Browse projects",
        "",
        "| Project | Current product | Conditional-future product |",
        "|---|---:|---:|",
    ]
    for record in records:
        project = record["project"]
        judgements = project["judgements"]
        lines.append("| [" + record["path"] + "](#" + anchor(record["path"]) + ") | " + value_summary(judgements["current_product_value"]) + " | " + value_summary(judgements["future_product_value"]) + " |")
    for record in records:
        lines += ["", f"<a id=\"{anchor(record['path'])}\"></a>", "", f"## {project_text(record['path'])}", "", f"**Source pin:** `{record['source_pin']}`", "", f"**Description:** {project_text(record['project']['description'])}", "", "| Project judgement | Assessment |", "|---|---|"]
        for key, value in record["project"]["judgements"].items():
            lines.append("| " + key.replace("_", " ") + " | " + project_text(fmt_rating(value)) + " |")
        lines += ["", "### Linked contributions", ""]
        if not record["contributions"]:
            lines.append("No separately valued contribution card is recorded.")
        for contribution in record["contributions"]:
            judgements = contribution["judgements"]
            values = ["**" + key.replace("_", " ") + ":** " + project_text(fmt_rating(judgements[key])) for key in ("non_obviousness", "depth_of_thought", "transferability", "current_contribution_value", "future_contribution_value")]
            lines += [f"#### {project_text(contribution['id'])} ({contribution['kind']})", "", "; ".join(values), ""]
        lines += ["Full scope, rationales, evidence provenance/locators, effort, metadata, limitations and next steps are in [assessments.json](assessments.json)."]
    lines += ["", "## Producer and limits", "", "Run `python3 scripts/catalogue_redesign.py --check` to validate coverage, contract shape, source pins, evidence references, contribution links, and generated-view freshness. Run `python3 scripts/catalogue_redesign.py --render` after changing `assessments.json`. `--self-test` exercises safe negative controls. The optional filtered application was not generated because this searchable index and detail tables expose the same sources without requiring a separate interface. The view does not claim source code execution, visual/runtime verification, public-source completeness, or independent acceptance.", ""]
    return "\n".join(lines)


def project_text(value):
    import html
    return html.escape(str(value).replace("\n", " "), quote=False).replace("|", "\\|")


def check():
    data = json.loads(ASSESSMENTS.read_text(encoding="utf-8"))
    records = validate_dataset(data)
    expected = render(data)
    if not VIEW.is_file() or VIEW.read_text(encoding="utf-8") != expected:
        raise ValueError("generated catalogue redesign view is missing or stale; run --render")
    print(f"PASS {len(records)} root-pinned assessments; {sum(len(r['contributions']) for r in records)} linked contributions; evidence, uncertainty, pins, coverage and Markdown projection are consistent")


def render_file():
    data = json.loads(ASSESSMENTS.read_text(encoding="utf-8"))
    validate_dataset(data)
    RESULT_DIR.mkdir(parents=True, exist_ok=True)
    VIEW.write_text(render(data), encoding="utf-8")
    print(f"Rendered {VIEW.relative_to(ROOT)}")


def self_test():
    data = json.loads(ASSESSMENTS.read_text(encoding="utf-8"))
    context = contract_data()
    validate_dataset(data, context)
    cases = []
    def rejects(label, mutate):
        sample = copy.deepcopy(data)
        mutate(sample)
        try:
            validate_dataset(sample, context)
        except (ValueError, KeyError, TypeError):
            cases.append(label)
        else:
            raise AssertionError(f"negative control was accepted: {label}")
    rejects("missing project", lambda d: d["assessments"].pop())
    rejects("wrong assessment container", lambda d: d.__setitem__("assessments", "not-a-list"))
    rejects("duplicate project", lambda d: d["assessments"].__setitem__(-1, copy.deepcopy(d["assessments"][0])))
    rejects("wrong root pin", lambda d: d["assessments"][0].__setitem__("source_pin", "0" * 40))
    rejects("forbidden aggregate", lambda d: d["assessments"][0].__setitem__("overall_score", 5))
    rejects("dangling evidence reference", lambda d: d["assessments"][0]["project"]["judgements"]["current_product_value"].update(evidence_refs=["missing-evidence"]))
    integrate_calibration_evidence(data["assessments"])
    agentic = next(r for r in data["assessments"] if r["path"] == "agentic-animation")
    hyper = next(r for r in data["assessments"] if r["path"] == "hyperframaker")
    if not any(e["provenance"] == "owner_testimony" for e in hyper["evidence"]):
        raise AssertionError("hyperframaker owner calibration testimony was not preserved")
    if not any(c["id"] == "agentic-animation:documented-story-pipeline" for c in agentic["contributions"]):
        raise AssertionError("pinned-source documented-story practice is absent")
    print("PASS negative controls: " + ", ".join(cases) + "; unknowns accepted; owner testimony and pinned story-pipeline source are retained")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--integrate", metavar="HANDOFF_DIRECTORY")
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--render", action="store_true")
    mode.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.integrate:
        integrate(args.integrate)
    elif args.check:
        check()
    elif args.render:
        render_file()
    else:
        self_test()


if __name__ == "__main__":
    main()
