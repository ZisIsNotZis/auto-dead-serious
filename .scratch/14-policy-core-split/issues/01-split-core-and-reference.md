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

- [ ] `AGENTS.md` = core only: how-to-use, invariants, coordination scope, trigger table, maintenance.
- [ ] `docs/policy/reference.md` = all remaining rule content, deduplicated, one meaning per rule,
      remote-only rules tagged and skippable.
- [ ] `WORKSPACE.md` declares the coordination mode (default local) — policy works shipped unconfigured.
- [ ] Every one of the 108 existing rules maps to a destination in `.scratch/14-policy-core-split/mapping.md`
      (core / reference section / deleted-with-reason).
- [ ] Customer-recalibration applied: local mode is the default; no locking, heartbeat, mailbox,
      ordinal race or tracker unless M2; no dependency on external skills for compliance.
- [ ] Core size measured with `wc -m`; reference size measured; both within the declared budget.
- [ ] `git diff --check` clean.
- [ ] Fresh-context review (loss detection + citation resolution) passed or findings fixed.
- [ ] Merge commit records the size delta.

## Comments

- 2026-09-15 (agent, pi) — Created and claimed on the PO's "go" after four independent
  review passes (contradictions, focus, SSOT/size, actionability) and the design sketch.
  Evidence: `.scratch/14-policy-core-split/mapping.md`, size measurements in the closing Comments entry.
