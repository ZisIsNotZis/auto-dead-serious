# Portfolio

This workspace holds thirteen names, ten of which advance now, one of which waits for a live writer to stop, one of which waits for a product that does not exist, and one of which is still a discussion.

The portfolio holds a project's goal at the level the person states it, because a name alone does not say which drawing project is meant. A goal is stable and it is not a description of how the project works; anything that would shift when the project reorganises belongs to the project and not here.

It also holds what a root must decide without looking inside anything: what a name refers to on disk, whether that name advances, how much authority its nodes hold, which model runs its work, and which model its product calls at runtime. Everything about a project's insides belongs to that project, so this file does not say what any project is, where it keeps its documents, or what state it is in. A root that knew those things would be maintaining a second copy of somebody else's layout.

Every advancing project receives the same first contract, which is to take the roadmap over and carry it to its next milestone. The root learns a project by asking it, not by reading it, so the order in which projects are asked costs nothing and needs no plan.

## Milestones

- `join` — of the two projects a live writer held, one is root's from the person's word of 2026-10-21 and the other is not taken while its writer holds it.
- `taste` — one project reaches a thing the person can run, with a pinned artefact and a rebuild command.
- `spend` — the first metered work is compared against the price clock, so the shift-or-any rule stops being a claim.

## Work packages

- `register` — thirteen names recorded with a directory, a status, a degree of agency and two models. Done.
- `go` — permission to act by the law and this register as they stand, not a list of launches. Each advancing project starts with the same first contract; the advance ends at the first of its milestone, a decision the root cannot take, or an exhausted grant, and that terminator is what bounds concurrency without a plan. Started: ten manager contracts are out, one per advancing project.
- `orient` — the first contract root ran before the rule changed: one read-only package per advancing project, 15 minutes each, reporting what the project is, the milestone it proposes next with evidence, and any question it cannot answer. Done: nine reports are filed in their projects' `mail/`, and root's answer sits beside each.
- `inbox` — `docs/raise/` with one directory per question, and `docs/needs-you.md` rendered from it by `tools/needs.py`. Done.
- `join-orders` — the takeover is folded into `go`: a project root may now manage gets the same manager contract as the others. Done for the one; the one a live writer holds has none.

## Current facts

- Ten projects advance, one is `later` because a live writer holds it, one is `dormant` and one is `early`.
- Every advancing project has its manager: one agent owning that directory, its document and its roadmap. Root plans inside no project.
- Each advancing project's `mail/` holds root's answer naming the next milestone, except where the answer is the person's; those questions are in `docs/needs-you.md` and their projects advance only as far as the gate.

## Who plans a project

Root does not plan inside a project, and a package is not a plan. Dispatching implementation packages straight into a project makes root the thing the law forbids it to be: the planner of a node it does not own. A project that advances gets a manager — one agent, that directory, that document, that roadmap — and the manager splits its own work, by the law's `kind test` and `manager owns`.

Root's acts are then exactly three: accept or refuse the milestone that manager proposes, answer the `contract` report it raises about the contract root wrote, and pass a `direction` report upward. A manager is not launched into an area that has a live writer, because two writers there produce a diff nobody owns.

## The loop after a report

A report is filed into the project it came from, in that project's `mail/`, because nothing about a project is filed above it. The milestone it proposes is accepted or refused there, in one line, before a second contract is written; a `contract` finding is answered there too, by rewriting the contract rather than by cancelling the package. Only the questions go up, and they go up through `mail/` addressed to `person`, where `tools/needs.py` renders them. This file therefore never names a project's insides, and the scope check enforces that rather than trusting it.

## Running

**2026-10-21, provider failure.** Five runs then in flight died together with a connection error from the model provider, within the same minute; the nine orientation packages had finished, and the five that followed all failed at once. None had written a file. The ten manager contracts were launched after that, against the same provider; whether it answers is read from the first report and not assumed here.

The ids, working directory and output log of whatever is live are not copied into this file: `subagent({action:"status"})` lists them with all three, so this file cannot drift from the truth.

## Evidence

- The register: `docs/plan/portfolio.tsv`.
- The launch record for the ten contracts: the `go` entry above and the commit that carries this file.
- The boundary between this file and a project: `docs/method/portfolio.md`.
- The law: `agent-policy/law/`, pinned in `agent-policy`.
- What waits on the person: `docs/needs-you.md`.
