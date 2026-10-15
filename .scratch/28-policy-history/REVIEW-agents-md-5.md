## Review

VERDICT: **BLOCK** — 2 blocking, 6 non-blocking.
- Blocking 1: `doctrine._text` calls this file "the root the rest is derived from" while `change.docs.rules_are_a_render` / `generated_is_write_only` make it a derived render that is "never an input", so checklist #6 has no single root.
- Blocking 2: `resources.split` is a catch-all holding VCS, scheduling and context-budget rules, which its own `by_logic`/`granularity` forbid — #5 fails and the push/branch rules sit where a reader will not look.

**Revision confirmed.** `/home/z/vibe/AGENTS.md`, 229 lines, one fenced YAML block, top-level keys in order: `doctrine`, `precedence`, `intent`, `resources`, `attention`, `change`, `proof`. Nothing else was opened; no `find`/`ls`/`grep` was used (2 reads of the target only).

## Checklist (`change.docs.doc_checklist`, line 157)
1. One home — **FAIL**. The fact "what is the root / what outranks what" has two homes (F1); the preserve norm has three (F7); `_text` carries two meanings (F4).
2. Resolvable — **PASS with one gap**. All `@`-references resolve here (`@main_point`, `@justified`, `@attention`, `@rules_are_derived`, `@fact_record:172`, `@propagate_down:171`, `@ssot_boundary:161`, `@silent_advance:146`, `@resources`, `@outdated:190`, `@references_resolve:167`, `@citation_not_value:168`, `@declare_what_a_file_is:165`, `@structure_is_absolute:105`); named paths `AGENTS.yaml`, `AGENTS.schema.yaml`, `PEOPLE.yaml`, `docs/`, `.scratch/` are defined at 159–160/175. Gap: F3.
3. Sourced — **PASS**. No measured value is stored in prose; the numerals are prescriptions ("at least two options":115, "five to ten common overreaches":38, "one writer":85). Note F9.
4. Declared — **PASS**. Line 1 "generated from AGENTS.yaml - edit that file" plus `rules_are_a_render` (170) identify it as a render. Note: the declaration is a comment outside the YAML block, so a parser of the block sees no self-declaration.
5. Sound — **FAIL**. F2, F5.
6. Derived — **FAIL**. F1: with two roots named, no rule's trace is uniquely determined at the root `doctrine._text` (4) points at.
7. Justified — **PASS**. `@justified` (8) is applied consistently; the only near-miss is the meta clause in F1.

## Findings
- **F1 (blocking)** `doctrine._text` (4) "the root the rest is derived from" + `precedence.order` (15) "then this file, then docs" against `change.docs.rules_are_a_render` (170) "is a render of its doc layers, never a second source" and `change.docs.generated_is_write_only` (166) "never an input ... nobody edits it by hand" with `change.docs.propagate_down` (171). Consequence: `change.docs.doc_driven` (177) "update this policy first" points at hand-editing a file that (166) forbids hand-editing, while the banner points at AGENTS.yaml. Violates #1 and #6. Smallest fix: state one direction at the top and name the file `doc_driven` edits.
- **F2 (blocking)** `resources.split` (74–96) holds `writers`/`commits`/`pushes`/`preserve_state` (85–89), `schedule`/`finite_concurrency`/`never_block_on_a_resource`/`overlap_waits` (90–93) and `focus`/`budget`/`fresh_context` (94–96), against its own `by_logic` (76) "The key a split is made on must be one that every fact has exactly one value of" and `granularity` (185) "forbid catch-alls". Violates #5 and the "stated only where the reader will not look" test (`pushes`, 88, is found under *Splitting*). Smallest fix: rename the node to what it holds and give split-by-logic its own children.
- **F3 (non-blocking)** `change.docs.rebuild_after_edit` (178) "run the renderer's consistency check" and `doc_schema` (163) "a check that runs with the work": no renderer name, path or command appears anywhere in the file. Violates #2 as read in-file.
- **F4 (non-blocking)** `_text` is used 25 times, never defined, and does two jobs: intro (156) and binding rule carrying its own link (4; 156 "@outdated"). Violates #1 and `field_admission` (184).
- **F5 (non-blocking)** `resources.environment.desktop_courtesy` (102) sits under an `_text` (98) about toolchain/lockfile, but is about human interaction ("check focus and get agreement before pointer or keyboard actions"); its decision home is `attention`/`intent.user_model`. Violates #5/#6.
- **F6 (non-blocking)** `proof.process.subagent_self_report` (226) "spawns its own subagent to take over. Any method that serves the goal is fair." against `intent.roles.sub_owner` (56) "only under explicit permission and runtime bounds" and `resources.split.handoff` (83) "prose grants neither tools nor recursion". Not blocking: `precedence.levels` (16)/`specificity` (17) and `parent_contract` (18) let the stricter rule win — but the default is unstated.
- **F7 (non-blocking)** One norm, three homes, no `@` between them: `intent.risk.preserve_work` (64), `resources.split.preserve_state` (89), `resources.environment.cleanup_check` (103). Violates #1 and `main_point`'s own remedy (5).
- **F8 (non-blocking)** `change.docs.doc_checklist` (157) names no owner and no trigger, and nothing in the file says when it runs. Fails the "no trigger, no owner" test.
- **F9 (non-blocking)** `intent.scope.derive_non_goals` (38) "five to ten common overreaches" — an uncalibrated bound with no basis stated; #3 still passes (prescription, not measurement).

## Not verified / limits
- By scope I read only `AGENTS.md`; `AGENTS.yaml`, `AGENTS.schema.yaml`, `PEOPLE.yaml`, the renderer and `docs/` were not opened. If any judgement depends on them, this review does not cover it.
- No repo, git or command access: I did not verify that any path named here exists, or that a renderer exists. #2 is judged against in-file definitions only, which is why F3 is a gap rather than a proven break.
- Line numbers are from the file as read now (229 lines; line 229 is the closing fence, corroborating the count).
- No rule was executed against a live agent, so I did not test whether these rules produce the intended behaviour; blocking/non-blocking is my judgment against the checklist and the task's BLOCK definition.
- Fixed nothing, committed nothing, per instruction.