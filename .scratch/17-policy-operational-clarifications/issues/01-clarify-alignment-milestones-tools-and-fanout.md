# 01 — Clarify alignment, milestones, tools, and exploratory fanout

- **Status:** done
- **Blocked by:** none
- **Need-review:** passed
- **Need-test-cases:** none (policy text)

## Objective

Apply the user's operational clarifications without expanding ceremony:

- Align critical product requirements, philosophy, design intent, methodology, roadmap, and granularity; do not require users to decide unfamiliar technical implementation.
- Only a user-agreed roadmap checkpoint is an acceptance milestone; agents may not invent milestones as reasons to stop.
- Prefer non-disruptive computer control and do not steal the user's input or focus when an accessibility/debug/automation interface can do the work.
- Write plain language for non-native speakers; avoid idiom, slang, and decorative metaphor.
- Bound every tool call and underlying command; do not require user rescue from a hung operation.
- Put durable/user-facing artifacts in project-local `.tmp/` or `.scratch/`, not global `/tmp`; clean transient artifacts when their purpose ends.
- For unknown-path creative/research work, fan out only genuinely independent directions, balancing urgency/token budget against shared compute contention.
- Prefer fresh-context subagents with complete cold-start briefs. Use inherited/forked context only when essential context cannot be compactly transferred; avoid repeating the inherited transcript.

## Acceptance criteria

- [x] Core distinguishes pre-agreed milestones from agent-invented progress points.
- [x] Collaboration distinguishes product/philosophy alignment from user-owned technical implementation.
- [x] Computer-use, timeout, artifact-lifecycle, exploratory-fanout, and subagent-context rules are actionable.
- [x] Size delta, citation check, `git diff --check`, scoped reread, and proportionate fresh review are recorded.

## Baseline

`wc -m AGENTS.md WORKSPACE.md docs/policy/*.md` = 54,418 characters.

## Verification

- `wc -m AGENTS.md WORKSPACE.md docs/policy/*.md`: 57,768 characters after the first edit pass, +3,350 from the 54,418 baseline; final rerun pending.
- `git diff --check`: passed after the first edit pass.
- Key-term/routing grep: passed for pre-agreed milestones, non-native language, non-disruptive computer use, artifact lifetime, exploratory fanout, context isolation, and finite timeout; added shared-desktop control to the environment topic trigger after review.
- Definition audit first attempt failed because the audit regex itself had an unclosed group; no policy result was inferred. Corrected audit pending.
- Fresh-context review: first pass blocked on two routing gaps. Fixed by moving the complete tool/command timeout requirement into the always-on safeguards and making artifact storage/lifetime selection an explicit environment-topic trigger. Focused fresh rereview passed with no findings (`Merge verdict: OK`).
- Final `wc -m AGENTS.md WORKSPACE.md docs/policy/*.md`: 58,206 characters, +3,788 from the 54,418 baseline.
- Final `git diff --check`: passed with no output. Scoped diff reread covered only `AGENTS.md`, four existing topic files, and this ticket.

## Comments

- 2026-09-17 (main agent, pi) — Created and claimed from the user's request for a fast clarification pass; limited to existing policy homes and no topology change.
- 2026-09-17 (fresh reviewer, pi) — Blocked on two applicability gaps: timeout behavior was not fully always-on, and artifact lifetime could be selected before its topic loaded. Both were fixed in the core/router and environment topic.
- 2026-09-17 (focused fresh reviewer, pi) — Verified both fixes and found no new P0/P1 regression. Verdict: `Merge verdict: OK`.
