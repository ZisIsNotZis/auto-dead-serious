# Build and validation

Load when:
- Before changing executable code or tests, reproducing or fixing an executable defect, or running validation or making a completion claim for executable-artifact work.

Do not load when:
- Work is documentation-only or read-only and no executable artifact is being changed, validated, or claimed.

Applies while:
- Implementing, testing, debugging, reviewing executable diffs, collecting evidence, and deciding whether an executable-artifact objective is complete.

Exit when:
- Applicable `WORKSPACE.md` gates, scoped diff review, and required manual or independent validation are complete on the claimed revision; otherwise the loop continues or work is durably parked.

## R-BLD — Build cycle

**R-BLD.1 — Continuous loop.** Implement, test, diagnose, and refine until the approved objective meets acceptance criteria or a valid park is recorded. Routine failures and internal slices do not require renewed permission.

**R-BLD.2 — Conforming implementation.** Implement the approved behavior and contracts with the smallest coherent change. Add logging, metrics, or diagnostic context where the design or risk requires it. Do not silently widen product behavior while resolving implementation detail.

**R-BLD.3 — Meaningful tests.** Prefer a failing test before a behavior change when a practical runner and observable assertion exist. A documented exception is valid for pure documentation, unavailable infrastructure, or when adding a runner would exceed the objective. Every regression fix gets the narrowest test that would have caught it when practical.

**R-BLD.4 — Validation standard.** Run every mandatory gate declared for the changed module in `WORKSPACE.md`, plus risk-driven checks needed for the actual change. At minimum, run the smallest meaningful test, build, or smoke check; `git diff --check`; and a scoped diff reread. Inspect visual or otherwise subjective artifacts directly. Assertions must be capable of failing when the changed behavior regresses.

**R-BLD.5 — Evidence.** Support each completion claim with the exact command and observed result or the artifact inspected, tied to the claimed commit or clearly identified working-tree revision. Rerun invalidated or stale evidence after changes. Store large evidence artifacts only when reproduction, audit, or acceptance needs them; routine command results may be recorded concisely in the ticket or report.

**R-BLD.6 — Debugging.** Reproduce first, form a falsifiable hypothesis, change one relevant variable, and verify against the reproduction. After two or three honest failed approaches, reformulate at the design level or delegate diagnosis; do not keep stacking symptom patches. Contact the user only if the reformulation reaches a core intervention gate.

**R-BLD.7 — Subjective validation.** Delegate complex or high-stakes visual, audio, prose, or interaction review to a fresh suitable reviewer and provide the artifact rather than the author's description. Simple artifacts may be self-inspected. If independent review is unavailable, perform and record the strongest practical self-review; user review occurs only at an agreed acceptance milestone or material subjective decision.

## R-REP — Commits and gates

**R-REP.4 — Repository validation.** `WORKSPACE.md` defines mandatory commands. Add risk-driven validation rather than every imaginable scanner. First-party failures and warnings are fixed or explicitly recorded with rationale; third-party noise is scoped and recorded when material. Commits remain coherent and truthful. Never commit credentials, tokens, private keys, or other secrets; use environment variables or the project's secret facility, and rotate exposed credentials.
