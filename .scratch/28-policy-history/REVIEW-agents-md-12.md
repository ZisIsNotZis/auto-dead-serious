## Review

Target: `/home/z/vibe/AGENTS.md` (render, line 1 banner). Criteria are taken from the file itself: `change.checklist:168` (ten law questions), `change.render:180`, and `proof.review.reviewer_contract:226` ("Where the object states its own criteria, the contract carries only the object, the bound and the budget").

Job derivation: **derivable from the file alone** — no finding here. The file states the questions, the law each points at, and which of them a program settles.

**Correct**
- Every cross-reference resolves. A sweep of all `@…` tokens (`@ssot @projection @no_op @falsifiable @top_down @derived @absent @controlled @invalidate @authority @chain @layout @partition @atomic @preserve_work @attention @resources @silent_advance @levels_in_order @specificity @handoff @fresh_reviewer @fact_record @layer_and_source @propagate_down @current_fact @retraction @outdated`) matches a key that exists in this file → `change.resolvable:177` holds as far as the render alone can show.
- `checklist:168` "one question per law" holds exactly: its ten questions map 1:1, in order, onto the ten nodes of `laws` (lines 5–19), matching `laws.projection:9` (sibling order is priority).
- Banner line 1 ("generated from AGENTS.yaml - edit that file") fulfils `change.write_only:176`'s requirement that a render carry a banner naming what produced it and where the edit belongs.
- One statement per line, no manual wraps or decorative blanks → `change.no_manual_wrap:191` holds.

**Finding P2 — the render's source is stated twice with two different answers.** `change.render:180` "A project's agent-rules file is a render of its **doc layers**" vs `change.files:171` "this policy in AGENTS.yaml with its render AGENTS.md". `change.layout:170` puts layers under `docs/` and `change.files:171` lists the policy separately from those layer folders, so "its doc layers" cannot mean AGENTS.yaml without the reader applying `precedence.specificity:28`. Violates `laws.ssot:6` (one home per fact) and undercuts render's own purpose, "the reader is told which file to edit". Smallest fix: in `render:180` write "…is a render of the policy that owns each rule (@files here)".

**Finding P2 — "this file" is ranked as a source while this file is declared not to be one.** `precedence.source_order:26` ranks "…then this file, then docs…" above docs; `change.write_only:176` says of a generated artefact "Nothing reads it back as a source", and `change.file_kind:175` "The kinds are never mixed". Read literally, source_order makes the render outrank AGENTS.yaml's docs, so the reader must re-derive that "this file" means AGENTS.yaml. Violates `laws.ssot:6` / `precedence.levels_in_order:27`. Smallest fix: "then this policy".

**Finding P2 — PEOPLE.yaml has no declared kind or schema.** `change.files:171` lists it in the set; `change.people:185` describes only its content. `change.file_kind:175` requires "Every file says what it is" and `change.schema:173` requires a doc set to be validated against a schema, which `files:171` names once for the set. Violates `change.file_kind:175`. Smallest fix: end `people:185` with "a store validated by AGENTS.schema.yaml".

**Finding P2 — `checklist:168` restates two facts that already have homes.** The command's home is `change.rebuild_after_edit:188`, the fresh-eyes rule's home is `proof.review.fresh_reviewer:223`. Violates `change.cut_repetition:190` and `laws.ssot:6`. Smallest fix: end the node at "@authority" and let the two clauses point at `@rebuild_after_edit` and `@fresh_reviewer`.

**Blocking — the file's own mechanical acceptance was not exercised.** `checklist:168` assigns "One home, the tree and the derived question" to `python3 scripts/render_policy.py --check`, and `change.schema:173` to validation against AGENTS.schema.yaml. No result came with this revision and this review may not run commands. Per `laws.falsifiable:12` ("A step that did not run is not a step that passed") and `proof.review.unverified:234`, those questions are not PASS. Supervisor must run: `python3 scripts/render_policy.py --check` (with the schema validation it wraps).

**Merge verdict: BLOCK** — solely on that unverified acceptance; no P0/P1 defect found in the judgement part. If the check passes against the delivered revision, this becomes **OK with notes** (the four P2s).

**Limits**
- Bound to `/home/z/vibe/AGENTS.md`: AGENTS.yaml, AGENTS.schema.yaml, `scripts/render_policy.py`, `docs/`, PEOPLE.yaml and `.scratch/` were not read, so render↔source divergence, schema coverage of PEOPLE.yaml, command existence (`resolvable:177`) and index presence (`environment.structure_is_absolute:118`) are unverified.
- No commands run: `render_policy --check`, schema validation and `git diff --check` (`proof.execution.check_gates:220`) all remain unrun.
- No baseline or worktree hash supplied, so evidence binds only to line numbers of the file as read, not to a revision (`proof.execution.bind_to_revision:212`).
- The dispatch carries no blocking/nonblocking split; per `reviewer_contract:226` the object's criteria govern, so unmet acceptance was treated as blocking and P2s as nonblocking — declared, not invented.
- Facet-level coverage (`laws.ssot.partition:7`, `laws.ssot.atomic:8`, `laws.falsifiable.fail_loud:13`) was checked only as far as "one question per law" required.

---
Reply: **BLOCK** — 0 P0, 0 P1, 4 P2, 1 unexercised acceptance.
Blocking: `checklist:168` assigns one-home/tree/derived to `python3 scripts/render_policy.py --check`, which was never run for this revision (`unverified:234`); verdict flips to OK-with-notes if it passes.
P2 a: `render:180` "render of its doc layers" vs `files:171` "render AGENTS.md" of AGENTS.yaml — two sources.
P2 b: `source_order:26` ranks "this file" as a source though `write_only:176` says a render is "never an input".
P2 c/d: `people:185` gives PEOPLE.yaml no kind/schema (`file_kind:175`); `checklist:168` restates `rebuild_after_edit:188` and `fresh_reviewer:223`.