# Catalogue calibration: local evidence for dojo, VibeOS, agentic-animation, PathLM

Observation time: 2026-10-19 09:59 +08:00 (local clock). This is the local-evidence half of catalogue calibration. The user named these four as personally high-quality candidates; that attribution is preserved, but is not treated as evidence for any score or verdict.

## Scope and evidence limits

Inspected parent revision: `f54666f21f50b7cceffc907efd4646208f6586ab`. Parent gitlinks and child HEADs agree at these pins:

| Repository | Parent pin = child HEAD | State observed |
|---|---|---|
| `dojo` | `9026a02ddb89b15f232a330e35093cf7c69110f9` | No tracked or normal untracked changes in bounded status |
| `vibeos` | `b81f0e248c07bb0098b0f454d42adecaef2e8bf0` | No tracked or normal untracked changes |
| `agentic-animation` | `8e7a5520dce956e409ddd45415a09cc3bcd12f4d` | No tracked or normal untracked changes |
| `pathlm` | `62c60d36f56668a115ca90c871ae62c0a375e277` | Four tracked files dirty; details below |

`pathlm` was handled as pre-existing live work. Bounded status/diff snapshots showed changes only to `axes/2-depth/2.2.2-attention-residual/experiments/2653-interlayer-attn-13m/{run_log.txt,supervise.out}` and `axes/2-depth/2.2.3-learned-layer-sum/experiments/2651-inter-layer-topology-s1-13m/{run_log.txt,supervise.out}`. The later diff-stat snapshot showed additions of 6, 90, 6, and 488 lines respectively. I did not read those files, inspect processes, or interrupt anything. Their contents and any live outcome remain unknown; changing diff counts are not proof of progress. PathLM findings below use tracked README/docs/source and the committed, non-dirty 2613 result records, not mutable outputs.

Each repo was opened at its README and declared docs layout, then scope expanded only to representative source/tests and result records. No network/public search, install, build, project-code execution, or test run was performed. The parent owns external alternatives, so no originality or non-duplication verdict is live-verified. I did not visually inspect agentic-animation's linked films.

## Provisional scoring anchors

The five dimensions are independent; do not average them or turn scores into automatic membership decisions. To avoid the pilot's zero/absence conflation, **0 means direct evidence contradicts the dimension; U means insufficient evidence**. `1` is narrow, weak, or mainly asserted; `2` is concrete local value or a credible prototype with material limits; `3` is a coherent, substantive outcome in its stated scope with important gaps; `4` is a mature, independently validated outcome for its audience. Creativity scores locally observed distinctiveness, not proven novelty. Expected usefulness needs a named use and credible advantage, not aspiration alone. Implementation progress is based on behavior/experiment evidence, not code or commit volume. Presentability is how well the project surface explains, lets a user try, and lets a user evaluate the project.

## Scorecards

### `dojo` — provenance-aware ideas and discussions in a local CLI/SQLite POC

**Description and distinctive contribution.** A Chinese, no-UI workbench for discussion candidates with type, scope, premises, alternatives, unknowns, provenance, versions, and relations. Its offline three-character story demonstrates a separately retrievable method claim, an application, and a logical challenge. The distinctive local merit is the epistemic boundary: confirmation makes a candidate discussable, not true; retrieval reports lexical overlap, not semantic relevance; explicit relations and versions preserve disagreement rather than auto-merging it (`dojo/README.md:1-3,17,41-51`; `dojo/dojo/demo.py:1-8,31-42`; `dojo/dojo/storage.py:599-647`).

**Scenario and intended audience.** Current use is an individual using local CLI commands to structure and revisit an idea, claim, counterexample, or unknown; `discuss` can use a configured live model. The newer product direction imagines ordinary-chat interaction and a backend agent pipeline for classifying and connecting bounded conclusions (`dojo/docs/product.md:3-28`). That document supersedes the older product-direction claim in `current-demo-direction.md`, but the README still calls the older document current (`dojo/README.md:5-7`; `dojo/docs/product.md:3`). The installed POC is not the envisioned knowledge network or agent pipeline.

| Creativity | Current usefulness | Expected usefulness | Impl progress | Presentability |
|---:|---:|---:|---:|---:|
| 3 | 2 | 2 | 2 | 2 |

- **Creativity 3:** the locally observed combination of provenance-aware claim types, revisable relations, user-directed discussion, and inspectable lexical retrieval is distinctive. Public novelty remains unknown.
- **Current usefulness 2:** real CLI/store operations support candidate and history use, and retrieval returns matched terms plus scope/source/unknown context. This is practical as a personal structured-notes experiment, but retrieval is lexical and there is no multi-user/network transfer (`dojo/dojo/storage.py:599-647`; `dojo/README.md:29-51`).
- **Expected usefulness 2:** the target problem—reasoning through an issue and retaining bounded, sourced conclusions—is clear, but the cross-session/network pipeline is still product design. Human review, broadcast value, and retention are unvalidated (`dojo/docs/product.md:21-41,53-59`).
- **Implementation progress 2:** substantive evidence is behavior, not size: the store supports versioned state/event history/provenance/relations; a focused mocked-model conversation test describes edit, challenge, revision, and history assertions (`dojo/tests/test_conversation.py:124-193`). This is inspected test/source evidence, not a test run or proof of real-user effectiveness.
- **Presentability 2:** README gives a one-command demo, CLI examples, privacy handling, and clear simulation limits, but directs a stranger to an obsolete product-direction document while the current product document describes a materially different product (`dojo/README.md:5-17,27,72-79`; `dojo/docs/product.md:3-7`).

**Membership routes (OR).** Creativity: **provisionally supported locally; novelty unsearched**. Useful without merely repeating existing OSS: **not established pending public comparison**. Substantial work proving it is trying: **supported** by the stateful claim lifecycle, provenance/revision behavior, and focused tests—not by project size. **Local view:** provisionally supported through the substantial-work route; prominence is not implied.

**Strongest merit / why a high-quality impression could mislead.** The data model is more careful than a generic notes CLI: it distinguishes evidence status, discussability, provenance, disagreement, and truth. But the fluent three-person story can look like a social knowledge network: it is fixed dialogue, not live AI or user research; lexical overlap does not establish shared meaning; and the network/agent pipeline remains design (`dojo/docs/current-demo-direction.md:37-46`; `dojo/docs/product.md:3,45-51`). The README/product-direction mismatch is a further orientation defect.

**Next decisive step.** Align the README/demo entry with the current product decision, then test one real, bounded discussion including a genuine textual objection that must not be persisted as agreement. The documented false-accept risk is explicitly untested (`dojo/docs/product.md:45-51`).

**Parent's strongest alternative-search question.** Which open-source chat-first thinking, personal-knowledge, or claim-tracking systems combine explicit source/evidence status, scoped claims, objections/revisions, reversible merge, and cross-session retrieval? Compare the same user task; distinguish shared knowledge from ordinary personal notes or chat history.

### `vibeos` — browser OS that stages generation of missing app surfaces

**Description and distinctive contribution.** A local browser desktop/runtime provides windows, launcher, storage, and a generic app bridge. On a cache miss the runtime stages a scoped Codex worker, validates an app artifact, publishes under `world/`, and resumes the initiating operation (`vibeos/README.md:5-22`; `vibeos/apps/server/src/runtime.ts:76-78,125-126`). The distinctive local contribution is the platform/app boundary plus staged, structured generation and publication, not an app-specific prompt alone (`vibeos/apps/server/src/generation-harness.ts:45-78,97-110,113-153`).

**Scenario and intended audience.** A single user asks for an app or route not already in the local world and continues their action after generation. Developers/agent users are the evident audience. It is explicitly local-first and experimental, not a production OS; generation requires a configured Codex CLI/provider (`vibeos/README.md:7-18,20-32`; `vibeos/docs/project-status.md:23-28`).

| Creativity | Current usefulness | Expected usefulness | Impl progress | Presentability |
|---:|---:|---:|---:|---:|
| 3 | 2 | 3 | 3 | 3 |

- **Creativity 3:** lazy, user-intent-preserving generation inside a general browser OS is a coherent and locally distinctive design; novelty relative to app generators/agent IDEs remains open.
- **Current usefulness 2:** a real prototype has desktop/runtime operations and a harness path, but no browser or live provider was run here. This recognizes a concrete prototype, not verified live generation (`vibeos/apps/server/src/runtime.ts:76-78,125-126`).
- **Expected usefulness 3:** the advantage is specific and credible: request a missing tool/surface without leaving the OS, then resume the triggering action. Durable quality, security, and recovery remain unproven (`vibeos/docs/vibeos-design.md:11-18`).
- **Implementation progress 3:** staged jobs carry scoped work orders/acceptance and structured results; validation/publication preserves data and rolls back on post-publish failure. Tests cover worker invocation/sandbox arguments, environment allowlisting, and staging boundaries (`vibeos/apps/server/src/generation-harness.ts:45-78,97-110,113-176`; `vibeos/apps/server/src/generation-harness.test.ts:33-78`). This is meaningful behavior/test design; the tests were not run and app quality was not observed.
- **Presentability 3:** README provides purpose, prerequisites, quickstart, architecture, and limits; screenshots are declared in docs. Configured Codex is a meaningful dependency, and the front door remains a developer quickstart rather than a demonstrated generated-app result (`vibeos/README.md:5-18,24-32`; `vibeos/docs/project-status.md:14-28`).

**Membership routes (OR).** Creativity: **provisionally supported locally; novelty unsearched**. Useful without merely repeating existing OSS: **plausible local use, but non-repetition unresolved**. Substantial work proving it is trying: **supported** by runtime/harness, validation/publication code, and focused tests. **Local view:** supported through substantive work, not a claim of production readiness.

**Strongest merit / why a high-quality impression could mislead.** The artifact is more than “AI can generate a page”: it has staging, acceptance, typed handoff, preserved user data, and transactional rollback. But local tests establish harness contracts, not reliable generated-app quality. Resource/network limits, cancellation/restart recovery UI, provenance/license handling, and accessibility gates are deferred and explicitly “not current security guarantees” (`vibeos/docs/generation-harness-plan.md:15-18`). The repo is closed as a milestone, not an active product commitment (`vibeos/docs/project-status.md:9-12`).

**Next decisive step.** Exercise one fresh local cache-miss with a real configured provider: generate a useful small app, verify its primary workflow, then force a failed candidate/recovery path. This tests the gap between harness seams and observable utility.

**Parent's strongest alternative-search question.** Which open-source local/browser environments generate missing routes from natural-language intent, preserve the initiating action, and validate/transactionally publish app-owned artifacts? Compare one end-to-end task with agent IDEs, code generators, and desktop shells rather than feature lists.

### `agentic-animation` — deterministic local story-to-animation toolkit

**Description and distinctive contribution.** An agent-operated pipeline maps a written story to a narrated 2D MP4 using generated still art where desired, but code-driven puppet/keyframe motion and Remotion rather than generative video. Story source, image generation, speech, lip-sync, music, and rendering are adapter-selected (`agentic-animation/README.md:3-10`). Its local distinction is a structured YAML-to-performance-IR pipeline with deterministic, constraint-checked puppet motion and reusable category assets. The motor declares physical invariants and fixed-timestep compile-time simulation (`agentic-animation/packages/core/src/motor/index.ts:1-17`); a swing test asserts full-turn behavior and rejects an unreachable grip (`agentic-animation/packages/core/test/hangingSwing.test.ts:1-75`).

**Scenario and intended audience.** A local creator/agent authors a structured episode and produces a narrated animation. The intended user wants repeatable, inspectable motion instead of an opaque video-generation result. The repo separates a closed, usable engine milestone from finished-film delivery: three demo episodes are recorded as validating, compiling, and rendering, but are not a stable API or finished-film release (`agentic-animation/README.md:12-16,29-45`; `agentic-animation/docs/STATUS.md:3-10`).

| Creativity | Current usefulness | Expected usefulness | Impl progress | Presentability |
|---:|---:|---:|---:|---:|
| 3 | 3 | 3 | 3 | 3 |

- **Creativity 3:** deterministic code-controlled motion, swappable media adapters, and physical puppet constraints form a distinct local combination. Public alternatives have not been checked; novelty is not settled.
- **Current usefulness 3:** a coherent workflow has three recorded end-to-end demos and canonical YAML check/make/preview/render commands. This rests on committed records/examples, not a fresh run or inspection of linked films (`agentic-animation/README.md:18-45,106-124`; `agentic-animation/docs/STATUS.md:3-10`).
- **Expected usefulness 3:** authors can iterate on timing, assets, and motion without a video model owning motion; CLI and adapter contracts support the use case. Breadth is not established because new-situation work remains incomplete (`agentic-animation/README.md:3-10`; `agentic-animation/docs/ART_ASSET_PROGRAM.md:11-20`).
- **Implementation progress 3:** motor/compiler contracts and focused physical-motion tests exist; committed status records earlier engine/art milestones and reviews (`agentic-animation/packages/core/src/motor/index.ts:1-17`; `agentic-animation/packages/core/test/hangingSwing.test.ts:13-75`; `agentic-animation/docs/STATUS.md:31-75`). Not 4: current generalization work has open slices and full-film rendering is future work (`agentic-animation/README.md:121-124`; `agentic-animation/docs/ART_ASSET_PROGRAM.md:231-240`).
- **Presentability 3:** README explains workflow, prerequisites, limitations, and embeds three linked episode previews. The films were not viewed; their presence is evidence of a strong project surface, not independent visual-quality judgement (`agentic-animation/README.md:18-45,106-127`).

**Membership routes (OR).** Creativity: **provisionally supported locally; novelty unsearched**. Useful without merely repeating existing OSS: **concrete task utility, but distinctiveness against existing toolchains unresolved**. Substantial work proving it is trying: **supported** by engine, focused tests, authored examples, and recorded milestones. **Local view:** supported through substantive work, not a claim the episodes are finished films.

**Strongest merit / why a high-quality impression could mislead.** It has more than plans: a plausible vertical slice and recorded positive evidence. Yet current docs distinguish the closed engine milestone from active art/generalization work. Slice A still needs projectile contact and a following camera; Slice B's swing works in controlled proof but the target shot does not yet bake; Slice C has not started (`agentic-animation/docs/STATUS.md:138-175`; `agentic-animation/docs/ART_ASSET_PROGRAM.md:190-240`). These are project-record claims, not independently reproduced visual QA.

**Next decisive step.** Finish one new Slice A episode through projectile contact, following camera, YAML check/make/render, and normal-size visual review. This tests generalization beyond existing demos before more slices (`agentic-animation/docs/ART_ASSET_PROGRAM.md:13-15,65-75,231-240`).

**Parent's strongest alternative-search question.** Which open-source pipelines turn structured story into narrated, repeatable 2D puppet animation using authored/keyframed motion and replaceable image/TTS/lip-sync/render adapters? Compare editability, determinism, and a real short output with animation editors and generative-video systems.

### `pathlm` — research map and experimental workbench for LM compute paths

**Description and distinctive contribution.** A Chinese-first, machine-checkable map of language-model compute-path research: each item has purpose, prior-art baseline, method, criteria, falsification, work packages, state, result, and gaps; shared methodology stresses uncertainty, matched controls, cost units, and negative findings (`pathlm/README.md:1-30`; `pathlm/docs/research-schema.md:1-82`; `pathlm/docs/methodology.md:1-38`). Strongest local merit is a repeatable research/evidence discipline and readable failure ledger, not a claim that its research mechanisms are new (`pathlm/README.md:12-26`; `pathlm/docs/playbook.md:1-7`).

**Scenario and intended audience.** A researcher investigating architecture/training/inference choices uses the map to choose one falsifiable question, compare to stock/SOTA, and retain reproducible evidence. The README names Chinese readers as its audience. This is a local work copy, not pushed public work; experiment weights are not committed (`pathlm/README.md:49-61`).

| Creativity | Current usefulness | Expected usefulness | Impl progress | Presentability |
|---:|---:|---:|---:|---:|
| 2 | 3 | 3 | 3 | 2 |

- **Creativity 2:** the research-tree/evidence-ledger format is locally distinctive, but mechanisms are established research topics and no external search was done. No originality claim is established; this is not a penalty for repository size.
- **Current usefulness 3:** tracked model/training source, shared measurement rules, and committed experiment records exist. The 2613 record describes a same-configuration four-arm comparison: dense aggregation is unrankable at Δbpc −0.0008 under the 0.014 band, while parallel variants are worse (`pathlm/axes/2-depth/2.2.3-learned-layer-sum/experiments/2613-inter-layer-topology-13m/analysis.md:24-51,53-74`). This is useful bounded evidence, not a universal result.
- **Expected usefulness 3:** target user/problem and a path to useful evidence are clear. Payoff depends on filling the research tree and maintaining comparable results; README says many cells remain blank (`pathlm/README.md:3-6,12-18`).
- **Implementation progress 3:** tracked model code exists (`pathlm/pathlm/model.py:1-17`; `pathlm/pathlm/depth_ar.py:1-20`), as do a measured-result project and committed analysis (`pathlm/axes/2-depth/2.2.3-learned-layer-sum/project.yaml:16-30`; `pathlm/axes/2-depth/2.2.3-learned-layer-sum/experiments/2613-inter-layer-topology-13m/analysis.md:24-51`). A separate attention implementation has explicit causal aggregation/equivalence gates (`pathlm/axes/2-depth/2.2.2-attention-residual/experiments/2653-interlayer-attn-13m/interlayer_attn.py:1-100`), but its project says training arms and paired Δbpc remain unmeasured (`pathlm/axes/2-depth/2.2.2-attention-residual/project.yaml:17-28`). Dirty logs were not counted as completion.
- **Presentability 2:** README offers strong research orientation and navigation but no one-command environment setup; it says checkout is local/unpushed, and a stranger must infer the research environment beyond the summary command (`pathlm/README.md:28-56`). Chinese-first presentation is appropriate for the declared audience, not a defect.

**Membership routes (OR).** Creativity: **not established as an originality claim from local evidence alone**; public comparison can change this. Useful without merely repeating existing OSS: **not established pending comparison with research catalogs/frameworks and mechanism prior art**. Substantial work proving it is trying: **supported** by tracked model code and committed controlled results, including negative findings and limits—not by the number of project YAML files. **Local view:** supported through substantive work; current live status remains unknown.

**Strongest merit / why a high-quality impression could mislead.** The 2613 record is a useful example of reporting a negative result with an activity check, controls, and scope limits. But a “complete research tree” is a map, not complete experimental coverage; many cells are blank. The 2.2.3 result is one seed/scale and leaves higher-scale/seed checks open. The newer 2.2.2 idea has implementation and pre-registered gates but no training verdict. README states the checkout has not been pushed (`pathlm/README.md:3-6,54-56`; `pathlm/axes/2-depth/2.2.3-learned-layer-sum/project.yaml:17-30`; `pathlm/axes/2-depth/2.2.2-attention-residual/project.yaml:17-28`). The dirty live files are deliberately uninterpreted.

**Next decisive step.** Let existing 2653/2651 work reach its own safe completion without interruption; then compare only committed per-arm records with pre-registered criteria and update the owning project record. Do not infer a favorable result from changing logs. The attention question is whether causal aggregation beats stock and cheaper linear aggregation, not whether code exists (`pathlm/axes/2-depth/2.2.2-attention-residual/project.yaml:37-55`).

**Parent's strongest alternative-search question.** Which public research databases, architecture-taxonomy projects, or experiment frameworks already cover LM compute-path design and preserve controlled comparisons/negative results? For 2.2.2/2.2.3, what published baselines or prior art overlap the mechanisms rather than only the wiki format?

## Cross-project membership and calibration summary

| Project | Creativity route | Useful-without-merely-repeating route | Substantial-work route | Provisional local membership view |
|---|---|---|---|---|
| `dojo` | Plausible locally; novelty unsearched | Not established pending alternatives | Supported by claim lifecycle + tests | Provisionally supported via substantial work |
| `vibeos` | Plausible locally; novelty unsearched | Plausible use, non-repetition unresolved | Supported by runtime/harness and contract tests | Provisionally supported via substantial work |
| `agentic-animation` | Plausible locally; novelty unsearched | Concrete use, non-repetition unresolved | Supported by engine/tests/recorded milestones | Provisionally supported via substantial work |
| `pathlm` | Originality not established locally | Not established pending alternatives | Supported by tracked source + committed results | Provisionally supported via substantial work |

These four are not automatically accepted because the user selected them. Their merits and gaps differ: `dojo` has a careful epistemic model but a product/implementation gap; `vibeos` has a concrete generation boundary but no observed live generation; `agentic-animation` has the clearest recorded end-to-end utility but incomplete generalization slices and unreviewed media; `pathlm` has the strongest research ledger but narrow result evidence and dirty live outputs. The user's high-quality judgement remains user-attributed, not the investigator verdict.

## Evidence index

- `docs/plan/catalogue.md:15-23` — scope, local-only authority, parent/public-comparison split, acceptance.
- `docs/product/catalogue.md:3-13` — OR criterion, independent dimensions, no automatic removal.
- `docs/result/catalogue-pilot.md:23-36` — pilot anchors and unknown-vs-zero calibration.
- `dojo/README.md:1-27,29-51,53-79`; `dojo/docs/product.md:3-28,43-59`; `dojo/docs/current-demo-direction.md:37-48` — current implementation, product boundary and evaluation limits.
- `dojo/dojo/demo.py:1-8,31-42`; `dojo/dojo/storage.py:599-647`; `dojo/tests/test_conversation.py:124-193` — story, retrieval, and inspected mocked-conversation behavior.
- `vibeos/README.md:5-18,20-32`; `vibeos/docs/project-status.md:3-28`; `vibeos/docs/generation-harness-plan.md:3-22`; `vibeos/docs/vibeos-design.md:5-26` — project purpose, status, architecture and deferred hardening.
- `vibeos/apps/server/src/runtime.ts:76-78,125-126`; `vibeos/apps/server/src/generation-harness.ts:45-78,97-110,113-176`; `vibeos/apps/server/src/generation-harness.test.ts:27-78` — cache-miss flow, staged worker, validation/publication, and inspected tests.
- `agentic-animation/README.md:3-45,106-127`; `agentic-animation/docs/STATUS.md:3-10,12-75,138-175`; `agentic-animation/docs/ART_ASSET_PROGRAM.md:1-20,36-50,90-119,190-240` — workflow, recorded status, new scenarios, blockers.
- `agentic-animation/packages/core/src/motor/index.ts:1-17,20-65`; `agentic-animation/packages/core/test/hangingSwing.test.ts:1-75`; `agentic-animation/packages/cli/src/commands/yamlPipeline.ts:1-50` — motor, representative test and pipeline implementation.
- `pathlm/README.md:1-61`; `pathlm/docs/structure.md:1-45`; `pathlm/docs/research-schema.md:1-82`; `pathlm/docs/methodology.md:1-38`; `pathlm/docs/playbook.md:1-45` — research map and evidence discipline.
- `pathlm/pathlm/model.py:1-17`; `pathlm/pathlm/depth_ar.py:1-20`; `pathlm/axes/2-depth/2.2.2-attention-residual/project.yaml:7-29,37-55`; `pathlm/axes/2-depth/2.2.2-attention-residual/experiments/2653-interlayer-attn-13m/README.md:1-110`; `pathlm/axes/2-depth/2.2.2-attention-residual/experiments/2653-interlayer-attn-13m/interlayer_attn.py:1-100` — tracked model/project and inspected attention code, not dirty outputs.
- `pathlm/axes/2-depth/2.2.3-learned-layer-sum/project.yaml:7-31`; `pathlm/axes/2-depth/2.2.3-learned-layer-sum/experiments/2613-inter-layer-topology-13m/analysis.md:1-80`; `pathlm/axes/2-depth/2.2.3-learned-layer-sum/experiments/2613-inter-layer-topology-13m/results.json:1-100` — committed result and scope limits; not re-executed.

## Completion and residual risks

Completed: four revision-bound local scorecards with all five dimensions, evidence of substantive work, all three membership routes, descriptions/scenarios/audiences, strongest merits and misleading impressions, decisive next steps, and parent-directed alternative questions. Public comparison remains deliberately outstanding for the parent.

Residual risks: scores are provisional; no public alternatives were searched, so originality and non-duplication remain unresolved. No tests were run, and no install/build/runtime/model generation/render occurred. Linked agentic-animation films were not viewed. `pathlm`'s four changing dirty files and current experiment state remain unknown and untouched. Documentation/results are inspected evidence, not independent reproduction; those limits do not turn unknown into zero.
