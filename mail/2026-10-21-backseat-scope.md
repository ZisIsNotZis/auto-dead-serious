kind:    direction
spend:   taste
from:    root
to:      person
id:      raised from the first orientation report of `backseat`

One question, about the price of entry to the next milestone.

`backseat`'s M0′ gate has four items and three are not met. One of them — the
cursor backlog — needs the pipeline running, which needs your LiteLLM proxy at
`127.0.0.1:4000` (a separate `resource` message). The scope question is this:

> Is M0′ all five channels (A screen, B accessibility tree, C filesystem, E
> process/input/audio), or is M0′ channel A plus a narrowed milestone, with
> B/C/E re-homed into their own milestone?

Today only channel A has data: one screen sensor, `kb` 0 rows, and
`EventKind` in `backseat/bus.py` carries screen kinds only, with the other five
sensors marked unimplemented in `docs/SCHEMA.md`. The evidence harness can now
score channel A end to end. Five adapters in one package would be a multi-day
build whose acceptance — a per-channel exit criterion — nobody has written yet.

## effort

Tried: measured that only A has data, checked `bus.py` and the schema for the
other sensors, and confirmed the eval harness's channel-A numbers on the frozen
snapshot. Closed because "is A-alone evidence enough to start the witness
harness" is a judgement about what the product is worth showing, not a fact
about the tree. Reopens on: your one sentence, or a written per-channel exit
criterion that makes five adapters a bounded package.

## root's row

cost: five adapters is days; narrowing costs one roadmap edit and re-homes three
rows.
priority: high among the taste questions — three of this project's milestones
(deposit: M1′, and the witness release behind it) wait behind it.
recommendation: narrow M0′ to channel A and re-home B/C/E. A witness that sees
one channel and can be scored beats five adapters nobody can accept.
