# Policy maintenance

Load when:
- Before changing `AGENTS.md`, anything under `docs/policy/`, or policy routing or topology declarations in `WORKSPACE.md`.

Do not load when:
- Applying policy to ordinary project work without changing policy artifacts or routing declarations.

Applies while:
- Proposing, authoring, measuring, auditing, validating, and reviewing a policy change.

Exit when:
- Routing and citation audits, size delta, `git diff --check`, scoped reread, and fresh-context policy review are recorded in the ticket.

## S — Policy maintenance

**S1 — Size accounting.** Record `wc -m` before and after each policy change for `AGENTS.md`, `WORKSPACE.md`, and every file under `docs/policy/`; report total delta in the ticket. Treat 12,000 characters per authored topic file as a review signal and target a compact always-on core, but never delete necessary safety behavior merely to hit a byte target. Growth must replace or justify existing behavior; shrinking must be deliberate.

**S2 — Rule admission.** Admit a policy line only when an observable trigger causes a decision that professional judgment would not reliably make, or when it protects a known invariant. State scope, action, and operational completion. Delete the line and reread: if no fresh-agent decision changes, omit it. Prefer replacing redundant rules over adding another formulation.

**S3 — Policy change gate.** Every policy change has a durable ticket and `Need-review: yes`. Record baseline, migration or rationale, commands, findings, and disposition. Before acceptance run the declared policy gates, inspect the full scoped diff, and obtain a fresh-context review against the documentation review rubric. Record reviewer or role, diff identity, verdict, and all blocking-finding fixes. Do not claim final acceptance before this review.

**S4 — One meaning and explicit routing.** Define each live rule code once. A citation is only a locator and never imports another topic. Cross-topic behavior must be self-contained or say explicitly which observable condition loads the other topic. Audit that every active policy citation resolves uniquely, retired identifiers are not active, every topic has the four-field applicability header exactly once, and `AGENTS.md` maps live code families to their files.

**S5 — Topology changes and self-sufficiency.** A topology change includes a responsibility map, updates active routing and `WORKSPACE.md`, checks child-repository compatibility, and removes obsolete live-rule containers only after retained codes resolve. Historical ticket citations need not be rewritten when preserved IDs remain intelligible. Policy methods must work without optional skills, external indexes, or a specific harness.
