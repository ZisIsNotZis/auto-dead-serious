# 01 — Orchestration ladder rule

- **Status:** done
- **Blocked by:** none
- **Assignee/lock:** agent (pi, volc2/glm-5.3-flash)

## Issue

PO direction after discussion rounds: five-mode orchestration ladder ordered by plan
binding force — workflow (subagent tree, one-pass graph with gates inside) > PTC (tool
program; agents via harness API ok with native governance, external CLI user-gated) >
bash script > forced continuation (/goal, /loop — persistence not orchestration) >
step-by-step + reminders (mirror only). Plus companion clauses: mid-to-high complexity →
delegate, main session orchestrates; repo-writable tools over harness-global state;
single-line-too-long sed case in Proper tools 12.

## Acceptance criteria

- [x] Sessions & tools 13 (Orchestration ladder) added; Proper tools 12 extended.
- [x] Consistency with Delegation 3, Tickets 1 (todo mirror), Self-knowledge 5 (CLI gate), Sessions 1.3 — references not restatements.
- [x] Subagent review: OK with notes (6 P2, no P1) — all fixed: delegation-test pointer, bash-mode selection test, durable-knowledge vs execution-state scoping (1.3 ↔ 13 cross-link), harness execution-plan wording, Delegation no-subagent fallback. 156 lines.

## Comments

- 2026-09-04 (agent, pi coding agent, volc2/glm-5.3-flash) — Created and claimed from the ladder discussion (turn-based billing + context re-entry tax favor one-pass emission; semantic forks become in-graph decision agents).
