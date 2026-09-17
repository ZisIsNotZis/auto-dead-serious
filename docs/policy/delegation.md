# Delegation

Load when:
- Work has multiple independent streams or modules, is expected to exceed roughly 20 minutes, needs specialist expertise, consumes large artifacts or context, requires independent review, or has complex validation.

Do not load when:
- One tightly coupled, low-risk task is expected within roughly 20 minutes, has straightforward validation, and needs neither independent review nor complex validation.

Applies while:
- Decomposing, assigning, isolating, monitoring, reviewing, synthesizing, and reconciling delegated work.

Exit when:
- Worker outputs and evidence are accepted or rejected, ownership is reconciled, and worker slots and worktrees are cleaned up or durably parked.

## R-DEL — Delegation, workers, and models

**R-DEL.1 — Complexity routing.** Delegate when duration, independent workstreams, module breadth, specialist need, validation complexity, or context volume would displace parent orchestration. Keep a tightly coupled low-risk task under roughly 20 minutes with straightforward validation in the parent when delegation overhead would exceed benefit. Decompose by explicit outputs and dependencies; parallelize only disjoint ownership.

**R-DEL.1.1 — Exploratory fanout.** When the goal is clear but the route is genuinely unknown, choose breadth from the user's urgency and effort/token preference. Fan out only hypotheses or approaches that are materially different, independently testable, and separable into clean contexts; near-duplicates stay in one lane. Check shared compute before parallel training, inference, simulation, or other resource-heavy work: serialize or cap concurrency when contention would make every lane slower. This is a judgment based on expected information gain, cost, wall time, and bottlenecks—not a fixed lane count.

**R-DEL.2 — Patience.** Judge progress from harness state, artifacts, logs, or meaningful status, not elapsed time alone. A slow endpoint or difficult task is not dead. Request status only when expected progress is absent or a dependency requires it.

**R-DEL.3 — Liveness and recovery.** Define expected progress and a bounded check when launching a worker. Before termination, inspect available output, worktree diff, logs, and status; send one focused recovery request. Re-engage from durable state when possible. Terminate only after evidence shows the worker cannot progress or its output is no longer needed; preserve useful artifacts first. Do not require periodic heartbeat files unless the active harness specifically depends on them.

**R-DEL.4 — Slots and accountability.** Release completed or failed worker slots promptly. Every task has one current owner. Delegation never transfers parent accountability, and worker completion is input to synthesis rather than acceptance by itself.

**R-DEL.5 — Model selection.** Use the lowest-cost model or tool demonstrably capable of the task, scaling reasoning and context to risk and complexity. Verify the served model or capability when material. Treat model names, prices, and availability as dated `WORKSPACE.md` facts, not durable policy.

**R-DEL.6 — Capability fit.** Match harness, model, context window, modality, and tool access to the task. Escalate capability when evidence shows a mismatch. External services require user involvement only when they introduce material cost, data exposure, or an unapproved dependency; otherwise choose the best available in-scope route.

**R-DEL.7 — Professional roles.** Assign the professional role and evaluation standard the output needs. A recurring role prompt belongs in a reusable project artifact after demonstrated reuse; one-off work gets a complete scoped prompt without speculative process scaffolding.

**R-DEL.8 — Context isolation.** Prefer fresh-context workers when the task can be detached cleanly; their cold-start brief includes objective, scope, authoritative inputs, acceptance criteria, constraints, validation, output, and stop conditions. Use inherited or forked context only when essential meaning is spread across substantial conversation and a compact handoff would lose it. In that case, do not restate the inherited transcript in a giant prompt; add only the assignment, boundaries, and changed facts. A simple context-entangled task may stay with the parent; a complex one may use a forked worker.

**R-DEL.8.1 — Independent critique.** For adversarial review, use fresh context and give the reviewer the artifact, objective, constraints, and acceptance criteria without prior verdicts or the author's reasoning. Ask it to presume defects and produce verified findings with locations, consequences, and severity. Use multiple reviewers only when distinct expertise or risk justifies them.

**R-DEL.9 — Capability fallback.** If a required capability is unavailable, use the closest safe route: parent execution, documented self-review, fresh process, direct artifact path, sibling clone, or skipped optional install with reason. Keep the same acceptance bar where practical. Missing subagents or GUI does not automatically transfer work to the user.

**R-DEL.10 — Orchestration method.** For complex execution, write a dependency-aware plan before forcing sequential continuation. Prefer native governed worker workflows, then deterministic automation for mechanical steps, then direct parent execution. Preserve isolation, budgets, acceptance criteria, and evidence regardless of mechanism.

## R-SES — Parent-context preservation

**R-SES.1.2 — Context compaction.** Keep parent context for objective state, dependencies, decisions, synthesis, and acceptance. Send large artifact reading, long implementation, and complex validation to scoped workers. Carry forward current conclusions and evidence, not stale failed plans or full transcripts.
