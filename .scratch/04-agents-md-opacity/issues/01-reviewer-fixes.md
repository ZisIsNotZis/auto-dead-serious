# 01 — Opacity-pass fixes from fresh-context review

- **Status:** done
- **Blocked by:** none
- **Assignee/lock:** VPO (main session)

## Issue

Fresh-context reviewer (fork=false, opacity-only axis) returned BLOCK: 1 P1 + 14 P2. All 15
verified against the text and accepted; reviewer's fix for #2 (pre-push check) was corrected
— it means the ordinal check as a git pre-push hook, not the Repository-files-4 gate.
Additionally PO supplied the externalization preference ladder for Sessions 1.3:
harness mechanisms (skills, hooks, plugins, goals) > scripts/ > AGENTS.md/WORKSPACE.md >
docs/ > remembering on the fly.

## Acceptance criteria

- [x] P1: Repository files 3 evidence committed-vs-ignored contradiction resolved (evidence is committed).
- [x] All 14 P2s applied (see commit).
- [x] Sessions 1.3 carries the PO's externalization ladder.
- [x] AGENTS.md ≤ 200 lines (143), `git diff --check` clean.

## Comments

- 2026-09-04 (VPO, pi coding agent, volc2/glm-5.3-flash) — Created and claimed; reviewer session file referenced in PO chat; findings verified one-by-one before acceptance.
- 2026-09-04 (VPO, pi coding agent, volc2/glm-5.3-flash) — All 15 findings + ladder applied in one batch (17 edit blocks). Verified: 143 lines, git diff --check clean, no stale phrasings ("not directly writable" ×0, "<feature>/" ×0).
