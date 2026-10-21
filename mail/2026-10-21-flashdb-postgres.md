kind:    cost
spend:   money
from:    root
to:      person
id:      raised from the first orientation report of `flashdb`

One install, asked for because a comparison cannot be re-run without it.

The external comparison that this project lost (3/5 sustained blocks against
sqlite 5/5 and postgres 5/5 at 200 rps) was measured against postgres 18.6. It
is now absent from the box: `which psql pg_ctl` → nothing, `/usr/lib/postgresql`
→ absent, only `libpq5` installed. M5's postgres leg and any honest re-run of
the lost comparison need it back. The project's own rule forbids substituting a
different engine for it.

## effort

Tried: the binary paths above, the package list, and the workplan's rule that no
substitute stands in. Closed because installing a system package is an act on
your machine. Reopens on: an authorised install, system or unprivileged
user-space build, with version and settings read back from the running server.

## root's row

cost: one package install, no money beyond bandwidth; the re-run itself is idle compute.
priority: after the quiet window — the quiet window decides M3 and this only
re-arms M5.
recommendation: install it in user space when convenient; it unblocks the one
comparison the project's README currently reports as lost.
