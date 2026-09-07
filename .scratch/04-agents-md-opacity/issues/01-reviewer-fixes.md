# 01 — Opacity-pass fixes from fresh-context review

- **Status:** claimed
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

- [ ] P1: Repository files 3 evidence committed-vs-ignored contradiction resolved (evidence is committed).
- [ ] All 14 P2s applied: pre-push check defined, PO-gated ↔ Review 4 linked, lock "set" defined, full/partial conflict operational test, people-doc pointer, timer interval 15–30 min, clarity-test trigger/actor, philosophy single home, artifact scan defined, user-level installs reconciled, skill-deletion counter trackable, "directly writable" operational test, context-window test, evidence path NN- prefix.
- [ ] Sessions 1.3 carries the PO's externalization ladder.
- [ ] AGENTS.md ≤ 200 lines, `git diff --check` clean.

## Comments

- 2026-09-04 (VPO, pi coding agent, volc2/glm-5.3-flash) — Created and claimed; reviewer session file referenced in PO chat; findings verified one-by-one before acceptance.
