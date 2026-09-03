# Vibe workspace rules

This directory aggregates independent child repositories. Universal agent policy lives in `AGENTS.md`; this file adds rules that apply only to this aggregation workspace. Precedence here: the child's `docs/` tree > the child's `AGENTS.md`/`CLAUDE.md` (project specifics) > root `AGENTS.md` (universal policy) > agent judgment.

## Layout and discovery

1. Re-scan top-level directories and inspect actual content before acting. Treat folder names as paths only.
2. Treat each top-level Git repository as a pinned submodule. Keep nested repositories independent and preserve the parent submodule relationship.
3. Work inside a child follows that child's `AGENTS.md`/`CLAUDE.md` first; read root `AGENTS.md` for the universal policy every child inherits.

## Repository preparation

1. For a child being prepared for GitHub, inspect and update applicable repository files (README, LICENSE, AGENTS.md, CLAUDE.md, `.agents/`, `.claude/`) following the universal Repository files rules, plus these workspace deltas: the README is bilingual (`README.md` + `README.zh-CN.md`); follow existing conventions and add only files with a clear purpose.
2. Derive the product name, package name, publication title, and GitHub slug from project content and metadata; preserve intentional underscores in the slug (a trailing `_private` means a private GitHub repository).
3. Preserve existing history, remotes, branches, licenses, and policy decisions.

## Publication

1. Publication is approval-gated. Only after explicit approval may `gh` create or update `zisisnotzis/<content-derived-slug>` (public unless `_private`), then push the intended branch and verify the remote, visibility, and result. Leave accurate or unchanged repositories untouched.
2. After approved publication, verify the submodule commit, remote URL, branch, visibility, and clean status.
