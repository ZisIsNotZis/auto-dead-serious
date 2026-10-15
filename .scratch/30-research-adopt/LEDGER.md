# Migration ledger — `/home/z/hf/research`

Adoption ledger per `change.upkeep.adopt` and `change.upkeep.lossless`. One row per source file, and per claim where a file holds several. Every fact gets exactly one outcome: **lands** / **retired** / **unplaceable** (`change.upkeep.lossless`). Two flags are marked where they apply: **DUP** (same fact already in another source file) and **DER** (a derivable value stored rather than generated, where the store or a script already owns it).

Read-only pass. No file under `/home/z/hf/research` was written, moved or deleted.

## Target model this ledger maps onto

Policy chain (`change.shape.chain`), highest priority first: **pain → need → product → architecture → method → plan → result → code**. Layout (`change.shape.layout`): one folder per layer under `docs/`, one file inside a layer when that layer is cut by a key every fact in it has exactly one value of; the layer file is a YAML mapping from fact id to fact (`change.shape.file_shape`) and is a **store** (`change.shape.file_kind`).

Target homes used below:

| Layer | Target file | Cut by |
|---|---|---|
| pain | `docs/pain/pain.yaml` | sufferer |
| need | `docs/need/need.yaml` | — |
| product | `docs/product/product.yaml` | artefact / quality bar / non-goal |
| architecture | `docs/architecture/database.yaml` | module / boundary |
| method | `docs/method/method.yaml`, `docs/method/naming.yaml`, `docs/method/operations.yaml` | topic |
| plan | `docs/plan/plan.yaml` | work package |
| result | `docs/result/result.yaml` (measured), `docs/result/analysis.yaml` (inferred) | status |
| code | the script itself (`docs/code/` is a router to it) | file |
| router | `docs/README.md` | — (holds no fact of its own) |
| work record | `.scratch/<effort>/` (`change.work_record`) | ticket |

Outcome column is exactly `lands`, `retired`, or `unplaceable`. Flags column is `DUP`, `DER`, `DUP,DER`, or `—`.

---

## `AGENTS.md` (root)

| id | claim / fact | outcome | target | flags |
|---|---|---|---|---|
| R01 | Data trust order: trust non-`_analysis` json/jsonl first, then txt, `_analysis` last | lands | method/operations.yaml | — |
| R02 | Numbered `experiments.sqlite.bakN` backup before any DB mutation | lands | method/operations.yaml | DUP |
| R03 | Post-mutation DB cleanliness checks (integrity, nulls, boolean/range) | lands | architecture/database.yaml | DUP |
| R04 | No blind grid/random search; weakest-point-first targeted experiments | lands | method/method.yaml | DUP |
| R05 | Keep GPU occupied with highest-value run; don't stop before questions clear | lands | method/method.yaml | DUP |
| R06 | Don't modify upstream projects unless absolutely required | lands | method/method.yaml | DUP |
| R07 | Prefer passing sampling params to llama-server over patching code | lands | method/operations.yaml | DUP |
| R08 | Run evals in background; avoid foreground waits that stall | lands | method/operations.yaml | DUP |
| R09 | "Documentation SSOT `docs/`; data SSOT `experiments.sqlite`; `report.html` generated, never hand-edited" | lands | method/conventions + product/report.yaml | DUP |
| R10 | The file as a whole is the project agent-rules set | lands | render of `AGENTS.yaml` (`change.upkeep.render`) | — |

## `docs/README.md`

| id | claim / fact | outcome | target | flags |
|---|---|---|---|---|
| R11 | Project positioning: study how local-model settings change benchmark scores; quantisation is one sub-item | lands | product/product.yaml | DUP |
| R12 | SSOT assignment table (each fact → one home) | lands | router `docs/README.md` | DUP |
| R13 | Consistency rule: one fact, one file; resolve conflict at the home first | lands | method/conventions | DUP |
| R14 | Layer map L0/L1/L2/L3 + planning + index | lands | router + method/conventions | DUP |
| R15 | Directory table of `docs/` | lands | router | DUP |
| R16 | Current scale: ~3300 rows, 208 model files, 59 protocols | lands | result/result.yaml as a **citation** (query), not prose | DER |
| R17 | Reproduce commands (`make_report.py`, `mktables.py`, `migrate_db.py`, `check_consistency.py`) | lands | method/operations.yaml (resolvable commands) | — |
| R18 | `report.html` is a derived view: numbers from DB only, wording from docs, no new claims | lands | architecture (render contract) | DUP |
| R19 | Licence MIT | lands | product metadata → `LICENSE` (authored) | — |
| R20 | `check_consistency.py` named as a gate but absent from the tree | unplaceable | finding (resolvable-reference failure, `change.upkeep.resolvable`) | — |

## `docs/L0-要求.md`

| id | claim / fact | outcome | target | flags |
|---|---|---|---|---|
| R21 | Research object = effect of settings/hyperparameters on benchmark scores; quant is one sub-item; one study per setting (X/Y/series) | lands | product/product.yaml | DUP |
| R22 | Control-variable principle: exactly one variable per study, everything else fixed identical | lands | method/method.yaml | — |
| R23 | Quant width study: variable = bpw, therefore provider and scheme must be held identical | lands | method/method.yaml | — |
| R24 | Forbid nominal `Q2/Q3/Q4/Q5` labels as quant description; use effective bpw only | lands | method/naming.yaml | DUP |
| R25 | Report structure: 总—分—总 | lands | product/report.yaml | DUP |
| R26 | Each section: raw data table → its figure → analysis; raw data must have both table and figure | lands | product/report.yaml | DUP |
| R27 | Conclusions may add summary/charts but never replace the underlying data/figure | lands | product/report.yaml | DUP |
| R28 | Prose in Chinese; professional readable tables; paper-like layout | lands | product/report.yaml | DUP |
| R29 | Docs must be layered by source L0/L1/L2/L3; layers not mixed | lands | method/conventions | DUP |
| R30 | SSOT: measured numbers only in `experiments.sqlite`; prose knowledge only in `docs/`; report derived | lands | method/conventions | DUP |
| R31 | "待补" (to-be-filled) meta note about future user conclusions | retired | scaffolding, no fact (`change.upkeep.outdated`) | — |

## `docs/REPORTING.md`

| id | claim / fact | outcome | target | flags |
|---|---|---|---|---|
| R32 | The only report = generated `report.html`; forbid hand-editing, markdown-as-data, and same-data second formats | lands | product/report.yaml + architecture render contract | DUP |
| R33 | Table shape: one variable per table; col1 = fixed series, col2 = varied X, rest = one column per benchmark | lands | product/report.yaml | DUP |
| R34 | Columns never filtered; row filter = drop empty rows and single-value groups only | lands | product/report.yaml | DUP |
| R35 | Cell = `score (n)`; missing = `—`/`无结果`, never 0 | lands | product/report.yaml | DUP |
| R36 | Report structure 总—分—总 + closing significance recap table (significant / not significant / untested) | lands | product/report.yaml | DUP |
| R37 | Language/naming: Chinese human prose, quant word must appear, benchmark column names in Chinese | lands | product/report.yaml | DUP |
| R38 | Significance encoding: red = 95% CI does not cross 0 | lands | product/report.yaml | — |
| R39 | Figures: one per study, drawn from DB by `make_report.py` into `figures/report/`; CJK font; full-width | lands | product/report.yaml (`producer:` make_report.py) | — |
| R40 | Recompute convention: `SE=√(p(1−p)/n)`, `SE_diff=√(SE₁²+SE₂²)`, 95% CI = diff ± 1.96·SE_diff | lands | method/method.yaml | DUP |
| R41 | `无结果`/`BLOCKED`/`GATE-FAIL` are explicit non-measurements, not 0 | lands | method/naming.yaml | DUP |

## `docs/NAMING.md`

| id | claim / fact | outcome | target | flags |
|---|---|---|---|---|
| R42 | effective bpw = `8 × GGUF bytes ÷ params`; source `bpw_map.json`; producer `gguf_params.py` | lands | method/naming.yaml | DUP,DER |
| R43 | Never use nominal labels as the quant axis (they span 2.76–5.04 bpw) | lands | method/naming.yaml | DUP |
| R44 | Model file naming `family-version[-type]-<quant suffix>.gguf`; family = same base weights | lands | method/naming.yaml | — |
| R45 | Quant suffix examples (UD-Q2_K_XL, UD-IQ3_XXS, UD-TQ1_0, Q2_0_g64, Q1_0) | lands | method/naming.yaml | — |
| R46 | MoE family name carries `A<activation>` (e.g. Qwen3.6-35B-A3B) | lands | method/naming.yaml | — |
| R47 | Benchmark column table (DB `_bench` key → report label → task type → tool) | lands | method/naming.yaml | DUP |
| R48 | Protocol name table (`protocol` column values and meaning) | lands | method/naming.yaml | DUP |
| R49 | Never mix protocols in one table (protocol can flip a quant conclusion's sign) | lands | method/method.yaml | DUP |
| R50 | `bfcl-prompt-nothink-greedy` protocol superseded by native-tools; kept historical | retired | historical, replaced (`change.upkeep.outdated`) | — |
| R51 | `run_tag` mandatory (`m<n>-<desc>`); a number without one is void | lands | method/naming.yaml | DUP |
| R52 | Special state words `无结果`/`NO RESULT`, `BLOCKED-on-VRAM`, `GATE-FAIL` | lands | method/naming.yaml | DUP |

## `docs/METHOD.md`

| id | claim / fact | outcome | target | flags |
|---|---|---|---|---|
| R53 | Question: how quantisation maps to measured task scores under a controlled protocol; non-goals = leaderboard, product rec, self-training, PPL-as-target | lands | product/product.yaml (non-goals) + method/method.yaml | — |
| R54 | A result is a difference with uncertainty, not a point estimate | lands | method/method.yaml | — |
| R55 | Significance is item-level: one item = one Bernoulli trial, `SE=√(p(1−p)/n + p'(1−p')/n')` | lands | method/method.yaml | DUP |
| R56 | Every number carries a `run_tag`; sourceless numbers void | lands | method/naming.yaml | DUP |
| R57 | Always report the noise floor of the axis (agentic ≈ ±0.015; greedy code = 0) | lands | method/method.yaml | — |
| R58 | Negative and null results are first-class; a narrow-CI null is a finding | lands | method/method.yaml | — |
| R59 | Data contract: record what happened, no interpretation; score written as-is, no-score written `无结果` | lands | method/method.yaml | DUP |
| R60 | Forbid agent-invented judgments (byte-identical=fail, output-format checks, category contradictions) | lands | method/method.yaml | — |
| R61 | Conclusions must rest on >1 benchmark family (code **and** knowledge/reasoning **and** instruction) | lands | method/method.yaml | — |
| R62 | Benchmark suite table (family, benchmark, item count, tool) | lands | method/method.yaml | DUP |
| R63 | Retired, historical only: BFCL single/multi-turn (incl. miss_func/miss_param), testfrac, fa-probe | retired | historical, retired (`change.upkeep.outdated`) | — |
| R64 | Measurement protocol table: llama-server build 4399 (4bc272fd72); `-c 8192 -np 1`; greedy, max_gen 1024, chat template, 5-shot; gsm8k flexible-extract; thinking OFF; echo shim; `HF_HUB_OFFLINE=1`; EvalPlus 164/378 full; `--limit` | lands | method/method.yaml | — |
| R65 | Protocol discipline rules 1–6 (state the protocol; never mix; match the tool-calling dialect; per-slot context; greedy unless sampling is the variable; one GPU task at a time) | lands | method/method.yaml | DUP |
| R66 | Never modify upstream (llama.cpp/BFCL/EvalPlus); build a new dir instead | lands | method/method.yaml | DUP |
| R67 | Choosing the next experiment: value = uncertainty-reduction × questions-touched ÷ (GPU-s × new-risk); priority order; explicit degradations | lands | method/method.yaml | — |
| R68 | Delegation/anti-idle: one GPU task serial; worker never blocks on the lock; `setsid nohup … &` then return; queue state in a `QUEUE` file not the session; successors armed | lands | method/operations.yaml | DUP |
| R69 | Never use a text liveness gate (`pgrep -f "<script>"`); judge alive only by `flock -n` or a completion banner | lands | method/operations.yaml | DUP |
| R70 | The 9.5-hour GPU-idle incident | lands | work record `.scratch/<effort>/` (evidence) | — |

## `docs/DATABASE.md`

| id | claim / fact | outcome | target | flags |
|---|---|---|---|---|
| R71 | `experiments.sqlite` is the data SSOT; one row per run; `__`-prefixed columns derived; analyses read-only (`mode=ro`) | lands | architecture/database.yaml | — |
| R72 | Backup rule: numbered `bakN` before change, then integrity/cleanliness checks | lands | method/operations.yaml | DUP |
| R73 | Cleanliness checks: `integrity_check=ok`, empty `foreign_key_check`, no null mandatory fields, `_score∈[0,1]` (speed rows null), `rows == distinct rows` | lands | architecture/database.yaml | DUP |
| R74 | Dedup event 2026-10-14: non-idempotent `migrate_db.py` × auto-finisher for ~13 h, 1800→9564 rows (12871 total, 3307 unique) | retired | historical narrative → work record `.scratch/<effort>/` | DER |
| R75 | Rule: don't schedule `migrate_db.py`; run once and verify `rows == distinct`; repeat-ingest via `DELETE … WHERE run_tag=?` | lands | method/operations.yaml | DUP |
| R76 | Schema gap: early ~1881 legacy rows have null ctx/protocol/seed, so any `ctx=`/`parallel=` scope is unauditable | lands | architecture/database.yaml (data-quality caveat) | DER |

## `docs/OPERATIONS.md`

| id | claim / fact | outcome | target | flags |
|---|---|---|---|---|
| R77 | One GPU task at a time via `flock /tmp/llama_gpu.lock`; liveness only by `flock -n`/banner | lands | method/operations.yaml | DUP |
| R78 | Orphan `llama-server` inherits the lock; find holder with `fuser`, kill only the orphan child | lands | method/operations.yaml | — |
| R79 | Panel scripts need `trap cleanup EXIT`; check the port; abort if a foreign server holds it | lands | method/operations.yaml | — |
| R80 | Foreign project on :8834 (`Spark-X2.5-4B`) is not ours, holds no lock, not touched, but occupies VRAM causing OOM | lands | work record / environment note | DUP |
| R81 | Load gate: CPU-only load test before a panel; FAIL excluded, never null; loadgate.jsonl | lands | method/operations.yaml | — |
| R82 | Known GGUF-type limits: type 42 (`Q2_0`) defined but mixed SSM may fail; type 142/143 exceed `GGML_TYPE_COUNT=43`; diffusion-gemma unsupported on any local build | lands | method/operations.yaml | DUP |
| R83 | Ingest: `migrate_db.py` unique path; ONCE/REFRESH; the summary file is the only refresh source — clearing it deletes the cell | lands | method/operations.yaml | DUP |
| R84 | `migrate_db.py` non-idempotent on per-language MultiPL-E paths; don't schedule | lands | method/operations.yaml | DUP |
| R85 | `0.00` handling: suspect the harness before the model (per-slot context, FC handler, stale result files) | lands | method/operations.yaml | — |
| R86 | Environment: HF domain poisoned / `hf-mirror` hangs → use ModelScope; loglik needs the repo echo shim; offline envvars required | lands | method/operations.yaml | DUP |

## `docs/L2-结果.md`

| id | claim / fact | outcome | target | flags |
|---|---|---|---|---|
| R87 | Within a family, scores rise from a lower bit tier to the next; per-benchmark step medians (GSM8K +0.460, HumanEval+ +0.409, IFEval +0.250, MBPP+ +0.235, MMLU +0.146, ARC-c +0.100, TruthfulQA +0.005) | lands | result/result.yaml | DER |
| R88 | Per-benchmark per-+1-bpw slopes (GSM8K +0.156 … TruthfulQA +0.014, ~11× span) | lands | result/result.yaml | DER |
| R89 | Paired diff (capability − knowledge) = +0.12/bit, 95% CI [+0.04,+0.20] | lands | result/result.yaml | DER |
| R90 | Qwen3.5-2B multilingual code effective-bpw→score ladder (3.27→0.0062 … 6.24→0.2774) | lands | result/result.yaml | DER |
| R91 | Larger parameter count → higher score under the same quant recipe | lands | result/result.yaml | DER |
| R92 | Scheme/vendor: IQ vs K differ (~+0.056, CI [+0.008,+0.104]); vendor label shows no difference (+0.009, CI [−0.058,+0.077]) | lands | result/result.yaml | DER |
| R93 | MoE layer bit-allocation results (uniform 3.88→0.335/0.447; exq2 2.92→0.287/0.427; exq4 4.48→0.134/0.287) | lands | result/result.yaml | DER |
| R94 | KV precision f16/q8_0/q4_0 shows no measurable difference at short context (~1–2k); long context untested | lands | result/result.yaml | DUP,DER |
| R95 | Sampling: temp 0→0.3/0.7 lowers code pass rate; temp 0 top_k has no effect; MMLU is sampling-insensitive | lands | result/result.yaml | DER |
| R96 | Speculative decoding speeds up with draft depth (+36% at 0.8B, +93% at 9B); score ~unchanged, MMLU bit-identical per depth | lands | result/result.yaml | DER |
| R97 | QAT: 0.36–0.95 bpw smaller; 4-bit mostly indistinguishable, except 12B MMLU −0.197 CI [−0.242,−0.153]; ~2-bit QAT clearly lower | lands | result/result.yaml | DUP,DER |
| R98 | Third-party GSQ-RCO: all differences vs nearest/interpolated native span 0 | lands | result/result.yaml | DER |
| R99 | Non-measurements: gemma-4-31B QAT/native, gemma-4-26B-A4B native (VRAM); diffusion-gemma (load) | lands | result/result.yaml (declared absent, not 0) | DUP |

## `docs/L3-分析.md`

| id | claim / fact | outcome | target | flags |
|---|---|---|---|---|
| R100 | Quant width choice depends on the family's own curve knee (~4–5 bpw); pick where the score flattens | lands | result/analysis.yaml (`from:` R87/R90) | — |
| R101 | Judge quant adequacy by code/reasoning/instruction, not knowledge/truthfulness benchmarks | lands | result/analysis.yaml | — |
| R102 | Small models need more bits for hard multi-step tasks | lands | result/analysis.yaml | — |
| R103 | Compare scheme/bytes, not vendor labels | lands | result/analysis.yaml | DUP |
| R104 | Don't use PPL for decisions (PPL and task score disagree in ~30% of cases) | lands | result/analysis.yaml | DUP |
| R105 | Don't expect QAT to recover quantisation loss; it is "smaller at the same recipe" | lands | result/analysis.yaml | — |
| R106 | After a protocol change, re-measure (protocol flips the sign of a quant conclusion) | lands | result/analysis.yaml | DUP |
| R107 | Open questions: long-context KV effect; 31B/26B-A4B VRAM blocks; diffusion runtime; 12B MMLU anomaly re-test | lands | plan/plan.yaml | DUP |

## `docs/BACKLOG.md`

| id | claim / fact | outcome | target | flags |
|---|---|---|---|---|
| R108 | Hard blocks: gemma-4-31B QAT/native (m142/m143), 26B-A4B native (m145) `BLOCKED-on-VRAM`; DiffusionGemma `GATE-FAIL`; APEX has no artifact | lands | plan/plan.yaml (blocked, not null) | DUP |
| R109 | Hypotheses B1 (ternary/low-bit anomaly), B2 (vendor-recommended sampling), B3 (cross-family multi-turn), MoE-activation joint regression, Tier-1A per-tensor MoE quant | lands | plan/plan.yaml | — |
| R110 | SKIP probes m34/m40/m53 (third-party ternary / ModelScope probes, no loadable candidate) | retired | work-record evidence, no artifact | — |

## Store, render and generated outputs

| id | claim / fact | outcome | target | flags |
|---|---|---|---|---|
| R111 | `experiments.sqlite` holds the measured rows (the data SSOT) | lands | store (result layer) | — |
| R112 | `__`-prefixed columns (`__size`, `__quant`, `__quant_ratio`, `__score_fix`, `__mtp` …) are computed in `exp.py`/`migrate_db.py` and stored | lands | store columns, but should be generated not stored | DER |
| R113 | Schema `CHECK` constraints (score range, `cache_*_draft=cache_*`, ratio identities) | lands | architecture/database.yaml | — |
| R114 | `report.html` — the whole report | lands | render (producer `make_report.py`) | DER |
| R115 | `figures/report/*.png` — per-benchmark figures | lands | render (producer `make_report.py`) | DER |
| R116 | `bpw_map.json` — GGUF basename → effective bpw | lands | store (producer `gguf_params.py`) | DER |
| R117 | `loadgate.jsonl` — load-gate verdicts | lands | store / evidence | — |
| R118 | `.wrapup/*_summary.jsonl` — per-panel summaries (ingest source) | lands | store / evidence | — |

## Code and supporting files

| id | claim / fact | outcome | target | flags |
|---|---|---|---|---|
| R119 | `make_report.py` — renders report + figures from DB, read-only | lands | code | — |
| R120 | `make_report.py` embedded `QAT_PAIRS`/`NATIVE_LADDER`/`GSQ_QUANTS` run_tag+bpw literals | lands | code, but duplicate of DB + `bpw_map.json` | DER |
| R121 | `make_report.py`/`mktables.py` canonical protocol + benchmark column set | lands | code, duplicate of method/naming.yaml | DUP |
| R122 | `.wrapup/mktables.py` `build_tables()` contract docstring (one table per variable, never filter columns, `score (n)`, effective-bpw axis, coverage row) | lands | code; the contract is product/report.yaml | DUP |
| R123 | `.wrapup/mktables.py` `LANG_N` per-language item counts, derived from `*_summary.jsonl` | lands | evidence, regenerated not stored | DER |
| R124 | `.wrapup/mktables.py` `M55_RECIPES` gguf filenames | lands | code, duplicate of DB model names | DER |
| R125 | `.wrapup/gguf_params.py` — reads GGUF header, computes effective bpw | lands | code | DUP,DER |
| R126 | `.wrapup/lmeval_run.py` — one lm-eval panel; exact echo shim; never returns 0.0 | lands | code | DUP |
| R127 | `.wrapup/gpu_locked.sh` — `flock` GPU wrapper | lands | code | DUP |
| R128 | `.wrapup/loadgate_cpu.sh` — CPU load gate | lands | code | DUP |
| R129 | `exp.py` — DB insert/patch helpers; model-name regex → derived columns | lands | code | DER |
| R130 | `migrate_db.py` — schema upgrade + unique ingest path (ONCE/REFRESH) | lands | code | DUP |
| R131 | `LICENSE` (MIT) | lands | authored document (legal, fixed) | — |
| R132 | `requirements.txt` | lands | store | — |
| R133 | `.gitignore` | lands | code/config | — |
| R134 | `.wrapup/` drivers, CAMPAIGN files, logs, `QUEUE` | lands | work record `.scratch/<effort>/` (outside SSOT) | — |

## Findings — facts with no home even after the retry

| id | finding | outcome |
|---|---|---|
| U1 | **The pain layer is empty.** No source records the sufferer or the evidence the pain exists (who was hurt by not knowing how settings change scores). Every other layer can be filled from L0/L1, but `docs/pain/` has nothing to receive. | unplaceable |
| U2 | **`check_consistency.py` is a referenced but nonexistent gate** (README "如何复现"). A documented command with no file is a resolvable-reference failure, not a fact. | unplaceable |
| U3 | **The operator himself is unrecorded.** There is no `PEOPLE.yaml` equivalent: L0 fixes requirements but not his wording, expertise, preferences or the domains he does not care about, so `change.entries.people` has no source. | unplaceable |
| U4 | **`experiments.sqlite.bak34/35/36`** sit in the root as historical DB snapshots. The model has no home for superseded-but-kept binary evidence as SSOT; `change.upkeep.archive` demands a marked, outside-SSOT archive. | unplaceable |
| U5 | **The ":8834 foreign process ~6.5 GB VRAM"** is a dated machine-state observation; it is not a method rule, not a result, and changes with the machine. | unplaceable |

---

## Duplicates (same fact in two or more source files)

| fact | homes | first home |
|---|---|---|
| SSOT statement (numbers→DB, prose→docs, report derived) | `README.md`, `L0-要求.md` §13, `AGENTS.md` | `README.md` table |
| Project positioning ("quant is one sub-item") | `README.md`, `L0-要求.md` items 1–3 | `L0-要求.md` |
| Forbid nominal `Q2/Q3` labels | `L0-要求.md` §6, `README.md`, `NAMING.md`, `L2-结果.md` header, `mktables.py` docstring §6 | `L0-要求.md` |
| effective-bpw formula | `NAMING.md`, `mktables.py` docstring, `gguf_params.py` docstring | `NAMING.md` |
| `report.html` generated, never hand-edited | `README.md`, `REPORTING.md`, `AGENTS.md` | `REPORTING.md` |
| Report shape 总—分—总 + table/figure/analysis | `L0-要求.md` §7–11, `REPORTING.md` §报告结构 | `L0-要求.md` |
| Table shape (one variable, col1 fixed, col2 varied, score (n), never 0) | `REPORTING.md`, `mktables.py` docstring | `REPORTING.md` |
| Never mix protocols | `METHOD.md` §5, `NAMING.md` | `METHOD.md` |
| `run_tag` mandatory | `METHOD.md` §2, `NAMING.md` | `METHOD.md` |
| `无结果`/`BLOCKED`/`GATE-FAIL` ≠ 0 | `METHOD.md` 2b, `NAMING.md`, `REPORTING.md`, `L2-结果.md`, `BACKLOG.md` | `METHOD.md` |
| Benchmark suite/column table | `METHOD.md` §3, `NAMING.md`, `mktables.py`, `make_report.py` | `METHOD.md` |
| GPU one-task/flock + liveness rule | `METHOD.md` §5.6/§7, `OPERATIONS.md`, `AGENTS.md` | `METHOD.md` |
| `migrate_db.py` non-idempotent / don't schedule | `DATABASE.md`, `OPERATIONS.md`, `AGENTS.md` | `DATABASE.md` |
| DB backup-before-mutation + cleanliness checks | `DATABASE.md`, `AGENTS.md` | `DATABASE.md` |
| Long-context KV untested | `L2-结果.md`, `L3-分析.md` | `L2-结果.md` |
| 31B/26B VRAM block; diffusion `GATE-FAIL` | `L2-结果.md`, `L3-分析.md`, `BACKLOG.md` | `L2-结果.md` |
| 12B MMLU anomaly | `L2-结果.md`, `L3-分析.md` | `L2-结果.md` |
| PPL must not drive decisions | `METHOD.md` §1 non-goals, `L3-分析.md` §5 | `METHOD.md` |
| Reproduce command for report generation | `README.md`, `REPORTING.md` | `README.md` |
| `.wrapup` echo shim required (stock lm_eval KeyError) | `METHOD.md` §4, `OPERATIONS.md` | `METHOD.md` |

## Derived facts stored rather than generated

| fact | where it is stored | owner that should generate it |
|---|---|---|
| Whole `report.html` | `report.html` | `make_report.py` from DB + docs |
| All figures | `figures/report/*.png` | `make_report.py` |
| L2 medians/slopes/CIs/ladders (R87–R98) | `L2-结果.md` prose | queries over `experiments.sqlite` |
| Current scale counts (~3300/208/59) | `README.md` | `SELECT count(*) …` |
| Dedup counts (12871/3307/9564) | `DATABASE.md` | DB history / ticket |
| Legacy-null count (~1881) | `DATABASE.md` | `SELECT count(*) WHERE protocol IS NULL` |
| effective bpw values | `.wrapup/bpw_map.json`, `NAMING.md` example | `gguf_params.py` |
| `__`-prefixed columns | `experiments.sqlite` | `exp.py`/`migrate_db.py` (should be a view) |
| Per-language item counts | `mktables.py` `LANG_N` | `*_summary.jsonl` |
| run_tag + bpw literals | `make_report.py` `QAT_PAIRS`/`NATIVE_LADDER`/`GSQ_QUANTS` | DB + `bpw_map.json` |
| MoE recipe filenames | `mktables.py` `M55_RECIPES` | DB model names |
| Model-name → quant/type regexes | `exp.py` | derived-column producer (fine as code) |

---

## File kind, per source file (`change.shape.file_kind`)

| source file | kind it becomes |
|---|---|
| `AGENTS.md` | **render** (of the project's `AGENTS.yaml`) |
| `docs/README.md` | **router** (index + SSOT map); its product facts move to `product.yaml` |
| `docs/L0-要求.md` | **store** (`need/` + `product/`, user wording preserved) |
| `docs/REPORTING.md` | **store** (`product/report.yaml`) |
| `docs/NAMING.md` | **store** (`method/naming.yaml`) |
| `docs/METHOD.md` | **store** (`method/method.yaml`) |
| `docs/DATABASE.md` | **store** (`architecture/database.yaml`) |
| `docs/OPERATIONS.md` | **store** (`method/operations.yaml`) |
| `docs/L2-结果.md` | **store** (`result/result.yaml`) |
| `docs/L3-分析.md` | **store** (`result/analysis.yaml`); its argument prose may remain ~authored with injected facts |
| `docs/BACKLOG.md` | **store** (`plan/plan.yaml`) |
| `experiments.sqlite` | **store** |
| `report.html` | **render** |
| `figures/report/*.png` | **render** |
| `.wrapup/bpw_map.json`, `loadgate.jsonl`, `*_summary.jsonl` | **store** |
| `make_report.py`, `mktables.py`, `gguf_params.py`, `lmeval_run.py`, `exp.py`, `migrate_db.py`, `gpu_locked.sh`, `loadgate_cpu.sh`, `.gitignore` | **code** (a layer, not one of the four kinds) |
| `LICENSE` | **authored document** |
| `requirements.txt` | **store** |
| `.wrapup/` logs, drivers, CAMPAIGN | work record (outside SSOT) |

---

## Answers

### 1. Does the model fit, and where does it not

It fits well: the repo already runs an almost-literal L0/L1/L2/L3 ladder that maps onto **product → method → result**, with **plan** = `BACKLOG.md` and **architecture** = `DATABASE.md`. `change`-wise, the docs already honour SSOT, one-fact-one-home and "derived does not own knowledge" — so adoption is mostly re-homing, not re-deciding.

It does **not** fit in three places:
- **pain and need are empty.** L0 holds *requirements*, i.e. product/need, but nothing records a sufferer or the evidence the pain exists. The chain's root is missing.
- **The user is absent as an entity.** There is no `PEOPLE.yaml`; the operator is only a voice inside L0.
- **The work record has no boundary.** `.wrapup/` mixes code, evidence and logs, and the dated migration history sits inside `DATABASE.md` (SSOT) rather than a ticket.

### 2. What the migration cannot express

After re-homing, these still have no home (U1–U5): the **pain fact**; the **operator's own profile**; the **binary backups** `bak34/35/36` (superseded evidence the SSOT model neither keeps nor archives); and the **dated machine-state observation** of the foreign :8834 process. Also, two "facts" turn out to be defects rather than facts: the missing `check_consistency.py` gate and the fact that ~1881 legacy rows can never be audited for context/parallel scope — truth from an unkept history.

### 3. The single rule this repository breaks hardest today

**`laws.ssot` / `change.upkeep.cut_repetition` — one fact, one home.** The most load-bearing rules are each written in two to five places: the effective-bpw formula and the "no nominal labels" rule in `NAMING.md`, `L0`, `README`, `L2` and `mktables.py`; the GPU-liveness rule in `METHOD` and `OPERATIONS`; the ingest/dedup rule in `DATABASE`, `OPERATIONS` and `AGENTS`. The repo even legislates against this in `README.md` ("同一事实不得在两个文件里各说一套") while violating it in the same file. The second-hardest is `change.entries.citation`/`laws.derived`: measured numbers (medians, CIs, slopes, scale counts) are stored as prose in `L2-结果.md` and `README.md` rather than generated from `experiments.sqlite`, which also owns them.
