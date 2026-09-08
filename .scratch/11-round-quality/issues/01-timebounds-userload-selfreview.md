# 01 — Time bounds, user cognitive load, round self-review

- **Status:** claimed
- **Blocked by:** none
- **Assignee/lock:** agent (pi, volc2/glm-5.3-flash)

## Issue

PO direction, three items: (1) every command/tool call runs with a proper time bound and
prefers resumable operations (checkpoints, idempotent steps) — in code/scripts too — so a
timeout never strands the user; subagent kills become last resort (multiple pings, evidence
gathering from all sources, resume-over-kill). (2) User cognitive load reduction: cut
mannered prose/jargon, decision-points-only attention filter, ELI5 words, structured forms
(tables/lists/checkboxes), visual artifacts (HTML/mermaid/plots) openable directly. (3)
End-of-round honest self-review ritual (right/wrong/worse, deliverable grading, best
representation form).

## Acceptance criteria

- [ ] Sessions 11 gains time-bound + resumability clause; Delegation 3 kill protocol revised (evidence → resume preference).
- [ ] Collab 7.1 attention filter; 7.2 extended visual forms; new 7.4 round self-review.
- [ ] Quick checklist review passes; `git diff --check` clean.

## Comments

- 2026-09-04 (agent, pi coding agent, volc2/glm-5.3-flash) — Created and claimed.
