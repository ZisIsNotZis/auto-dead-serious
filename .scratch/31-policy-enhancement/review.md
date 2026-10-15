# Independent review — 2026-10-15 work record

## Review

**BLOCK: one shared-machine admission loophole requires correction.** The remaining changed rules satisfy the scoped semantic criteria.

### Correct

- Consequence-based admission now accommodates a capable but distractible model without retaining consequence-free exposition (`AGENTS.md:9–12`).
- Work-family techniques remain subordinate to existing authority, delegation, review and delivery rules; they introduce no additional user gates (`AGENTS.md:237–262`).
- Diagnosis, testing, research and measurement guidance distinguishes relevant evidence from nearby green checks, circular expectations, contaminated evaluation and unsupported gain claims (`AGENTS.md:245–276`).
- Resource rules distinguish reservations, runtime enforcement and observed usage, and explicitly avoid claiming an allocator or runtime controls were implemented (`AGENTS.md:109–123`).
- Discussion/advance entry, main-agent delegation, silence and agreed user gates remain intact. The inactive source-only proposal remains explicitly inactive (`AGENTS.yaml:318–319`).

### Fixed

None. No files were edited.

### Finding: P0 — Advisory fallback does not establish machine-wide serialization

**Location:** `AGENTS.md:111,123`, `resources.machine.allocator_owner` and `resources.machine.advisory_limits`.

**Violated approved criterion:** shared-machine safety without an unsafe admission loophole; explicitly identified as blocking in `.scratch/31-policy-enhancement/handoff.md:13,21`.

When no coordinated allocator exists, `allocator_owner` sends distributed requesters to `advisory_limits`. That fallback permits “a conservative bounded instance” and requires coordination only “before scaling.” It does not establish a machine-wide fallback owner, exclusive launch right, or evidence that another requester cannot simultaneously launch its own first instance. Saying “rather than independent claims” does not supply that missing launch decision.

**Concrete counterexample:** A shared machine has 16 GiB RAM, 4 GiB existing unmanaged usage and a required 4 GiB recovery reserve. Two independent requesters have no coordinated allocator. Both observe the same available capacity and each launches one previously calibrated, bounded 6 GiB job under the fallback, with monitoring and a stop route. Neither requester scales beyond one instance. Together, their jobs consume the recovery reserve. Monitoring afterward does not prevent the simultaneous-admission race.

The “before scaling” restriction needs an explicit machine-wide interpretation and an observable way to establish it; otherwise each requester can apply the exception locally.

**Smallest fix:** Require the fallback instance to be serialized **across the machine**, under one identifiable owner or an already-authorized exclusive-use mechanism. If that exclusivity cannot be established, queue/report the coordination blocker rather than launch. This requires policy clarification, not allocator implementation. Add the competing-first-fallback-launch scenario to `scenarios.md`.

## Explicit changed-rule coverage

All changed/new homes listed in `rule-delta.json` were reviewed, including the authored-only proposal.

| Locations | Changed/new homes covered | Semantic result |
|---|---|---|
| `AGENTS.md:9–12` | `laws.projection`, `no_op`, `falsifiable` | Structural moves are inspectable; familiarity alone cannot evict consequential guidance; destructive negative controls are not required. |
| `AGENTS.md:31–47` | `intent`, `objective.true_metric`, `scope.derive_non_goals` | Negative research results remain valid; scope stops at decidable boundaries rather than arbitrary counts. |
| `AGENTS.md:60–61` | `intent.decisions.design_options`, `question_frontier` | Nominally renamed designs do not satisfy comparison; dependent questions stay behind their prerequisites. |
| `AGENTS.md:81,94,286` | `resources.efficiency.read_once`, `split.preflight`, `proof.review.scoped_review` | Truncation, changed revisions and acceptance-critical dependencies permit bounded inspection without permitting repository inventory. |
| `AGENTS.md:105–107` | `resources.scheduling.start_early`, `finite_concurrency`, `queue_behind` | Local compute is distinguished from remote coordination; detached launch alone cannot establish continuation or liveness. |
| `AGENTS.md:109–113,123` | `resources.machine`, `allocator_owner`, `capacity_accounting`, `recovery_reserve`, `advisory_limits` | Accounting and reserve distinctions are sound; competing fallback admission is the finding above. |
| `AGENTS.md:114–116` | `hierarchical_grants`, `absolute_limits`, `runtime_binding` | Child allocation transfers rather than creates capacity; worker counts do not excuse unrestricted library threads; ledger entries cannot prove enforcement. |
| `AGENTS.md:117–119` | `memory_containment`, `gpu_isolation`, `multi_resource` | Out-of-containment retries, utilization-only GPU sharing and indefinite partial-resource holding are rejected. |
| `AGENTS.md:120–122` | `reserve_monitoring`, `grant_recovery`, `bounded_calibration` | Agent exit/expired heartbeat cannot reclaim live descendants’ grants; unknown estimates cannot justify multiplication. |
| `AGENTS.md:145,169,173` | `brainstorm`, `conclusion_only`, `protect_willingness` | Clear small tasks avoid ceremonial alternatives; delivery includes consequential uncertainty without promising infallibility. |
| `AGENTS.yaml:318–319` | `attention.emphasis_by_evidence*` | Proposal remains inactive and does not authorize a reduced policy view. |
| `AGENTS.md:208,216–217` | `change.shape.granularity`, `upkeep.checklist`, `rule_form` | Admission principle, document-review checklist and authoring procedure have distinct jobs; semantic uniqueness is not falsely assigned to mechanical checks. |
| `AGENTS.md:237–244` | `practice`, `design`, `caller_complexity`, `abstraction_cost`, `dependency_isolation`, `feature` | Caller examples—not implementation size—justify boundaries; speculative abstraction and implementation batching lack acceptance evidence. |
| `AGENTS.md:245–250` | `diagnosis`, `reproduce_minimize`, `hypothesis_probe`, `unavailable_repro`, `diagnosis_closure` | A passing nearby test cannot close the original symptom; inaccessible production reproduction permits only bounded, explicitly provisional conclusions. |
| `AGENTS.md:251–253` | `refactor`, `caller_migration` | Replacement coverage must demonstrate preserved behavior before retirement; behavior changes require separate authority. |
| `AGENTS.md:254–257` | `testing`, `test_scope`, `test_doubles` | Independent expectations and realistic substitutes are required; justified internal checks remain allowed; unavailable integration stays disclosed. |
| `AGENTS.md:258–262` | `research`, `primary_evidence`, `evaluation_integrity`, `experiment_record` | Secondary evidence, held-out contamination and uncertain single runs cannot support unrestricted claims. |
| `AGENTS.md:266,271,273–276` | `proof.execution`, `gate_probe`, `measurement`, `intrinsic_benchmark`, `operational_load` | Safe failure-sensitivity checks replace universal destructive red runs; lower compute counters do not establish lower deployment latency; uncontrolled shared timing does not establish intrinsic improvement. |
| `AGENTS.md:297,302` | `think_first`, `context_pressure` | Planning is proportional and revisable; recovery revalidates revisions/jobs and cannot invent delegation authority. |

## Binding and limits

Handoff and hash-manifest labels agree for:

- `AGENTS.yaml`: `a2fdfb4f73a302b900ccf57e5a345a48af5cfcdacd71a29ff68f537e9388448b`
- `AGENTS.md`: `95396732440c82ce7fb1d9db503254b16d4687e7a7427a297bf0e5567f0a3367`
- `policy.diff`: `6f659439af562c10ef2ac052eeda2273e62cbe7799538afbed6a9acd602fe83a`
- `render.diff`: `bb2f4884f0cba09e367db84f5442f3749caa2ca8f7499ab6cf4530be13407eab`
- `scenarios.md`: `ac1f95209cdfdd00fb8ba9bf76e7a5209e4a60479b130170998bf61c9f7a070c`

The inspected generated text agrees with the final changed content in `render.diff`; the source-only change agrees with `policy.diff`. No unexpected content drift was observed. Existing mechanical results were inspected, not rerun. Digests were not independently recomputed through the read-only tools.

The counterexample is a static policy interpretation, not an executed allocator test. No runtime enforcement, benchmark, experiment or future compliance is certified. The date above identifies the supplied work record; an independent reviewer-clock timestamp was unavailable.

No write-capable tool was available, so this is the complete report for `.scratch/31-policy-enhancement/review.md`.

**Merge verdict: BLOCK.**