kind:    direction
from:    animation (node, `agentic-animation`), carried by root
to:      person
spend:   taste
id:      mail/2026-10-21-animation-takeover.md (c)

## The question

Is slice A still slice A if it ships without a return — a serve, a 40° arc, a bounce,
a camera that follows it, and a second native figure that reacts but does not strike?

The programme doc's slice A reads "two new native figures rally across the full court".
Two measurements now stand between that sentence and any episode:

1. **The return's contact window is 0.09 s** — two frames at 24 fps, with the striker's
   hand meeting the arc at hand height. Measured by E2 over a 0.01 s sweep: legal at
   2.00 and 2.08 s, missing at 1.98 and 2.10 s. A hand-authored cue has one frame of
   slack, so the return is not authorable as a cue; it is authorable only as a mechanism
   (a swept-box contact test across the frame, or a beat that names a window and lets the
   motor pick the contact frame).
2. **A full-court rally is not achievable by staging**: one fixed 40° elevation, a
   settle 1440–1560 px downrange on a painted 1920 stage, and no authored toss.

## Effort

Tried, all measured rather than argued:

- staging the receiver on the staged mark (the pre-E2 behaviour): the receiver walks to
  where the serve began and the second strike never happens — one `projectile.struck`,
  no second contact;
- staging it on the prop's **live** mark, which is now landed (`a1f848a`): the second
  contact works, and its window is the 0.09 s above;
- three receiver positions (x 1200 / 1250 / 1300 / 1400) and beats 2.0–2.15 s: the
  window does not widen, because it is set by the arc's descent through hand height,
  not by where the receiver stands;
- raising the strike elevation authorably: it is one engine constant
  (`STRIKE_ELEVATION = 40`) and lifting it means a new `library/action` procedure — a new
  authoring surface — which I deferred until a reviewer says one arc does not read;
- an authored toss to buy flight time: `prop.release` opens the hand with carry velocity
  and no upward impulse, so a released shuttle falls in ~0.5 s. A toss is a new
  procedure.

Every path is closed except the mechanism one, which is a package I can specify but not
justify on my own: it exists only to buy a second hit whose timing nobody will be able
to author by hand a second time either.

## What would reopen the question

One sentence from the person, in either direction:

- "a serve and an arc is the slice" — then EA is authored now, the milestone's
  observation is a reviewer's verdict on the serve, and the rally waits for the contact
  mechanism as its own later package;
- "it has to be a rally" — then the contact mechanism (swept-box overlap, or a beat with
  a declared window) enters the roadmap ahead of EA, spend `idle-compute`, and the
  milestone moves out by one package; and the elevation question probably opens too,
  because a one-shot rally is likely to be judged flat by the same reviewer.

## My recommendation, and what reversing it costs

Ship the serve first. The reviewer's verdict on an actual moving shot is worth more than
any argument about whether a second hit would have helped, and it is the observation the
milestone is defined by. Reversing it costs one package that has not been written yet and
nothing that has landed.

## One fact the person may want

`swing.grip` / `swing.release` were declared as events with no emitter in `packages/**`;
they are now undeclared, and a guard test refuses that class of declaration. Slice B
restores them with their emission when its shot bakes. This is in the roadmap, not a
question.

## Root's row

cost: either answer costs one package. "Ship the serve" is the package already specified;
"it has to be a rally" is that package plus a contact-mechanism package (swept-box overlap
or a declared contact window) and probably an elevation procedure behind it, so roughly
two to three times the work, all `idle-compute`.

priority: high, and it is the only thing standing between this project and a rendered shot
a person can look at. Everything the milestone needs is landed except the episode.

recommendation: **ship the serve.** The reviewer's verdict on one real moving shot is the
observation the milestone is defined by, and it cannot be bought by arguing about a second
hit. I accepted the content narrowing when I handed the project back to its node, and I am
noting that here rather than defending it — the slice's definition is the programme's
sentence, and changing what a slice *is* is the person's call, not mine.

what reversing costs: nothing that has landed. The rally path only adds packages that are
not written yet, and `swing.grip` / `swing.release` come back with slice B either way.
