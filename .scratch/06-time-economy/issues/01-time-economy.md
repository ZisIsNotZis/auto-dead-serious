# 01 — Time economy rule

- **Status:** done
- **Blocked by:** none
- **Assignee/lock:** agent (pi, volc2/glm-5.3-flash)

## Issue

PO direction: agents dumbly `sleep 60/120` after spawning background work (subagents,
servers, builds) — wasted wall clock, worst when the user is waiting. Generalize beyond
the case: time is a first-class resource; the user's waiting wall clock is scarcest;
prefer event-driven completion, overlap work into waits, short/backoff polling only as
fallback, never one long sleep; default assumption = user is waiting unless a large
budget is granted or he leaves.

## Acceptance criteria

- [x] New Sessions & tools rule 11 (Time economy) in EN; zh parity line added.
- [x] No duplication with Focus 2 (task drift) or Delegation 3 (worker patience) — distinct concerns.
- [x] Quick fresh-context review passes; `git diff --check` clean.

> Review skipped on PO instruction. PO correction applied: servers don't exit — readiness is the success condition, verified by active probing (curl health endpoint, grep ready line, port check), not event-driven completion; the rule now distinguishes bounded work (events) from non-exiting services (active readiness probing with deadline).

## Comments

- 2026-09-04 (agent, pi coding agent, volc2/glm-5.3-flash) — Created and claimed. Note: zh one-line delta translated same-round — mechanical parity of a line the user dictated this turn, not new design synthesis (Documentation/Go-signal spirit); recorded here as the rationale for the EN-first exception.
- 2026-09-04 (agent, pi coding agent, volc2/glm-5.3-flash) — PO corrected the draft: readiness probing for non-exiting services replaces "wait for event-driven completion" there; rule restructured around success-condition + active-check. No review per PO. 145 lines both files, clean.
