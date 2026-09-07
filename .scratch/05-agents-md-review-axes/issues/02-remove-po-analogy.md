# 02 — Remove the user=PO analogy

- **Status:** done
- **Blocked by:** none
- **Assignee/lock:** VPO (main session)

## Issue

PO decision: the user is no longer equated with "product owner". The agent plays the
lifecycle roles — first assuming the PO role (Stage 1) when a requirement arrives, then
walking the stages the task needs. All references to the human as "the PO" become "the
user"; VPO (defined only relative to user=PO) is removed; "Stage 1 — PO" remains the
agent's role name.

## Acceptance criteria

- [x] Collab 1 rewritten (user & roles framing); Collab header de-PO'd.
- [x] All human-referencing "PO" occurrences → "user" (mechanical sed + verified grep).
- [x] Only remaining "PO" = Stage 1 role name; `git diff --check` clean.

## Comments

- 2026-09-04 (VPO, pi coding agent, volc2/glm-5.3-flash) — Created and claimed from PO's terminology decision.
- 2026-09-04 (VPO, pi coding agent, volc2/glm-5.3-flash) — Collab 1 rewritten manually (last manual PO-analogy edits), then 24 sed patterns; grep verified: sole remaining "PO" is the Stage 1 role heading. 144 lines, clean. Note: future ticket comment entries should use "agent (pi, <model>)" or a role label instead of VPO.
