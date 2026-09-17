# Work management

Load when:
- Before the first repository mutation that is multi-file, behavior-changing, delegated, risky, review-gated, commit-producing, or likely to outlive the session; also when parking or resuming work.

Do not load when:
- Work is read-only and is neither parking nor resuming, or it is a low-risk single-file correction that meets no load condition and is completed and validated in the current session.

Applies while:
- Tracking ownership, durable state, branches, commits, review, bounded execution, continuity, parking, and integration for the objective.

Exit when:
- The objective is integrated and accepted, or a durable park records status, evidence, blocker, and next step.

## R-TKT — Tickets, commits, and review

**R-TKT.1 — Ticket trigger.** Create or use a durable ticket for multi-step, behavior-changing, delegated, risky, review-gated, or session-outliving work. Policy changes always require one. A low-risk single-file correction finished this session may rely on its scoped diff and validation evidence instead. One ticket owns one concern; discovered unrelated work gets a separate ticket.

**R-TKT.1.1 — Layout and identity.** Use `.scratch/NN-<feature-slug>/spec.md` when a feature specification is needed and `.scratch/NN-<feature-slug>/issues/NN-<slug>.md` for one issue. Choose the next unused ordinal from current on-disk state; never reuse numbers. Use stable problem-domain kebab-case names and join an existing issue rather than creating a synonym. If remote mode independently triggers, load `remote-coordination.md` before allocating from shared state.

**R-TKT.1.2 — Status.** Preserve these exact statuses:

- Triage: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`.
- Work: `claimed`, `done`, `deferred`, `split`.

New incoming work starts `needs-triage`. Missing input exits to `ready-for-agent` when supplied. `ready-for-human` exits after the recorded decision to `ready-for-agent` or `wontfix`. `deferred` re-enters triage when its trigger occurs. Reopen `wontfix` as a new ticket when evidence changes. A split records successors before the original becomes done. Parking is session state; set the ticket status that truthfully describes its durable queue state.

**R-TKT.1.3 — Ticket content.** Record status, issue, objective or acceptance criteria, blockers, `Need-review`, `Need-test-cases`, and append-only timestamped comments naming actor and material change. Keep a ticket small enough for its specification, relevant source, and diff to be reviewed in one pass; split oversized work with explicit `Blocked by` edges. A research ticket produces a decision; an implementation ticket produces a narrow end-to-end result. Record reusable knowledge in its durable home and link it rather than duplicating it.

**R-TKT.1.4 — Commits.** Each commit is coherent, truthful, and references its ticket when one exists. Do not make empty, speculative, or unrelated commits. Record relevant branch and implementation revisions in the ticket when committing. Triage by dependencies, user priority, then impact relative to effort. Push or shared-state behavior is governed only if remote mode independently triggers and `remote-coordination.md` is loaded.

**R-TKT.2 — Review.** `Need-review: yes` gates integration. Use a fresh-context reviewer with the objective, acceptance criteria, and scoped diff; ask for correctness, edge cases, conformance, simplicity, and evidence. Record reviewer or role, reviewed diff hash, findings disposition, and verdict. If no independent reviewer exists, perform and record a fresh scoped self-review; user review is required only by a core acceptance or material-decision gate. Fix every blocking finding and rerun affected checks before another review. A review loop that stops yielding progress triggers diagnosis, rescoping, delegation, or parking rather than automatic user interruption.

**R-TKT.3 — Branching and isolation.** Use a dedicated branch or worktree for delegated writers, risky work, multi-commit work, or unfinished implementation that must not touch shared main. A small clean concern may finish directly on the current branch. Two writers never share a worktree or branch. Preserve pre-existing changes and integrate only the scoped objective. If remote mode independently triggers, load `remote-coordination.md` before shared synchronization or handoff.

**R-TKT.4 — Self-sufficiency.** Repository methods must remain usable without optional skills or trackers. Use an installed compatible workflow when helpful; otherwise apply these in-repository rules directly. Missing tooling changes the method, not the acceptance bar.

## R-SES — Session continuity and bounded work

**R-SES.1 — Bootstrap.** At the start or on resume, read `WORKSPACE.md`, the relevant ticket and authoritative docs, inspect actual paths and state, and verify assumptions against the repository. Harness memory and folder names are not evidence.

**R-SES.1.1 — Serialization.** When knowledge would take more than roughly ten minutes to re-derive or has survived more than one failed attempt, write it once to the durable home that owns it and link it from `WORKSPACE.md` or the ticket as appropriate. Do not copy the knowledge into multiple indexes.

**R-SES.1.3 — Cognitive load.** Externalize durable state at the point of use and keep the active plan limited to current decisions, dependencies, and evidence. Prefer discoverable repository state over remembered instructions. Remove stale plans when evidence invalidates them.

**R-SES.2 — Focus and parking.** After two focused failed approaches or roughly 30 minutes without useful progress, diagnose the obstacle and choose among design reformulation, delegation, narrower reproduction, durable parking, or another queued task. The threshold does not itself trigger user contact. A park records status, attempted evidence, current blocker, and exact next step; re-entry starts from that record. Never work around an irreversible or user-owned choice.

**R-SES.3 — Time economy.** Give every command and tool call an expected-duration timeout. Wait for an observable event or readiness probe, not elapsed time alone. Non-exiting services need bounded health, log, or port checks. Make long operations resumable and overlap independent useful work when safe.
