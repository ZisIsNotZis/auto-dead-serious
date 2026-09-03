# Vibe workspace rules

This directory aggregates independent child repositories. Universal agent policy lives in `AGENTS.md`; this file adds rules that apply only to this aggregation workspace. Precedence here: the child's `docs/` tree > the child's `AGENTS.md`/`CLAUDE.md` (project specifics) > root `AGENTS.md` (universal policy) > agent judgment.

## Layout and discovery

1. Re-scan top-level directories and inspect actual content before acting. Treat folder names as paths only. Derive the product name, package name, publication title, and GitHub slug from project content and metadata; preserve intentional underscores in the slug (a trailing `_private` means a private GitHub repository).
2. Treat each top-level Git repository as a pinned submodule. Keep nested repositories independent and preserve the parent submodule relationship.
3. Work inside a child follows that child's `AGENTS.md`/`CLAUDE.md` first; read root `AGENTS.md` for the universal collaboration and engineering policy that every child inherits.

## Repository preparation

1. For a child being prepared for GitHub, inspect and update applicable repository files: bilingual `README.md`/`README.zh-CN.md`, `LICENSE`, `AGENTS.md`, `CLAUDE.md`, `.agents/`, and `.claude/`. Follow existing conventions and add only files with a clear purpose. These are repository metadata the agent maintains; they are not the read-only `docs/` tree.
2. Keep the README current and concise: name, promise, status, logo/badges when useful, tested Quickstart, usage, evidence, limitations, version or changelog, Future vision, and welcoming issue/PR guidance. Investigate the Quickstart in the real project; make small obvious fixes when safe and record unresolved known problems. If documentation is accurate, make no documentation change.
3. Preserve existing license decisions; add `AGPL-3.0-only` only when no license decision exists.
4. Before committing related changes, inspect `.gitignore` and exclude generated files, build output, credentials, and local artifacts. Commit coherent changes with truthful messages. Do not create empty or speculative commits.

## Publication

1. Publication is approval-gated. Only after explicit approval may `gh` create or update `zisisnotzis/<content-derived-slug>` (public unless `_private`), then push the intended branch and verify the remote, visibility, and result. Leave accurate or unchanged repositories untouched.
2. After approved publication, verify the submodule commit, remote URL, branch, visibility, and clean status.

## Media

1. Papers belong under `papers/` and are prepared only when explicitly required. Bilibili materials belong under `videos/` and are prepared only when explicitly required. Neither is uploaded automatically; never commit upload credentials. When approved, keep paper/video source, metadata, and evidence with the child.
