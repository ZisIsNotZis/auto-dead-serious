# Design

Load when:
- Before selecting or changing product behavior, architecture, data or interface contracts, UI workflow, or when repeated defects require design-level reformulation.

Do not load when:
- Mechanically implementing an already approved and documented design.

Applies while:
- Deriving requirements, evaluating alternatives, choosing design boundaries, and defining how the choice will be validated.

Exit when:
- Assumptions, alternatives, selected design, boundaries, and validation approach are recorded, and any material user-owned choice is resolved.

## R-INT — Change analysis

**R-INT.9 — Change flexibility.** Keep assumptions, reversibility, change cost, risk, and priority visible. Derive routine trade-offs from the approved objective. Escalate only a material user-owned choice; otherwise choose, record rationale, and continue.

**R-INT.10 — Projection map.** Before a structural migration or change spanning roughly ten or more files, map each current responsibility or artifact to its destination, resolve ambiguous ownership, and finish with a coverage check. For smaller but high-risk changes, use the same technique when it reduces omission risk.

## R-DSN — Design principles

**R-DSN.1 — Autonomous analysis.** Before implementation, verify that the relevant goal, roadmap or milestone, design philosophy, methodology, and working granularity form one coherent basis for execution. Test it against real use cases, constraints, failure modes, and acceptance criteria, and compare routine alternatives internally. If materially different interpretations remain, do not choose by “probably”; surface the consequential difference and request the smallest user-owned decision that resolves it. After alignment, continue routine design autonomously.

**R-DSN.2 — Decision tiers.** Distinguish product philosophy, design goals, contracts, and implementation detail. Preserve higher-tier intent when choosing lower-tier detail. Record material assumptions and negotiation room rather than treating every choice as permanent.

**R-DSN.3 — Simplest sufficient solution.** Evaluate, in order: no change, simpler design with the same user outcome, deferral of nonessential scope, an established suitable library, decomposition into library-supported parts, then minimal custom implementation. A dependency is acceptable only within the objective's authorization and consequence boundaries.

**R-DSN.5 — One concept, one name.** Use one stable domain name across contracts, code, configuration, tests, and documentation. Follow ecosystem casing and file conventions. Avoid redundant identity or type fields when location or schema already provides the fact.

**R-DSN.7 — Compact interfaces.** Make mandatory inputs explicit and defaults implicit. Show overrides at the call site. Automate repeated mappings or transformations when doing so removes a real defect surface; do not abstract a single occurrence prematurely.

**R-DSN.8 — Shift-left validation.** Place each error class at the earliest affordable detection point: type or schema, static analysis, test, assertion, bounded runtime handling, or observability. Add instrumentation before risky paths when diagnosis would otherwise be expensive. Choose checks by scoped risk rather than an exhaustive category list.

**R-DSN.9 — Root-cause design.** Reproduce the failure, identify the invariant that permits it, and prefer a representation or boundary that makes the invalid state impossible. Fix the root cause rather than the visible symptom. Define observability for common, risky, slow, and failure paths where it materially improves diagnosis.

**R-DSN.10 — Automation over repeated instruction.** Turn repeated deterministic steps into a script, hook, or repository command when automation is clearer and safer. A service needing multiple setup commands should expose one supported entry point. Keep judgment-heavy guidance in documentation rather than brittle automation.

**R-DSN.11 — User-interface design.** Derive workflow from approved use cases and minimize cognitive load through clear hierarchy, recognition over recall, visible feedback, error prevention, and recovery. Use a visual prototype when it materially reduces ambiguity. An approved UI objective proceeds autonomously; interrupt only for material divergence or the agreed subjective acceptance milestone.

**R-DSN.12 — Quality priorities.** Prioritize correctness, robustness, and scope-bound safety. Choose longevity, scalability, accessibility, and performance investment from the actual use case and objective. Measure performance against a relevant threshold rather than optimizing without a target.

**R-DSN.14 — Extraction threshold.** Extract a shared module, interface, or schema when at least two real consumers need the same concept or one boundary independently warrants isolation. Otherwise keep it with its single use to avoid speculative abstraction.
