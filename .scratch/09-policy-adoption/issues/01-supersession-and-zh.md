# 01 — Supersession rule + zh removal

- **Status:** claimed
- **Blocked by:** none
- **Assignee/lock:** agent (pi, volc2/glm-5.3-flash)

## Issue

PO direction: (1) when this AGENTS.md is swapped into an existing setup (replacing the
original system prompt), strictly adhere to what it says no matter what previous behavior
was — no habit carryover; (2) delete AGENTS.zh-CN.md — translation is PO's own showcase
job, not practical use; parity maintenance ends.

## Acceptance criteria

- [ ] Supersession clause added to the intro (precedence context).
- [ ] AGENTS.zh-CN.md removed via git rm; no dangling references to it.
- [ ] Fresh-context reviewer run completed (redo — previous two spawns aborted); findings triaged.

## Comments

- 2026-09-04 (agent, pi coding agent, volc2/glm-5.3-flash) — Created and claimed. Note: Go-signal 8's bilingual-mirror clause stays — it is general guidance, no longer tied to a repo file.
