# Portfolio

This workspace advances thirteen projects, of which three are experiments rather than products. The portfolio exists because nothing else held the answers to four questions the root must answer without reading a project: whether a project is advanced at all, how much authority its nodes hold, what it may spend, and when spending it is cheapest.

The order of work follows from what can and cannot be started. Two projects are mid-experiment, so the root cannot touch them until the person says they have stopped; that is the only hard ordering constraint and it removes nothing else from the schedule. After that the first work goes to what a person can experience soonest, because a felt result is the only evidence that the standard is right before it is applied thirteen times. Projects that need a product which does not exist yet wait, because their first step is a decision rather than work. The one project still in discussion waits for the rest to be arranged, which is what the person asked for.

## Milestones

- `join` — the two running projects are taken over, on the person's word and not before.
- `taste` — one project reaches a thing the person can run, with a pinned artefact and a rebuild command.
- `spend` — the first metered work is compared against the price clock, so the shift-or-any rule stops being a claim.

## Work packages

- `register` — the thirteen projects recorded with a level, a spend class and a pointer. Done.
- `plan-pointer` — the register names each project's plan by the path that file actually has, not by a directory this repository hopes exists. Two projects have no plan found by that search, and the row says `unknown` rather than inventing one; the first work in either of them is to find or write it.
- `petfleet-notes` — the person's product notes land in that project rather than in a conversation. Done.
- `join-orders` — the takeover of a running project written as its own first step, so the transition is a decision rather than an interruption.
- `go` — permission to act by the law and this register as they stand, not a list of launches. Every active project advances until its own advance ends: its milestone reached, a decision the root cannot take, or its granted spend exhausted, whichever comes first. That terminator is what bounds how many are alive at once, so no launch list is needed and nine simultaneous dispatches cannot happen by accident. Each contract declares its spend and its expected time, and the root decides shift-or-now by the wait-is-shorter-than-the-work rule rather than by the hour alone. Only one child may hold the gpu.
- `inbox` — a question no layer could answer is a directory under `docs/raise/`, and `tools/needs.py` renders `docs/needs-you.md` from it. On each new item the root sends one line naming that file and the count, plus the new item; it never restates the queue, because a message that grows is a summary the law refuses and a cost paid on every turn.

## Current facts

- Thirteen projects are in scope. Twelve are active, dormant or in discussion; two of those are running experiments and are not touched.
- `agent-policy` is infrastructure, not a project: it holds the law and is pinned like a child.
- The price clock, stated by the person: Beijing time, weekdays 09:00–12:00 and 14:00–18:00 are peak, and everything else including weekends and public holidays is idle at half price.
- The model rule, stated by the person: development uses the strongest available model, which today is `deepseek-flash`; a cheap model is for work a check decides rather than judgement, and a product's own calls run `gpt-6-luna`. `deepseek-pro`, `gpt-6.1-sol`, the volcano plan, `glm-5.3-flash` and the copilot pool are each unused for a reason recorded in `docs/method/models.md`.
- The price clock is a reason to wait, never a reason to choose a weaker model.
- A project with GPU or queue-bound work ignores the clock, because most of its wall-clock is spent waiting and its tokens are few. A project whose cost is tokens and whose work is a few hours waits for the idle window.
- Every project in the register now names a plan file. The search that establishes this reads content rather than filenames: `grep -rilE "roadmap|milestone|work package|路线图|里程碑|工作包" --include=*.md .` returns 45 files in `agentic-animation` and 77 in `local_lm_research`, where a filename search at depth three returned nothing and a plan was recorded as missing.
- `agentic-animation` keeps milestone state in `docs/STATUS.md` and its forward programme, the art asset programme, in `docs/ART_ASSET_PROGRAM.md`. Its engine milestone is closed; the programme is what remains.
- `local_lm_research` is a container in the sense this law means: `docs/plan/subprojects.md` owns which units exist, their goals, acceptance, dependencies and owners, and sixteen subprojects each own a `PLAN.md`. It also keeps a GPU lock and a resource table with a concurrency rule, which is the same discipline the law states, practised before it was written.
- `prompt_fixed_point` has no plan because its repository has no commits, which is a fact about git rather than a search result.
- `sys_gal`'s top-level `ROADMAP.md` is superseded by its own words and points at the v5 plan. The live plan is the v5 file.
- `prompt_fixed_point` holds nothing yet and stays in discussion until the others are arranged.

## Evidence

- The register: `docs/plan/portfolio.tsv`.
- The layout and the boundary between this file and a project: `docs/method/portfolio.md`.
- The law: `agent-policy/law/`, pinned in `agent-policy`.
- Per-project plans: the path column of the register.
