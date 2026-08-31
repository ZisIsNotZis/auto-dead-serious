# Auto Dead Serious workspace

This directory is the **Auto Dead Serious** aggregator. It contains independent
child repositories; work in a child follows that child's `AGENTS.md`/`CLAUDE.md`
first.

## Required workflow

1. Re-scan top-level directories and actual content before changing anything.
2. Resolve product name, GitHub slug, package name, and publication titles from
   content; a folder name is only a local path.
3. Preserve history, remotes, licenses, branches, and decisions. Add
   `AGPL-3.0-only` only where no license decision exists.
4. Every top-level Git repository is a pinned submodule here. Nested Git repos
   remain independent inside their owning child and remain submodules there.
5. Use `gh` to create missing `zisisnotzis/<slug>` repositories: public unless
   the folder ends in `_private`, then private. Push meaningful changes; leave
   unchanged repositories untouched.
6. Keep one source of truth. Put parallel documents in `docs/`/`designs/` with
   an index; after verified migration remove the old source. Markdown stays
   under **200 lines**.

## Child baseline

Each useful public child should have a truthful bilingual README with name,
promise, status, logo, badges, Quickstart, usage, evidence, limitations,
version/changelog, Future vision, and issue/PR guidance. It should prepare a
reviewed screenshot, screen recording, and manual Bilibili introduction package
under `docs/` and `media/`. Innovative public projects additionally prepare an
approval-gated arXiv package under `paper/` with source, bibliography, figures,
PDF, claim/evidence map, baselines, reproducibility, limitations, and rights
checks. Do not upload videos or papers automatically.

Runnable apps/games need tested versioned GitHub Release artifacts; libraries
need registry metadata and an install/import smoke test before publishing.
Agents may triage, investigate, test, document, and implement accepted issues;
maintainers review and merge.

## Verification gate

Run the smallest meaningful test/build/smoke check for every changed child,
inspect visual artifacts when relevant, run `git diff --check`, review the
scoped diff, then verify submodule commit, remote URL, branch, visibility, and
clean status. Record blockers honestly; a failed command is not completion.
