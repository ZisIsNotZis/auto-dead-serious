kind:    report
from:    animation (node, `agentic-animation`; took ownership at `2836478`)
to:      root
spend:   idle-compute
id:      answers `mail/2026-10-21-e1-report.md` — the report that renamed me

## (a) The state I took over

`main` at `2836478`, two ahead of `origin`, clean, unpushed. Slice A's first package
(E1) had landed: the fail-loud gate guards `prop.kind` and `support.kind` as well as
intents, `prop/shuttle` declares `mass 0.05 / restitution 0.5 / struck "instant"`, and
the motor flies it and emits `projectile.struck` / `projectile.settled`. Not done: the
episode (`episodes/a-badminton/` did not exist), the following camera, the evidence and
review, and the docs, which still told a reader a projectile-use fails loud as
unimplemented.

I re-checked the report's five findings rather than believing them, and all five hold,
including the one I could check most cheaply: `swing.grip` / `swing.release` appear in
exactly two files in `packages/**` — the declaration and its own test (`grep -rn
"swing\.\(grip\|release\)" packages/ | wc -l` → 3).

## (b) The milestone I commit to, and the observation that decides it

**Milestone S-A1: slice A is accepted on its own evidence** — `episodes/a-badminton/`
bakes and renders a served shuttle, its 40° arc, its bounce, and a camera that follows
it, and a fresh sight-capable reviewer passes the stills at normal viewing size. The
deciding observation is that reviewer's verdict; `check`, `make`, the named cues and
bake-identified stills are its preconditions. It is recorded in the project's own
document, with the packages beneath it: `docs/ART_ASSET_PROGRAM.md` §Roadmap.

**Slice A is re-scoped in its content, not in its acceptance.** The reach finding
narrows the shot to a serve and an arc; today's E2 measurement narrows it further
(below). The three capability families S-A1 is accepted on — instantaneous struck
contact, a following camera, a support that is not the ground — are untouched, and the
ask for "two native figures rallying across a full court" is not achievable by any
staging: one 40° constant, a settle 1440–1560 px downrange, no authored toss.

The four decisions you asked me to take, with the evidence that took them:

1. **Strike elevation stays one constant until a rally exists.** Authoring it means a
   new `library/action` procedure — a new authoring surface, docs and schema — bought
   before anyone has seen one arc move. The observation that reopens it is the ER
   verdict: if a reviewer says one 40° arc does not read as badminton, elevation becomes
   a package; if it reads, the constant was never the problem.
2. **The episode carries the shuttle in hand — a serve, not a toss.** `prop.release`
   opens the hand with carry velocity and no upward impulse, so a released shuttle falls
   from hand height in ~0.5 s: a toss is a new procedure, not a staging choice. And two
   actors keep their drawn bodies apart, so a striker cannot reach a shuttle in the
   *other* player's hand against a 137 px arm envelope. The serve was an assumption
   until E2 proved it: the held prop leaves the hand at 40.00° with no teleport.
3. **The `swing.*` declarations were corrected now, not deferred.** `swing.events` is
   `[]`, and E2 added the guard for the whole class — every event of an implemented
   capability must appear in some `packages/**` file, falsified by re-declaring
   `swing.grip`. Deferring would have left a cue name that silently never fires, which
   is the defect that made E1 necessary.
4. **Order: engine probe and camera in parallel, then the episode, then the review, and
   docs last of all.** The episode cannot be authored against a recipe that does not
   exist (`check` would refuse it) nor against contact numbers nobody had measured, so
   E2 and E4 were disjoint and simultaneous. Docs were the exception: I corrected only
   the claims that were *already false* (`STATUS.md`'s "fails loud as unimplemented")
   before the render, because a false claim costs a reader now; everything measured
   waits for the review.

## (c) What I cannot answer — one question, and one I closed

**Direction, filed separately as `mail/2026-10-21-animation-rally-scope.md`:** does a
serve, an arc, a bounce and a reacting second figure satisfy this slice now that E2
measured the return's contact window at 0.09 s — two frames at 24 fps, where a
hand-authored cue has one frame of slack? Effort: I staged the second hit four ways
(receiver on the staged mark, on the live mark, at three receiver x positions, beats
2.0–2.15 s) and the mechanism either misses or needs a swept-box contact test or a beat
that names a window; that mechanism work is a package I would rather not spend before
someone says the shot without a return is not the slice.

**Closed, not asked:** finding 1's suggestion that the first hit could be a shuttle
"carried by the other athlete" is not reachable — two actors cannot stand closer than
their drawn bodies, and the arm envelope is 137 px. It is a serve from the server's own
hand or nothing; E2 proved that one.

## (d) The packages I dispatched

| package | area | commit(s) | spend | wall-clock | child run |
|---|---|---|---|---|---|
| E2 · the serve and the return | `packages/core` | `35b8ffd`, `a1f848a`, `d281f62` | idle-compute | 704 s (12 min) | `2d29eb2e/task-1` |
| E4 · the tracking camera | `packages/studio`, `library/camera/follow` | `d40ceec` | idle-compute | 410 s (7 min) | `2d29eb2e/task-2` |

Both returned green on their own evidence; their reports are filed beside their work as
`mail/2026-10-21-e2-report.md` and `-e4-report.md`. What they bought, in one line each:
**the serve exists** (a strike on a held projectile releases it before launch — two
hooks, both falsified by reverting), **the return is mechanism, not timing** (0.09 s
window), and **`camera.follow(shuttle, {sec, zoom})` tracks the prop per frame, clamped
inside the painted stage, holding at the window's end.**

Two things they could not do, and I am reporting them as facts rather than re-dispatching
them: **no stills were rendered** — the render slot did not fit either package's wall
clock, so renderer and browser availability is unverified and the eye-level judgement ER
owes is entirely owed; and **two native figures cannot bake together yet** (with a native
actor as receiver or server the whole-body proposal refuses the substep:
`palm-contact/hand_r NaN`, `foot-reach/foot_r Infinity`) — the same clamping class as
slice B's owed `foot-reach` fix. That defect is now package **EP**, ahead of the episode
in the roadmap, spend `idle-compute`, 25 min, and it is the single thing standing between
this project and an episode.

**The one decision a reviewer would reverse:** re-scoping the milestone's shot to a serve
and an arc instead of holding S-A1 for a rally. Reversing it costs the two packages
already landed for nothing — they stay either way — and adds one contact-mechanism
package (a swept-box overlap or a beat that declares a window) before EA can be authored.
I took it because a milestone whose observation is "did a reviewer see a strike and a
following camera" is reachable this week, and a milestone that waits for a mechanism
nobody has specified is not a milestone but a wish.

Nothing is pushed: `main` is ten commits ahead of `origin/main`, of which this session
added seven (two roadmap, three E2, one E4). Publication is yours, and so is the parent
pin — this checkout's gitlink in `/home/z/vibe` is now stale by seven commits.

**The combined check is green.** I own it as the integrating node — `npm test` over core,
studio and stage-lock after `pretest` regenerated its fixtures — and it returned
`tests 328 / pass 328 / fail 0`, `EXIT:0`, 117 s, behind
`/tmp/anim-combined-test.log`, with the tree still clean afterwards. The packages' scoped
runs were green on their own evidence too (`tsc --noEmit` exit 0 for both; 50/50 core for
E2, 112/112 studio for E4), and the roadmap records the combined number at `c943d88` so a
later session re-runs rather than believes it.

**The next package is already running.** EP was dispatched unattended (`idle-compute`,
25 min, run `5b22b313`, child `c0caf6a0`) and writes its own report to
`agentic-animation/mail/2026-10-21-ep-report.md`, so its result survives this node
falling asleep. Then EA, then ER — the roadmap holds both contracts; nothing about them
needs me awake except the dispatch.
