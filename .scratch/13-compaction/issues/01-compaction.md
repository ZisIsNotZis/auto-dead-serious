# 01 — Compaction: 61.7K → target <32K chars, whys kept

- **Status:** claimed
- **Blocked by:** none
- **Assignee/lock:** agent (pi, volc2/glm-5.3-flash)

## Issue

PO: file too big (61.7K chars), goal <20K originally, recalibrated on PO's instruction to
keep the whys (easier to remember, less cognitive load) → telegraphic register, whys kept
where non-obvious, trivial whys dropped. No renumbering (pointers preserved). All numbers,
operational tests, commands, status vocab, and cross-references untouchable.

## Acceptance criteria

- [ ] Rewritten file ≤ ~32K chars; rule inventory identical (156 lines → same rules, no renumbering).
- [ ] Fresh-context loss-detection review (old vs new side by side) passes; findings fixed.
- [ ] `git diff --check` clean.

## Comments

- 2026-09-04 (agent, pi coding agent, volc2/glm-5.3-flash) — Created and claimed. Old file snapshot for the reviewer at `.tmp/AGENTS-old.md`.
