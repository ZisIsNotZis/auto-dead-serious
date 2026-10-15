## Review

**TLDR (verdict, counts, blocking gist)**
- Verdict: **BLOCK** — two P1s, both file-internal (no runtime impact), smallest fixes named.
- Counts: P0 0, P1 2, P2 4. Fixed: none (fix nothing was instructed).
- P1-a: one rule ("a missing value is declared, never filled in") has two homes, `change.entries.fabricated` and `change.entries.say_unknown`, and neither is cited anywhere — a direct `@ssot` "One home?" violation.
- P1-b: `resources.effort.budget` says "a cap with no number is not a cap", while its own sibling `resources.effort.earned_budget` gives no number and no earning trigger.
- Job derivation: no problem — the file states its own criteria (`change.upkeep.checklist`, `change.upkeep.resolvable`, `@falsifiable`), so the review job was derivable from the file alone.

**Correct (evidence)**
- Banner `<!-- generated from AGENTS.yaml - edit that file -->` satisfies `change.upkeep.write_only` ("carries a banner naming what produced it and where the edit belongs").
- 14 in-file references resolve to keys that exist (`@ssot`, `@projection`, `@no_op`, `@falsifiable`, `@top_down`, `@derived`, `@absent`, `@controlled`, `@invalidate`, `@authority`, `@partition`, `@atomic`, `@handoff`, `@levels_in_order`, `@files`, `@chain`/`@layout` → `change.shape.*`), per `change.upkeep.resolvable`.
- One node per rendered line, no manual wrap, no decorative blanks — matches `change.entries.no_manual_wrap`.

**Findings**

- **P1 — duplication (two homes for one rule).** `change.entries.fabricated` (AGENTS.md:177) vs `change.entries.say_unknown` (AGENTS.md:178). Quote: fabricated "A missing measurement is recorded as a declared state" / say_unknown "A missing value is declared missing, never filled in". Criterion: `@ssot` "every fact has exactly one home", via `change.upkeep.checklist` "One home? @ssot"; `laws.ssot.atomic` only lets a facet "earn a name" when "something references it", and grep shows neither id is cited. Both also restate `laws.absent`. Smallest fix: delete the leading clause of `say_unknown`, keeping only its facet (the three admissible answers: unknown / not verified / cannot be established).

- **P1 — contradiction with its own standard + not specific.** `resources.effort.earned_budget` (AGENTS.md:109) vs `resources.effort.budget` (AGENTS.md:110). Quote: "earns more only for genuinely complex or repeatedly failing work" against "a cap with no number is not a cap". Criterion: nothing contradictory + everything specific and actionable. `proof.process.deadline` carries the same defect ("A long task needs a deadline" with no number and no trigger). Reader cannot say which way to deviate: is the extra budget one attempt, three, or unbounded? Smallest fix: give `earned_budget` a number/trigger and reuse `proof.process.change_hypothesis` ("attempts yield no useful evidence") as the condition.

- **P2 — contradiction (unresolved scope) plus second home.** `proof.process.baseline` (AGENTS.md:253) "capture a scoped baseline before acting" vs `resources.split.preflight` (AGENTS.md:92) "Capture a scoped baseline when attribution matters". One is unconditional, the other conditional, and `precedence.specificity` cannot decide (different subjects). The same decision also already owns `proof.execution.separate_preexisting` (AGENTS.md:227). Smallest fix: make `baseline` name the attribution condition, and let `preflight` point at it instead of restating it.

- **P2 — duplication + two subjects in one node.** `attention.delivery.ship_at_gate` (AGENTS.md:148) "pause dependent work until approval or an explicit waiver" vs `attention.communication.ask_the_gap` (AGENTS.md:161) "honour agreed gates, pause dependent work and continue the safe independent work". Criterion: one home (`@ssot`) and `laws.ssot.atomic` ("Every node is one line and one subject"). Smallest fix: keep the pause rule in the gate nodes, trim it from `ask_the_gap`.

- **P2 — contradiction across phases, undecidable.** `change.upkeep.doc_first` (AGENTS.md:202) "update that policy's SSOT rather than its render ... This holds in both phases" vs `attention.phases.discussion.wait_for_yes` (AGENTS.md:131) "Do nothing before the user confirms". Both govern an agent action inside the discussion phase with no rule ranking them. Smallest fix: one clause in `doc_first`, e.g. "this holds once the user has confirmed the intent".

- **P2 — claim that no named check can falsify.** `change.upkeep.checklist` (AGENTS.md:200) "One home, the tree and the derived question are settled by a check rather than by an eye; how it runs is @rebuild_after_edit" vs `change.upkeep.rebuild_after_edit` (AGENTS.md:203), whose whole described check is render parity ("python3 scripts/render_policy.py writes it and --check verifies it"). A render-parity check cannot come out red for a duplicated fact or a stored derived figure, so the claim fails `@falsifiable` ("could have come out the other way, and that has been shown") and is not actionable. Smallest fix: name the checks that actually detect those three, or return them to `@fresh_reviewer`'s eye and say so.

- **P2 — near-contradiction on uploading.** `attention.communication.open_for_user` (AGENTS.md:155) "when he is remote upload it somewhere reachable" vs `proof.process.external_compute` (AGENTS.md:261) "never quietly hunt for a service to upload, pay or compute". Only the adverb "quietly" separates them; the reader cannot tell whether uploading the artefact needs prior consent. Smallest fix: add the authority condition to `open_for_user` ("using an already-authorised destination").

**Limits**
- Read only `/home/vibe/AGENTS.md`; no other path, no sweep, no shell, no edits, no commit. Nothing to run, no test command for a supervisor.
- `change.upkeep.resolvable` could not be exercised outward: `AGENTS.yaml`, `AGENTS.schema.yaml`, `PEOPLE.yaml`, `scripts/render_policy.py`, `docs/`, `.scratch/` were not inspected, so existence and currency of those references are unverified ("A step that did not run is not a step that passed"). Resolution was verified only inside the render.
- `laws.projection` ("siblings are ordered and the order is a priority") and render parity with the SSOT YAML are unverifiable from this file alone.
- Order/priority findings are therefore report-only; severity here is document-standard severity, not runtime severity.

**Merge verdict: BLOCK** — fix the two P1s (`say_unknown`/`fabricated` duplication; numberless `earned_budget` against its own cap standard) before treating this render as the standard. P2s are report-only for the next revision pass.