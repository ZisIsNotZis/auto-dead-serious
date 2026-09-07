# 02 — Ordinal lock: two-level numbering + canonical slugs

- **Status:** claimed
- **Blocked by:** none
- **Assignee/lock:** VPO (main session)

## Issue

Follow-up to 01 (PO refinement): extend collision-by-design to a two-level ordinal lock.
Duplicate ordinal = mechanical proof of a stale view (concurrent creation), independent of
git path conflicts. Constraints from PO: nothing ships besides AGENTS.md itself — the
allocator/checker script is spec'd inline so any agent writes it on the fly; synonym
duplication is a capability (IQ/prompting) problem, addressed by a canonical-slug naming
rule, not machinery.

## Acceptance criteria

- [ ] Tickets 1.1: two-level numbering format (`NN-feature/issues/NN-slug.md`), max+1 allocation from fetched state, never reused, canonical-slug rule with join-don't-fork instruction.
- [ ] Sync 6.4 rewritten: ordinal lock with inline one-sentence algorithm spec (fetch → max numeric prefix + 1); duplicate = stale-view proof; resolve by merge-or-renumber-retry; git non-FF still catches identical paths.
- [ ] Existing categories migrated: `01-agents-md-systematization`, `02-agents-md-sync-protocol`.
- [ ] AGENTS.md ≤ 200 lines, `git diff --check` clean.

## Comments

- 2026-09-04 (VPO, pi coding agent, volc2/glm-5.3-flash) — Created and claimed from PO's approval round ("others seems fine"; ship only AGENTS.md; script spec'd inline, not shipped).
