# Closure-doc brief (shared spec)

Goal: every listed child repo must clearly claim a proper end ("收口").
This is a documentation-only change. Do NOT change code, tests, or behavior.

## What to do in each repo

1. `README.md`: add ONE blockquote immediately after the top title (and after
   any existing language-switch line), unless an equivalent closed-status line
   already exists. Exact shape:

   ```
   > **Status: closed (milestone, 2026-09-29).** <one factual sentence>. No
   > further development is planned unless the project's inputs or goals change.
   ```

   For paused repos use `**Status: paused (indefinite, 2026-09-29).**`.
   If there is a known successor, append: `Future work may continue in
   [Help Agent](../helpagent/), which may supersede this project.`

2. `docs/project-status.md`: if it exists, add/update a `## Status` section with
   the same closure claim and a short `## Deferred` list of work intentionally
   left undone (from existing docs only). If it does not exist, create it using
   the repo's README/CHANGELOG for Classification, Evidence, and Boundaries.

3. Do not invent benchmarks, dates, or claims. Keep it concise and factual.

4. Commit inside the child repo only, message:
   `Close out: record closed-milestone status`
   Do NOT push. Do NOT touch the parent repo or any other repo.

## Per-repo status sentences

- aps: "The experimental planning workbench reached its goal: a runnable,
  inspectable prototype with a unified model, multiple solvers, nine scenarios,
  and a browser UI."
- auto_maintain_bench: "The deterministic tiny-LM host-maintenance benchmark
  reached a usable milestone (184 scenarios, observable scoring)." + successor
  sentence pointing at Help Agent, which "may supersede this benchmark".
- drive: "The offline Suzhou driving simulator reached its documented 0.1.0
  milestone on the roadmap-v2 record."
- expyssion: "The expyssion language reached a milestone: a frozen LANGUAGE.md
  v1 spec plus a working Python-hosted v1 implementation."
- hfget: "The Hugging Face GGUF download helper is a complete small personal
  utility."  (closed, not paused)
- huaqiang_game: "The Huaqiang social-stealth prototype was an exploratory test;
  it is paused indefinitely and is not under active development."
- hyperframaker: "The local-first node-based artifact orchestration app reached
  its experimental milestone."
- tokenqr: "The TokenQR token-authorization protocol POC is complete; remaining
  roadmap items are optional future extensions."
- vibeos: "The browser-hosted generative OS runtime reached its experimental
  milestone."
- ideas: "The speculative-idea notebook is a complete archive of its notes."
- npchallenge: "The NumPy attention/convolution teaching implementations are
  complete."
- mux: "The small tmux media mux/split helpers are complete."
- timecolumn: "The Timetable time-series prototype reached its documented
  milestone."
- raid_calc: "The hierarchical storage reliability calculator reached its
  documented v1 milestone."
- mycar: "The variable-cabin crossover design workspace and its parametric
  blueprint tool reached the v13 milestone."
- colleague_private: "The private AI-colleague skill collection is complete."
- tutor_private: "The private tutorial production workspace snapshot is
  complete."
- horse_video: "The code-authored horse-running animation is a finished art
  experiment with a checked-in render."
- huaqiang_video: "The Huaqiang melon short is a finished creative prototype
  with a checked-in render."
- pelican_bike: "The single-page Pelican bike demo is complete."

## Repos NOT in scope

resume_img_gen, resume_improve_loop, resume_private (owner maintains these),
danmaku, litellmgen (already done).
