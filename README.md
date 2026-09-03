# Auto Dead Serious 🧱

English | [简体中文](README.zh-CN.md)

> A serious, inspectable home for weird software ideas: independent projects,
> pinned together without flattening their histories.

[![Repositories](https://img.shields.io/badge/repositories-growing-6f42c1)](https://github.com/zisisnotzis/auto-dead-serious)
[![License](https://img.shields.io/badge/license-AGPL--3.0--only-blue)](LICENSE)
[![Policy](https://img.shields.io/badge/docs-AGENTS.md-0f766e)](AGENTS.md)

## What this is

Auto Dead Serious turns a growing folder of experiments into a navigable
portfolio. Each child remains a real repository with its own history, tests,
license, release path, and future vision; this repository pins the exact
versions that form the current collection.

**The advantage:** one place to discover the work, **zero history flattening**,
and an explicit quality bar for documentation, evidence, releases, media, and
research.

## Explore

The submodule list and each child README are canonical. Representative projects:

- [APS](aps/) — advanced planning and scheduling.
- [Auto Maintain Bench](auto_maintain_bench/) — tiny-LM maintenance benchmark.
- [Suzhou Drive](drive/) — OSM-backed browser driving simulator.
- [Hypermaker](hyperframaker/) — local-first artifact orchestration app.
- [Iron Meridian](ra2/) — data-driven browser RTS prototype.
- [VibeOS](vibeos/) — generative local operating-system runtime.

## Quickstart

```sh
git clone --recurse-submodules https://github.com/zisisnotzis/auto-dead-serious.git
cd auto-dead-serious
git submodule status
```

Run a project from its own README. Toolchains are intentionally not unified:
each child owns its prerequisites and test command.

## What “serious” means

- **Reproducible:** version, changelog, commands, and dated evidence.
- **Readable:** bilingual product README, compact docs, honest status.
- **Visible:** useful public projects prepare screenshots, recordings, and a
  manual Bilibili package; innovative projects prepare formal paper materials.
- **Maintainable:** issues and PRs are welcome; agents can help, while humans
  retain review and merge authority.

## Scope and non-goals

This is an index and release boundary, not a monorepo, shared build system, or
promise that every experiment is production-ready. Generated dependencies,
credentials, private material, and unreviewed media do not belong here.

## Workspace rules for agents

This directory aggregates child repositories as pinned submodules: keep each child independent, preserve the parent submodule relationship, and treat folder names as paths only. Work inside a child follows that child's `AGENTS.md`/`CLAUDE.md` first; root [AGENTS.md](AGENTS.md) supplies the universal policy every child inherits. When preparing a child for GitHub, a trailing `_private` in the content-derived slug marks a private repository.

## Future vision 🛰️

The collection should become a coherent catalogue of working ideas: every
useful project can be tried in minutes, every innovation has measurable
evidence, and every mature app has a release users can install. New projects
join by following [AGENTS.md](AGENTS.md); the roadmap is driven by the next
meaningful project rather than a fixed inventory.

## Contributing

Open an issue or PR against the relevant child repository, or against this
index for membership and policy. Include the affected path, evidence, and
verification command. Agents may assist with triage, research, tests, docs, and
implementation; maintainers review and merge.

## License

This aggregator's policy and original materials are AGPL-3.0-only. Child
repositories retain their own licenses; inspect each child before reuse.
