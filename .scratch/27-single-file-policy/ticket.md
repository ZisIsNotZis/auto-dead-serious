# Single-file policy + phase model — ticket (2026-10-13)

## Contract
- Interpretation: consolidate all agent policy into the single root `AGENTS.md` (no linked policy files), add the discussion/execution phase model, lossless human-viewable delivery, and objective-first/end-to-end thinking. Ad hoc documentation change in the Discussion Phase; done by Main directly, no delegation.
- Scope: `/home/z/vibe/AGENTS.md`; delete `docs/policy/execution.md`. Preserve the uncommitted working-tree content and all unrelated dirty work. No commit.
- Acceptance: every rule from both baselines preserved undiminished; N1 single-file; N2 phase model coherent with the Main role and progress rules; N3 lossless/viewable/opened delivery; N4 objective-first/end-to-end; no dangling `docs/policy` reference.
- Baseline (pre-change): `AGENTS.md` sha256 00e17db4… (10,094 B); `docs/policy/execution.md` sha256 0bcf1021… (17,710 B). Snapshots: `baseline-AGENTS.md`, `baseline-execution.md`.
- Budget: one implementation pass + self-checks. No independent review requested; self-proof only.

## Coverage map (every baseline rule → new home)

Baseline `AGENTS.md`:
- Authority and information → same section (verbatim).
- Shared boundaries (8 bullets) → same section (8 bullets, verbatim; Main scoping referenced).
- Roles: Main → Roles (rescoped to Execution Phase; Discussion Phase direct work added).
- Roles: Worker, Authorized sub-PO, Reviewer → Roles (verbatim; the `(enumeration in Task routing)` link became `(see Task routing)`).
- Fresh/non-inherited context paragraph → Roles (verbatim).
- Conditional methods index (6 pointers) → replaced by the in-file sections Task routing, Proof and review, Product decisions, Documentation, Environment, Remote coordination. Trigger definitions folded in: the remote trigger + "configured remote alone is not a trigger" → Remote coordination bullet 1; "ordinary configured-command use does not trigger environment changes" → Environment.

Baseline `docs/policy/execution.md`:
- Task routing (8 bullets) → Task routing (8 bullets, verbatim).
- Proof and review (6 bullets) → Proof and review (6 bullets, verbatim).
- Product decisions (8 bullets) → Product decisions (8 bullets; old presentation bullet expanded with the N3 lossless/viewable requirement).
- Documentation (3 bullets) → Documentation (3 bullets; "this companion for conditional methods" replaced by "this single `AGENTS.md` … all operating methods"; "core/package size and file count" simplified to "file count and size").
- Environment (5 bullets) → Environment (6 bullets; added the preserved configured-command line).
- Remote coordination (4 bullets) → Remote coordination (4 bullets; trigger definition prepended to bullet 1).

## New content
- N1 single-file rule: `AGENTS.md:3` (self-contained; never split into linked companion documents).
- N4 objective-first/end-to-end: section `Objective and end-to-end thinking`.
- N2 discussion/execution phases: section `Discussion and execution phases`; Main role rescoped at `Roles`.
- N3 lossless, human-viewable delivery + open: Product decisions delivery bullet.

## Verification (self-proof, documentation only)
- Mechanical losslessness: token-multiset diff of `baseline-AGENTS.md` + `baseline-execution.md` vs final `AGENTS.md`. All residual token diffs are the removed index/conditional-methods pointers, the "Methods add no authority" → "sections … grant no authority" rewording, and consolidation count reductions; no rule text is absent.
- `grep -n docs/policy AGENTS.md` → none. `docs/policy/` removed (`ls docs/` → `people.md`).
- `git diff --check -- AGENTS.md` → clean.
- Final: 100 lines, 30,050 B, sha256 604be315… ; `docs/policy/execution.md` deleted.
- Limits: documentation proof only; no independent review, no runtime enforcement, no desktop-opening verification was requested.
