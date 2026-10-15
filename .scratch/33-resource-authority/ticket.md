# 33-resource-authority
Kind: append-only work record; owner: worker; status: implementation pending independent review.
## Contract — 2026-10-15T14:33:32+08:00
- Confirmed user intent (task wording): “现有调度资源规则导致跑 git 都问如何调度；改为用户没有明确限制就是授予全部资源权限。”
- Confirmed semantics: 未明确限制时，默认可自主使用本机全部可用计算资源、自主调度，无须用户逐次授权；git/读取/搜索/轻量脚本等常规命令不触发资源调度仪式；重任务按实际必要程度自主判断协调监控，不得让 allocator/ledger/exclusivity/固定额度等成为默认启动前置、缺少它们不得为了本机资源权限询问用户。
- Confirmed boundary: 保留机器实际容量/避免失控、用户明确限制优先；全部资源权限不意味着付费、外部计算、破坏操作权限。
- Agent inference from confirmed intent: Replace conflicting scheduling/machine rules in place, reducing mandatory admission mechanics to proportionate autonomous safety measures; repair references only where the changed rules require it, without changing delegation, review or external-compute policies.
- Scope: AGENTS.yaml scheduling/machine and directly affected cross-references; generated AGENTS.md; this ticket only. No unrelated rules, environment changes, commits, staging, subagents or heavy compute.
- Acceptance: (1) git status/read/search/light scripts run without resource scheduling ceremony; (2) unrestricted local heavy work can autonomously use all actually available resources without allocator/ledger/exclusivity/fixed-quota prerequisites or user resource permission requests; (3) explicit resource limits and actual capacity/recoverability still constrain work; (4) paid/external/destructive authority does not expand; (5) schema/reference/render checks and scoped diff whitespace checks pass; unrelated pre-existing work remains unchanged.
- Proof: Baseline render/schema check; final render and --check (includes JSON Schema validation, unique keys, reference resolution and generated-byte identity); safe negative controls against baseline for new authority expectations; four scenario-specific textual assertions plus human semantic review; exact baseline-to-current diff and SHA-256 evidence. No heavy workload is needed to test a policy edit; checks cannot prove future agents follow it.
- Budget: 1 writer; 0 child agents; at most 2 repair rounds; 10 minutes, deadline 2026-10-15T14:43:32+08:00; stop on out-of-scope ambiguity or preservation risk. Independent review belongs to parent and is pending, not self-certified.
## Baseline
- HEAD: 7ace6bf5dd1f23c85fcaf17e5fbbb19913c79d76.
- Baseline command `python3 scripts/render_policy.py --check`: exit 0, `checks passed; AGENTS.md matches AGENTS.yaml.` (includes applicable schema check).
- `git diff --cached --name-only`: empty; no staged files.
- Original AGENTS.yaml is untracked and AGENTS.md is already modified; HEAD is not the edit baseline.
- SHA-256:
  - AGENTS.yaml: b762e4cb86fcefc6ffc349ba72e7659ad6429202f5391ac239c43374db0dcf21
  - AGENTS.md: 5ca1334c1afceccc6774a019752d9ab1be91f2b2e191b61f0bbac8d4dc0834d0
  - AGENTS.schema.yaml: 1aaf0d4c1e6ec6b99e07cc48eef89f8115dfb1f9478e21314ae14ca7f43269ba
  - scripts/render_policy.py: 4c76240b9860198776cb0d1f827e75e2ff81f2ce7bceb9eed403086b72e349ab
```text
 M AGENTS.md
 m agentic-animation
 M agentworld
 M autofe
 M backseat
 D docs/policy/execution.md
 M flashdb
 M helpagent
 M learn_draw
 m litellmgen
 M pathlm
 M resume_private
 M ringsvr
 M sys_gal
?? .scratch/21-autonomous-work-policy/
?? .scratch/22-clean-context-policy/
?? .scratch/23-policy-consolidation/
?? .scratch/24-delegation-ssot-context/
?? .scratch/25-slice-review-selfloop/
?? .scratch/26-delivery-tree-policy/
?? .scratch/27-single-file-policy/
?? .scratch/28-policy-history/
?? .scratch/29-lessons/
?? .scratch/30-research-adopt/
?? .scratch/31-policy-enhancement/
?? .scratch/32-git-hygiene/
?? .scratch/policy-delegate-ssot.round2.workflow.js
?? .scratch/policy-delegate-ssot.round3.workflow.js
?? .scratch/policy-delegate-ssot.round4.workflow.js
?? .scratch/policy-delegate-ssot.round5.workflow.js
?? .scratch/policy-delegate-ssot.workflow.js
?? .scratch/slice-review-recovery.workflow.js
?? .scratch/slice-review-selfloop.workflow.js
?? .scratch/thinking-focus.workflow.js
?? AGENTS.docs.schema.yaml
?? AGENTS.schema.yaml
?? AGENTS.yaml
?? dojo/
?? local_lm_research/
?? murderMysteryGame/
?? pi-keys/
?? scripts/
```
## Scoped baseline policy text
```yaml
  scheduling:
    _text: Time on the machine is the scarce thing, so the plan states what starts early and what a turn may wait on.
    start_early:
      _text: "Start useful independent packages early and prioritise the critical path only after their local compute fits admitted CPU, memory, disk, GPU, process, port and service constraints. @machine"
    finite_concurrency:
      _text: "Use dynamic, finite, observable concurrency and numeric budgets sized to the effective machine capacity. Distinguish lightweight remote agent coordination from local compute; worker count alone does not bound tests, builds or numerical-library threads. Maximize useful throughput within safety and recovery bounds, not an arbitrary desktop-responsiveness percentage. @machine"
    queue_behind:
      _text: "When a scarce resource is held, record a queued request and a verifiable continuation trigger rather than holding a turn or partial resources indefinitely; detach only when launch, ownership and completion are observable. Establish liveness through managed job/descendant identity and allocator state, not a process-name match or a completion banner alone. @multi_resource @async_continuation"
    overlap_waits:
      _text: Overlap version-bound, stable review, tests and docs with other implementation instead of waiting idle.
  machine:
    _text: For local compute, maximize useful throughput subject to machine safety and recoverability. Apply the admission contract below before multiplying jobs; it specifies required coordination, not an allocator already implemented or authority to install one. @authority @external_compute
    allocator_owner:
      _text: With distributed requesters, use one authoritative allocator per machine and an atomic coordinated admission ledger/queue recording job identity, ownership, resource request, grant and lifecycle. A requester obtains admission before launch; if no coordinated allocator is available, declare that limitation and use the bounded advisory fallback rather than independent claims on the same capacity. @advisory_limits
    capacity_accounting:
      _text: Before admission and while jobs run, refresh actual effective CPU, RAM, GPU/device memory and process capacity including container/service restrictions; account for unmanaged usage and protected capacity once, without counting managed observed usage again on top of its reservation. Keep reservation (promised capacity), enforced limit (runtime bound) and observed usage (measurement) distinct; stale or unknown capacity blocks multiplication.
    recovery_reserve:
      _text: Choose a machine-specific reserve for OS, control and recovery from actual conditions and recovery needs, record its rationale and absolute thresholds, and admit only work that leaves it intact. No universal numeric reserve is assumed; unknown safety headroom requires bounded calibration or queuing. @bounded_calibration
    hierarchical_grants:
      _text: A parent and all descendants must fit the parent grant; subdivision transfers capacity and never creates it. Record child allocation against that grant so a child cannot also claim it independently; revise the parent request before expanding the subtree, and include child-created processes and threads.
    absolute_limits:
      _text: Express grants as absolute CPU quota, RAM bytes, GPU/device-memory allocation and process/worker limits; if percentages are used, state their effective-capacity denominators. Account for test/build runners, BLAS and data-loader internal parallelism as well as agent workers; cap their threads/processes within the same grant. @hierarchical_grants
    runtime_binding:
      _text: Before calling a cap enforced, bind the actual job and descendants to applicable runtime controls and verify that binding with safe evidence. Pair CPU quotas with worker/thread controls; prose, a ledger entry or a launch flag alone proves neither enforcement nor descendant containment. @gate_probe @unverified
    memory_containment:
      _text: Contain memory overrun within the grant using available runtime limits; report the resulting failure, preserve a recovery checkpoint where safe, and revise or queue the request rather than retrying outside containment. If containment is unavailable, declare memory advisory and use conservative measured bounds with stop monitoring. @advisory_limits
    gpu_isolation:
      _text: Start with exclusive GPU admission, including device memory and subprocesses. Share only when workload isolation, interference and safety are justified and monitored; if isolation cannot be established, queue instead of inferring safe sharing from low momentary utilization.
    multi_resource:
      _text: For a job needing several resources, coordinate admission of the complete resource bundle; avoid indefinite hold-and-wait by queuing until it fits or releasing partial reservations before retry. A queued job has an observable owner and continuation route; authority or unavailable capacity is a recorded blocker, not a hidden spin loop. @async_continuation
    reserve_monitoring:
      _text: Monitor observed usage, remaining reserve and job liveness during admitted work. At reserve threat, stop new admission and reduce, checkpoint/stop or queue work within authority; record the trigger and outcome. Release grants only after the job and all its descendants stop, not merely when the launching agent returns.
    grant_recovery:
      _text: On stale entries, allocator restart or requester crash, reconcile grants against identifiable live jobs and descendants before reclaiming capacity. Missing heartbeat alone is not proof of exit; retain uncertain reservations and queue until liveness is established or authorized containment stops the work. @reserve_monitoring
    bounded_calibration:
      _text: When resource estimates are unknown, run one conservatively bounded representative instance, measure peaks and internal parallelism, and revise the request with margin before multiplying it. If a safe bound cannot be established, queue or report the missing capacity/control rather than fabricate an estimate. @absent
    advisory_limits:
      _text: Where coordinated admission or runtime controls are unavailable, state exactly which limits are advisory. Before even the first advisory calibration or heavy launch, establish and record observable machine-wide exclusivity under one identifiable owner or an already-authorized exclusive-use mechanism; if exclusivity cannot be established, queue or report the coordination blocker and do not launch. A requester-local one-instance limit is insufficient. Under that exclusivity, restrict launch to one conservative bounded instance with calibration, monitoring and a stop/queue route; require coordinated admission before scaling. Do not label advisory caps enforced or compensate for missing controls by silently escaping them. @bounded_calibration @runtime_binding
```
## Baseline related cross-references
```text
177:       _text: "Start useful independent packages early and prioritise the critical path only after their local compute fits admitted CPU, memory, disk, GPU, process, port and service constraints. @machine"
179:       _text: "Use dynamic, finite, observable concurrency and numeric budgets sized to the effective machine capacity. Distinguish lightweight remote agent coordination from local compute; worker count alone does not bound tests, builds or numerical-library threads. Maximize useful throughput within safety and recovery bounds, not an arbitrary desktop-responsiveness percentage. @machine"
181:       _text: "When a scarce resource is held, record a queued request and a verifiable continuation trigger rather than holding a turn or partial resources indefinitely; detach only when launch, ownership and completion are observable. Establish liveness through managed job/descendant identity and allocator state, not a process-name match or a completion banner alone. @multi_resource @async_continuation"
187:       _text: With distributed requesters, use one authoritative allocator per machine and an atomic coordinated admission ledger/queue recording job identity, ownership, resource request, grant and lifecycle. A requester obtains admission before launch; if no coordinated allocator is available, declare that limitation and use the bounded advisory fallback rather than independent claims on the same capacity. @advisory_limits
191:       _text: Choose a machine-specific reserve for OS, control and recovery from actual conditions and recovery needs, record its rationale and absolute thresholds, and admit only work that leaves it intact. No universal numeric reserve is assumed; unknown safety headroom requires bounded calibration or queuing. @bounded_calibration
195:       _text: Express grants as absolute CPU quota, RAM bytes, GPU/device-memory allocation and process/worker limits; if percentages are used, state their effective-capacity denominators. Account for test/build runners, BLAS and data-loader internal parallelism as well as agent workers; cap their threads/processes within the same grant. @hierarchical_grants
199:       _text: Contain memory overrun within the grant using available runtime limits; report the resulting failure, preserve a recovery checkpoint where safe, and revise or queue the request rather than retrying outside containment. If containment is unavailable, declare memory advisory and use conservative measured bounds with stop monitoring. @advisory_limits
207:       _text: On stale entries, allocator restart or requester crash, reconcile grants against identifiable live jobs and descendants before reclaiming capacity. Missing heartbeat alone is not proof of exit; retain uncertain reservations and queue until liveness is established or authorized containment stops the work. @reserve_monitoring
211:       _text: Where coordinated admission or runtime controls are unavailable, state exactly which limits are advisory. Before even the first advisory calibration or heavy launch, establish and record observable machine-wide exclusivity under one identifiable owner or an already-authorized exclusive-use mechanism; if exclusivity cannot be established, queue or report the coordination blocker and do not launch. A requester-local one-instance limit is insufficient. Under that exclusivity, restrict launch to one conservative bounded instance with calibration, monitoring and a stop/queue route; require coordinated admission before scaling. Do not label advisory caps enforced or compensate for missing controls by silently escaping them. @bounded_calibration @runtime_binding
475:         _text: For shared-load operational claims, define the representative concurrent load and resource/admission policy for both alternatives and report observed interference and failures alongside throughput/latency. Do not use an isolated microbenchmark alone to promise a shared-load gain, or a noisy shared run to infer intrinsic compute efficiency. @machine
523:       _text: "On interruption, context loss or a resource stop, checkpoint artefacts, revision, decisions, grants and job identities, remaining acceptance and next action before yielding. On resumption validate the actual revision and job state and rerun stale checks; hand off independent remainder or a fresh replacement only within granted delegation authority. @interrupt @resumable @grant_recovery"
```
## Parent takeover — 2026-10-15T14:34:27+08:00
- User corrected phase interpretation: current interaction is eager mode, immediate direct execution, not subagent delegation; worker stopped before policy edits and main agent took exclusive ownership.
- Scope extended by that explicit correction to roles.main_agent and discussion.act_now: immediate edit/run requests do not imply advance, and eager mode executes directly unless delegation is explicitly requested.
- Main agent rewrote conflicting machine/scheduling requirements in place: all available local resources authorized by default; ordinary commands exempt from admission ceremony; heavy work autonomously scheduled with proportionate recovery safeguards; explicit limits and external/paid/destructive authority unchanged.
- Executed `python3 scripts/render_policy.py`, `python3 scripts/render_policy.py --check`, and `git diff --check -- AGENTS.yaml AGENTS.md`: all exited 0; schema/reference/render consistency passed. No advance-phase independent review dispatched, consistent with user correction; future agent compliance is not established by mechanical validation.
- Status: direct requested policy edits complete; no commit, staging or unrelated changes.
## Explicit advance trigger — 2026-10-15T14:35:56+08:00
- User confirmed: “只有我说自动推进，继续推进，反正提及推进之类的才是advance”。
- Main agent updated attention.phases: only an explicit instruction to 推进 enters advance; bare 继续 or immediate execution does not. Mere quotation or discussion of 推进 is not an instruction.
- Re-rendered AGENTS.md; `python3 scripts/render_policy.py`, `python3 scripts/render_policy.py --check` and `git diff --check -- AGENTS.yaml AGENTS.md` all passed.
## Command log
- 2026-10-15T14:33:32+08:00 — worker: read AGENTS.yaml (complete), AGENTS.schema.yaml and scripts/render_policy.py; ran date, git rev-parse HEAD, git status --short, git diff --cached --name-only, sha256sum and baseline renderer --check; all commands succeeded. No resource-permission question or scheduling ceremony was used for these routine commands.
