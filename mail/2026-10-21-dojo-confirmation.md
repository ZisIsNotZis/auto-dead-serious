kind:    direction
spend:   taste
from:    root
to:      person
id:      raised from the first orientation report of `dojo`

One question only you can answer: did you ever confirm M1 and M1.5 by hand?

`docs/plan.md:46` makes M1.5's checkpoint "play a session yourself, then tell me
the trace path", and `docs/plan.md:3` says the plan only enters automatic
execution after you confirm it. The project searched its own evidence directories
and found model-run provenance but no record of your verdict — not "no", but
"nothing written down that a later session can check".

This matters now because M2 (the end-of-session distillation pipeline) is
proposed as the next milestone, and M2 is the only milestone that unlocks M3, M4
and M5. Running it on top of an unconfirmed M1.5 would be building on a
checkpoint nobody closed.

Reopens on: one sentence — "M1.5 is confirmed" or "it is not" — or a landed
record of the checkpoint that a reader can point at.

## effort

Tried: both plan lines, the M1.5 checkpoint text, and a grep across the evidence
directories and `.scratch/` for a checkpoint verdict. Closed because only you
know whether you played the session. Reopens as above.

## root's row

cost: one sentence, or a short session if you play it now.
priority: highest of the taste questions, because it gates this project's whole
remaining chain.
recommendation: confirm or refuse it explicitly; if you no longer remember, say
"unconfirmed" and let M2's first package re-run the M1.5 checkpoint as its entry
condition.
