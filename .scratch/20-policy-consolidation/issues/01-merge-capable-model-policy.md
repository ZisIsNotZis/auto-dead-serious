# 01 — Consolidate capable-model policy

- **Status:** done
- **Need-review:** scoped self-review completed; independent model review not run under user's time/budget constraint
- **Blocked by:** none

## Objective

Merge the nine conditional policy files into a smaller navigable set for capable coding models without assuming unverified behavior of named model versions. Retain only non-obvious workspace-specific decisions and hard safety/continuity boundaries; preserve relative-path semantics and no-real-project-test constraint.

## Baseline

`wc -m AGENTS.md WORKSPACE.md docs/policy/*.md`: 29,047 characters, nine topics. Existing policy changes are uncommitted; preserve them and unrelated repository state.

## Responsibility map

- `collaboration.md` + `design.md` → `decisions.md` (intent, questions, design choice).
- `work-management.md` + `delegation.md` + `build-and-validation.md` → `execution.md` (handoff, review, delegation, checks).
- `documentation.md` + `policy-maintenance.md` → `writing.md` (product truth, agent writing, proportional maintenance).
- `environment-and-repository.md` → `environment.md` (tools, privilege, artifacts, repository safeguards).
- `remote-coordination.md` remains a separate rare conditional topic.
- `AGENTS.md` remains the core and topic index; `WORKSPACE.md` only carries workspace facts and local gate references.

## Acceptance

- [x] New index and workspace references resolve; old live topic files removed after responsibility mapping.
- [x] Safety, user-decision, evidence, cross-session, first-discovered external-writer, and path-base cases remain decidable from core plus relevant topic.
- [x] Run structural/link audits and `git diff --check`; scoped self-review. No expensive real-project or multi-model testing.

## Evidence and disposition

- Final `wc -m AGENTS.md WORKSPACE.md docs/policy/*.md`: 18,987 characters across five topics, versus 29,047 across nine topics (−10,060). The uncommitted combined change versus the original 58,206-character baseline is −39,219; this measures size, not model behavior.
- Python link audit: all five root topic entries match the five existing files and every explicit `docs/policy/*.md` reference in active root/workspace/topic text resolves. Responsibility-keyword smoke checks pass.
- `git diff --check -- AGENTS.md WORKSPACE.md docs/policy`: passed without output. Child instruction file search found no active links to retired topic paths. Reviewed current new topic files and root/workspace references; old topic meanings mapped above.
- Scenario self-review: a simple fix needs no ticket or roadmap; material product ambiguity goes to the user; resumed work finds a current item and checks revision-bound evidence; global companion paths remain owning-AGENTS-relative; an external writer triggers collision safeguards before shared writes; absent tests are reported, not fabricated.
- Independent model review and real-project behavior tests were not run because the user explicitly prioritized time and budget. This is a structural/textual optimization for capable models, not a measured improvement for any named model.
- No commit. Other pre-existing repository modifications remain untouched. Historical ticket links to retired paths remain archival and are not live entry points.

