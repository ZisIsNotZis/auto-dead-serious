#!/usr/bin/env python3
"""Validate authored catalogue assessments and generate their browsing view; owns no ratings."""
import argparse
import collections
import configparser
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
    calibration = ROOT / "docs/product/catalogue-calibration.md"
    if calibration.is_file():
        status = re.search(r"^Status: (disputed|approved|provisional)$", calibration.read_text(), re.MULTILINE)
        if not status:
            raise ValueError("calibration discussion must declare its current Status")
        if status.group(1) == "disputed":
            lines.insert(3, "**Creativity and current-usefulness ratings are disputed.** They are retained as draft evidence, not a trusted ranking; see the [owner calibration and proposed rubric](../../product/catalogue-calibration.md). No full rescore has been applied.")
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


REDESIGN_CONTRACT = ROOT / "docs/method/catalogue-contract.json"
REDESIGN_FIXTURE = ROOT / "tests/fixtures/catalogue_redesign_failed_product.json"
REDESIGN_AGENT = "catalogue-public-research"
REDESIGN_JUDGEMENTS = {
    "non_obviousness", "depth_of_thought", "transferability",
    "current_product_value", "future_product_value",
    "current_contribution_value", "future_contribution_value",
    "technical_feasibility", "delivery_feasibility",
}
VALUE_JUDGEMENTS = {
    "non_obviousness", "depth_of_thought", "transferability",
    "current_product_value", "future_product_value",
    "current_contribution_value", "future_contribution_value",
}
FORBIDDEN_AGGREGATES = {
    "total", "total_score", "average", "ordinal_average", "weighted_total",
    "overall_score", "composite_score", "mean_score", "rank_score",
}
REVISION_RE = re.compile(r"^[0-9a-f]{40,64}$")


def gitmodules_paths(text):
    modules = configparser.ConfigParser()
    modules.read_string(text)
    paths = [section.get("path") for section in modules.values() if section.get("path")]
    if len(paths) != len(set(paths)):
        raise ValueError("duplicate .gitmodules path in pinned source")
    return sorted(paths)


def gitlink_pins(revision):
    tree = subprocess.check_output(["git", "ls-tree", "-r", revision], cwd=ROOT, text=True)
    pins = {}
    for line in tree.splitlines():
        metadata, path = line.split("\t", 1)
        mode, kind, oid = metadata.split()
        if mode == "160000" and kind == "commit":
            pins[path] = oid
    return pins


def split_lanes(paths):
    ordered = sorted(paths)
    quotient, remainder = divmod(len(ordered), 4)
    lanes = []
    offset = 0
    for index in range(4):
        size = quotient + (index < remainder)
        lanes.append({"key": f"lane-{index + 1:02d}", "paths": ordered[offset:offset + size]})
        offset += size
    return lanes


def validate_partition(lanes, expected_paths):
    if not isinstance(lanes, list) or not 1 <= len(lanes) <= 4:
        raise ValueError("routing must contain one to four lanes")
    keys = [lane.get("key") if isinstance(lane, dict) else None for lane in lanes]
    if len(keys) != len(set(keys)) or any(not isinstance(key, str) or not key for key in keys):
        raise ValueError("lane keys must be unique nonempty strings")
    flattened = []
    for lane in lanes:
        if set(lane) != {"key", "paths"} or not isinstance(lane["paths"], list):
            raise ValueError("each lane must contain exactly key and paths")
        if lane["paths"] != sorted(lane["paths"]) or len(lane["paths"]) != len(set(lane["paths"])):
            raise ValueError(f"{lane['key']}: paths must be unique and lexically sorted")
        flattened.extend(lane["paths"])
    if len(flattened) != len(set(flattened)):
        raise ValueError("routing lanes overlap")
    if set(flattened) != set(expected_paths) or len(flattened) != len(expected_paths):
        raise ValueError("routing does not exactly cover the pinned registry")
    if lanes != split_lanes(expected_paths):
        raise ValueError("routing must use the documented balanced lexical partition")


def no_aggregate_keys(value):
    if isinstance(value, dict):
        forbidden = FORBIDDEN_AGGREGATES.intersection(value)
        if forbidden:
            raise ValueError("forbidden aggregate fields: " + ", ".join(sorted(forbidden)))
        for child in value.values():
            no_aggregate_keys(child)
    elif isinstance(value, list):
        for child in value:
            no_aggregate_keys(child)


def _nonempty_string(value):
    return isinstance(value, str) and bool(value.strip())


def _valid_refs(value, evidence_ids, field):
    if not isinstance(value, list) or len(value) != len(set(value)) or any(ref not in evidence_ids for ref in value):
        raise ValueError(f"invalid {field}: evidence references must resolve uniquely")


def validate_rating(rating, evidence_ids, label):
    if not isinstance(rating, dict):
        raise ValueError(f"{label}: rating must be an object")
    if rating.get("status") == "unknown":
        if set(rating) != {"status", "reason"} or not _nonempty_string(rating.get("reason")):
            raise ValueError(f"{label}: unknown rating requires only a reason")
        return
    expected = {"status", "estimate", "plausible_range", "rationale", "evidence_refs"}
    if set(rating) != expected or rating.get("status") != "estimated":
        raise ValueError(f"{label}: expected estimated or unknown rating")
    estimate, bounds = rating["estimate"], rating["plausible_range"]
    if type(estimate) is not int or not 0 <= estimate <= 10:
        raise ValueError(f"{label}: estimate must be an integer from 0 through 10")
    if not isinstance(bounds, list) or len(bounds) != 2 or any(type(bound) is not int or not 0 <= bound <= 10 for bound in bounds):
        raise ValueError(f"{label}: plausible_range must contain two integers from 0 through 10")
    if not bounds[0] <= estimate <= bounds[1]:
        raise ValueError(f"{label}: estimate must lie within plausible_range")
    if not _nonempty_string(rating["rationale"]):
        raise ValueError(f"{label}: estimated rating needs a rationale")
    _valid_refs(rating["evidence_refs"], evidence_ids, f"{label}.evidence_refs")
    if not rating["evidence_refs"]:
        raise ValueError(f"{label}: estimated rating needs source evidence")


def validate_forecast(forecast, evidence_ids, label):
    if not isinstance(forecast, dict):
        raise ValueError(f"{label}: feasibility judgement must be an object")
    if forecast.get("status") == "unknown":
        if set(forecast) != {"status", "reason"} or not _nonempty_string(forecast.get("reason")):
            raise ValueError(f"{label}: unknown feasibility requires only a reason")
        return
    expected = {"status", "probability_range", "constraints", "horizon", "rationale", "evidence_refs"}
    if set(forecast) != expected or forecast.get("status") != "range":
        raise ValueError(f"{label}: feasibility requires a constrained range or unknown")
    bounds = forecast["probability_range"]
    if not isinstance(bounds, list) or len(bounds) != 2 or any(type(bound) not in (int, float) or not 0 <= bound <= 1 for bound in bounds):
        raise ValueError(f"{label}: probability_range must contain two numbers from 0 through 1")
    if bounds[0] > bounds[1]:
        raise ValueError(f"{label}: probability_range is reversed")
    for field in ("constraints", "horizon", "rationale"):
        if not _nonempty_string(forecast[field]):
            raise ValueError(f"{label}: probability range requires {field}")
    _valid_refs(forecast["evidence_refs"], evidence_ids, f"{label}.evidence_refs")
    if not forecast["evidence_refs"]:
        raise ValueError(f"{label}: probability range needs source evidence")


def validate_assessment(assessment, expected_pin=None):
    no_aggregate_keys(assessment)
    required = {"path", "source_pin", "project", "contributions", "evidence", "effort", "metadata", "limitations", "next_decisive_step"}
    if not isinstance(assessment, dict) or set(assessment) != required:
        raise ValueError("assessment fields do not match the WP2 contract")
    if not _nonempty_string(assessment["path"]) or not REVISION_RE.fullmatch(str(assessment["source_pin"])):
        raise ValueError("assessment requires a path and root-pinned source revision")
    if expected_pin is not None and assessment["source_pin"] != expected_pin:
        raise ValueError(f"{assessment['path']}: source_pin differs from the contract root gitlink")
    evidence = assessment["evidence"]
    if not isinstance(evidence, list) or any(not isinstance(item, dict) or set(item) != {"id", "provenance", "claim", "source", "locator", "revision"} for item in evidence):
        raise ValueError(f"{assessment['path']}: invalid evidence records")
    evidence_ids = [item["id"] for item in evidence]
    if any(not _nonempty_string(value) for value in evidence_ids) or len(evidence_ids) != len(set(evidence_ids)):
        raise ValueError(f"{assessment['path']}: evidence ids must be unique and nonempty")
    for item in evidence:
        if item["provenance"] not in {"owner_testimony", "independent_observation", "agent_inference"}:
            raise ValueError(f"{assessment['path']}: evidence provenance must distinguish testimony, observation and inference")
        for field in ("claim", "source", "locator"):
            if not _nonempty_string(item[field]):
                raise ValueError(f"{assessment['path']}: evidence requires {field}")
        if item["revision"] != "unknown" and not REVISION_RE.fullmatch(str(item["revision"])):
            raise ValueError(f"{assessment['path']}: evidence revision must be a hash or unknown")
    project = assessment["project"]
    if not isinstance(project, dict) or set(project) != {"description", "intended_scope", "judgements", "inside_value_refs"}:
        raise ValueError(f"{assessment['path']}: invalid project fields")
    for field in ("description", "intended_scope"):
        if not _nonempty_string(project[field]):
            raise ValueError(f"{assessment['path']}: project requires {field}; state unknown explicitly")
    judgements = project["judgements"]
    project_fields = {"current_product_value", "future_product_value", "technical_feasibility", "delivery_feasibility"}
    if not isinstance(judgements, dict) or set(judgements) != project_fields:
        raise ValueError(f"{assessment['path']}: project judgement fields do not match the contract")
    for field in ("current_product_value", "future_product_value"):
        validate_rating(judgements[field], evidence_ids, f"{assessment['path']}.{field}")
    for field in ("technical_feasibility", "delivery_feasibility"):
        validate_forecast(judgements[field], evidence_ids, f"{assessment['path']}.{field}")
    contributions = assessment["contributions"]
    if not isinstance(contributions, list):
        raise ValueError(f"{assessment['path']}: contributions must be a list")
    contribution_ids = [item.get("id") for item in contributions if isinstance(item, dict)]
    if len(contribution_ids) != len(contributions) or any(not _nonempty_string(value) for value in contribution_ids) or len(contribution_ids) != len(set(contribution_ids)):
        raise ValueError(f"{assessment['path']}: contribution ids must be unique and nonempty")
    transferable_ids = set()
    contribution_fields = {"non_obviousness", "depth_of_thought", "transferability", "current_contribution_value", "future_contribution_value"}
    for contribution in contributions:
        if set(contribution) != {"id", "kind", "description", "reuse_scope", "judgements"}:
            raise ValueError(f"{assessment['path']}: invalid contribution fields")
        for field in ("description", "reuse_scope"):
            if not _nonempty_string(contribution[field]):
                raise ValueError(f"{assessment['path']}.{contribution['id']}: requires {field}")
        kind = contribution["kind"]
        if kind not in {"transferable_practice_insight", "internal_module", "output"}:
            raise ValueError(f"{assessment['path']}.{contribution['id']}: invalid contribution kind")
        if kind == "transferable_practice_insight":
            transferable_ids.add(contribution["id"])
        ratings = contribution["judgements"]
        if not isinstance(ratings, dict) or set(ratings) != contribution_fields:
            raise ValueError(f"{assessment['path']}.{contribution['id']}: contribution judgement fields do not match the contract")
        for field, rating in ratings.items():
            validate_rating(rating, evidence_ids, f"{assessment['path']}.{contribution['id']}.{field}")
            if kind != "transferable_practice_insight" and rating["status"] != "unknown":
                raise ValueError(f"{assessment['path']}.{contribution['id']}: internal modules and outputs are not independently valued contributions")
    inside_refs = project["inside_value_refs"]
    if not isinstance(inside_refs, list) or len(inside_refs) != len(set(inside_refs)) or not set(inside_refs) <= transferable_ids:
        raise ValueError(f"{assessment['path']}: inside_value_refs must reference transferable contribution cards only")
    if not isinstance(assessment["effort"], dict) or set(assessment["effort"]) != {"human", "ai"}:
        raise ValueError(f"{assessment['path']}: human and AI effort must be separate")
    for kind, effort in assessment["effort"].items():
        if not isinstance(effort, dict):
            raise ValueError(f"{assessment['path']}: {kind} effort must be descriptive or unknown")
        if effort.get("status") == "unknown":
            if set(effort) != {"status", "reason"} or not _nonempty_string(effort.get("reason")):
                raise ValueError(f"{assessment['path']}: unknown {kind} effort requires a reason")
        elif effort.get("status") == "described":
            if set(effort) != {"status", "quantity", "source"} or not _nonempty_string(effort.get("quantity")) or not _nonempty_string(effort.get("source")):
                raise ValueError(f"{assessment['path']}: described {kind} effort requires quantity description and provenance")
        else:
            raise ValueError(f"{assessment['path']}: invalid {kind} effort status")
    metadata = assessment["metadata"]
    metadata_fields = {"maturity", "evidence_strength", "audience", "tags", "delivery_form", "requirements", "reuse_extraction_burden"}
    if not isinstance(metadata, dict) or set(metadata) != metadata_fields:
        raise ValueError(f"{assessment['path']}: invalid separate metadata fields")
    if metadata["maturity"] not in {"idea", "partial", "usable", "complete", "unknown"} or metadata["evidence_strength"] not in {"low", "medium", "high", "unknown"}:
        raise ValueError(f"{assessment['path']}: invalid maturity or evidence_strength")
    for field in ("audience", "delivery_form", "reuse_extraction_burden"):
        if not _nonempty_string(metadata[field]):
            raise ValueError(f"{assessment['path']}: metadata requires {field}; state unknown explicitly")
    for field in ("tags", "requirements"):
        values = metadata[field]
        if not isinstance(values, list) or any(not _nonempty_string(value) for value in values):
            raise ValueError(f"{assessment['path']}: metadata {field} must be a list of nonempty strings")
    for field in ("limitations",):
        values = assessment[field]
        if not isinstance(values, list) or any(not _nonempty_string(value) for value in values):
            raise ValueError(f"{assessment['path']}: {field} must be a list of nonempty strings")
    if not _nonempty_string(assessment["next_decisive_step"]):
        raise ValueError(f"{assessment['path']}: next_decisive_step must state an action or unknown")


def validate_schema_shape(contract):
    expected_top = {"contract_version", "lane", "root_source_revision", "assessments"}
    if contract.get("type") != "object" or set(contract.get("required", [])) != expected_top or contract.get("additionalProperties") is not False:
        raise ValueError("WP2 JSON Schema top-level handoff shape is incomplete or permissive")
    properties = contract.get("properties", {})
    if set(properties) != expected_top:
        raise ValueError("WP2 JSON Schema top-level fields do not match its required set")
    wp1 = contract.get("x_wp1", {})
    expected_judgements = REDESIGN_JUDGEMENTS
    if set(wp1.get("judgements", {})) != expected_judgements:
        raise ValueError("WP2 contract does not define all nine approved judgements")
    for name in VALUE_JUDGEMENTS:
        item = wp1["judgements"][name]
        if item.get("kind") != "integer_estimate" or item.get("range") != [0, 10] or item.get("unknown_allowed") is not True:
            raise ValueError(f"invalid integer anchors for {name}")
        anchors = item.get("anchors", [])
        if not anchors or anchors[0]["range"][0] != 0 or anchors[-1]["range"][1] != 10:
            raise ValueError(f"{name}: anchors must cover 0 through 10")
        for previous, current in zip(anchors, anchors[1:]):
            if previous["range"][1] + 1 != current["range"][0]:
                raise ValueError(f"{name}: anchor bands must be contiguous and disjoint")
    for name in {"technical_feasibility", "delivery_feasibility"}:
        item = wp1["judgements"][name]
        if item.get("kind") != "subjective_probability_range" or set(item.get("requires", [])) != {"constraints", "horizon", "rationale"} or item.get("unknown_allowed") is not True:
            raise ValueError(f"{name}: range must require constraints, horizon and rationale or allow unknown")
    aggregation = wp1.get("source_rules", {}).get("aggregation", "")
    if "No total" not in aggregation or "weighted score" not in aggregation or "genuine ties" not in aggregation:
        raise ValueError("contract must prohibit aggregation and preserve genuine ties")
    defs = contract.get("$defs", {})
    if not {"rating", "feasibility", "evidence", "effort", "assessment"} <= set(defs):
        raise ValueError("WP2 contract definitions are incomplete")
    assessment_required = {"path", "source_pin", "project", "contributions", "evidence", "effort", "metadata", "limitations", "next_decisive_step"}
    if set(defs["assessment"].get("required", [])) != assessment_required or defs["assessment"].get("additionalProperties") is not False:
        raise ValueError("WP2 assessment fields are incomplete or permissive")


def validate_redesign_contract():
    contract = json.loads(REDESIGN_CONTRACT.read_text())
    validate_schema_shape(contract)
    wp1 = contract["x_wp1"]
    root_revision = wp1.get("root_source_revision")
    if not isinstance(root_revision, str) or not REVISION_RE.fullmatch(root_revision):
        raise ValueError("invalid root_source_revision in WP2 contract")
    pinned_registry = gitmodules_paths(subprocess.check_output(["git", "show", f"{root_revision}:.gitmodules"], cwd=ROOT, text=True))
    pinned_tree = gitlink_pins(root_revision)
    entries = wp1.get("registry_pins")
    if not isinstance(entries, list) or entries != [{"path": path, "source_pin": pinned_tree.get(path)} for path in pinned_registry]:
        raise ValueError("WP2 source pins do not match the contract's root-pinned registry")
    current_paths = sorted(registry())
    if current_paths != pinned_registry:
        raise ValueError("current registry differs from WP2's root-pinned registry")
    if gitlink_pins("HEAD") != pinned_tree:
        raise ValueError("current root gitlinks differ from WP2's pinned source revisions")
    lanes = wp1.get("lanes")
    validate_partition(lanes, pinned_registry)
    if wp1.get("partition_policy", "").find("lexically") < 0 or wp1.get("output", {}).get("file") != "<runtime-managed-output>/<lane>.json":
        raise ValueError("WP2 output or lexical routing policy is missing")
    if not REDESIGN_FIXTURE.is_file():
        raise ValueError(f"missing WP1 negative/positive fixture: {REDESIGN_FIXTURE.relative_to(ROOT)}")
    fixture = json.loads(REDESIGN_FIXTURE.read_text())
    validate_assessment(fixture)
    if fixture["project"]["judgements"]["current_product_value"].get("estimate", 10) >= fixture["contributions"][0]["judgements"]["current_contribution_value"].get("estimate", 0):
        raise ValueError("WP1 fixture must demonstrate a valuable contribution despite failed product value")
    if fixture["effort"]["human"]["status"] != "unknown" or fixture["effort"]["ai"]["status"] != "unknown":
        raise ValueError("WP1 fixture must preserve unknown human and AI effort")
    if any(fixture["project"]["judgements"][key]["status"] != "unknown" for key in ("future_product_value", "technical_feasibility", "delivery_feasibility")):
        raise ValueError("WP1 fixture must preserve unknown future value and feasibility")
    if not any(item["provenance"] == "owner_testimony" for item in fixture["evidence"]) or not any(item["provenance"] == "independent_observation" for item in fixture["evidence"]):
        raise ValueError("WP1 fixture must distinguish testimony from independent observation")
    negative = json.loads(json.dumps(fixture))
    negative["overall_score"] = 5
    try:
        validate_assessment(negative)
    except ValueError:
        pass
    else:
        raise ValueError("WP1 no-ordinal-averaging negative control was accepted")
    return {"contract": contract, "lanes": lanes, "pin_count": len(entries)}


def validate_redesign_handoff(file_path, lane_key):
    checked = validate_redesign_contract()
    contract = checked["contract"]
    wp1 = contract["x_wp1"]
    lane = next((item for item in checked["lanes"] if item["key"] == lane_key), None)
    if lane is None:
        raise ValueError(f"unknown WP2 lane: {lane_key}")
    data = json.loads(Path(file_path).read_text())
    if no_aggregate_keys(data) is not None:
        raise AssertionError("unreachable")
    if not isinstance(data, dict) or set(data) != {"contract_version", "lane", "root_source_revision", "assessments"}:
        raise ValueError("handoff fields do not match the WP2 contract")
    if data["contract_version"] != 1 or data["lane"] != lane_key or data["root_source_revision"] != wp1["root_source_revision"]:
        raise ValueError("handoff contract version, lane or root revision is wrong")
    records = data["assessments"]
    if not isinstance(records, list) or [record.get("path") for record in records if isinstance(record, dict)] != lane["paths"]:
        raise ValueError("handoff must include each assigned lane path exactly once in lexical order")
    pins = {item["path"]: item["source_pin"] for item in wp1["registry_pins"]}
    for record in records:
        validate_assessment(record, pins[record["path"]])


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
    mode.add_argument("--redesign-contract-json", action="store_true")
    mode.add_argument("--validate-redesign-handoff", metavar="FILE")
    parser.add_argument("--lane", help="WP2 lane key required with --validate-redesign-handoff")
    args = parser.parse_args()
    if args.redesign_contract_json:
        checked = validate_redesign_contract()
        print(json.dumps({"ready": True, "contract_path": str(REDESIGN_CONTRACT.relative_to(ROOT)), "lanes": checked["lanes"], "research_agent": REDESIGN_AGENT}, separators=(",", ":")))
        return
    if args.validate_redesign_handoff:
        if not args.lane:
            parser.error("--validate-redesign-handoff requires --lane")
        validate_redesign_handoff(args.validate_redesign_handoff, args.lane)
        print(f"PASS WP2 handoff {args.lane}: exact lane coverage, contract fields, evidence provenance and root-pinned revisions")
        return
    if args.lane:
        parser.error("--lane is valid only with --validate-redesign-handoff")
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
    sources = [ROOT / ".gitmodules", Path(__file__), ROOT / "docs/method/catalogue.md", ROOT / "docs/product/catalogue.md", *([ROOT / "docs/product/catalogue-calibration.md"] if (ROOT / "docs/product/catalogue-calibration.md").is_file() else []), ROOT / "docs/result/catalogue-comparison.md", *sorted(HOME.glob("*.json"))]
    for source in sources:
        digest.update(str(source.relative_to(ROOT)).encode() + b"\0" + source.read_bytes() + b"\0")
    digest.update(expected.encode())
    print(f"PASS {len(records)} assessments: exact coverage, schema, current pins/HEADs, evidence files, generated view")
    print("Assessment/rubric/producer/view sha256: " + digest.hexdigest())


if __name__ == "__main__":
    main()
