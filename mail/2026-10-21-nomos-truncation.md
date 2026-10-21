kind:    cost
spend:   money
from:    root
to:      person
id:      raised by the `nomos` node from mail/2026-10-21-nomos-takeover.md C2

One question about a 1.6% leak: may it be measured or must it stay labelled?

42 of 2664 anchor answers hit `finish_reason: length` at max_tokens 320 (1.6%; 30 of
1452 on the local arm). They enter the statistics as they are, which can only push
hit rates down by an amount nobody has measured. Measuring it means re-drawing the
whole anchor at 600 tokens — 2664 metered calls, roughly the same ¥2.1 again. The
local arm's 30 can be regenerated on the 4090 for free, but that covers one side only.

The alternative is to keep the word 未测 in the report and the paper, which is
honest and costs nothing.

## effort

Tried: counted the truncations per arm, confirmed the local arm can be redrawn
free, and confirmed the metered arm cannot. Closed because 2664 more calls is money.
Reopens on: a ceiling, or "not worth measuring".

## root's row

cost: ≈¥2.1, the same as the whole anchor.
priority: middle — it does not change any sign, only a possible underestimate.
recommendation: don't pay. 1.6% truncations can only make the law's advantage look
smaller than it is, so the direction of the finding is safe; write 未测 and move on.
