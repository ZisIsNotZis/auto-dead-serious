# Vibe workspace knowledge

Project-specific knowledge for the Auto Dead Serious workspace — the recommended companion to the project-agnostic `AGENTS.md`, which holds universal policy only.

## Layout

1. This directory aggregates independent child repositories as pinned submodules: keep each child independent and preserve the parent submodule relationship.
2. Work inside a child follows that child's `AGENTS.md`/`CLAUDE.md` first; root `AGENTS.md` supplies the universal policy every child inherits.
3. When preparing a child for GitHub, a trailing `_private` in the content-derived slug marks a private repository.
4. The policy is split: root `AGENTS.md` is the always-on core (invariants, coordination scope, triggers, maintenance); `docs/policy/reference.md` holds the detail, cited as `R-*` sections. Project knowledge stays here, never in `AGENTS.md` (`R-DOC.11`).

## Declarations

- **Coordination mode: local** (core M1) — one primary checkout plus a worktree per concurrent writer, subagents only. No locks, heartbeats for tickets, mailbox polling, ordinal races or formal trackers; `docs/policy/remote-coordination.md` is not read. Switch to **remote** (M2) when the user says so, or when another writer is known to push to the same branch; record the change in this file.
- **Harness: pi** — generic and model-agnostic; subagents, workflows and skills are available, so the `R-DEL.9` fallbacks are a safety net rather than the normal path.

## Gate commands (the "gate" of core I1 and `R-REP.4`)

- Every change to the policy files: `wc -m AGENTS.md docs/policy/reference.md docs/policy/remote-coordination.md`, with the delta recorded in the ticket (core S1 — measured, no cap), plus `git diff --check`.
- Child repositories: their own test/build commands; when a child has no runner, the gate is the smallest smoke check that exercises the change, recorded in the ticket with its observed result.
- Fix bugs with `git diff --check` and a re-read of the scoped diff before any commit.

## Environment facts (dated; re-verify before relying on them)

- 2026-09-15: cheap-tier ranking used for delegation was `glm-5.3-flash > deepseek-v4-flash > qwen-3.8-flash`, GPT cheap tier `gpt-5.6-luna`, flagship `terra`/`sol`, harnesses `pi` (generic, model-agnostic) and `opencode`. `R-DEL.5` states only the invariant (cheapest capable, verify the served spec) and points here; names and prices age fast.
- 2026-09-15: observed from this machine — Google, OpenAI, Anthropic and HuggingFace unreachable; pypi, npm and GitHub degraded. `R-ENV.1.3` states the behavior (assume a restricted network, verify before trusting, use the regional mirror for each ecosystem); re-verify this observation before relying on it.
