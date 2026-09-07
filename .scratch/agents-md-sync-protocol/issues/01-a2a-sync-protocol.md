# 01 — A2A sync protocol in AGENTS.md

- **Status:** claimed
- **Blocked by:** none
- **Assignee/lock:** VPO (main session)

## Issue

The current Stage 0.2 "A2A via ticket Comments, else a message board" is a general-purpose
mechanism without a concrete use case — the exact anti-pattern the policy's own Design 3/6
ban. Replace it with a concrete git-based sync protocol covering (PO brainstorm, this round):
eager optimistic-lock sync at ticket creation/claim/status/comment/complete; polling that
never interrupts or touches the checkout; blocker handling; any-real-problem ticketing;
collision-by-design naming; no auto-takeover (PO-mediated only).

## Acceptance criteria

- [ ] Stage 0.2 rewritten: tickets are the only A2A channel; any real problem is ticket-worthy; solver greps tickets blocked on what it just solved; no message board.
- [ ] New Tickets & git rule (Sync): eager write protocol (fetch → read mail → edit → commit → plain push; no --force/auto-rebase; non-FF rejection = race detector), fetch-based reads (no branch switch), timer poll spec, collision-by-design slug rule.
- [ ] Locks: 24h auto-takeover replaced by PO-mediated takeover (explicit instruction only).
- [ ] AGENTS.md stays under 200 lines; `git diff --check` clean.

## Knowhow learned

- `git fetch` never touches the working tree — reads of shared state need no checkout
  (`git show origin/main:<path>`); only writes need the detached main worktree. This is what
  makes an interrupt-free timer poll possible on any branch.

## Comments

- 2026-09-04 (VPO, pi coding agent, volc2/glm-5.3-flash) — Ticket created and claimed from PO's sync-protocol brainstorm + 3 answered decision points (event+timer polling, PO-mediated recovery, inline in AGENTS.md). zh translation deliberately deferred until EN review.
