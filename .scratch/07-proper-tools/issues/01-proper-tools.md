# 01 — Proper tools rule (builtin over bash)

- **Status:** claimed
- **Blocked by:** none
- **Assignee/lock:** agent (pi, volc2/glm-5.3-flash)

## Issue

PO direction: always prefer the harness's built-in tools (read/write/edit/search) over
the bash tool; sed/grep/cat etc. only when no builtin covers the job — batch edits across
many sites being the legitimate sed case. Self-observed this session: grep/sed used where
read/edit existed.

## Acceptance criteria

- [ ] New Sessions & tools rule 12 (Proper tools) in EN; zh parity line added.
- [ ] 145→146 lines each, `git diff --check` clean. Review skipped per PO's standing preference for dictated one-liners.

## Comments

- 2026-09-04 (agent, pi coding agent, volc2/glm-5.3-flash) — Created and claimed.
