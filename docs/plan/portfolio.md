# Portfolio

This workspace holds fourteen names, ten of which advance now, one of which waits for a live writer to stop, one of which waits for a product that does not exist, and one of which is still a discussion.

The portfolio holds a project's goal at the level the person states it, because a name alone does not say which drawing project is meant. A goal is stable and it is not a description of how the project works; anything that would shift when the project reorganises belongs to the project and not here.

It also holds what a root must decide without looking inside anything: what a name refers to on disk, whether that name advances, how much authority its managers hold, which model runs its work, and which model its product calls at runtime. Everything about a project's insides belongs to that project, so this file does not say what any project is, where it keeps its documents, or what state it is in. A root that knew those things would be maintaining a second copy of somebody else's layout.

Every advancing project receives the same first contract, which is to take the roadmap over and carry it to its next milestone. The root learns a project by asking it, not by reading it, so the order in which projects are asked costs nothing and needs no plan.

## Decided while the person was away

The person left on the evening of 2026-10-21 and said that a question whose answer follows from root's model of him may be answered for him, and that anything he must review or decide waits for him. Six decisions were taken under that instruction, each recorded as `assumed` with root as the decider and each filed where it changes work — inside the project it belongs to, never in this file. None is a milestone acceptance: every milestone waits for him.

## The first contract

One text, dispatched to each advancing project with `{project}` replaced by its directory name. It is written once because ten copies that must stay in step are ten chances to drift.

```
kind:     manager
name:     {project}
roadmap:  docs/plan/portfolio.md, the `go` package; you serve the portfolio and you own {project}/

goal
Take {project}/'s roadmap over and carry it to its next milestone.

scope
Inside {project}/ only. Start from the checkout's current HEAD; do not fetch, pull or switch branch.
Commit inside {project} at each cohesive step; do not push. Touch no other directory, not this file, not docs/.

accept
Your report names the milestone, the command that shows the state it claims, and the decision you need from root, which may be none.
It passes when root can read those three without opening {project}/.

paths
Working directory {project}/; your document and roadmap inside it; your report into {project}/mail/ addressed `to: root`.

spend
machine_time, idle class; no device held exclusively; no money authorised beyond the development model; wall-clock 25 minutes for this advance, because the runtime kills a child at 30 and a killed child writes no report.
The model that runs you is deepseek/deepseek-flash at thinking medium; a model your product calls at runtime is the one its row names, and the two are not interchangeable. Terminator: the milestone, a decision beyond you, or the 25 minutes.

stop
At 15 minutes, start no new package and land what exists. At the terminator report once and return; do not wait for root.
```

A manager that finds a field of this contract unreadable raises `contract` rather than guessing, and root rewrites the contract instead of cancelling the package.

## Milestones

- `join` — of the two projects a live writer held, one is root's from the person's word of 2026-10-21 and the other is not taken while its writer holds it.
- `taste` — one project reaches a thing the person can run, with a pinned artefact and a rebuild command.
- `spend` — the first metered work is compared against the price clock, so the shift-or-any rule stops being a claim.

## Work packages

- `register` — fourteen names recorded with a directory, a status, a degree of agency and two models. Done.
- `go` — permission to act by the law and this register as they stand, not a list of launches. Each advancing project starts with the same first contract; the advance ends at the first of its milestone, a decision the root cannot take, or an exhausted grant, and that terminator is what bounds concurrency without a plan. Running: the ten managers came back or are still out; each return was judged by one fresh reviewer against the project's own acceptance, the verdict was filed into that project's `inbox/` with the next contract, and the manager was dispatched again. A milestone that passed its review still waits for the person's acceptance.
- `orient` — the first contract root ran before the rule changed: one read-only package per advancing project, 15 minutes each, reporting what the project is, the milestone it proposes next with evidence, and any question it cannot answer. Done: nine reports are filed in their projects' `mail/`, and root's answer sits beside each.
- `inbox` — `docs/raise/` with one directory per question, and `docs/needs-you.md` rendered from it by `tools/needs.py`. Done.
- `join-orders` — the takeover is folded into `go`: a project root may now manage gets the same manager contract as the others. Done for the one; the one a live writer holds has none.

## Current facts

- Ten projects advance, one is `later` because a live writer holds it, one is `dormant` and two are `early`.
- Every advancing project is assigned a manager: one agent owning that directory, its document and its roadmap, and the only writer in it. Root plans inside no project.
- Root's answer to a project's question goes into that project's `inbox/`; the questions that are the person's are in `docs/needs-you.md`, and a project advances only as far as a gate the person has not passed.
- The tree's message directories are still named `mail/` while the law calls them `inbox/`; each manager migrates its own on next touch, and root writes new messages to `inbox/`.

## Who plans a project

Root does not plan inside a project, and a package is not a plan. Dispatching implementation packages straight into a project makes root the thing the law forbids it to be: the planner of a directory it does not own. A project that advances gets a manager — one agent, that directory, that document, that roadmap — and the manager splits its own work, by the law's `kind test` and `manager owns`.

Root's acts are then exactly three: accept or refuse the milestone that manager proposes, answer the `contract` report it raises about the contract root wrote, and pass a `direction` report upward. A manager is not launched into an area that has a live writer, because two writers there produce a diff nobody owns.

## The loop after a report

A report is filed into the project it came from, in that project's `mail/`, because nothing about a project is filed above it. The milestone it proposes is accepted or refused there, in one line, before a second contract is written; a `contract` finding is answered there too, by rewriting the contract rather than by cancelling the package. Only the questions go up, and they go up through `mail/` addressed to `person`, where `tools/needs.py` renders them. This file therefore never names a project's insides, and the scope check enforces that rather than trusting it.

## Running

**2026-10-21, the first large-scale run.** The person said `go` and left, so all ten advanced at once. Two lessons are in the record rather than in a rule. Ten dispatches went out before anyone checked that the manager role resolves from a child's own directory; the role lived in the root's `.pi/agents/` and eight of the ten could not find it, so they failed at once and cost their full token price for nothing. One canary dispatch would have found it in seconds, and the role is now reachable from every directory rather than from one.

The second: the returned reports were dense enough that reading them myself would have made root the judge of work it can no longer see the inside of, so each went to a fresh reviewer whose verdict was filed into the project. The reviews found three things a manager's own reading would not have: a commit one `git gc` away from being lost, a milestone marked done whose criterion the tree contradicts, and an advance of 199 prose lines and zero code lines.

**2026-10-21, the runtime's own limit.** The first ten contracts declared a 120-minute wall-clock. The runtime kills a child at 30 minutes, so three advances were cut mid-action with nothing filed, and the declared number was advice nobody enforced. The contract now declares 25 minutes and names why; a limit this layer does not enforce is still the limit it must plan inside.

The ids, working directory and output log of whatever is live are not copied into this file: `subagent({action:"status"})` lists them with all three, so this file cannot drift from the truth.

## Evidence

- The register: `docs/plan/portfolio.tsv`.
- The launch record for the ten contracts: the `go` entry above and the commit that carries this file.
- The boundary between this file and a project: `docs/method/portfolio.md`.
- The law: `agent-policy/law/`, pinned in `agent-policy`.
- What waits on the person: `docs/needs-you.md`.
