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

## Who plans a project

Root does not plan inside a project, and a package is not a plan. Dispatching implementation packages straight into a project makes root the thing the law forbids it to be: the planner of a node it does not own. A project that advances gets its own node — one agent, that directory, that document, that roadmap — and the node splits its own work. Root's acts are then exactly three: accept or refuse the milestone that node proposes, answer the `contract` report it raises about the contract root wrote, and pass a `direction` report upward unchanged.

`node` is that agent, defined at `.pi/agents/node.md`; it reports to root and never to a person. The packages in flight when this rule was written are the last root-dispatched ones: each finishes, its report is filed under its project, and the project's node is launched to take the roadmap over. A node is not launched into an area that has a live writer, because two writers there produce a diff nobody owns.

## The loop after a report

A first report is filed into the project it came from, in that project's `mail/`, because nothing about a project is filed above it. The milestone it proposes is accepted or refused there, in one line, before a second contract is written; a `contract` finding is answered there too, by rewriting the contract rather than by cancelling the package. Only the questions go up, and they go up through `mail/` addressed to `person`, where `tools/needs.py` renders them. This file therefore never names a project, and the scope check enforces that rather than trusting it.

## Running

**2026-10-21, provider failure.** All five runs then in flight died with a connection error from the model provider, within the same minute: the nine orientation packages had finished, and the five that followed (one engine package, one benchmark package, one art study, one independent review, one late orientation) all failed at once. None had written a file — all five checkouts are clean and their last commit is one of mine — so the loss is the tokens already spent and nothing else.

Handling, in the order the law gives it: the failure is reported rather than retried silently; one run is relaunched as a probe, because a provider that answers again answers for all of them; the rest wait behind that probe rather than burning five runs' worth of tokens to learn the same thing. A run that fails at its first tool call is a provider problem and costs nothing to notice.

The ids, working directory and output log of whatever is live are not copied here: `subagent({action:"status"})` lists them with all three, so this file cannot drift from the truth. A report that arrives is filed under the directory it came from, and the milestone it proposes is accepted or refused there in one line before a second contract is written.

## Evidence

- The register: `docs/plan/portfolio.tsv`.
- The launch record for the nine first contracts: the `orient` entry above and the pinned commit that carries this file.
- The boundary between this file and a project: `docs/method/portfolio.md`.
- The law: `agent-policy/law/`, pinned in `agent-policy`.
- What waits on the person: `docs/needs-you.md`.
