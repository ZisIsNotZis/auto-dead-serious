# 03 — Final migration check + zh translation

- **Status:** claimed
- **Blocked by:** none
- **Assignee/lock:** agent (pi, volc2/glm-5.3-flash)

## Issue

Quick fresh-context check of the PO-analogy removal (reviewer found the sed over-reach:
"assumes the PO role" had become "assumes the user role" — P1 — plus a phantom "user
role"); fix, then translate AGENTS.zh-CN.md to full parity with the final English.

## Acceptance criteria

- [ ] Collab 1 restored: "assumes the PO role (Stage 1)", "decide as the user would".
- [ ] AGENTS.zh-CN.md mirrors final EN rule-for-rule (144 lines).
- [ ] `git diff --check` clean on both files.

## Comments

- 2026-09-04 (agent, pi coding agent, volc2/glm-5.3-flash) — Created and claimed; reviewer verdict BLOCK on the self-inflicted rename (validated, fixed below).
