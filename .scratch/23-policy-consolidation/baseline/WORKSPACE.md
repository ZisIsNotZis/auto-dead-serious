# Vibe workspace knowledge

Project-specific facts for the Auto Dead Serious workspace. Portable authorization and routing live in `AGENTS.md`; scoped policy lives under `docs/policy/`.

## Layout

1. This directory aggregates independent child repositories as pinned submodules; preserve each child and the parent submodule relationship.
2. Work inside a child follows the root-to-leaf instruction chain defined in root `AGENTS.md`; local `AGENTS.md` and platform-equivalent `CLAUDE.md` specialize the child without weakening the root safety or evidence floor.
3. When preparing a child for GitHub, a trailing `_private` in its content-derived slug marks a private repository.

## Declarations

- **Coordination mode: local.** External writers are not known to share this branch or repository. Isolated local subagents and a configured git remote do not change this mode. If an external writer becomes known or the user requests remote coordination, stop competing writes and apply `docs/policy/remote-coordination.md` safeguards immediately; record `remote` here after shared ownership is established.
- **Harness: pi.** Subagents, workflows, and skills are available. Model and tool availability must still be verified when material.

## Gate commands

- Policy changes: use proportionate checks in `docs/policy/writing.md`; review changed references and the scoped diff. For authority or routing changes, compare `wc -m AGENTS.md WORKSPACE.md docs/policy/*.md` and record review evidence or its limitation.
- Child repositories: use their declared test and build commands. If a child has no runner, use the smallest smoke check that exercises the change and record its observed result.
- Bug fixes: follow the changed module's gates and risk-based validation in `docs/policy/execution.md`.

## Environment checks

Verify current model capability, price, and any required network endpoint at the point of use; past observations are not a substitute for a current check.
