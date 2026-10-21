kind:    resource
spend:   tokens
from:    learn_draw (the node that holds /home/z/vibe/learn_draw)
to:      root
id:      answers the ownership contract issued after mail/2026-10-21-answers.md

Ownership taken at `5e12d36`, now `5e15e0b`; tree clean, nothing staged. One grant is
needed and it is at the end; the four things you asked for are first.

## (a) The state I took over, verified rather than read

`learn_draw` at `5e12d36` plus the report commits. Two facts in the tree were wrong and are
now corrected in `STATUS.md`, `evidence/acceptance-ledger.md` and `work/wave-log.md`:

- **`B-hand-study-v1` is real and reproducible.** Rebuilt from committed source at
  `evidence/B-hand-study-v1/`: `source/`, `tests/` (23, OK), `artwork.svg` 2 997 633 B,
  `artwork.png` 900x700, `check/` with `draft-fullres.png` first, `manifest.json` +
  `manifest.sha256` (19/19), README, dispatch record `work/wave11-b-study.js`. It carries
  **no art verdict**, correctly. Its report was untracked in this project's `mail/` — landed
  as `ed24d88`.
- **`A-bow-study-v2` is worse than "awaiting artwork" and better than "no artwork".** It has
  `artwork.svg`/`artwork.png` that are exactly the committed source's output, but it is not
  reviewable: `README.md` is byte-identical to v1's (`46e772ff…`) and describes numbers the
  source no longer emits, there is no `check/`, no manifest, no negative control, and the
  inherited suite fails **8 of 17** — re-run by me in place, not taken from a report:
  `test_every_crossing_has_a_depth_break_and_a_broken_rear_edge` (13 audited crossings,
  |dz| 0.7–15.8 px against a 16 px cloth thickness; two rear edges drawn through),
  `test_every_triangle_wears_its_own_winding` (4 of 1240), `test_the_field_actually_varies`
  (width 77.7–301.6 px, ratio 3.88 against the 4.0 floor), `test_the_knot_is_a_waist_between_the_loops`
  (knot 113.3–113.5 px vs loops 159.6 px), `test_width_is_continuous_along_the_emitted_strip`
  (9.03 px isolated jump against a 3.0 limit), plus the three bundle/manifest tests.
- **The v1 image review, whose six defects v2 exists to repair, has no verbatim record
  anywhere in the tree.** It survives only as a paraphrase in the ledger. That is why the new
  review archive exists: every verdict from now on lands verbatim, bound to a hash.
- Two structural gaps inherited: no independent structural verification of B was ever
  recorded (wave 4/7 runs were reaped or never returned), and A v6/v6-closeout/v8 carry no
  image review at all.
- Budget fact I am designing around: the harness kills a child at 30 minutes unless the
  dispatch raises the deadline (P34). B's writer had 2 hours and overran by ~25 minutes on
  renderer geometry, not on drawing.

## (b) The milestone I commit to next, and the observation that decides it

**R1a exit**, on the roadmap's own exit line: both object studies exist as frozen, verifiably
reproducible packages and each carries an independent image-only verdict with **no blocking
finding** bound to a pinned image hash — then root presents the two separately to the person.
R1b, M2 and the sealed brief are untouched by this.

It is decided by two observations, neither of them mine:

1. `evidence/reviews-r1a/B-hand-study-v1-image-review-1.md` returns no blocking finding
   against `check/draft-fullres.png` `e428bb0d…` / `check/draft.png` `0dbeb263…` at `5e12d36`.
2. In `evidence/A-bow-study-v2/`, `PYTHONDONTWRITEBYTECODE=1 ../../../../.venv/bin/python -m
   unittest discover -s tests -t .` prints `OK` with the four inherited test files unweakened
   and six defect controls failing on return, and then `evidence/reviews-r1a/A-bow-study-v2-image-review-1.md`
   returns no blocking finding against its frozen image.

If either review returns blocking findings, R1a is not "still in flight": one scoped repair by
the original writer and one re-review, then the study is reported **unresolved** with its image
and its findings. I will not move that line, and I will not award a verdict myself.

**Observation 1 has already returned, and it says BLOCK.** The review is archived verbatim at
`evidence/reviews-r1a/B-hand-study-v1-image-review-1.md`: three blocking findings, five
nonblocking. (1) The occlusion is inverted — the digits are drawn in front of the plate's near rim,
so nothing visible carries the dish and the rim is cut where it must be foreground; (2) a radial
spoke fan with concentric terracing in the well turns the bowl into a flat lens with one rim — the
loudest artefact in the picture, and its cause was already named in B's own README (sub-pixel apex
quads inflated 0.45 px, 60-step revolution flat-shaded); (3) the hand is five near-parallel
near-equal prongs, no thumb opposition, no knuckle mass. Two of the three are the study contract's
own named failure readings — "a hand intersecting a plate" and "fingers as rake tines". The
reviewer stated it opened only the two PNGs and executed nothing, so the verdict is independent of
the producer's reasoning, which is what you asked for. B's writer was right to refuse the verdict
and right about what a reviewer would strike: uniformity and palm anatomy are exactly blockers 3
and part of 1. So R1a now has its first bound art disposition, and it is a failure, not a pass.

The plan's repair cycle therefore opened: one scoped repair, then a re-review against the repaired
revision with a fresh manifest (package 3 below). I took four directions as **assumed** so the
writer is not left guessing, and I name what reversing each costs: the hand is under the plate with
an unbroken near rim; the thumb opposes on the near side — which is the contract's own wording that
v1's README records itself as having violated; digits vary in width and reach; the palm gains a
knuckle row and a heel. Reversal costs one full review cycle each, because each reversal leaves a
blocker standing.

## (c) What I cannot answer

**One grant: this node's own wall clock.** My 90 minutes end before both children return, so
the filing of their reports, the A image review that follows the repair, and the R1a exit
report all need a second session of this node. Effort: I sized the two packages to fit
*inside* the harness rather than the session (75- and 25-minute deadlines, checkpoint steer at
65), committed every contract and run id before launching, and left the tree at a safe point —
status current, both run ids in `work/wave12-contracts.md`, `git status` clean, so a kill now
loses nothing but the wall clock. What would reopen it: nothing; it closes only with the grant. The B verdict landing inside this
session made the grant less optional, not more: the repair returns in roughly 75 minutes from its
launch, and the re-review that decides whether B is passable needs a session that is awake after that.

Residual risk I am not asking you to answer, named so it is not a surprise: defect 6 of v1's
review ("nearly all interior strokes free-terminate, and a single flat fill leaves overlap
order unreadable") is the least likely of the six to have an honest mechanical signature. I
mapped all six to emitted-geometry signatures and forbade a lowered threshold, so if the writer
finds one untestable it raises a `contract` report and I re-cut that item to a measured
statement plus the reviewer's verdict. The other risk is the one B's own writer flagged: the
digits are uniform in width and reach and the palm has no anatomy, which is the contract's
"rake tines" failure moved from pose to uniformity. If the review strikes those, the repair is
a pose parameter change in `source/scene.py`, not a new construction.

## (d) The packages I dispatched, spend class and wall clock

All three launched `async`, `fresh` context, `worktree: false`, from the checkout. No reservation is
written for any: none holds an exclusive resource.

1. **`r1a-a-bow-v2-repair`** — work package, **one writer**, owns exactly
   `evidence/A-bow-study-v2/`. Retune the turn geometry until the inherited law holds with the
   inherited tests unmodified; a test per named defect with a control that fails when v1's
   behaviour returns; a real README; `check/` + manifest + negative control; byte-identical
   rebuild. **Spend: `idle-compute` + `time`** (local CPU only, no network write, no paid API,
   no GPU). **Wall clock 75 min, hard stop, checkpoint at 65.** Run
   `97d0e1c2-0ef3-410a-8afe-449930bc6c3a`.
2. **`r1a-b-image-review-1`** — review package, **the art verdict B's writer refused to
   award**. It judges exactly two artefacts and nothing else:
   `evidence/B-hand-study-v1/check/draft-fullres.png` (`e428bb0d…`, 900x700, 1:1 — detail is
   judged here) and `check/draft.png` (`0dbeb263…`, byte-identical to `artwork.png`), at
   `5e12d36`. **It is blind to the producer's reasoning:** `fresh` context, two PNGs and the
   four acceptance questions as its whole window, forbidden the README, `source/`, `tests/`,
   `check/report.txt`, the manifest, the ledger, the wave log and the writer's own
   self-assessment; it is told that a verdict formed after reading any producer document is
   void. It writes one report and no other file. **Spend: `idle-compute` + `time`. Wall clock
   25 min, hard stop.** Run `d5852429-afb3-47ae-b6d8-2cf270ce7655`.

**Why not before-or-after, which is how you framed it.** The review is read-only in the study
tree — it holds no write area there — so it is not a second writer and "one live writer per
area" is satisfied with exactly one writer, v2. I ran them together because the review is the
short pole and its verdict is independent of the repair. One consequence I did act on: the
B **structural** review is deliberately not dispatched yet, because it would regenerate
`check/` inside the directory the image reviewer is reading, which is a write into a frozen
area mid-read; it goes out the moment the verdict lands, against the revision the verdict binds
to. The verdict landed inside this session and it BLOCKED, so that structural pass now reviews
the repaired revision rather than `5e12d36` — a mechanical pass over a construction that is
about to change is work that has to be redone.

3. **`r1a-b-hand-repair-1`** — work package, **one writer**, owns a new directory
   `evidence/B-hand-study-v1-r1/` copied from the frozen revision; `B-hand-study-v1/` is left
   untouched because it is the revision the BLOCK binds to by hash. Repairs the three blockers
   with the four directions in (b), a test and a failing mutation per blocker, fresh
   `check/`+manifest, a README carrying a finding-to-repair table against the archived review.
   **Spend: `idle-compute` + `time`.** **Wall clock 75 min, hard stop, checkpoint at 65.** Run
   `eec45d67-36fe-4af2-8454-ef17ebeaa3e1` — launched the same session, forty minutes after the
   verdict returned, so the repair does not wait on the grant this message is asking for.

**Cut but not launched** (`work/wave13-contracts.md`): the A v2 image review, blind to v2's
producer and **not** given the six v1 defects as a checklist, because a reviewer handed the
previous verdict answers the previous verdict; and the B structural review against the repaired
revision.

## effort

State claims: `git log`, `git status --porcelain`, `sha256sum` over `B-hand-study-v1/{README.md,artwork.png,artwork.svg,check/*}`,
`wc -c`, the two PNG headers for dimensions, and the v2 suite re-run in place with
`PYTHONDONTWRITEBYTECODE=1` and `-v` so the eight failing test names are the run's own output;
`git status` clean afterwards. Reads: this project's `mail/` (three files), `AGENTS.md`,
`STATUS.md`, `work/r1a-object-study-contracts.md`, `work/m1a-m1b-plan.md` (owners, budgets,
review pattern, repair cycle), `work/wave-log.md`, `evidence/acceptance-ledger.md`,
`check/report.txt`, `work/wave11-b-study.js` for the dispatch form, and
`/home/z/vibe/agent-policy/AGENTS.md` once for the law. The sealed brief was not opened. No
network write, no paid API, no GPU, no similarity/CLIP run — "no model run" read as this node
not running a model over the artwork; the two packages' own model runs are their declared
spend. Closed paths: I did not repair the two studies myself, because a node that splits work
does not then execute it, and I did not restate the six v1 defects as my own judgement — they
are quoted from the ledger with the reviewer's own "locations are approximations" caveat.
Reopens on: a `contract` report from either package (a test that cannot be satisfied by a
truthful drawing), a review that returns BLOCKED for missing modality, or a run reaped before
its first commit — each of which I answer from the tree, not from this message.
