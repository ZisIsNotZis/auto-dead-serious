# Ticket 0001 — Systematize AGENTS.md as universal multi-user agent policy

- **Status:** doing
- **Owner:** agent (pi, main session); requester: PM zisisnotzis
- **Need review:** yes · **Need test cases:** no (policy file; gates = line limits, git diff --check, consistency audit)

## Issue

The original AGENTS.md was a 29-line workspace file. The PM supplied a large fragmented draft of documentation/design/engineering philosophy to be formalized into a copy-pasteable, project-agnostic, multi-user agent policy with ticket-based change tracking.

## Acceptance criteria

- AGENTS.md is project-agnostic (no vibe-specific content; those moved to README).
- Every PM point from all rounds is present, S.M.A.R.T.-phrased, conflict-free, ≤200 lines, one physical line per paragraph.
- Multi-user support: git-config identity detection, docs/people.md profiles.
- All changes ticket-tracked under docs/tickets/ with issue/AC/status/owner/updates.
- CLAUDE.md symlink → AGENTS.md per standard scaffold.

## Updates

- 2025-09-03: Restructured through iterative rounds (commits 302e069 → 49f9886): collaboration contract, docs policy (SSOT/S.M.A.R.T./200-line), design process, 8 engineering principles, quality priorities, repository files (commit bar, checkpoint rule), work management (bootstrap/memory, focus, tool autonomy, 5S/6S cleanup), delegation + subagent model policy, verification gate with hooks and subjective-artifact review.
- 2025-09-03: Deleted WORKSPACE.md; vibe-specific rules moved to README.md/README.zh-CN.md ("Workspace rules for agents" section).
- 2025-09-03 (this round): Migrated single-user → multi-user (git identity, people doc); replaced todo tiers with mandatory file tickets (docs/tickets/, harness tool demoted to mirror); removed anti-Matt-Pocock clause (scaffolding set up automatically instead); added asking-protocol interest-bar model (≤5 recommended / 10 cap, never offload); added repo scaffold convention (vendor/, .agents/skills/, .claude symlink, .scratch/); added information-gathering ladder, skill minimalism, China mirror preference, sudo avoidance, subjective-artifact open review; docs/ write regimes carved into three (design truth = permission, PM info = mandatory, tickets = working state).

## Knowhow

- Conflict resolutions applied: ask-for-information vs never-offload-work; ticket folder exempt from docs write permission; mid-session user alternation retracted in favor of per-session identity.
- Open question flagged: README still positions Bilibili/paper materials that were removed as policy.

## Acceptance check

- [ ] PM review of conflict resolutions and open questions
