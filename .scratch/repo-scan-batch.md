# Repository scan batch

Scope: all top-level project directories except `sys_gal` and `silly_2d_animate`.

## Shared acceptance criteria

- Re-scan current content and meaningful uncommitted updates.
- Read and follow existing `AGENTS.md`/`CLAUDE.md`, licenses, and project policies.
- Determine preferred product/repository names from content; preserve local folder names.
- Initialize Git when absent; preserve existing remotes/history; add nested Git repositories as submodules when needed.
- Apply the root README rules: concise bilingual README where appropriate, tested Quickstart, Future vision, versioning, contribution/agent guidance, and Markdown under 200 lines.
- Use AGPL-3.0-only only when no license decision exists.
- Correct `.gitignore`, preserve important user work, and avoid secrets/caches/build output.
- For useful/innovative projects, prepare only manual instructions for Bilibili/arXiv creation or publication; do not create or publish videos/papers automatically.
- Run proportionate checks and report paths, actions, blockers, and remaining work.

## Batches

- [ ] Batch A: `aps`, `auto_maintain_bench`, `colleague_private`
- [ ] Batch B: `drive`, `horse_video`, `huaqiang_game`
- [ ] Batch C: `huaqiang_video`, `hyperframaker`, `ideas`
- [ ] Batch D: `lm_gh_test`, `lm_paper_test`, `mux`, `npchallenge`
- [ ] Batch E: `ra2`, `timecolumn`, `tutor_private`, `vibeos`

Excluded by request: `sys_gal`, `silly_2d_animate`.
