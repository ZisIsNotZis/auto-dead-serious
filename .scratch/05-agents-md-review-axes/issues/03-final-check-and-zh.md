# 03 — Final migration check + zh translation

- **Status:** done
- **Blocked by:** none
- **Assignee/lock:** agent (pi, volc2/glm-5.3-flash)

## Issue

Quick fresh-context check of the PO-analogy removal (reviewer found the sed over-reach:
"assumes the PO role" had become "assumes the user role" — P1 — plus a phantom "user
role"); fix, then translate AGENTS.zh-CN.md to full parity with the final English.

## Acceptance criteria

- [x] Collab 1 restored: "assumes the PO role (Stage 1)", "decide as the user would".
- [x] AGENTS.zh-CN.md mirrors final EN rule-for-rule (144 lines).
- [x] `git diff --check` clean on both files.

## Comments

- 2026-09-04 (agent, pi coding agent, volc2/glm-5.3-flash) — Reviewer verdict BLOCK on the self-inflicted rename (validated, fixed below).
- 2026-09-04 (agent, pi coding agent, volc2/glm-5.3-flash) — P1 fixed (PO role restored in Collab 1); zh translation written to 144/144 line parity. Both committed as 2ae2125.
