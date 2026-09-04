# Ticket 0001 — Systematize AGENTS.md as universal multi-user agent policy

- **Status:** doing
- **Owner:** agent (pi, main session); requester: PO zisisnotzis
- **Need review:** yes · **Need test cases:** no (policy file; gates = line limits, git diff --check, consistency audit)

## Issue

The original AGENTS.md was a 29-line workspace file. The PO supplied a large fragmented draft of documentation/design/engineering philosophy to be formalized into a copy-pasteable, project-agnostic, multi-user agent policy with ticket-based change tracking.

## Acceptance criteria

- AGENTS.md is project-agnostic (no vibe-specific content; those moved to README).
- Every PO point from all rounds is present, S.M.A.R.T.-phrased, conflict-free, ≤200 lines, one physical line per paragraph.
- Multi-user support: git-config identity detection, docs/people.md profiles.
- All changes ticket-tracked under docs/tickets/ with issue/AC/status/owner/updates.
- CLAUDE.md symlink → AGENTS.md per standard scaffold.

## Comments (change log)

- 2026-09-03 — VPO via pi coding agent, main session — restructured AGENTS.md across rounds (commits 302e069 → 49f9886): collaboration contract, docs policy (SSOT/S.M.A.R.T./200-line), design process, 8 engineering principles, quality priorities, repository files (commit bar, checkpoint rule), work management (bootstrap/memory, focus, tool autonomy, 5S/6S cleanup), delegation + subagent model policy, verification gate with hooks and subjective-artifact review. Deleted WORKSPACE.md; vibe-specific rules moved to README.md/README.zh-CN.md.
- 2026-09-03 — VPO via pi coding agent, main session — migrated single-user → multi-user (git identity, people doc); replaced todo tiers with mandatory file tickets (harness tool demoted to mirror); removed anti-Matt-Pocock clause; added asking-protocol interest-bar model; repo scaffold convention; information-gathering ladder; skill minimalism; China mirror preference; sudo avoidance; subjective-artifact open review; docs/ write regimes carved into three (design truth = permission, PO info = mandatory, tickets = working state).
- 2026-09-04 01:50 UTC — requester zisisnotzis (PO) via pi coding agent, main session, model volc2/glm-5.3-flash — renamed PM→PO everywhere (PO carries no commercial connotation; VPO = technical vice product owner); added ticket locking protocol (pull→set→push-to-confirm, exclusive lock, `Dear <owner>:` messages, "let's call it a day" wrap-up); adopted append-only `## Comments` change-log format (who, harness, model, when, what); added Matt Pocock compatibility clause (his tracker shape, kept under committed docs/tickets/); China-default + IP-verification mirror rule; intro efficiency-over-workflow clause.
- 2026-09-04 01:55 UTC — VPO via pi coding agent, main session, model volc2/glm-5.3-flash — lock auto-release on natural completion ("call it a day" demoted to interrupt path); ownership redefined as lock-not-identity (any free agent claims a released ticket); formalized branching: per-ticket branches, unfinished code never on main, merge only after review gate; review-and-merge gate via need-review property (independent fresh-context reviewers, fork=false); subjective-artifact rule: reviewer compares rendered targets directly, worker never mediates; self-applied: this round committed on branch ticket-0001-agents-md-systematization instead of main.

## Knowhow

- Conflict resolutions applied: ask-for-information vs never-offload-work; ticket folder exempt from docs write permission; mid-session user alternation retracted in favor of per-session identity.
- Open question flagged: README still positions Bilibili/paper materials that were removed as policy.

## Acceptance check

- [ ] PO review of conflict resolutions and open questions
