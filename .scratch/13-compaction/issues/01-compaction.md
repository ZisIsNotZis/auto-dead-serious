# 01 — Compaction to size budget

- **Status:** done
- **Blocked by:** none
- **Assignee/lock:** agent (pi, volc2/glm-5.3-flash)

## Issue

PO recalibration: ideal size 10K chars, try-best. Bottom lines: specific & actionable
(numbers/thresholds over descriptions), complete (no non-trivial info lost, no missing
side of the story), minimal whys (only those aiding understanding/memory). Methods:
wording, caveman register, merge/fusion, remove niche examples. Rule goes into the file
itself (Doc 6.2 Size economy + 4.1 Compact bullet) and subagent checks enforce size
efficiency.

## Acceptance criteria

- [x] Doc 6.2 Size economy + 4.1 Compact strengthening added.
- [x] Full caveman rewrite: 61.7K → 48.1K chars (−22%). Loss-detection review (old vs new, rule-by-rule): 1 P1 — Collab 11 accidentally dropped in rewrite, restored compressed; all numbers/tests/commands/rules/whys verified preserved otherwise.
- [x] Honest floor: ~48K is the complete floor under bottom lines (specific+actionable, complete, minimal whys) — 10K would require cutting ~75% of rule content itself, violating completeness. 157 lines, `git diff --check` clean.

## Comments

- 2026-09-04 (agent, pi coding agent, volc2/glm-5.3-flash) — Created and claimed.
