kind:    direction
spend:   taste
from:    root
to:      person
id:      raised from the first orientation report of `nomos`

One question about what the project is allowed to say it did.

`docs/method/design.md §1` claims the model does not fall out of its own noise
band on **two** axes: general capability and agentic capability. The selection
table at `report/sft-benchmark.md:132-140` records real attempts at the agentic
axis and every one is blocked offline: `huggingface.co` and PyPI unreachable,
MMLU blocked on `pyarrow`, HumanEval on docker and missing data, BFCL on HF data
plus a thousand-line harness. So half of the §1 claim currently has **zero
measurement**, and no release text may repeat it as though it did.

The choice: narrow §1 to the two axes actually measured (format and action
agreement), or keep the claim and buy the measurement.

## effort

Tried: the per-candidate offline verdicts above are attempts, not guesses, and
each names its blocker. Closed because the choice between "measure it" and
"stop claiming it" is a claim about the product's own worth, which is yours.
Reopens on: network access at package-install time, a local BFCL harness, or your
one sentence narrowing the claim.

## root's row

cost: a paragraph of §1 rewritten, or days of harness work.
priority: second — it rides on the same file as the money question and neither
blocks the other.
recommendation: narrow the claim now. A measured half that is true is worth more
than a whole that a reader can falsify in an afternoon.
