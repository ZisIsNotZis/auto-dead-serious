# Documentation and knowledge

Load when:
- Before creating or changing durable project documentation, recording project truth or philosophy, resolving a documentation conflict, or reviewing documentation.

Do not load when:
- Code-only work preserves documented behavior, notes are transient ticket bookkeeping, or work is read-only inspection other than documentation review.

Applies while:
- Deciding what durable knowledge means, where it belongs, how it is written, and whether the resulting documentation is acceptable.

Exit when:
- The authoritative node and affected cross-references are updated and documentation checks and required review are complete.

## R-DOC — Documentation and knowledge

**R-DOC.1 — Product truth.** Approved project documentation is authoritative for product goals, behavior, contracts, and recorded trade-offs. Record user-supplied facts promptly with provenance. An approved execution objective authorizes documentation implied within its boundaries. A change to goals, public contracts, or a user-approved trade-off is a material user-owned decision; never overwrite conflicting confirmed truth silently.

**R-DOC.2 — Update timing.** Before or with implementation, update the authoritative documentation when behavior, contracts, goals, or durable decisions change. First inspect related nodes and tickets. Code-preserving work does not require manufactured documentation. Resolve a conflict at its authoritative source rather than appending a contradictory note.

**R-DOC.3 — Single source.** Give each durable fact or decision one topic-centered authoritative home. Design intent belongs in design documentation; code-coupled detail belongs in code or comments. Update the original node and affected cross-references together. Archives preserve provenance but do not become competing operational truth.

**R-DOC.4 — Clarity.** Optimize for correct interpretation. State each instruction's observable trigger, scope, action, rationale when it changes judgment, and completion condition. Prefer a concrete example or executable check over abstract explanation. Close a change with an ambiguity reread.

**R-DOC.4.1 — Documentation review rubric.** A fresh-context review checks:

- **Correct:** internally consistent, consistent with authoritative product truth, and explicit about conflict resolution.
- **Necessary and complete:** every behavioral line changes a decision over professional default; every question is answered or deliberately open; every state has an exit.
- **Specific and actionable:** a fresh agent can decide compliance; each gate has an operational test; each process has a checkable end.
- **Compact:** one meaning in one place, related meanings together, repository facts discoverable from their source, and declared budgets respected.
- **Professional and positive:** established domain terms for agent-facing material; plain language for user-facing material; prohibitions reserved for hard guardrails and paired with target behavior.
- **Selectively disclosed:** each topic file has operational load, exclusion, scope, and exit fields; routing exposes only relevant material; no citation silently imports another topic.

One reviewer covers the rubric unless the artifact's breadth warrants specialist reviews. Verify every finding against the text before accepting it.

**R-DOC.5 — Operational writing.** Translate informal requirements into precise domain language without changing intent. Every action-triggering rule must be decidable from a concrete condition, action, and result. A style or philosophy sentence is exempt only when removing it changes no decision.

**R-DOC.6 — Structure and size.** Default authored-content budget is at most 200 lines or 12,000 characters, whichever comes first, unless a `Budget:` header declares a justified exception. Exempt immutable source archives and append-only evidence or ticket comments. Exceeding a budget triggers deletion or restructuring of low-value material, not silent cap growth. Policy sizing and admission are governed by the policy-maintenance topic when its trigger independently fires.

**R-DOC.6.1 — Markdown style.** Use one paragraph or list item per physical line; do not hard-wrap prose. Use headers, lists, and tables where structure carries meaning. Remove filler, repeated summaries, and duplicated caveats.

**R-DOC.7 — Appropriate level.** Durable documentation describes goals, contracts, architecture, decisions, and operating knowledge. Put line-level implementation detail in code comments and avoid file-by-file diaries.

**R-DOC.8 — Philosophy.** Record durable product philosophy revealed by approved decisions when it will guide later choices. Derivations within an approved objective may be recorded autonomously; material changes to the philosophy use the user-owned decision gate.

**R-DOC.9 — People notes.** Record only user-provided role, expertise, contact detail when needed, and working or communication preferences useful for continuity. Do not infer or maintain temperament, personality, or reliability dossiers.

**R-DOC.10 — Source layers.** Separate provenance from operational truth and interpretation.

- **R-DOC.10.1 — Raw sources (L1).** Preserve supplied source material verbatim under `docs/sources/` when provenance or audit value warrants it. Index it; do not treat unreviewed raw material as current operational truth.
- **R-DOC.10.2 — Approved structured truth (L2).** Confirmed, approved, structured documentation is the operational source used for decisions.
- **R-DOC.10.3 — Working interpretation (L3).** Agent-derived understanding is revisable and may fill gaps that approved truth leaves open; label consequential uncertainty.
- **R-DOC.10.4 — Resolution.** Raw sources establish what was supplied, L2 establishes approved meaning, and L3 supplies revisable interpretation. Preserve L1 verbatim, update L2 through the applicable authority, and promote confirmed L3 understanding into L2. A source annotation can flag conflict but cannot silently change approved truth.

**R-DOC.11 — Knowledge routing.** Decisions others build on go in `docs/`; project, environment, and gate facts go in `WORKSPACE.md`; reusable procedures go in `.agents/skills/`; reusable evaluation roles go in `docs/roles/`; automation goes in `scripts/`; transient execution history stays in tickets or evidence. Policy routing lives in `AGENTS.md`, with scoped behavior under `docs/policy/`. If two homes appear plausible, choose the one that owns the decision and link from the other.
