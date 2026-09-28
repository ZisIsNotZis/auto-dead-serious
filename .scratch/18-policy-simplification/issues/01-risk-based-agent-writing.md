# 01 — Simplify agent-writing policy

- **Status:** done
- **Blocked by:** none
- **Need-review:** passed (read-only independent review and focused rereview)
- **Need-test-cases:** scenario-based policy checks

## Objective

Delete repetitive or unjustified ceremony from root agent policy and related topic files; make the resulting agent-writing guidance apply to itself and future agent-facing documents. Preserve safety, ownership, validation, continuity, and local child-instruction compatibility.

## Acceptance criteria

- [x] Root and topic files have one clear home for each decision; no extra permission checkpoints for routine work.
- [x] Clarify risk-proportionate alignment, tickets, delegation, validation, and policy editing; distinguish evidence from ritual.
- [x] Agent-facing writing rubric explicitly tests its own files, observable decisions, and deletion/replacement of ineffective rules.
- [x] Resolve policy references relative to the owning `AGENTS.md`, whether project-local or harness-loaded global; do not assume a global file is automatically loaded.
- [x] Current facts and topology in WORKSPACE.md remain accurate; no unrelated state is altered.
- [x] Run declared checks, review scoped diff, obtain independent fresh-context review, and record scenario outcomes and residual limits.

## Baseline

`wc -m AGENTS.md WORKSPACE.md docs/policy/*.md`: 58,206 characters. Root policy files clean before edits; broader repository has unrelated pre-existing changes and untracked content.

## Comments

- 2026-09-28 (main agent, pi) — Claimed user's requested deletion-first rewrite; independent read-only critique launched before modifying policy files. Scope: root policy and topic files, WORKSPACE topology if needed. Do not alter child repositories or unrelated working-tree changes.
- 2026-09-28 (main agent, pi) — User clarified that policy paths belong to the owning `AGENTS.md` directory and questioned the need for extensive policy. Root instructions now state path-base and harness-dependent global loading; deletion-first edits are in progress. Independent diff review launched.

## Scenario probes (checked against current text)

1. Small one-file bug: outcome and regression observable; no roadmap or ticket required, run applicable local checks and report the actual revision.
2. Cross-session change: find recorded work-item path, check Git dirty state and verification revision, resume from a concrete next action; never rely on session memory alone.
3. Two materially different product outcomes: present the difference and recommendation, rather than choose a technical-looking default.
4. Unavailable hardware runner: run feasible static or simulated checks and explicitly state the unexercised behavior; no false green claim.
5. External writer: verify workspace coordination mode and use the remote procedure; local isolated agents do not imply remote mode.
6. Global policy: a companion `policy/foo.md` in a harness-loaded global `AGENTS.md` resolves from that file's directory; a missing companion is skipped and a project ticket remains relative to the target project. Loading is harness-dependent.

## Verification in progress

- Final `wc -m AGENTS.md WORKSPACE.md docs/policy/*.md`: 51,881 versus 58,206 baseline (−6,325); root `AGENTS.md`: 5,855 versus 8,979 (−3,124). Size reduction does not itself prove clarity.
- `git diff --check -- AGENTS.md WORKSPACE.md docs/policy`: passed (no output).
- Topic index check: all nine entries resolve beneath this root `AGENTS.md`; `WORKSPACE.md` exists. A globally relocated file's optional companions are conditional, not asserted present.
- Independent first read-only review identified missing global/project path distinction, handoff discovery, remaining low-value prose, and stale environment facts. Revised those areas. Focused rereview found no safety/evidence blocker; its remote-trigger finding was fixed in `AGENTS.md`, `WORKSPACE.md`, and `remote-coordination.md`, then the affected diff and scenario were self-checked. The reviewer used read-only file inspection, not Git diff; parent performed the scoped diff review and checks.
- Final `git diff --check -- AGENTS.md WORKSPACE.md docs/policy`: passed with no output. Parent reread the scoped diff. All nine topic index targets exist; rule-definition check found no duplicate identifiers and each topic has one applicability header set.
- No `.scratch/active-work.md` was created: this item completed in the current session, so there is no active cross-session item to index. For a future interrupted task, the new policy requires that entry before handoff.
- Residual limitation: this is a policy-text and scenario review, not an empirical study of future agents; optional topic files still contain generic guidance that can be pruned separately without claiming this pass removed all low-value text.


