# 01 — Standing docs review axes (4)

- **Status:** done
- **Blocked by:** none
- **Assignee/lock:** VPO (main session)

## Issue

PO direction: encode the standing review methodology for AGENTS.md/docs changes as four
axes — (1) correctness: SSOT, self/cross consistency especially of abstract philosophy,
conflicts; (2) specific & actionable; (3) redundancy; (4) completeness (proposed by VPO,
accepted: dead-end states, coverage gaps — the inverse of correctness). Spawn 1–3(4)
fresh-context reviewers, usually 1 covering all axes, per-axis only when findings are
plentiful. Then run one check round on the current file.

## Acceptance criteria

- [x] Documentation 4.2 encodes the four axes + spawn policy + verify-before-accept.
- [x] One fresh-context reviewer run completed; findings triaged; real ones fixed.
- [x] AGENTS.md ≤ 200 lines, `git diff --check` clean.

## Comments

- 2026-09-04 (VPO, pi coding agent, volc2/glm-5.3-flash) — Doc 4.2 committed (144 lines).
- 2026-09-04 (VPO, pi coding agent, volc2/glm-5.3-flash) — Reviewer returned BLOCK: 1 P1 + 15 P2; all 16 verified against text and accepted; fixed in one 15-block batch (tool-autonomy/dependency-approval scoping; micro-fix exceptions; 6.1 merge step; 9.1 recording carve-out; ladder-vs-Routing boundary; fork=true defined; id anti-example; clarity fallback; dedupe of rejection rule + 1.3 restatement; unified skill bar; Routing home for scripts/ + kind boundaries; Stage 0.2 channel scoping; dropped dangling ≈10× figure). Verified: 144 lines, git diff --check clean.
