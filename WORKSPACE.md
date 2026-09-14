# Vibe workspace knowledge

Project-specific knowledge for the Auto Dead Serious workspace — the recommended companion to the project-agnostic `AGENTS.md`, which holds universal policy only.

## Layout

1. This directory aggregates independent child repositories as pinned submodules: keep each child independent and preserve the parent submodule relationship.
2. Work inside a child follows that child's `AGENTS.md`/`CLAUDE.md` first; root `AGENTS.md` supplies the universal policy every child inherits.
3. When preparing a child for GitHub, a trailing `_private` in the content-derived slug marks a private repository.
4. The policy is split: root `AGENTS.md` is the always-on core (invariants, coordination scope, triggers, maintenance); `docs/policy/reference.md` holds the detail, cited as `R-*` sections. Project knowledge stays here, never in `AGENTS.md` (`R-DOC.11`).

## Declarations

- **Coordination mode: local** (core M1). One machine, one checkout, subagents only. No locks, heartbeats, mailbox polling, ordinal races or formal trackers; `R-REM` is not read. Switch to `remote` (M2) only if another writer pushes to the same branch or the user asks.
- **Harness: pi** — generic and model-agnostic; subagents, workflows and skills are available, so the `R-DEL.9` fallbacks are a safety net rather than the normal path.

## Environment facts (dated; re-verify before relying on them)

- 2026-09-15: cheap-tier ranking used for delegation was `glm-5.3-flash > deepseek-v4-flash > qwen-3.8-flash`, GPT cheap tier `gpt-5.6-luna`, flagship `terra`/`sol`, harnesses `pi` (generic, model-agnostic) and `opencode`. `R-DEL.5`/`R-DEL.6` state only the invariants (cheapest capable, verify the served spec); the names belong here and age fast — re-verify before relying on them.
- 2026-09-15: network restrictions assumed: Google, OpenAI, Anthropic and HuggingFace unreachable; pypi, npm and GitHub degraded. Mirrors and workarounds in `R-ENV.1.3`.
