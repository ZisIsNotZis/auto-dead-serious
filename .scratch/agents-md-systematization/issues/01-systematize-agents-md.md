# Ticket 01 — Systematize AGENTS.md as universal multi-user agent policy

- **Status:** doing
- **Owner:** agent (pi, main session); requester: PO zisisnotzis
- **Need review:** yes · **Need test cases:** no (policy file; gates = line limits, git diff --check, consistency audit)

## Issue

The original AGENTS.md was a 29-line workspace file. The PO supplied a large fragmented draft of documentation/design/engineering philosophy to be formalized into a copy-pasteable, project-agnostic, multi-user agent policy with ticket-based change tracking.

## Acceptance criteria

- AGENTS.md is project-agnostic (no vibe-specific content; those moved to README).
- Every PO point from all rounds is present, S.M.A.R.T.-phrased, conflict-free, ≤200 lines, one physical line per paragraph.
- Multi-user support: git-config identity detection, docs/people.md profiles.
- All changes ticket-tracked in the Matt Pocock local-tracker layout (`.scratch/<feature-slug>/issues/`), committed, bi-directionally compatible with his skills.
- CLAUDE.md symlink → AGENTS.md per standard scaffold.

## Branch & commits

- Branch: `ticket-0001-agents-md-systematization` — merged into main as `3351bdd`, branch deleted.
- Implementation commits: f22b17d, cc2ea9c, c6896e5, 3a638ce, 709694a, 73826d6, 06f81a4, merge 3351bdd; this ticket's latest update commit is excluded per the self-reference rule.

## Comments (change log)

- 2026-09-03 — VPO via pi coding agent, main session — restructured AGENTS.md across rounds (commits 302e069 → 49f9886): collaboration contract, docs policy (SSOT/S.M.A.R.T./200-line), design process, 8 engineering principles, quality priorities, repository files (commit bar, checkpoint rule), work management (bootstrap/memory, focus, tool autonomy, 5S/6S cleanup), delegation + subagent model policy, verification gate with hooks and subjective-artifact review. Deleted WORKSPACE.md; vibe-specific rules moved to README.md/README.zh-CN.md.
- 2026-09-03 — VPO via pi coding agent, main session — migrated single-user → multi-user (git identity, people doc); replaced todo tiers with mandatory file tickets (harness tool demoted to mirror); removed anti-Matt-Pocock clause; added asking-protocol interest-bar model; repo scaffold convention; information-gathering ladder; skill minimalism; China mirror preference; sudo avoidance; subjective-artifact open review; docs/ write regimes carved into three (design truth = permission, PO info = mandatory, tickets = working state).
- 2026-09-04 01:50 UTC — requester zisisnotzis (PO) via pi coding agent, main session, model volc2/glm-5.3-flash — renamed PM→PO everywhere (PO carries no commercial connotation; VPO = technical vice product owner); added ticket locking protocol (pull→set→push-to-confirm, exclusive lock, `Dear <owner>:` messages, "let's call it a day" wrap-up); adopted append-only `## Comments` change-log format (who, harness, model, when, what); added Matt Pocock compatibility clause (his tracker shape, kept under committed docs/tickets/); China-default + IP-verification mirror rule; intro efficiency-over-workflow clause.
- 2026-09-04 01:55 UTC — VPO via pi coding agent, main session, model volc2/glm-5.3-flash — lock auto-release on natural completion ("call it a day" demoted to interrupt path); ownership redefined as lock-not-identity (any free agent claims a released ticket); formalized branching: per-ticket branches, unfinished code never on main, merge only after review gate; review-and-merge gate via need-review property (independent fresh-context reviewers, fork=false); subjective-artifact rule: reviewer compares rendered targets directly, worker never mediates; self-applied: this round committed on branch ticket-0001-agents-md-systematization instead of main.
- 2026-09-04 02:05 UTC — VPO via pi coding agent, main session, model volc2/glm-5.3-flash — adopted MP tracker layout verbatim: ticket migrated to `.scratch/agents-md-systematization/issues/01-systematize-agents-md.md`, `.scratch/` now committed (his `.gitignore` only excludes node_modules/.claude — verified), triage roles adopted verbatim (needs-triage/needs-info/ready-for-agent/ready-for-human/wontfix) plus work states (claimed/done/deferred); transient dumps moved to git-ignored `.tmp/`; .gitignore un-ignores .scratch/.agents/.claude per scaffold; review-method fallback inlined (works without code-review skill); historical change-log entries left verbatim per append-only rule.
- 2026-09-04 02:20 UTC — VPO via pi coding agent, main session, model volc2/glm-5.3-flash — PO decisions applied: git control refined to approval-gated-when-important (history rewrites, new deps, dir restructures, CI/env); TLDR/ELI5 communication style; new-user greeting/preference protocol (people.md). Absorbed from the PO's field guide: transitive doc-tree updates, upfront requirement disclosure, test integrity (no empty assertions), fresh session on major iterations, third-party model variant verification, low-res spot checks, try-it path in reports. Conflicts B/C resolved as keep-ours (single docs/ tree; tickets always).
- 2026-09-04 02:35 UTC — VPO via pi coding agent, main session, model volc2/glm-5.3-flash — weak-model escalation ladder added (self-assess; escalate design/arch/decisions via PO model switch, stronger subagent, or CLI; cheap-model and no-external-CLI rules demoted to non-absolute preferences); self-knowledge rule (harness+model identity, vendor-harness mismatch hint-once); Codex mentions generalized to higher-level statements; model pricing policy made example-based (Chinese models typically cheaper; list not fixed); merged engineering principles 3+7 into single "One thing, one name" (7 principles now); added docs/ knowledge layering (layer-1 immutable sources backup, layer-2 SSOT wiki, agent inferences marked inferred until PO confirms).
- 2026-09-04 02:45 UTC — VPO via pi coding agent, main session, model volc2/glm-5.3-flash — PO correction adopted: shared state (tickets, locks, docs) is always committed on main, never on a work branch — a lock recorded on a branch would be invisible to other agents, breaking the lock protocol; only implementation diverges and merges later. Tickets record their related branch and implementation commits (excluding the ticket's own latest update commit). Self-applied: this branch (which had mixed ticket updates into implementation commits) is being merged back to main now; AGENTS.md Branching and Ticket tracking paragraphs rewritten accordingly.
- 2026-09-04 02:55 UTC — VPO via pi coding agent, main session, model volc2/glm-5.3-flash — created AGENTS.zh-CN.md (87 lines, mirrors AGENTS.md; uncommon professional terms kept in English: SSOT, S.M.A.R.T., TDD, ponytail 链, triage roles verbatim, harness, just-in-time, append-and-drift); fixed "simplicity. and spawn" typo in AGENTS.md.
- 2026-09-04 03:05 UTC — VPO via pi coding agent, main session, model volc2/glm-5.3-flash — memory layering renamed L1/L2/L3 (L1 raw indexed+commented, L2 user-confirmed SSOT, L3 agent understanding; priority L1-with-comment > L2 > L3; confirmed L3 condenses into L2); /init rule (read code fully, derive business/arch/status/goals, keep questions open); automation-over-instruction principle (scripts/, hooks); skill-learning rule (procedural patterns → .agents/skills/, auto-triggered); sudo via pkexec/SUDO_ASKPASS; self-maintenance clause; evidence retention rule (.scratch/<feature>/evidence/). Mirrored into AGENTS.zh-CN.md.
- 2026-09-04 03:15 UTC — VPO via pi coding agent, main session, model volc2/glm-5.3-flash — skill acquisition rule hardened: project/module-level online skills always vendored as pinned submodule in vendor/ + symlinked into .agents/skills/, never npx skills (copies, breaks upstream tracking); npx skills -g allowed only with the every-session-justified bar; MP paragraph deduplicated to point at the general rule. Mirrored into AGENTS.zh-CN.md.
- 2026-09-04 03:25 UTC — VPO via pi coding agent, main session, model volc2/glm-5.3-flash — token-effectiveness self-review pass added to docs policy and applied: compressed intro, collaboration contract (all paragraphs), docs policy 3; meaning-preserving, no rules dropped. Mirrored into AGENTS.zh-CN.md.
- 2026-09-04 03:30 UTC — VPO via pi coding agent, main session, model volc2/glm-5.3-flash — report duty extended: intuitive medium over plain text (tables/diagrams/visual HTML for structure, architecture, relations); explicit report requests get the most intuitive, impressive presentation; no heavy jargon.
- 2026-09-04 03:40 UTC — VPO via pi coding agent, main session, model volc2/glm-5.3-flash — two-register principle (agent-facing = professional terms for token efficiency; PO-facing = easy intuitive forms for cognitive load); UX design principle added to Design process (Norman/Nielsen grounded: cognitive load, feedback, error prevention) with feel-able artifact rule (quick static HTML sketch / playable demo early — agent can't feel UX, PO judges feel).
- 2026-09-04 03:45 UTC — VPO via pi coding agent, main session, model volc2/glm-5.3-flash — show-don't-describe added to intuitive-medium rule: concrete examples (real request/response pairs, exported file format samples, actual data) beat schema tables and prose. Mirrored into AGENTS.zh-CN.md.

## Knowhow

- MP's answer to branch-vs-tracker: none — his `/implement` just says "commit your work to the current branch", and his wayfinder "claim" is a Status edit without pull/push CAS. Our docs/lock-on-main rule is deliberately stricter than MP because we run multi-agent with real locking; his architecture already anticipates the proper fix we noted: swappable tracker configs (local/github/gitlab) with identical skill vocabulary.

- When appending to change logs, match the full entry line — never a prefix. Prefix-matching edits have twice glued a new entry onto the previous one's tail; both were caught by re-reading the file before commit.

- Conflict resolutions applied: ask-for-information vs never-offload-work; ticket folder exempt from docs write permission; mid-session user alternation retracted in favor of per-session identity.
- Open question flagged: README still positions Bilibili/paper materials that were removed as policy.

## Acceptance check

- [ ] PO review of conflict resolutions and open questions
