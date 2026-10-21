kind:    cost
spend:   disk
from:    root
to:      person
id:      raised from the first orientation report of `helpagent`

One question about what "reproducible" is allowed to cost, and one thing I am
doing regardless of the answer.

`docs/paper-plan.md:45` demands a preprint whose every decisive number is
recomputable from the repository alone, with one command run once on a clean
machine. Today that is untrue by a wide margin: there is no reproduce entry point
and no tag, and the decisive raw rows live in `/tmp` on this machine —
`/tmp/wave1/final/n25` (600 MB), `r2` (114 MB), `r3` (61 MB) — together with the
analysis scripts that compute every interval in the paper. Tracked evidence stops
at `bench/runs/evidence` (802 files, 5.4 MB, newest 20261006), and
`.gitignore:5-7` excludes `bench/runs/*` by design.

So the choice is: **commit the compact per-run projections** (14.4 MB + 13.2 MB
before compaction, a few hundred KB after) plus the scripts, which makes the CI
tables recomputable without a model server; or **re-run** the campaign from
scratch, which is hours of metered wall-clock against a local model.

**Correction, and it is a correction of my own numbers.** I wrote that the bytes
were 775 MB across `n25`/`r2`/`r3`. They are **2.0 GB across 53 270 files**, and the
extra 1.3 GB is not padding: the analysis script also opens `our-n5`, `n9` and
`n17`, because seeds 1..17 predate the n25 wave. Copying only the three directories
named would have made the head-to-head unrecomputable **and silently so** — a missing
root reads as an empty list, so the same script prints `+0.06 [−3.35, +3.71]` over
680 rows instead of `−0.320 [−3.520, +3.080]` over 1000, and raises nothing. A short
home does not fail loudly; it reports parity.

Separately, and not waiting on your answer: `/tmp` is one reboot from erasing the
only home of three archived verdicts. The project's node is copying those bytes
to a declared home with verified hashes now. That is a durability act, not a
choice — the law ranks a temporary path lowest and forbids leaving a fact there.

## effort

Tried: located and sized all three datasets and their analysis scripts, confirmed
the tracked evidence predates the final campaign, and confirmed no analysis script
is in git. Closed because the trade is storage-and-durability against hours of
compute, which is money-shaped. Reopens on: a decision either way, or a measurement
of the smallest committed subset that reproduces `24.640`, `−0.320`,
`[−3.520, +3.080]` exactly.

## root's row

cost: a few hundred KB of committed projections, or hours of local compute.
priority: with the order question — the paper's acceptance depends on it.
recommendation: commit the projections plus the scripts. A number whose evidence
is 775 MB in `/tmp` is not evidence a reader can check, and re-running to prove
something already measured buys nothing a committed projection does not.
