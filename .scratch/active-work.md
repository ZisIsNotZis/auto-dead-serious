# Active work — 子仓库收口 (2026-09-29)

Owner decisions: close out all child repos except fat_kakeya_needle, agentworld,
learn_draw, flashdb, autofe, helpagent, backseat, sys_gal. ra2 = indefinite pause;
sys_gal_rt = paused (story only). resume_img_gen/resume_improve_loop = owner
maintains. Shared convention: `.scratch/closure-brief.md`.

## Done (committed in the child repo)

Closed milestone: agentic-animation (engine usable; rest = backlog), aps,
auto_maintain_bench (→ Help Agent successor), danmaku (AI roaster removed; pure
Qt engine), drive, expyssion, hfget, hyperframaker, ideas, litellmgen,
mux, npchallenge, pelican_bike, pushbus, raid_calc, timecolumn, tokenqr (POC),
vibeos, horse_video, huaqiang_video, mycar, colleague_private, tutor_private,
resume_private.
Paused: huaqiang_game (indefinite), ra2 (indefinite), sys_gal_rt.
Parent: resume_* registered as submodules; dead .gitmodules entries removed;
vendor submodule deletions and expyssion/uv.lock restored.

## Pending (owner-gated)

- [ ] Push the ~28 child closure commits to their remotes (publication).
- [ ] Catch up the parent submodule pointers (34 repos currently show ` M`).
