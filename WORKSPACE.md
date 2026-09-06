# Vibe workspace knowledge

Project-specific knowledge for the Auto Dead Serious workspace — the recommended companion to the project-agnostic `AGENTS.md`, which holds universal policy only.

1. This directory aggregates independent child repositories as pinned submodules: keep each child independent and preserve the parent submodule relationship.
2. Work inside a child follows that child's `AGENTS.md`/`CLAUDE.md` first; root `AGENTS.md` supplies the universal policy every child inherits.
3. When preparing a child for GitHub, a trailing `_private` in the content-derived slug marks a private repository.
