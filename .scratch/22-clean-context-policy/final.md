# Clean-context policy redesign — accepted

**The policy text is implemented and independently accepted.** Main is now explicitly the user-facing product owner: every substantive task goes to workers, and fresh reviewers check actual artifacts and evidence. Small tasks still delegate; unavailable delegation is a blocker, not permission for main to execute.

The package stands alone without mandatory ancestor WORKSPACE/README reads. A smaller core carries safety and role boundaries; five companions load only for concrete events. Workers record their contract before changes. Decomposition, context replacement, repair/re-review, autonomous in-scope choices, binding user gates and feedback all have explicit operational rules.

Safety, unrelated and pre-existing work, secrets, bounded operations, revision-bound proof and recoverable handoffs remain protected. The prior dirty policy changes were captured as baseline; workspace artifacts and prior task records were preserved. No commits, staging, pushes, child-repository edits or global configuration changes were made.

## Evidence and limits

- Independent source/diff and scenario review: [review-1.md](review-1.md).
- Structural, link, size and preservation checks passed; scoped `git diff --check` passed.
- Accepted revision: six working-tree hashes in [final-policy-sha256.json](final-policy-sha256.json), on HEAD `c82765e53faa60ae04cc3ae4fd1048d1ee5ef953`.
- Core: 6,694 → 5,609 characters (905 → 685 words). Package: 22,637 → 22,889 characters (3,140 → 2,953 words). The modest package character growth adds approved operational methods, not mandatory startup load.
- These are **documentation checks only**. Runtime configuration was not shipped; live behavior and enforcement across agent harnesses remain untested. Acceptance is not a promise of zero unknown defects or permission to publish.

This task is closed; only its own active-work link is cleared. Earlier implementation summaries/evidence retain their historical pending-review status; this file and the independent review provide the final disposition.
