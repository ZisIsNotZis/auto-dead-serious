# Vibe workspace knowledge

Project-specific facts for the Auto Dead Serious workspace. Portable authorization and routing live in `AGENTS.md`; scoped policy lives under `docs/policy/`.

## Layout

1. This directory aggregates independent child repositories as pinned submodules; preserve each child and the parent submodule relationship.
2. Work inside a child follows the root-to-leaf instruction chain defined in root `AGENTS.md`; local `AGENTS.md` and platform-equivalent `CLAUDE.md` specialize the child without weakening the root safety or evidence floor.
3. When preparing a child for GitHub, a trailing `_private` in its content-derived slug marks a private repository.
4. Policy topology:
   - `AGENTS.md`: always-on authorization, safeguards, user-intervention gates, delegation ownership, reporting, and router.
   - `docs/policy/collaboration.md`: `R-INT.1`–`R-INT.8` and `R-INT.11`–`R-INT.13`.
   - `docs/policy/documentation.md`: `R-DOC`.
   - `docs/policy/work-management.md`: `R-TKT` and work/session continuity parts of `R-SES`.
   - `docs/policy/delegation.md`: `R-DEL` and parent-context compaction.
   - `docs/policy/environment-and-repository.md`: `R-ENV` and repository-maintenance parts of `R-REP`.
   - `docs/policy/design.md`: `R-DSN` and `R-INT.9`–`R-INT.10`.
   - `docs/policy/build-and-validation.md`: `R-BLD` and `R-REP.4`.
   - `docs/policy/remote-coordination.md`: remote-only `R-REM`.
   - `docs/policy/policy-maintenance.md`: `S1-S5`.

## Declarations

- **Coordination mode: local.** External writers are not known to share this branch or repository. Isolated local subagents do not change this mode. A configured git remote alone does not change it. Record `remote` here only when the user requests remote coordination or an external writer is known to share state.
- **Harness: pi.** Subagents, workflows, and skills are available. Model and tool availability must still be verified when material.

## Gate commands

- Policy changes: `find docs/policy -maxdepth 1 -type f -name '*.md' -print | sort`; `wc -m AGENTS.md WORKSPACE.md docs/policy/*.md`; routing/header and `R-*` citation audits with `rg`; `git diff --check`; full scoped diff reread; fresh-context policy review recorded in the policy ticket.
- Child repositories: use their declared test and build commands. If a child has no runner, use the smallest smoke check that exercises the change and record its observed result.
- Bug fixes: use the changed module's declared gates, `git diff --check`, and a scoped diff reread before completion.

## Environment facts (dated; re-verify before relying on them)

- 2026-09-15: delegation cost observations were `glm-5.3-flash > deepseek-v4-flash > qwen-3.8-flash`, GPT cheap tier `gpt-5.6-luna`, and flagship `terra`/`sol`; observed harnesses were `pi` and `opencode`. Names, pricing, served capability, and availability age quickly.
- 2026-09-15: from this machine, Google, OpenAI, Anthropic, and HuggingFace were unreachable; PyPI, npm, and GitHub were degraded. Re-test the endpoint needed by current work before selecting a mirror or fallback.
