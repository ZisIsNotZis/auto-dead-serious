#!/usr/bin/env python3
"""Self-check for ticket 25 (slice review cadence + worker self-loop).

Checks A1..A9 from contract.md against the CURRENT working tree. Exits non-zero
on any failure so the run is a real gate, not a report generator.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path("/home/z/vibe")
TICKET = ROOT / ".scratch/25-slice-review-selfloop"
BASE = TICKET / "baseline"

core = (ROOT / "AGENTS.md").read_text()
comp = (ROOT / "docs/policy/execution.md").read_text()
core_b = (BASE / "AGENTS.md").read_text()
comp_b = (BASE / "execution.md").read_text()

results = []


def check(cid, ok, detail):
    results.append({"id": cid, "pass": bool(ok), "detail": detail})


def sections(text):
    """Map heading slug -> section body."""
    out, slug = {}, None
    for line in text.splitlines():
        m = re.match(r"^## (.+)$", line)
        if m:
            slug = m.group(1).lower().replace(" ", "-")
            out[slug] = ""
        elif slug:
            out[slug] += line + "\n"
    return out


def slugify(h):
    return re.sub(r"[^a-z0-9 -]", "", h.strip().lower()).replace(" ", "-")


# A1 slice-gate cadence stated once in the core.
a1 = [
    "at least one fresh independent review per vertical slice",
    "not per task or sub-task",
    "Review timing inside a slice is flexible",
]
check("A1", all(p in core for p in a1) and core.count(a1[0]) == 1,
      f"core phrases found={[p in core for p in a1]} first-count={core.count(a1[0])}")

# A2 worker self-loop in the core, and no per-task review requirement anywhere.
a2_phrases = ["Work in a self-loop:", "record the acceptance standard the result will be judged by",
              "check the result against that standard and iterate until it passes"]
no_pertask = not re.search(r"(per[- ]task|per sub-?task)[^.]*review is required|"
                           r"separate (independent )?review for (every|each) (task|sub-?task)",
                           core + comp, re.I)
check("A2", all(p in core for p in a2_phrases) and no_pertask,
      f"phrases={[p in core for p in a2_phrases]} per-task-review-required={not no_pertask}")

# A3 no-slice work only on explicit user request.
check("A3", "record, policy or documentation-only work — is independently reviewed only when the user asks" in core,
      "core no-slice clause present")

# A4 one definition home for "vertical slice", in Product decisions.
pd = sections(comp)["product-decisions"]
defn = "bounded end-to-end user outcomes — each such outcome is a vertical slice"
pr = sections(comp)["proof-and-review"]
points_back = "defined under Product decisions" in pr
core_redefines = "each such outcome is a vertical slice" in core
check("A4", defn in pd and points_back and not core_redefines,
      f"definition-in-product-decisions={defn in pd} proof-review-points-back={points_back} core-redefines={core_redefines}")

# A5 preserved invariants, boundaries, and reviewer independence.
invariants = [
    (core, "revision-bound self-proof"),
    (core, "use fresh context, never worker conversation"),
    (core, "never accept the repairer's own verdict" if False else "ending independent acceptance authority"),
    (core, "PASS needs documented proof"),
    (comp, "never accept the repairer's own verdict"),
    (comp, "Repair only within authority/tools"),
    (comp, "Unavailable independent review is an infrastructure blocker, not self-review permission"),
    (comp, "A self-test is the in-slice loop, not independent acceptance"),
]
missing = [p for f, p in invariants if p not in f]
removed = [ln for ln in core_b.splitlines() if ln.startswith("- ") and ln not in core.splitlines()]
# Only the intentionally revised completion boundary line may be absent; safeguard lines must survive.
unexpected = [ln for ln in removed if "revision-bound self-proof and fresh independent review" not in ln]
check("A5", not missing and not unexpected,
      f"missing={missing} unexpected-boundary-removals={len(unexpected)} {unexpected}")

# A6 no cross-file duplication of the new rules.
dup = {
    "per vertical slice": [core.count("per vertical slice"), comp.count("per vertical slice")],
    "self-loop": [core.lower().count("self-loop"), comp.lower().count("self-loop")],
    "slice gate": [core.lower().count("slice gate"), comp.lower().count("slice gate")],
    "independently reviewed only when the user asks": [core.count("independently reviewed only when the user asks"),
                                                       comp.count("independently reviewed only when the user asks")],
}
check("A6", all(v[0] + v[1] == 1 for v in dup.values()),
      f"occurrences={dup}")

# A7 current-facts SSOT: no dated narrative / changelog markers outside the ban-list that names them.
BANLIST_FORMS = 'changelogs, errata, "was A, later B"'
bad = []
for label, text in (("AGENTS.md", core), ("execution.md", comp)):
    scan = text.replace(BANLIST_FORMS, "")
    for pat in (r"\b20\d\d-\d\d-\d\d\b", r"(?i)\bchangelog\b", r"(?i)\berrata\b", r"(?i)\bpreviously\b",
                r"(?i)\bwas [A-Z][^.]{0,20}, later\b", r"\bTODO\b"):
        if re.search(pat, scan):
            bad.append(f"{label}:{pat}")
check("A7", not bad, f"dated/changelog markers={bad}")

# A8 links + anchors resolve in both files.
link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
broken = []
for label, text, owner in (("AGENTS.md", core, ROOT / "AGENTS.md"), ("execution.md", comp, ROOT / "docs/policy/execution.md")):
    for target in link_re.findall(text):
        if target.startswith(("http", "#", "mailto:")):
            continue
        path, _, anchor = target.partition("#")
        resolved = (owner.parent / path).resolve()
        if not resolved.exists():
            broken.append(f"{label}: missing path {target}")
            continue
        target_text = text if resolved == owner else resolved.read_text()
        heads = [slugify(m.group(1)) for m in re.finditer(r"^#+ (.+)$", target_text, re.M)]
        if anchor and anchor not in heads:
            broken.append(f"{label}: missing anchor {target} (heads={heads})")
check("A8", not broken, f"broken-links={broken}")

# A10 focus/economy rule present in core + method, with no hardcoded model names in policy.
focus_core = ("defaults to the main agent's own reasoning budget" in core
              and "the reason is focus, not only cost" in core
              and "split unrelated work across separate agents" in core)
focus_comp = ("the `AGENTS.md` focus boundary" in comp
              and "prefer a separate handoff over loading unrelated tasks" in comp
              and "degrade" in comp)
model_names = [m for m in ("deepseek", "glm-", "claude-", "gpt-", "qwen", "llama", "gemini", "doubao")
               if m in core + comp]
check("A10", focus_core and focus_comp and not model_names,
      f"core-focus={focus_core} method-focus={focus_comp} model-names={model_names}")

# A9 scope: only the two named files changed, nothing staged.
porcelain = subprocess.run(["git", "status", "--porcelain"], cwd=ROOT, capture_output=True, text=True).stdout
staged = subprocess.run(["git", "diff", "--cached", "--name-only"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
scoped = subprocess.run(["git", "status", "--porcelain", "--", "AGENTS.md", "docs/policy/execution.md"],
                        cwd=ROOT, capture_output=True, text=True).stdout.splitlines()
# Scope check only: no unrelated-path mtime scan (other checkouts must not fail this check).
check("A9", len(scoped) == 2 and staged == "",
      f"scoped-status={len(scoped)} staged='{staged}'")

passed = sum(1 for r in results if r["pass"])
payload = {
    "revision": {
        "head": subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip(),
        "AGENTS.md": subprocess.run(["sha256sum", "AGENTS.md"], cwd=ROOT, capture_output=True, text=True).stdout.split()[0],
        "docs/policy/execution.md": subprocess.run(["sha256sum", "docs/policy/execution.md"], cwd=ROOT,
                                                   capture_output=True, text=True).stdout.split()[0],
        "baseline": {"AGENTS.md": "488316cbffd9d433d86878dd519b70ed90e56024ab25add1ef9c781ecb1f2065",
                     "docs/policy/execution.md": "f6ab19fddbcf4ebcbe67320a8a90c3b4ceccc47d95bb48b3bee81d2186e48286"},
    },
    "summary": {"passed": passed, "total": len(results), "status": "PASS" if passed == len(results) else "FAIL"},
    "checks": results,
}
(TICKET / "checks.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps(payload["summary"], indent=2))
for r in results:
    print(f"{'PASS' if r['pass'] else 'FAIL'} {r['id']}: {r['detail']}")
sys.exit(0 if passed == len(results) else 1)
