# Slice review cadence + worker self-loop — ticket

Two deliverables: (A) policy change in `AGENTS.md` and `docs/policy/execution.md` making
independent review a vertical-slice gate and the worker self-loop the in-slice proof loop;
(B) record the verified subagent thinking/model-parameter fact in this ticket only.

Baseline: working tree (previous ticket's final state, uncommitted) on `c82765e`.
Pre-edit bytes in `baseline/`; hashes in `baseline/hashes.txt`.

## Interpretation and scope

- Interpretation: "review cadence" is the *when* of independent review. Today the policy
  reads as fresh independent review per delivery; the approved direction makes it one gate
  per vertical slice, with the worker's own record-implement-check loop covering everything
  inside the slice. Nothing about safety, authority, evidence, or reviewer independence changes.
- Scope: only the two named files. `AGENTS.md` carries the binding boundary; the companion
  carries the method and the pointer to the slice definition. No new sections, so no anchor churn.
- Out of scope: children, global config, unrelated root files, prior tickets, index/commits/
  publication, the policy text for (B) (kept model/platform independent).

Options considered:
- Put the whole cadence rule in `execution.md#proof-and-review` only → leaves the always-loaded
  core still readable as per-task review; rejected.
- Duplicate definition of "vertical slice" in both files → two homes for one fact; rejected.
- **Chosen:** one definition home (`execution.md#product-decisions`, extending existing
  "bounded end-to-end user outcomes" wording), a one-clause binding rule in `AGENTS.md`
  shared boundaries plus the worker self-loop clause in the Worker role, and the operational
  cadence bullet in `execution.md#proof-and-review`.

Cohesive single-leaf edit: core and companion must agree, so it is one coupled writing seam
and is not split. This worker owns the edit and self-proof; main routes a fresh reviewer at
the slice gate.

## (A) Self-derived acceptance standard

Recorded before editing, then verified against the final revision. Numbered so each line is
checkable with a command or a read of the final file.

- A1 Independent review is a per-slice gate, not per-task/sub-task: the final text binds review
  to the vertical slice and explicitly allows flexible timing within the slice.
- A2 Self-loop: within a slice the worker records its own acceptance standard, implements,
  checks against it and iterates; no separate independent review is required per task/sub-task.
- A3 No-slice work (record/policy/documentation-only) is independently reviewed only on
  explicit user request.
- A4 "Vertical slice" is defined once as a bounded end-to-end user outcome, consistent with the
  existing Product decisions wording, and that one clause is the home other text points at.
- A5 No weakening: revision-bound self-proof, fresh independent review, "never accept the
  repairer's own verdict", repair/re-review flow, safety/authority/evidence boundaries, and
  the reviewer-independence (fresh context) rule all survive verbatim or stronger; self-test is
  named the in-slice loop and NOT independent acceptance.
- A6 Concise and non-duplicative: each of the three new rules is stated once — boundary in
  `AGENTS.md`, method in `execution.md` — with no rule repeated inside a file.
- A7 Facts as current SSOT: no dated narrative, "was A then B", changelog, or errata in either
  policy file; the ticket alone holds process history.
- A8 Structural health: relative links and anchors in both files still resolve; no trailing
  whitespace or leftover conflict markers (`git diff --check`, anchor scan, marker scan);
  neither file grows materially (documentation-only change, size bounded and disclosed).
- A9 No collateral edits: `AGENTS.md` and `docs/policy/execution.md` are the only files this
  ticket changes; changes stay unstaged and uncommitted; prior dirty files untouched.

Method: record baseline, edit, self-check every item, iterate until all pass, then record
commands+results and a baseline→final diff bound to the final hashes. Documentation checks
only — not live agent-behavior tests, and not independent acceptance.

## (B) Verified subagent thinking/model parameters

Recorded from the harness configuration and a failed run; the policy text stays model/platform
independent, so this fact lives only in the ticket.

- Thinking is controlled only by the model suffix `provider/id:off|minimal|low|medium|high|xhigh|max`;
the dispatch `thinking` field is ignored (reserved for `watchdog.configure`). Evidence:
`~/.pi/agent/npm/node_modules/pi-subagents/docs/tool-reference.md:78` and that package's
`docs/models.md` ("Thinking ceiling" levels list).
- The bundled `worker` and `reviewer` agent frontmatter default `thinking: high`.
Evidence: `pi-subagents/agents/worker.md` and `pi-subagents/agents/reviewer.md` (both `thinking: high`).
- Children otherwise inherit the parent model; builtin agents inherit the parent session's default
model, and frontmatter wins only when it pins one. The bundled worker/reviewer set no `model`, so
their high `thinking` default is the exception, overridden per run by the model suffix. Evidence:
`docs/models.md` ("Builtin agents inherit your current Pi default model" and the precedence list
ending at "the parent session model").
- A high-thinking run of this very task timed out at 30 min: run `2ad01866`, model
`deepseek/deepseek-flash:high`, error `Subagent timed out after 1800000ms.`, transcript
`thinkingLevel: high`. Evidence:
`~/.pi/agent/sessions/--home-z-vibe--/subagent-artifacts/2ad01866-4637-405a-ad88-2729edfd4c41_worker_meta.json`
and its `_worker_transcript.jsonl`. The recovery run overrides to `deepseek/deepseek-flash:low`
(`.scratch/slice-review-recovery.workflow.js`).

## (C) Recovery + finish acceptance standard

Recorded before editing; the on-disk slice-review edits were treated as already written and
reconciled against (a)-(e) rather than redone. Numbered so each line is checkable.

- R1 Reconcile: semantics (a)-(e) are all present, coherent and non-contradictory in the final
  two files: slice gate not per task, worker self-loop, no-slice work reviewed only on request,
  one vertical-slice definition home, and self-test-not-independent-acceptance + fresh review +
  boundaries preserved.
- R2 Focus rule added: a binding sentence in `AGENTS.md` and method wording in `execution.md`
  pointing at it; states (i) default to the main agent's session budget, (ii) raise only for
  genuinely complex work or repeated failure, (iii) the reason is focus — keep each context small
  and prefer splitting over bundling unrelated work. No hardcoded model names.
- R3 Validator truthful: the link check resolves `AGENTS.md` targets against the target file's own
  headings; ban-list text no longer self-matches; unrelated-path mtime checks dropped; A4/A5/A6
  expectations match the contract; the corrected run honestly reflects the tree.
- R4 Ticket records the verified subagent-parameter fact (section B) with concrete evidence paths.
- R5 Scope: only `AGENTS.md`, `docs/policy/execution.md` and this ticket change; edits unstaged;
  no commit; `git diff --check` clean.

Method: record baseline, edit, run the corrected validator and `git diff --check`, iterate until
they pass, then record commands+results bound to final hashes. Documentation checks only.
