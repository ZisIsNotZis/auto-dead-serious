# Delegation / SSOT / context-inheritance policy — execution contract

Ticket for the approved direction to strengthen project policy for (A) unconditional
Main delegation, (B) ticket/log vs SSOT documents, (C) subagent context-inheritance
defaults. Baseline: working tree (in-progress consolidation, uncommitted) on
`c82765e`; exact pre-edit bytes captured in `baseline/`.

## Interpretation and acceptance

Implement the three approved semantics concisely in the existing style, preserving
all current wording and safeguards, with no speculative rules and no weakened
safety/authority/evidence boundaries. Edit only `AGENTS.md` and
`docs/policy/execution.md`; do not commit; leave changes in the working tree.

Proof: baseline copies + scoped baseline→final diff; before/after line and byte
counts; scoped `git diff --check`; relative-link/anchor resolution; rationale and
exact commands+results.

Scope: the two named files. Out of scope: children, global config, unrelated root
files, prior records, index/commits/publication, `README.md`/`WORKSPACE.md`.

## Options and decision

- Putting (B) only in the conditional `Documentation` section would leave the
  always-loaded core silent, so a model could still append dated logs to documents.
- Duplicating the full (B) ban in both files bloats the core and repeats prose.
- **Chosen:** state the enforceable (B) boundary in the core `AGENTS.md` shared
  boundaries, and the operational form in `execution.md#documentation`; scope the
  existing "Preserve other entries" line to the ticket ledger. (A) rewrites the
  Main role rule in place; (C) extends the existing fresh-context sentence. No new
  sections, so no anchor churn.

Placement is one coupled writing seam (core + companion must agree) and is a single
cohesive independently checkable leaf; no split. This worker owns the edit and
self-proof; main routes a fresh reviewer.

## Proof and bounds

One implementation pass plus bounded self-check; a 60s foreground bound per
command. Documentation checks only — not live agent-behavior tests. Fresh
independent review remains a separate acceptance requirement and is not claimed
here.
