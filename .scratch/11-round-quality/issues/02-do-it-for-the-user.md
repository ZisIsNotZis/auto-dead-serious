# 02 — Do-it-for-the-user rule

- **Status:** claimed
- **Blocked by:** none
- **Assignee/lock:** agent (pi, volc2/glm-5.3-flash)

## Issue

PO refinement of the invocation philosophy: (1) open artifacts/URLs for the user actively
(browser, editor, file manager; playwright/computer-use in extremes) — never hand him
instructions unless the key step is genuinely his (device-login code), and prepare
everything around that step in advance; surface what interests him (Audience). (2)
Consolidate legitimate user-invocation triggers: decisions/confirmations, subjective
judgment, stuck >30min (Focus), missing permissions, inaccessible environments. (3) When
invoking: background + viable options each with recommendation/pros/cons — no obviously
bad options, nothing beyond TLDR. 7.4's "openable" becomes "opened".

## Acceptance criteria

- [ ] New Collab rule 11 (Do it for the user); 7.4 amended.
- [ ] No restatement of Ask/Focus/6.2/6.4 content — triggers referenced by owner.
- [ ] Positive phrasing, one-line style, `git diff --check` clean. Review skipped per PO's standing preference.

## Comments

- 2026-09-04 (agent, pi coding agent, volc2/glm-5.3-flash) — Created and claimed.
