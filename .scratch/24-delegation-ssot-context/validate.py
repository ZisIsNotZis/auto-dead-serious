#!/usr/bin/env python3
"""Self-check for .scratch/24-delegation-ssot-context.

Checks: required semantics present (A/B/C plus round-3 D/E/F/G, round-4 P1-P9
and round-5 P10 cleanups), forbidden forms absent from fact docs, relative markdown
links/anchors resolve, scoped `git diff --check` clean.
Run: python3 .scratch/24-delegation-ssot-context/validate.py
"""
import json
import os
import re
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
AGENTS = os.path.join(ROOT, "AGENTS.md")
EXECUTION = os.path.join(ROOT, "docs", "policy", "execution.md")

results = []


def check(name, ok, detail=""):
    results.append({"check": name, "ok": bool(ok), "detail": detail})


with open(AGENTS, encoding="utf-8") as fh:
    agents = fh.read()
with open(EXECUTION, encoding="utf-8") as fh:
    execution = fh.read()

# --- (A) Main unconditional delegation ---
check("A1 main top priority", "highest-priority role rule" in agents)
check("A2 main no substantive work", "Perform no substantive work of any kind" in agents)
check(
    "A3 main no impl/verify/inspect/write",
    "no implementation, no verification, no inspection/review and no document writing" in agents,
)
check(
    "A4 all tasks incl documentation delegated",
    "delegate every task, including all documentation, to a sub agent" in agents,
)
check("A5 unconditional", "unconditional" in agents)
check(
    "A6 binds regardless of session/context",
    "regardless of session age or inherited/stale context" in agents,
)
check(
    "A7 manages only dialogue/...",
    "manage only user dialogue, intent, authority, confirmed principles, milestones, status/routing and concise delivery" in agents,
)
check(
    "A8 unavailable delegation = blocker",
    "Unavailable delegation is an infrastructure blocker, not a fallback to direct work" in agents,
)

# --- (B) ticket/log vs SSOT documents ---
check("B1 every task ticket", "Every task creates or updates a ticket" in agents)
check("B2 tickets log home", "tickets are the log home for history, provenance and process narrative" in agents)
check("B3 current facts only", "hold current facts only" in agents)
check("B4 rewrite in place", "rewritten in place on change" in agents)
for banned in ["dated narrative", "changelogs", "errata", '"was A, later B"', "dashboard timestamps"]:
    check(f"B5 banned '{banned}'", banned in agents)
check("B6 no duplication/staleness/conflict", "duplication, stale content or conflicting statements" in agents)
check(
    "B7 preserve-entries scoped to ledger",
    "Preserve other entries in the ticket/work-record ledger only" in execution,
)
# Round-2 dedup: the binding SSOT rule lives once in the core; execution points to it.
check(
    "B8 execution points to core SSOT rule",
    "binding in the core `AGENTS.md` shared boundaries" in execution,
)
check(
    "B9 execution no verbatim ticket restatement",
    "Every task also creates or updates a ticket" not in execution,
)
check(
    "B10 execution no verbatim current-facts restatement",
    "Documents of every form hold current facts only" not in execution,
)
check("B11 core: one home per fact", "one home per fact" in agents)
# Append-style wording must be scoped to tickets, not documents.
check(
    "B12 append scoped to tickets",
    "tickets are append-style, fact documents are not" in execution,
)

# --- (C) context inheritance ---
check(
    "C1 fresh default for compact handoff",
    "Default to fresh (non-inherited) context whenever a task is fully specifiable in a compact concrete handoff" in agents,
)
check(
    "C2 inherit when costlier to describe",
    "inherit context only when a context-free description would cost more than inheriting" in agents,
)
check("C3 docs/policy example", "holistic documentation or policy work" in agents)
check("C4 independent review never inherits", "Independent review never inherits context" in agents)

# --- Round-2 follow-up fixes (reviewer notes 1-4) ---
check(
    "R1 no redundant never-implement restatement",
    "Never implement or technically verify" not in agents,
)
check(
    "R2 escape hatch scoped to ticket/archived",
    "historical ticket/archived records need no rewrite when still recoverable" in execution,
)
check(
    "R3 worker records its contract",
    "the worker inspects" in execution and "records its contract" in execution,
)
check("R4 workers record authorized choices", "workers record source" in execution)
check(
    "R5 main has workers record directions",
    "have workers record justified in-scope directions" in agents,
)

# --- Round-3 semantics: (D) subagent subdivision, (E) SMART/fork-mode handoffs,
#     (F) concise agent messaging, (G) ticket vs fact-document classes ---
check(
    "D1 worker splits a splittable assignment",
    "split a splittable assignment into same-layer siblings" in agents,
)
check(
    "D2 core split boundary: permitted + coverage/ownership",
    "When permitted, split a splittable assignment into same-layer siblings, defining and recording complete coverage and ownership"
    in agents,
)
check(
    "D3 recursion still gated",
    "Recursive delegation needs explicit permission, runtime support and the bounds above" in agents,
)
check(
    "D4 subagent subdivides own assignment only when granted",
    "a worker subdivides its own assignment only when granted them" in agents,
)
check(
    "D5 no duplicate subdivision grant in companion",
    "subdivides its own assignment" not in execution,
)
check("E1 every assignment SMART", "Every assignment is SMART" in execution)
check(
    "E2 specific and actionable + AC",
    "above all specific and actionable" in execution and "acceptance criteria (AC)" in execution,
)
check(
    "E3 fresh = fork=false states task+AC and full contract",
    "A fresh / non-inherited handoff (`fork=false`) states its task and acceptance criteria (AC) and carries the full compact contract the child cannot otherwise know"
    in execution,
)
check(
    "E4 inherited = fork=true designates only role",
    "An inherited-context handoff (`fork=true`) already carries the task and AC in context, so it designates only the role"
    in execution,
)
check("E5 fork mapping stated once", (agents + execution).count("fork=") == 2)
check("E6 role designation wording", "you are the sub agent; do this work" in execution)
check("F1 agent-to-agent messages stay minimal", "Agent-to-agent messages stay minimal" in agents)
check("F2 no large prose blocks", "no large prose blocks" in agents)
check(
    "F3 results on disk as documents and tickets",
    "results land on disk as documents and tickets" in agents,
)
check(
    "F4 short done/not-done report to Main",
    "a report back to Main is a very short description plus done/not-done status" in agents,
)
check("F5 no transcript or restated detail", "never a transcript or restated detail" in agents)
check("F6 no duplicate messaging rules in companion", "Agent-to-agent messages" not in execution)
check(
    "G1 non-ticket docs are fact documents",
    "Documents other than tickets are fact documents" in agents,
)
check("G2 ambiguous universal removed", "All documents, in every form" not in agents)
check(
    "G3 in-place rule scoped after class split",
    "one home per fact, rewritten in place on change" in agents,
)
check(
    "G4 tickets still the log home",
    "tickets are the log home for history, provenance and process narrative" in agents,
)
check("G5 append-style named only in companion", "append-style" not in agents)

# --- Round-4 cleanups: (P2-1) fork handoff contradiction, (P2-2) conditional
#     split in the core, (P2-3) one home for the sibling enumeration ---
check("P1 every assignment SMART", "Every assignment is SMART — above all specific and actionable." in execution)
check(
    "P2 fresh handoff states task+AC",
    "A fresh / non-inherited handoff (`fork=false`) states its task and acceptance criteria (AC)" in execution,
)
check(
    "P3 inherited handoff already carries task+AC in context",
    "An inherited-context handoff (`fork=true`) already carries the task and AC in context, so it designates only the role"
    in execution,
)
check(
    "P4 old unconditional task+AC phrasing removed",
    "actionable — and states its task and acceptance criteria (AC)." not in execution,
)
check(
    "P5 core split is permitted-only",
    "When permitted, split a splittable assignment into same-layer siblings" in agents,
)
check("P6 core keeps coverage/ownership boundary", "defining and recording complete coverage and ownership" in agents)
check(
    "P7 core points to the enumeration",
    "enumeration in [Task routing](docs/policy/execution.md#task-routing)" in agents,
)
check(
    "P8 enumeration not duplicated into the core",
    "interfaces, dependencies and an integration owner" not in agents,
)
check(
    "P9 enumeration lives once in the companion",
    "interfaces, dependencies and exclusions" in execution and "assign a worker integration owner" in execution,
)

# --- Round-5 polish: (P2-A) persistence verb restored in the core split rule ---
check("P10 core split records coverage/ownership", "recording complete coverage and ownership" in agents)

# --- link/anchor resolution ---
slug_re = re.compile(r"^#{1,6}\s+(.*)$", re.M)


def slug(heading):
    text = heading.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"\s+", "-", text).strip("-")


# map doc -> set of heading slugs
anchors = {}
for doc in [AGENTS, EXECUTION]:
    with open(doc, encoding="utf-8") as fh:
        anchors[doc] = {slug(h) for h in slug_re.findall(fh.read())}

link_re = re.compile(r"\]\(([^)]+)\)")
for label, doc, base in [("AGENTS.md", agents, ROOT), ("execution.md", execution, os.path.dirname(EXECUTION))]:
    for target in link_re.findall(doc):
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        if "#" in target:
            path, _, frag = target.partition("#")
        else:
            path, frag = target, ""
        if not path:
            continue
        resolved = os.path.normpath(os.path.join(base, path))
        check(f"link exists: {label} -> {target}", os.path.isfile(resolved), resolved)
        if frag and os.path.isfile(resolved):
            with open(resolved, encoding="utf-8") as fh:
                target_slugs = {slug(h) for h in slug_re.findall(fh.read())}
            check(f"anchor resolves: {label} -> {target}", frag in target_slugs, frag)

# --- git diff --check (scoped) ---
proc = subprocess.run(
    ["git", "diff", "--check", "--", "AGENTS.md", "docs/policy/execution.md"],
    cwd=ROOT,
    capture_output=True,
    text=True,
)
check("git diff --check clean", proc.returncode == 0, proc.stdout.strip() or "no whitespace errors")

passed = sum(1 for r in results if r["ok"])
failed = [r for r in results if not r["ok"]]
print(f"{passed}/{len(results)} checks passed")
for r in failed:
    print(f"FAIL: {r['check']} :: {r['detail']}")

out = os.path.join(os.path.dirname(__file__), "checks.json")
with open(out, "w", encoding="utf-8") as fh:
    json.dump({"passed": passed, "total": len(results), "failed": failed, "results": results}, fh, indent=2)
print(f"wrote {out}")
sys.exit(1 if failed else 0)
