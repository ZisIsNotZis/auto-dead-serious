# 01 — Compaction to size budget

- **Status:** claimed
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

- [ ] Doc 6.2 Size economy + 4.1 Compact strengthening added.
- [ ] Full caveman rewrite, try-best toward 10K; report honest floor + what 10K would cost.
- [ ] Loss-detection review (old @ .tmp/AGENTS-old.md vs new) — non-trivial info loss = fix; `git diff --check` clean.

## Comments

- 2026-09-04 (agent, pi coding agent, volc2/glm-5.3-flash) — Created and claimed.
