# Independent final-delta review

## Review

**PASS — the original advisory first-launch blocker is closed.**

### Correct

- **Exclusivity precedes the first launch.** `AGENTS.md:123` explicitly requires establishing and recording observable **machine-wide exclusivity** before even the first advisory calibration or heavy launch. It expressly rejects requester-local one-instance limits.
- **Missing exclusivity prohibits launch.** The same rule requires queuing or reporting the coordination blocker **and not launching**. Monitoring afterward cannot substitute for admission.
- **The original counterexample is no longer permitted.** In `.scratch/31-policy-enhancement/scenarios.md:66`, two independent requesters cannot each launch their bounded 6 GiB first job against the same headroom. Neither may launch independently without established machine-wide exclusivity. An exclusive fallback admits only one conservative bounded instance, while the recovery-reserve requirement still applies.
- **Neighboring rules remain consistent.** `allocator_owner` routes unavailable coordinated admission to this fallback (`AGENTS.md:111`); calibration does not bypass its precondition (`:122–123`). Capacity accounting, recovery reserve, hierarchical grants and descendant/thread accounting remain applicable (`:112–115`). Exclusivity does not create capacity or authorize a second independent allocation.
- **No implementation or new user gate is implied.** The machine contract disclaims an implemented allocator or installation authority (`AGENTS.md:110`). The repair permits an **already-authorized** exclusive-use mechanism, otherwise requiring a blocker—not new implementation or a mandatory user confirmation. Runtime enforcement still requires actual binding evidence (`:116`), and advisory caps must not be labeled enforced (`:123`).
- **The delta is minimal.** The precise repair diffs change only `resources.machine.advisory_limits._text` (`AGENTS.yaml:211`) and its generated line (`AGENTS.md:123`). The scenario delta retains the failure case and adds explicit exclusive-success and unavailable-exclusivity paths. Preservation evidence reports all other policy nodes, text and order unchanged.

### Fixed

**Original P0: advisory fallback did not establish machine-wide serialization — CLOSED by the worker’s repair.**

The prior rule required coordination only before scaling. The final rule establishes the missing pre-first-launch decision, observable machine-wide scope and explicit no-launch failure route. I made no edits.

### Findings

No issues found.

### Merge verdict

**OK within the assigned final-delta semantic scope.** Together with the saved first review’s acceptance of unchanged rules, this repair resolves its sole blocker. This is not runtime allocator certification.

## Refreshed evidence

Inspected the updated handoff, saved first review, both changed-file manifests, precise repair diffs, final generated rule, competing-first-launch scenario and repair evidence.

The repair log and closure record refreshed successful execution of:

- `python3 scripts/render_policy.py`
- `python3 scripts/render_policy.py --check`
- `python3 .scratch/31-policy-enhancement/verify.py`
- `git diff --check -- AGENTS.yaml AGENTS.md`
- `sha256sum --check .scratch/31-policy-enhancement/final-sha256.txt`

The evidence includes schema/reference/render checks, preservation checks and safe negative controls. No-index whitespace checks report difference-only exit 1 without diagnostics; the whitespace negative control reports the expected failure. The closure records no staging or status drift.

## Exact content bindings

These SHA-256 labels agree between the inspected handoff and `final-sha256.txt`. They bind dirty-worktree artifacts, not HEAD alone; recorded HEAD remains `7ace6bf5dd1f23c85fcaf17e5fbbb19913c79d76`.

| Artifact | SHA-256 |
|---|---|
| `AGENTS.yaml` | `b762e4cb86fcefc6ffc349ba72e7659ad6429202f5391ac239c43374db0dcf21` |
| `AGENTS.md` | `5ca1334c1afceccc6774a019752d9ab1be91f2b2e191b61f0bbac8d4dc0834d0` |
| `policy.diff` | `a924c524d1508e59258ecb758641541f3419118c7edd530b08f02e5e5de8df82` |
| `render.diff` | `57ab6c89846a50def5fc97ca8ca856b043874a3140650cbe40a409be431f0c41` |
| `repair/policy.diff` | `68e0430e56b79ff04a5aee27fa993c587bfc01e722a661f050503a7c75fb1e68` |
| `repair/render.diff` | `aac613d59d5065cc59c34bc30f4b14d99d56af9f61811457dc236943eade9fb4` |
| `scenarios.md` | `c72c377b6e7c2b8147d372bdcc4eac9c57950cc65757f41891d385c756a86feb` |
| `repair/scenarios.diff` | `9917e4a162019f07e07dd6a0fa260a4d2a277ab893fdafc4c9795cec2404fa6f` |
| Saved first review, `review.md` | `586e81ba28217897b1b480f09c5b69fd79c134daed2d5b0cdb6db6231ede80bb` |

Paths other than the policy files are relative to `.scratch/31-policy-enhancement/`.

## Remaining limitations

- Mechanical results were inspected, not rerun; digests were not independently recomputed through the read-only tools.
- The counterexample assessment is semantic/static. No live admission race, exclusivity mechanism, runtime binding, memory containment or crash recovery was exercised or certified.
- Unchanged rules rely on the saved first review plus inspected preservation evidence; this was not a second full-policy review.
- Future agent compliance is not proven.

No write-capable tool was available. This is the complete report for the parent to persist as `.scratch/31-policy-enhancement/review-final.md`.