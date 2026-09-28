# Execution, handoff, and validation

Use when executable work needs checks, or work needs a durable handoff, concurrent ownership, delegation, or a review trail. A self-contained task finished in one session needs no ticket merely because code or multiple files changed.

## Delivery and evidence

- Implement the approved behavior without silently widening contracts. For defects, reproduce where practical and use a check capable of catching the failure. Run applicable project gates and risk-driven checks; inspect the scoped diff and run `git diff --check` for textual changes. If hardware, external systems, or a runner is unavailable, perform feasible checks and name the unexercised behavior.
- Tie a completion claim to the command/result or inspected artifact and the actual commit or working-tree revision. Rerun checks invalidated by later edits. Resolve first-party failures or explicitly report them; a worker verdict or unrun test is not evidence. For consequential subjective output, seek independent review if useful; otherwise state the self-review limit.
- When attempts stop yielding evidence, change the hypothesis or boundary, narrow reproduction, seek review, delegate, or leave a recoverable handoff. Elapsed time and attempt count are diagnostic prompts, not automatic permission or user-contact gates.

## Recoverable work

- Use a discoverable work record when work spans sessions, concurrent writers, consequential decisions, or a review trail the diff cannot explain. In this workspace, existing local issues live under project-root `.scratch/NN-<feature-slug>/issues/NN-<slug>.md`; reuse one for the same concern. Preserve an existing ticket's status convention rather than inventing a synonym.
- For unfinished work record objective and completion criteria, owner/status, work-item path, branch/revision and relevant dirty files, checks and the revision they cover, pending decisions, blocker, and next executable step. If no current-work entry exists, link active items from project-root `.scratch/active-work.md`; remove completed links. On resume, compare the record with current Git state and rerun stale checks rather than trusting session memory.
- Isolate concurrent writers in separate branches or worktrees; preserve pre-existing changes and integrate only the approved concern. Seek independent review for consequential risk or a declared gate, providing objective, criteria, and scoped revision; record findings and disposition. Low-risk work may use scoped self-review. User review is reserved for a user-owned decision or agreed checkpoint.

## Delegation

- Delegate independently verifiable or specialist work when benefit exceeds handoff cost; duration alone is not a trigger. Assign one owner per task and disjoint ownership to parallel writers. The parent checks evidence, integrates results, and owns acceptance.
- Give a fresh worker objective, scope, authoritative inputs, criteria, constraints, validation, output, and stop condition. Use inherited context only when a compact handoff loses essential meaning. For adversarial critique, provide the artifact and criteria without the author's verdict, then verify findings.
- Define expected progress and cancellation before launch; observe logs, status, and artifacts rather than elapsed time alone. Inspect evidence and try a focused recovery before terminating a stalled worker. Release resources after use. If a worker is unavailable, use safe parent execution or documented self-review and report remaining limitations.
