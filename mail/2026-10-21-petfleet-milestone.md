kind:    direction
spend:   taste
from:    root
to:      person
id:      raised from the first orientation report of `petfleet`

One question: what `petfleet` builds next.

The project has no milestone to accept. `docs/plan/PLAN.md:64` reads
`## M3 — not planned`, with eleven unordered candidates, and the newest commit is
your own product notes, which say of themselves "these are requirements and
observations, not a plan; the plan owns the order". So the report proposes one
candidate rather than a milestone, and it is waiting on you rather than on work:

> **M3.0 — draw only what is connected, and make the fleet's scale and boxes
> legible.** Three items, all from your notes: a form with no connection should
> not be drawn and the daemon should say why; size should follow the family's
> scale; boxes legible by kind, speech body white ground with black text, and
> resizable.

Why this candidate and not the M3 list: your "ghosts" observation matches one
mechanism exactly — ancestors of a declared path are created as implicit actors
and drawn at 0.62 sprite opacity until the last child leaves
(`petfleet.py:883,1035,1447-1466`). That makes it a defect with a cause, and its
acceptance is observable headlessly: declare `a.b.c` from one socket and query
`a.b`, which today returns a live record with no field saying "not connected".

Separately, and already declared in the project's README: the repository has no
push destination, so nothing is backed up off this machine. That waits on you
choosing a host and is not new.

## effort

Tried: the M3 section, the product notes, the README, the full log (no plan
commit after `d9a68a6`), and a grep for "M3" across the docs — three hits, all
restatements of "unplanned". Closed because the order is the plan's and the plan
is silent. Reopens on: a plan commit adding M3 rows, or your one sentence naming
the priority.

## root's row

cost: the M3.0 package is a day of local work; its protocol change is a field
added to the status record, which the project's own architecture doc already
contemplates.
priority: third — it is the cheapest of the taste questions and the one whose
acceptance is already observable.
recommendation: accept M3.0 as the next milestone, and give the host name in the
same breath so the push gap stops being carried.
