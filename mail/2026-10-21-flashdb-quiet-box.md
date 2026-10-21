kind:    resource
spend:   tokens
from:    root
to:      person
id:      raised from the first orientation report of `flashdb`

One machine, asked for a quiet window.

`flashdb`'s M3 milestone has two open clauses and both need a measurement that
cannot run under load. Its own rule (`docs/plan/workplan.md:71-72`) is that the
paired block never runs under foreign load. Measured at 2026-10-21T03:30Z:
`uptime` → 7.13 / 5.52 / 5.13 on 12 cores. The previous probe was invalidated
the same way — loadavg 1.9 → 9.9 from another project — and its twelve output
files are still in the tree as evidence of that.

The measurement itself is cheap: 5 paired blocks, snapshot restore verified,
stderr kept, and a per-window attribution of any rejected lag. It decides
whether the external comparison stays lost.

## effort

Tried: WP-2 is written and queued and has never run; the old probe is invalid
and says so only in prose; the fix it would test is committed and bound by
`engine/tests/order_no_index.rs`. Closed because idle compute cannot manufacture
a quiet box — the load is another project of yours on the same 12 cores.
Reopens on: sustained loadavg < 2 before each arm run, or a second machine.

## root's row

cost: one quiet window on this box, or one borrowed machine.
priority: first among the resource items — it is the only thing that can change
this project's roadmap, and its acceptance already exists.
recommendation: give it a window you choose; the project can queue itself and
resume without further instruction.
