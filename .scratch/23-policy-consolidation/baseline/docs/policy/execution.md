# Execution, delegation, and independent review

Use the relevant section for dispatch, decomposition, checks, review/repair, interruption, or resumption. Main routes work and status; execution, integration, and technical acceptance belong to assigned workers/reviewers.

## Dispatch and task contracts

- Parent dispatches a narrow packet: objective, scope/exclusions, authoritative inputs, inherited acceptance/proof, owners, outputs, dependencies, authority/user gates, and stop conditions. Set finite resource limits and an observable status/completion path using actual tools. Send status and pointers, not conversation dumps.
- For the core's exceptional worker inheritance, supply only essential context. Reviewers never receive worker conversation. Prose cannot grant tools or recursive delegation permission.
- Before changes, the worker inspects target/Git state and relevant instructions/current record, then writes the core's upfront contract. Preserve pre-existing dirt and capture a scoped baseline when attribution matters. Resolve routine gaps with task-scoped evidence and reversible choices; record consequential assumptions.
- If acceptance cannot be met, record the unmet criterion/dependency, not reduced scope or routine supervisor questions. Required authority/infrastructure escalation uses a minimal signal pointing to the concrete issue and recommendation in the record.

## Decomposition and context replacement

- Split only into sibling outcomes at the same abstraction layer under one parent. For each child name inputs, output, acceptance/proof, owner, interfaces, dependencies, and exclusions. Map the children to complete parent coverage and assign an execution integration owner for cross-child behavior and final checks. Unequal size is allowed; the parent goal beside its tiny substep is not.
- Keep a cohesive independently checkable outcome as a leaf; do not split editing/testing/reporting into artificial deliverables or forward the unchanged task through more agents. Main delegates even a leaf. Workers recurse only when explicitly permitted and supported, within recorded concurrency/depth/time bounds; otherwise keep the leaf or return a decomposition record for routing.
- Parallel writers need disjoint ownership and isolated branches/worktrees. Record shared interfaces/dependency order first; the integration worker preserves baseline changes and checks the combined result. Do not parallelize one coupled seam merely to create fanout.
- At insufficient context, checkpoint completed artifacts, remaining acceptance, decisions, revision, and next actions. Split remaining independent outcomes with explicit coverage/interfaces, or hand an unsplittable remainder to a fresh replacement under the same acceptance/authority. Report observed pressure, not a made-up percentage; do not restart an infinite delegation chain.

## Worker proof

- Implement only the authorized behavior. For a defect, reproduce it where practical and use a check capable of catching it. Run target-project gates and risk-driven checks; inspect the scoped final diff and run scoped `git diff --check` for text. If hardware, a runner, or an external system is unavailable, perform feasible checks and identify the unexercised acceptance criteria.
- Bind evidence to the commit or working-tree hashes, commands/results, and inspectable artifacts; rerun invalidated checks. Separate unrelated existing failures from introduced ones. Self-tests are not independent acceptance; completion claims and unrun tests are not proof.
- Integration checks the combined parent outcome/interfaces, not child verdicts. Store results/limitations in evidence files and notify with status/pointers; upper layers read only what their responsibility needs.

## Adversarial review and repair loop

1. Give a fresh reviewer objective, full acceptance, final scoped artifact/revision, evidence, constraints, and repair authority/tools, never worker conversation. The reviewer inspects actual artifacts/proof, attempts to falsify acceptance, and checks missing scope, safety, regressions, and stale evidence; worker verdicts are not authority.
2. Record material in-scope verifiable defects with location, violated criterion, and evidence/reproduction. If authorized and capable, repair as a worker, relinquishing independent acceptance. Otherwise label an assigned-writer fallback and route to an authorized writer; read-only reviewers gain neither tools nor authority by prose.
3. After repair and renewed self-tests, assign a new fresh reviewer to the current artifacts/evidence. Iterate on material defects, not speculative polish; record non-blocking limitations without inventing requirements.
4. PASS requires documented full acceptance at the reviewed revision. Missing proof, blocked checks, and unknown acceptance are not PASS. Unavailable independent review is an infrastructure blocker and incomplete acceptance, never a self-review substitute.

Set finite review/time/resource and no-progress bounds at dispatch. On exhaustion, save a discoverable checkpoint with unresolved criteria and the next useful action, and report incomplete. Do not loop for perfection, certify zero unknown defects, or treat technical PASS as permission to commit, publish, or cross a user gate.

## Progress and recovery

- After status, continue the next authorized step. For long work, record result path, deadline/cancellation, and verified foreground/notification/active bounded-check continuation. Detached jobs, records, and promises do not wake an agent; claim background continuation only when established.
- When attempts no longer produce useful evidence, change the hypothesis/check, narrow reproduction, or route a bounded specialist task if available and permitted. Continue independent work while a dependent action awaits indispensable user input, authority, or an agreed gate. For research, stop repetitive avenues that cannot change the conclusion. Stopping with unmet acceptance is incomplete, even when no useful authorized step remains.
- Reuse the target project's work-record convention. If no active entry point exists, use project-root `.scratch/active-work.md`; preserve other entries. Keep an unfinished task discoverable with objective/scope/acceptance, owner/status, input/output paths, granted authority and user gates/availability, decisions/assumptions, baseline/current revision and dirty files, checks/review and covered revision, unresolved criteria/blockers, next action, and running-job result/continuation if any. Remove only this task's active link after independently accepted closure and any agreed user gate.
- On resumption, compare the durable record to current target/Git state, recover authoritative decisions and ownership, and rerun stale checks. Do not substitute session memory or an old test result for the current artifact. Use task/decision/evidence/handoff files as the communication channel; reserve control signals for status/pointers and required escalation.
