# Catalogue pilot: hfget, Suzhou Drive, causalmlp

Observation: 2026-10-19 (local checkout clock, 09:42 +08:00). This is a read-only investigation of the three scoped child repositories, bound to the parent pin and child HEADs below. Scores and editorial routes are provisional proposals, not removal decisions or full-collection results.

## Contract, scope, and evidence limits

The plan calls for revision-bound scorecards, membership-route judgements, evidence of substantive work beyond progress/volume, and bounded public-alternative comparison; it forbids execution, installs, edits to children, and any project change except this report (`docs/plan/catalogue.md:5-14`). The product document states the user's OR criterion, separates membership from prominence, and calls for five independent anchored 0–4 dimensions with unknown distinct from zero (`docs/product/catalogue.md:3-10`). No README, submodule, project, or plan/product file was changed.

The available session tools did not expose `web_search_ds` or `web_fetch_ds`. I made zero external searches (of the six permitted) and fetched no public pages. The alternative references below are public pointers from general domain knowledge, not live-checked evidence; they support only a preliminary comparison and do not support a novelty or duplication verdict. Public comparison acceptance is therefore incomplete. No private repository contents were searched, fetched, or included in queries.

No child code was executed; no tests, build, installation, or network request was run. The findings distinguish inspected source and committed evidence from documentation claims and run-time behavior. The drive README points to a `.scratch` verification record; I did not inspect that record, so its historical unit/build/E2E totals and visual checks remain claims in the README, not independently audited observations. No project behavior is represented as freshly verified.

## Revision and state binding

| Repository | Parent pin at `dce402d01914c3ea6c92b43e61faca693120f670` | Child HEAD | Dirty state observed |
|---|---|---|---|
| `hfget` | `3b4bc96a465a166bc20d8773c1bb233d0a87d5df` | `3b4bc96a465a166bc20d8773c1bb233d0a87d5df` | clean (`git status --porcelain` empty) |
| `drive` | `6f803b4ca0f274f2118de0fc6aa484a5be5c5708` | `6f803b4ca0f274f2118de0fc6aa484a5be5c5708` | clean |
| `causalmlp` | `e4046d7b3b158911e5e59a38a26390d7917c955b` | `e4046d7b3b158911e5e59a38a26390d7917c955b` | clean |

The parent checkout is on `main` at the hash above. Its pre-existing dirty state is only `m pathlm`; that submodule is excluded and was not inspected or touched. The parent README presents the collection as independent repositories pinned without flattening history and links Suzhou Drive as an OSM-backed browser simulator (`README.md:12-20,23-32`); `.gitmodules` identifies the three public child slugs (`.gitmodules:10-12,70-72,124-126`).

## Proposed scoring anchors

These anchors are a pilot calibration because the product document requests anchored scales but does not yet define the anchors. Apply evidence to each dimension separately; do not total or average the dimensions.

| Score | Shared reading |
|---|---|
| 0 | No evidence for the dimension, or directly contradicted. |
| 1 | Weak, narrow, or mostly asserted evidence; a plausible idea or highly specific convenience. |
| 2 | Concrete local value or a credible prototype, with meaningful limits or unverified claims. |
| 3 | Coherent, substantial milestone with behavior/evidence across the stated scope; important gaps remain visible. |
| 4 | Mature, independently validated outcome with compelling evidence for its stated audience and scope. |
| Unknown | Evidence is insufficient to place the dimension; this is not a zero. |

Dimension-specific calibration: creativity scores the observed distinctiveness of the idea/mechanism, not proven patent-level novelty; current usefulness is demonstrated present use or practical value, not stated potential; expected usefulness requires a named user/problem and credible path; implementation progress rates behavior/experiment completeness, not code volume; presentability rates whether a new user can understand, try, and evaluate it from the project surface. Lack of external search limits novelty assessments. Lack of execution limits usability claims.

## Scorecards

### hfget — personal Hugging Face GGUF selector/downloader

**Description.** A small Python utility searches Hugging Face model repositories, filters by pipeline/parameter criteria, ranks GGUF files by configurable quantization preferences, identifies shards and companion files, then downloads selected files. The README and status document label it a closed personal milestone and disclose that search/preferences are constants in the script (`hfget/README.md:3-21`; `hfget/docs/project-status.md:3-26`).

**Distinctive contribution observed.** Opinionated GGUF selection in one workflow: ranked main-model candidates plus MTP/DSpark2/mmproj sidecars, shard grouping, retry handling, a dry-run listing, and user confirmation before download (`hfget/hfget.py:39-54,56-115,126-145,152-205,247-285`). This is a tailored convenience, not evidence of a novel downloader. Heuristics are visible in code but have no test suite or CI, as the project status explicitly confirms (`hfget/docs/project-status.md:22-26`).

**Scores (0–4, proposed).**

| Creativity | Current usefulness | Expected usefulness | Impl progress | Presentability |
|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 2 | 2 |

- Creativity 1: custom ranking and sidecar selection are more tailored than a bare transfer call, but appear as narrow workflow glue. External novelty is unknown.
- Current usefulness 2: source shows an end-to-end search/select/download path and explicit large-file caution; runtime and current Hugging Face compatibility were not exercised.
- Expected usefulness 2: there is a specific recurring scenario (choosing preferred quantizations and companions), but settings are in-file and no broader caller or demand evidence is recorded.
- Implementation progress 2: real selection, shard, retry, dry-run, and download paths exist; no tests, CI, packaging, or independently verified run (`hfget/hfget.py:56-145,247-285`; `hfget/docs/project-status.md:24-26`).
- Presentability 2: the README gives requirements, a command, configuration location, and disk/network warning, but not a sample selection result, install recipe, test evidence, or detailed CLI documentation (`hfget/README.md:9-21`).

**Membership routes.** Creativity: weakly indicated, not established as a decisive differentiator. Useful/can be useful without merely repeating existing OSS: not established by this pilot; the script plausibly helps its owner, but its overlap with the official Hub download interface was not live-compared. Substantial work proving it is trying: not established to the proposed threshold. The actual selector is more than a one-line example, but only one small script and no experiment/test evidence were found; code size alone does not make it substantial. Overall: **membership not established on this evidence; retain as a low-prominence candidate pending comparison, not an automatic remove.**

**Provisional editorial verdict: incubate / low prominence.** Next decisive step: compare the same model-selection task and dry-run output against the official Hub CLI/API on a small safe fixture; then decide whether the custom ranking removes enough user work to warrant retention. Do not download large artifacts as part of that check without deliberate safeguards.

### drive — Suzhou offline browser driving simulator

**Description.** A local Three.js/Vite app renders a checked-in Suzhou OSM extract and combines player driving, lane-aware navigation, traffic, weather, collisions, water hazards, and procedural roadside dressing. It is version 0.1.0 and explicitly closed after a milestone (`drive/README.md:5-12,30-40`). The status document says the existing origin has no URL and no public release artifact is claimed (`drive/docs/project-status.md:5-15`; `drive/README.md:38-40`).

**Distinctive contribution observed.** A compact offline city-data driving experience rather than a generic map viewer: the navigation module creates lane markings from OSM metadata, checks turn-lane/change-lane constraints, builds connected routes with maneuver guidance, and detects wrong-way travel (`drive/src/navigation.ts:3-45,106-167,185-205,259-270`). The simulation code and tests also cover deterministic traffic stepping and collision behavior (`drive/src/sim.ts:1-22,31-84,95-115`; `drive/src/sim.test.ts:4-21`). This is a coherent local integration; external distinctiveness versus public simulators remains unsearched.

**Scores (0–4, proposed).**

| Creativity | Current usefulness | Expected usefulness | Impl progress | Presentability |
|---:|---:|---:|---:|---:|
| 2 | 2 | 2 | 3 | 2 |

- Creativity 2: data-driven local driving plus lane-level OSM-derived guidance is a specific combination; uniqueness is not established without public comparison.
- Current usefulness 2: a bounded offline simulator with concrete driving/navigation/weather use is described and supported by substantial source; it was not run here, so actual usability is unverified.
- Expected usefulness 2: a clear demo/learning use exists, but coverage is one city extract and the project is closed; the status leaves named-place testing and target-hardware measurement undone (`drive/README.md:34-40`; `drive/docs/project-status.md:25-29`).
- Implementation progress 3: code covers a broad behavior-complete slice and tests express route, lane, collision, traffic, and weather-related invariants (`drive/src/navigation.test.ts:8-63`; `drive/src/sim.test.ts:4-21`). README reports 40 unit tests, a successful build, and 25/26 E2E pass with one fixture skip, but that prior record was not independently run or inspected (`drive/README.md:26-32`).
- Presentability 2: bilingual README, prerequisites, test/build/run commands, local-map explanation, scope limits, license, and release-status disclosure are present; no public release artifact or in-README screenshot/demo is claimed (`drive/README.md:13-28,34-52`). The separate OSM data attribution/license condition remains relevant before redistribution (`drive/README.md:50-52`).

**Membership routes.** Creativity: plausible but not externally established. Useful/can be useful without merely repeating existing OSS: plausible local demo value; whether it is sufficiently differentiated is unknown. Substantial work proving it is trying: **yes, provisionally**. Evidence is not file/commit count: a separated simulation/navigation implementation has caller-visible route and lane behaviors with corresponding focused tests, and the recorded milestone spans unit/build/E2E and visual checks (`drive/src/navigation.ts:106-167,185-205`; `drive/src/navigation.test.ts:8-63`; `drive/README.md:26-32`). The tests and claimed run record were inspected, not executed here. Overall: **membership supported by the substantial-work route; usefulness/novelty routes remain provisional.**

**Provisional editorial verdict: showcase candidate, conditional on a fresh quickstart and visual check.** Next decisive step: verify the documented `npm ci`, unit test, build, and local app startup on the pinned revision, then inspect one route in the checked-in OSM extract and verify the data-rights attribution before any public showcase. No performance claim should be made without the deferred target-hardware measurement.

### causalmlp — causal hidden-unit prefix MLP experiment

**Description.** A PyTorch research experiment asks whether one shared MLP can produce predictions at every hidden-unit prefix and improve quality as more units contribute. The implemented `CausalHiddenMLP` applies a shared linear output transform to hidden activations, cumulative-sums the per-unit logits, divides by prefix length, and emits `[batch, hidden, classes]` (`causalmlp/README.md:1-25`; `causalmlp/causal_mlp.py:16-69`). The project calls itself a synthetic-data research scratchpad, has no tests/CI/package, and is kept as an archive (`causalmlp/README.md:24-50`; `causalmlp/docs/project-status.md:3-22`).

**Distinctive contribution observed.** The investigated mechanism is cumulative-mean logits from one output layer, producing a prediction for each hidden-unit prefix. The report records the negative/partial result that mean-vs-sum changes the function, the run is not strictly monotonic, and the causal model needs additional width in its reported teacher comparison (`causalmlp/report.md:24-46,67-85,155-200`). This resembles the broader early-exit family; exact novelty is unknown without literature/repository searches.

**Scores (0–4, proposed).**

| Creativity | Current usefulness | Expected usefulness | Impl progress | Presentability |
|---:|---:|---:|---:|---:|
| 2 | 1 | 1 | 2 | 2 |

- Creativity 2: a concrete prefix/cumulative-mean mechanism and documented negative findings are distinctive within this artifact; prior art has not been checked, so novelty remains unknown.
- Current usefulness 1: useful as a research artifact/hypothesis, not yet as a demonstrated efficient early-exit model. `forward` computes all hidden activations and all exits in one call (`causalmlp/causal_mlp.py:51-69`); no saved-compute or deployment benefit is demonstrated.
- Expected usefulness 1: the question is clear, but the report leaves real-data validation and adaptive-inference savings open (`causalmlp/report.md:182-200`), and current code does not measure incremental/early-stop compute.
- Implementation progress 2: there is a model, synthetic train/test generator, comparison code for widths 32/64/128/256, a research report, and an actual-looking `results.json` with a non-monotonic result (`causalmlp/train.py:25-47`; `causalmlp/experiment.py:25-59`; `causalmlp/results.json:1-40`). These artifacts show meaningful experimental work but not reproducibility or real-data validation.
- Presentability 2: README explains question, results, limitations, commands, and archival status; no tests/CI or packaging is present (`causalmlp/README.md:8-46`).

**Material evidence issue.** The stored `results.json` shows causal max `0.7547` versus regular `0.889` and a `0.1343` gap, which the README calls accuracy (`causalmlp/results.json:32-39`; `causalmlp/README.md:20-25`). But `train.py` calls `causal_accuracy` for the causal outputs (`causalmlp/train.py:84-104`), and that helper defines the metric as mean `exp(-cross_entropy)` (`causalmlp/causal_mlp.py:164-183`); the regular path uses top-1 `argmax` accuracy (`causalmlp/train.py:131-152`). Therefore the direct causal-vs-regular gap from that pipeline is not an apples-to-apples accuracy comparison unless `results.json` came from another, undocumented producer. A separate helper computes classification accuracy, but this evaluation path does not call it (`causalmlp/causal_mlp.py:186-199`). Also, `results.json` contains no seed/configuration/revision metadata to bind it to a run. This is a static source-level finding, not a claim that the experiment was run during this investigation.

**Membership routes.** Creativity: plausible but originality unknown. Useful/can be useful without merely repeating existing OSS: not established; it does not currently demonstrate compute reduction and is synthetic-only. Substantial work proving it is trying: **yes, provisionally**. The model mechanism, nontrivial width sweep, train/test experiment code, comparative report, and saved non-monotonic result are meaningful implementation/experiment/result evidence rather than just progress or volume. The metric mismatch weakens particular headline conclusions but does not erase evidence of an actual research attempt. Overall: **membership supported provisionally by the substantial-work route; not by demonstrated utility or proven novelty.**

**Provisional editorial verdict: incubate as a research archive; repair evidence before featuring claims.** Next decisive step: fix evaluation to compare top-1 accuracy on the same held-out examples, make the JSON include the exact configuration/seed/model revision and metric names, rerun the documented CPU experiment, then decide if any speed/early-exit hypothesis merits real-data evaluation. Do not present the existing 0.134 gap as a valid accuracy comparison until then.

## Preliminary public-alternative comparison (not live-verified)

These are bounded reference points, not an exhaustive search or proof of duplication. Links are public source pointers supplied for the parent to verify; no page was fetched on this run.

| Candidate reference | Comparison with scoped project | What this pilot can and cannot conclude |
|---|---|---|
| Hugging Face Hub CLI/API: [CLI guide](https://huggingface.co/docs/huggingface_hub/guides/cli), [file download API](https://huggingface.co/docs/huggingface_hub/package_reference/file_download) | Same model-host ecosystem and direct file-download capability. hfget adds opinionated repository discovery, quantization ranking, shard/companion selection, and confirmation flow. | Strong overlap at the download layer; no live feature/maintenance comparison. A task-level side-by-side is the decisive check for whether its custom selection saves enough effort. |
| CARLA: [repository](https://github.com/carla-simulator/carla) | Public open-source driving simulator in the broad category. Suzhou Drive is a small browser app over one offline OSM extract with a different scope/weight. | Establishes a broad category comparator, not direct duplication. No current feature or install comparison was performed. |
| Eclipse SUMO: [repository](https://github.com/eclipse-sumo/sumo) | Public road-network/traffic simulation reference adjacent to Suzhou Drive's traffic and road model; it is not the same player-facing browser driving slice. | Useful to test whether the distinctive story is the local interactive driving experience, rather than traffic simulation alone. No live comparison performed. |
| BranchyNet: [paper](https://arxiv.org/abs/1709.01686) | Public early-exit neural-network reference. The scoped code instead emits exits at hidden-unit prefixes using cumulative-mean logits; the inspected implementation computes all prefixes at once. | Shows the general early-exit problem family is established, not that this exact prefix mechanism is duplicate or novel. No paper/code retrieval or novelty search performed. |

## Rubric ambiguities for parent calibration

1. **Creativity versus prior art:** whether a mechanism need be novel relative to all OSS, the relevant category, or only the user's collection; without a stated search boundary, scores can imply unsupported novelty.
2. **“Useful/can be useful without merely repeating an existing OSS project”:** what counts as “merely repeating” when an existing tool overlaps the core capability but the project adds a personal workflow, local data, or different deployment surface.
3. **Expected usefulness:** whether this means a credible forecast for a named user or any plausible future application; archive status, feature roadmap, and hypothetical future use need different evidential weight.
4. **Substantial work:** the current interpretation requires behavior/experiment evidence, not size or progress. It still needs a calibrated threshold for a small utility versus research work, and how invalid or incomparable reported metrics affect the route.
5. **Progress versus usefulness/presentability:** a large tested milestone may score high on progress but lower on current use, release readiness, or showcase quality. Keep dimensions independent as the contract says.
6. **Scale anchors and confidence:** no current anchor definitions or confidence field are authored. The anchors above are proposed only; whether to score low evidence as 1 or `unknown` should be settled before applying them across the collection.

## Acceptance and residual risks

**Completed:** all three scorecards are tied to parent/child revisions; descriptions, contribution, five separate proposed scores, limits, membership OR routes, editorial verdicts, next steps, and rubric ambiguities are recorded. Source and documentation were inspected selectively; no code was executed.

**Incomplete:** public-alternative research could not be conducted because web search/fetch tools were unavailable. No claims of originality or direct duplication are settled. Drive's historic verification record was not inspected or rerun. hfget was not tested against the current Hub service. causalmlp's run is not reproducibly bound to JSON, and the apparent comparison metric mismatch must be corrected. These limits do not authorize removals; the product contract requires separately approved removal while preserving work (`docs/product/catalogue.md:11-13`).

**Residual risks:** score anchors remain proposed; one-off source inspection cannot establish current runtime compatibility; public alternatives are not current-verified; the drive OSM extract has a separate attribution/license condition; causalmlp's headline comparison is unreliable until its metric provenance is resolved. No single average is given and no automatic removal is recommended.
