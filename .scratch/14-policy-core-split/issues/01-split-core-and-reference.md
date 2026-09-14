# 01 — Split policy into always-on core + on-demand reference

- **Status:** claimed
- **Blocked by:** none
- **Assignee/lock:** agent (pi)
- **Need-review:** yes (behavior change: the policy itself)
- **Need-test-cases:** none (policy text; verification = size measurement + rule-coverage diff + fresh-context review)

## Issue

`AGENTS.md` is 48,178 chars / 172 lines / 108 numbered rules, injected into every session.
It violates its own size rule (L61: "targets ~10K chars") 4.8x, has no priority signal, no
deletion machinery (69 commits, 21 review rounds, rule count 100 -> 108, never down), and
states many rules without a firing trigger.

PO decision (this round): split into an always-on core and an on-demand reference, recalibrate
the customer image, and stop shipping a fleet's machinery to a single-developer, single-machine,
local-subagent workflow.

## Acceptance criteria

- [x] `AGENTS.md` = core only: how-to-use, terms, invariants, coordination scope, trigger table, maintenance.
- [x] `docs/policy/reference.md` = all remaining rule content, deduplicated, one meaning per rule, remote-only rules tagged and skippable.
- [x] `WORKSPACE.md` declares the coordination mode (default local) — policy works shipped unconfigured.
- [x] Every one of the 108 existing rules maps to a destination in `.scratch/14-policy-core-split/mapping.md` (core / reference section / deleted-with-reason).
- [x] Customer-recalibration applied: local mode is the default; no locking, heartbeat, mailbox, ordinal race or tracker unless M2; no dependency on external skills for compliance.
- [x] Core size measured with `wc -m`; reference size measured; both within the declared budget (core S1).
- [x] `git diff --check` clean.
- [x] Fresh-context review (loss detection + citation resolution) passed or findings fixed.
- [x] Merge commit records the size delta.

## Measurements (2026-09-15, `wc -m`, final state of the branch)

| Artifact | Chars | Note |
|---|---:|---|
| `AGENTS.md` (core, always in context) | 7992 | was 48,178 standing → **−83%** |
| `docs/policy/reference.md` (on demand) | 47994 | 11 sections, read section-wise (~2–5K each) |
| `WORKSPACE.md` | 2535 | mode + gate commands + dated environment facts |
| Total text | 58521 | was 48,788 → **+20%** |
| Rule heads preserved | 108/108 | verified by ID diff; no duplicate IDs; all citations resolve |
| Automated token diff vs the old file | 13 hits, all verified non-losses | `(common)` label, the 3 external skill names, the dead `~10K` target, the replaced `<200 lines` unit, and regex artefacts |

Honest note on total growth: the split added content the old file lacked — canonical fallbacks
for missing harness capabilities, stated exits for gated states, a review-completion artifact, the
gate command list, the precedence mechanism, the self-sufficiency rule, per-clause IDs — and wrote
sentences where the old file used caveman fragments. The win is standing context and focus, not
total bytes: 48,178 → 7,994 chars of always-loaded prompt.
To go **below** the old total, rules must be deleted. Candidate class, not taken here: the
general-engineering defaults (config-driven, just-in-time abstraction, compact interfaces,
low-level conditional, ~1.5–2K) plus a de-duplication pass; that is a separate PO decision.

## Review record (need-review)

- Reviewer 1 (fresh context, loss audit): verdict **reject** — 25 findings; A-severity: lost
  "tighten, never contradict" guard; no trigger for docs-before-code; per-render frontend review
  deleted; product decisions dropped from the user gate; core-only vocabulary undefined;
  `I9`'s delegation test unqualified.
- Reviewer 2 (fresh context, coherence audit): verdict **reject** — 21 findings; A-severity:
  remote-mode test undecidable from the stated evidence; kill protocol depended on remote-only
  locks/heartbeats; worktree command existed only inside the remote-only section.
- Fixes: commit `1ed2dbe` (all A/B defects, citation fixes, exits for triage states, one-home
  fixes, core trimmed back under its own S1 budget after the fixes pushed it to 9,187 chars).
- Re-verification: fresh context, 15 claims checked — 13 CONFIRMED, 2 PARTIAL (M2 "necessary but
  not sufficient" vs the bare-repo fallback; the worktree rule duplicated between `R-TKT.3` and
  `R-DEL.1`), plus 4 new defects (no `Budget:` header declaration; reference preamble saying
  remote sections are "never cited" against M3's allowed pointers; an empty re-verification
  pointer; `R-DSN.11`'s offline flag against the I1 product-shaping gate).
- Verdict after fixes: **accept** — commit `d28a85c`, final sizes core 7992 / reference 47994,
  both inside the S1 caps.

## Comments

- 2026-09-15 (agent, pi) — Created and claimed on the PO's "go" after four independent review
  passes of the pre-split file (contradictions, focus, SSOT/size, actionability), which found
  68 raw findings, ~25 distinct after de-duplication.
- 2026-09-15 (agent, pi) — Branch `ticket-14-policy-core-split`: `cd9c2ae` split, `1ed2dbe`
  review fixes + trim, `d28a85c` verification fixes + trim. Evidence: `mapping.md`, the
  measurements above, the subagent reviews summarised in the review record.
