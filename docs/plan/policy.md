# Policy

The repository's product is the policy in AGENTS.yaml, rendered to AGENTS.md and checked by `python3 render_policy.py`. This is the plan for that product.

## Status

- AGENTS.yaml is the only source; AGENTS.md is its generated view, and `python3 render_policy.py --check` passes.
- The workspace holds neither .scratch nor .tmp, and no document cites a ticket, an issue or a session.

## Open questions

- Split attention.communication, whose children mix asking, reporting, presenting and prose craft, into four named groups: ask, report, present, prose. Proposed, not applied, because the current names still retrieve and a wide move would hide the semantic diff.
- Enforce the record rules mechanically as well as by policy: a check that fails when docs/ names .scratch or a ticket, or when the main area leaves main. Proposed, not written, because it is new code rather than a policy gap.
