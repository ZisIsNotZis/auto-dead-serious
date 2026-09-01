# Auto Dead Serious workspace

This directory aggregates independent child repositories. Work inside a child follows that child's `AGENTS.md`/`CLAUDE.md` first.

## Standard of responsibility

Treat every request as an outcome to finish, not a progress report. Work through the full scope, resolve routine decisions yourself, and hand back the highest-quality final deliverable that the evidence supports; do not stop at a partial result or merely describe a next step. Be 1000% serious about correctness, polish, user experience, and honest verification. If a genuine requirement, authority, environment, or high-impact product decision blocks completion, explain the concrete evidence and ask one focused question; otherwise continue using the available tools and best professional judgment.

Use TDD for behavior changes where practical and perform manual multimodal inspection for UI, visual, 3D, audio, video, screenshots, or other perceptual deliverables whenever applicable. Install or use available tooling such as `uv`, `npm`, `fnm`, `wget`, `curl`, `gh`, browsers, Playwright, and publication CLIs when relevant; missing convenience setup is not a reason to abandon verification. For long or multi-stage work, maintain a compact checklist, continue until every applicable acceptance criterion is met, and report the final state with material evidence and blockers.

## Operating rules

Markdown style: keep each ordinary prose paragraph and each list item as one physical line so wide-screen auto-wrapping can work. Do not manually wrap every paragraph or every file. Preserve structural breaks for headings, code fences, tables, YAML/front matter, and genuinely necessary long or semantically clearer content.

1. Re-scan top-level directories and inspect actual content before acting. Treat folder names as paths only. Derive the product name, package name, publication title, and GitHub slug from project content and metadata; preserve intentional underscores in the slug (a trailing `_private` means a private GitHub repository).
2. Preserve existing history, remotes, branches, licenses, and policy decisions. Add `AGPL-3.0-only` only when no license decision exists.
3. Treat each top-level Git repository as a pinned submodule here. Keep nested repositories independent and preserve their parent submodule relationship.
4. For a child being prepared for GitHub, inspect and update applicable repository files: bilingual `README.md`/`README.zh-CN.md`, `LICENSE`, `AGENTS.md`, `CLAUDE.md`, `.agents/`, and `.claude/`. Follow existing conventions and add only files with a clear purpose.
5. Keep the README current and concise: name, promise, status, logo/badges when useful, tested Quickstart, usage, evidence, limitations, version or changelog, Future vision, and welcoming issue/PR guidance. Investigate the Quickstart in the real project; make small obvious fixes when safe and record unresolved known problems. If documentation is accurate, make no documentation change.
6. Keep documentation docs-first and single-source-of-truth. Put substantial parallel material under `docs/` or `designs/`, maintain a concise index/tree, verify links, and remove superseded copies only after migration. Keep every Markdown file under 200 lines; do not duplicate the README in policy files.
7. Before committing related changes, inspect `.gitignore` and exclude generated files, build output, credentials, and local artifacts. Commit coherent changes with truthful messages. Do not create empty or speculative commits.
8. Publication is approval-gated. Only after explicit approval may `gh` create or update `zisisnotzis/<content-derived-slug>` (public unless `_private`), then push the intended branch and verify the remote, visibility, and result. Leave accurate or unchanged repositories untouched.
9. Papers belong under `papers/` and are prepared only when explicitly required. Bilibili materials belong under `videos/` and are prepared only when explicitly required. Neither is uploaded automatically; never commit upload credentials. When approved, keep paper/video source, metadata, and evidence with the child.
10. Choose execution deliberately: do small, tightly coupled tasks yourself; for complex work, split independent subtasks with explicit dependencies and fan out Luna workers when available. Give each worker a complete scoped prompt, forbid recursive delegation and Codex CLI, parallelize only disjoint work, be patient with running workers, and review all evidence before integration. The main agent remains responsible for the complete final deliverable; delegation never transfers ownership or justifies stopping early.
11. Make routine, low-impact, and common-sense decisions without asking. Ask only when the choice materially changes the product, publication, safety, authority, or requested outcome and cannot be resolved from project content or policy. When requirements are unclear, investigate first and ask a focused question only after the ambiguity is real.

## Verification gate

For every changed child, run the smallest meaningful test, build, or smoke check; inspect visual artifacts for UI/3D work; run `git diff --check`; and review the scoped diff. Record commands, results, and blockers honestly. Do not claim completion from a failed command or stale result. After approved publication, verify the submodule commit, remote URL, branch, visibility, and clean status.
