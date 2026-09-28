# 01 — Prune generic agent policy

- **Status:** done
- **Need-review:** passed (independent review and focused rereview)
- **Blocked by:** none

## Objective

Continue deletion-first reduction of generic engineering advice and over-specified local process in `docs/policy/`, retaining only decisions, safety boundaries, and workspace-specific recovery/coordination rules. Preserve ownership, validation, and relative-path semantics from the prior pass.

## Baseline and acceptance

- Baseline: `wc -m AGENTS.md WORKSPACE.md docs/policy/*.md` = 51,881 characters; root `AGENTS.md` = 5,855.
- Reduce low-value topic text; do not simply transfer it to the root or another topic.
- Verify meaningful scenarios, scoped diff, references, `git diff --check`, and independent review of revised policy.
- Preserve unrelated working-tree state and record final size, findings, and limitations.

## Comments

- 2026-09-28 (main agent, pi) — Claimed user's follow-up to continue deleting. Scope: topic files and only necessary root/workspace corrections.
- 2026-09-28 (main agent, pi) — Replaced generic design, tooling, model selection, communication, documentation, work-status, and test-process prose with shorter condition-specific rules; kept root and workspace unchanged from prior pass. All nine topic headers remain present and active rule identifiers are unique (49 definitions). Independent read-only review launched.

## Scenario checks

- Small executable fix: no mandatory roadmap or ticket; project gates, scoped diff, meaningful regression check, revision-bound report.
- Material product ambiguity: ask user for the consequential outcome; no technical-choice questionnaire.
- Interrupted task: find `.scratch/active-work.md` when needed, inspect ticket and Git revision/dirty state, rerun stale checks.
- Harness-loaded global instructions: companion policies resolve from the global `AGENTS.md`; project tickets remain target-project-relative, optional absent files are not fabricated.
- First discovered external writer: remote collision safeguards apply before shared writes and workspace mode update.

## Checks so far

- Final `wc -m AGENTS.md WORKSPACE.md docs/policy/*.md`: 29,047 versus 51,881 baseline (−22,834); root `AGENTS.md` 5,705. Relative to the pre-first-pass 58,206-character baseline, net reduction is 29,159 characters. Metrics do not prove correctness.
- `git diff --check` first found one blank line at EOF in `collaboration.md`; corrected it. Final rerun pending review.
- Python audit: all nine topic files have one each of four applicability headers; 49 unique active rule definitions; no duplicate identifier.
- Child `AGENTS.md`/`CLAUDE.md` reference search found no active citations to removed rule identifiers. Historical ticket citations were not rewritten.
- First independent review found no blocking safety, authority, path, or continuity omission; recommended removing duplicate handoff fields and clarifying initial remote ownership. Focused independent rereview also found no blocking regressions; its two clarifications were applied: explicit topic path and no shared `WORKSPACE.md` write before ownership.
- Final `git diff --check -- AGENTS.md WORKSPACE.md docs/policy`: passed with no output after removing an EOF blank line. Python audit: one applicability header set per topic, 47 unique live rule definitions, nine root topic links resolve. Parent reviewed scoped diff and final relevant sections; no child policy references to retired rule IDs found. No executable code changed, so no build/test gate applies.
- Remaining risk: textual scenario checks and independent file review do not empirically measure future agent behavior. Historical ticket references to removed rule identifiers are preserved as historical records, not live policy.
- Completed in this session; no active-work index is needed. No commit or unrelated state mutation was performed.

