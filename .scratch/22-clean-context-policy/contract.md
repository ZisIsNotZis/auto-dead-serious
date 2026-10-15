# Clean-context policy redesign — contract and rationale

Status at kickoff: authorized implementation; independent acceptance pending. Current handoff: [summary.md](summary.md). One implementation writer; parent owns review and acceptance. Authority: the user's explicit implementation request and approved design in this task. Scope is policy text, not runtime configuration.

## Outcome and scope

Deliver a portable, selectively loaded agent policy package: a slim shared core, a user-facing product-owner main, execution workers, and fresh independent reviewers. Remove inherited workspace-document dependencies without deleting workspace artifacts. Preserve instruction hierarchy, safety, granted autonomy, revision-bound evidence, and recovery.

Edit only `AGENTS.md`, its five `docs/policy/*.md` companions, this `.scratch/22-clean-context-policy/` record, and a minimal additive entry in `.scratch/active-work.md`. Do not alter `WORKSPACE.md`, README, child repositories, global configuration, the index, history, or unrelated records. Existing dirty policy content is the implementation baseline, not newly authored work; preserve its safety, user-facing expression, autonomy, and continuation requirements unless superseded by this approved redesign. Preserve `.scratch/21-autonomous-work-policy` byte-for-byte.

## Acceptance and proof

- Package works without ancestor `WORKSPACE.md`/README facts or blanket document reads; policy references are owner-relative, project evidence task-scoped.
- Main always delegates substantive work, including small/indivisible tasks; no execution or technical-verification fallback when delegation is unavailable.
- Workers record a pre-change contract, keep inherited acceptance, self-test, and produce durable evidence. Decomposition has peer outcomes and complete coverage; late splitting/replacement is bounded by actual runtime capabilities.
- Fresh narrow packets are the default; essential-session inheritance is exceptional; reviewers never inherit worker conversation. Agent communication is through records plus minimal control signals and indispensable escalations.
- Adversarial review checks actual artifacts and revision-bound evidence, repairs material in-scope defects through an authorized reviewer or labelled writer fallback, then requires a fresh reviewer. PASS is evidenced; blocked/unknown/resource exhaustion is incomplete, not success.
- Authorized routine decisions continue autonomously; explicit user gates and safety/authority boundaries remain binding. Product milestones are conditional user outcomes, not mandatory gates for this policy edit. Feedback updates originating decisions and affected work without inventing a user profile.

Proof: baseline snapshots and diff; core/package size before/after; reference audit; scoped whitespace check; source-bound scenario matrix (isolation, small task, worker contract, sibling/late split, replacement, fresh review/repair, absent user/gate, unavailable delegation, safeguards, feedback); final policy hashes; preservation checks. These are documentation checks only. Parent must arrange independent fresh review before closure; implementation self-checks cannot substitute for it.

## Choices and decomposition

Choose one compact shared-boundary core with short role rules, and event-triggered methods in the existing five companions. Reject a monolithic expanded core and a mandatory companion read chain: both defeat clean-context loading. Reject direct-main fallback, optional independent acceptance, and generic documentation-context inheritance because the user explicitly disallowed them. Keep topic filenames and reusable safety methods; remove workspace-specific ticket conventions and mandatory workspace reads.

This is one coupled leaf outcome: role boundaries, routing, decomposition, communication, and review must agree across the whole policy package. Mechanical edit/check steps are not sibling deliverables; parallel writers would introduce conflicting ownership. No recursive fanout is needed or available to this worker. Independent review is a separate acceptance role, not another implementation subtask. Reversible wording/layout choices are resolved within the approved design, not sent as routine questions.

## Baseline and continuation

Starting HEAD: `c82765e53faa60ae04cc3ae4fd1048d1ee5ef953`. Starting policy contents, HEAD diff, status, counts, and protected-file hashes are in `baseline/`. Original dirty files: `AGENTS.md`, `docs/policy/decisions.md`, `docs/policy/execution.md`; unrelated child dirt is recorded, not touched. Core: 6,694 characters / 905 words; package: 22,637 characters / 3,140 words (WORKSPACE excluded intentionally).

Plan recorded before policy edits: implement all policy seams, self-check the final scoped artifacts, write evidence and user-readable summary, return pointers for independent review. Keep the active-work link until independently accepted closure; remove only this task's link then.
