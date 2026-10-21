# Portfolio

This workspace holds thirteen names, nine of which advance now, two of which wait for the person's word, one of which waits for a product that does not exist, and one of which is still a discussion.

The portfolio holds a project's goal at the level the person states it, because a name alone does not say which drawing project is meant. A goal is stable and it is not a description of how the project works; anything that would shift when the project reorganises belongs to the project and not here.

It also holds what a root must decide without looking inside anything: what a name refers to on disk, whether that name advances, how much authority its nodes hold, which model runs its work, and which model its product calls at runtime. Everything about a project's insides belongs to that project, so this file does not say what any project is, where it keeps its documents, or what state it is in. A root that knew those things would be maintaining a second copy of somebody else's layout.

The order of work has one hard constraint: two projects are mid-experiment, so nothing touches them until the person says they have stopped. Beyond that, every advancing project receives the same first contract, which is to orient itself and report what it proposes next. The root learns a project by asking it, not by reading it, so the order in which projects are asked costs nothing and needs no plan.

## Milestones

- `join` — the two running projects are taken over, on the person's word and not before.
- `taste` — one project reaches a thing the person can run, with a pinned artefact and a rebuild command.
- `spend` — the first metered work is compared against the price clock, so the shift-or-any rule stops being a claim.

## Work packages

- `register` — thirteen names recorded with a directory, a status, a degree of agency and two models. Done.
- `go` — permission to act by the law and this register as they stand, not a list of launches. Each advancing project starts with the same first contract; the advance ends at the first of its milestone, a decision the root cannot take, or an exhausted grant, and that terminator is what bounds concurrency without a plan. Started: nine first-orientation contracts are out, one per advancing project (see the launch record).
- `orient` — the first contract, one per advancing project: boundary is reaching the next milestone by orienting inside its own directory, the acceptance is a report naming what the project is, the milestone it proposes next with evidence, and any question it cannot answer, and the report target is the root. Spend: `idle-compute`, read-only, 15 minutes wall-clock each, no metered device and no exclusive one. It is a package, so the root files each report into that project's own directory when it arrives.
- `inbox` — `docs/raise/` with one directory per question, and `docs/needs-you.md` rendered from it by `tools/needs.py`. Done.
- `join-orders` — a takeover written as its own first contract, so the transition is a decision rather than an interruption.

## Current facts

- Nine projects advance, two are `later` on the person's word, one is `dormant` and one is `early`.
- The nine advancing projects each received the same first-orientation contract on this `go`; none had been dispatched before, and no project has a report back yet. A report that comes back is filed into that project's own directory, and the milestone it proposes is accepted or refused here in one line before any second contract is written.

## Running

Nine orientation runs, launched together, declared at 15 minutes wall-clock each. A run silent past that is presumed stuck when this file is next read, and is cancelled rather than waited for, because it is read-only and would lose nothing.

Their ids, working directory and output log are not copied here: `subagent({action:"status"})` lists the nine active async runs with all three, so the schedule is one command away and this file cannot drift from it. A report that arrives is filed under the directory it came from, and the milestone it proposes is accepted or refused here in one line before any second contract is written.

## Evidence

- The register: `docs/plan/portfolio.tsv`.
- The launch record for the nine first contracts: the `orient` entry above and the pinned commit that carries this file.
- The boundary between this file and a project: `docs/method/portfolio.md`.
- The law: `agent-policy/law/`, pinned in `agent-policy`.
- What waits on the person: `docs/needs-you.md`.
