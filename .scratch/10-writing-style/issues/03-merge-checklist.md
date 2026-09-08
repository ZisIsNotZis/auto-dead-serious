# 03 — Merge 4.2+4.3 into one dual-use checklist, positive phrasing

- **Status:** done
- **Blocked by:** none
- **Assignee/lock:** agent (pi, volc2/glm-5.3-flash)

## Issue

PO: (1) merge the docs-related rules — 4.2 (check) and 4.3 (writing) are one list with two
duties, not two rules; (2) stop repeating 6/6.1/Sessions 1.3 content inside the checklist —
point at owners; (3) the checklist itself must obey the positive-phrasing rule it just
adopted (previous draft was full of negations). 4.1 (QA pairs) stays — distinct mechanism.

## Acceptance criteria

- [x] Doc 4.2 = single bulleted checklist, dual use (authoring follow-list + review rubric), positive phrasing throughout, owners referenced not restated.
- [x] Doc 4.3 removed; QA-pair mechanism (old 4.1) removed entirely per PO addendum — Doc 3 exemption reverted, 6.1 reference dropped; grep-verified zero dangling refs.
- [x] `git diff --check` clean (153 lines).

## Root-cause note
PO asked why reviews never flagged the QA mechanism: reviewers checked internal consistency, so they validated the premise instead of challenging it (round-7 even patched the SSOT conflict via exemption rather than questioning the mechanism). The necessity/no-ops axis that would have caught it did not exist yet, and QA predated the checklist. Lesson: the new necessity axis now covers premise-challenge; reviewers should grill mechanisms, not just their wiring.

## Comments

- 2026-09-04 (agent, pi coding agent, volc2/glm-5.3-flash) — Created and claimed; continuation of 02's checklist work.
