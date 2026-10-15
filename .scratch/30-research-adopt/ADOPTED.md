# Adoption result — `/home/z/hf/research`

Reconciliation of the migration described by `LEDGER.md`. `change.upkeep.adopt`
(convert the whole set once every fact has a home) and `change.upkeep.lossless`
(each claim lands, retires with a reason, or is a finding) applied to the result.
Add-only: the ten source `.md` files and root `AGENTS.md` are byte-identical to
`BASELINE.txt`; no git action; nothing else written outside `docs/` and this file.

## Counts by outcome

| outcome | claims | note |
|---|---|---|
| landed | 129 | R01–R134 minus the 5 retired; 100 of them live in the 7 layer files, the rest in the named non-layer homes (`code`, `store`, `render`, work record, `LICENSE`, router) |
| retired | 5 | R31, R50, R63, R74, R110 — each with its reason below |
| unplaceable | 5 | U1–U5; **three are facts with no home** (U1, U3, U4), two are defects/observations, not facts (U2, U5) |

Layer files hold **100 facts**: pain 1, need 1, product 15, architecture 7, method 47, plan 7, result 22.

## Files written (everything under `/home/z/hf/research/docs/`)

| path | kind | content |
|---|---|---|
| `docs/pain/pain.yaml` + `pain.schema.yaml` | store + refinement schema | declared absence (1 fact) |
| `docs/need/need.yaml` + `need.schema.yaml` | store + refinement schema | the root need, derived from L0 (1 fact) |
| `docs/product/product.yaml` + `product.schema.yaml` | store + refinement schema | positioning, report shape, quality bar, non-goals (15) |
| `docs/architecture/architecture.yaml` + `architecture.schema.yaml` | store + refinement schema | database module + render contract (7) |
| `docs/method/method.yaml` + `method.schema.yaml` | store + refinement schema | conventions, method, measurement, protocol, naming, operations (47) |
| `docs/plan/plan.yaml` + `plan.schema.yaml` | store + refinement schema | hard blocks, hypotheses, open questions (7) |
| `docs/result/result.yaml` + `result.schema.yaml` | store + refinement schema | measured facts, a citation, agent analyses (22) |
| `docs/check_docs.py` | checker | gate for the whole set |

Each refinement schema is `allOf: [{"$ref": "docs@1"}, <domain pattern>]`. It
refines, never replaces: the standard's `_text` floor, coordinates and
`unevaluatedProperties: false` are inherited, and the domain pattern only adds a
closed `project` holding that layer's cut key (`sufferer` / `must_become_true` /
`kind` / `module` / `topic`). The cut key is kept as a field rather than a file
split, so a later finer split costs no reshape (`change.shape.forward_compatible`).

## The check (proves, not claims)

Command, run from the repository root: `python3 docs/check_docs.py`.

```
docs set check
  [ok] pain           1 facts
  [ok] need           1 facts
  [ok] product       15 facts
  [ok] architecture   7 facts
  [ok] method        47 facts
  [ok] plan           7 facts
  [ok] result        22 facts
  schema validation   : 7 files vs docs@1 + refinement
  ids unique in file  : ok
  from resolves       : 15 references checked
  _text unique        : 100 distinct texts
  _text present       : every node carries _text

PASS
```

The gate was shown to fail, twice, on a deliberate break, and restored:

* dangling `from` — `result.res2: from 'result.nope' does not resolve` → `exit=1`.
* empty `_text` — `result/result.yaml: schema: ['res3','_text']: '' should be non-empty`
  plus `result/result.yaml: fact res3: missing or empty _text` → `exit=1`.

After restore the same command prints `PASS`, `exit=0`.

## Where I disagreed with `LEDGER.md` (and why)

1. **One file per layer, not the ledger's topic/status cut.** The ledger proposed
   `method/{method,naming,operations,conventions}.yaml`, `result/{result,analysis}.yaml`
   and `architecture/database.yaml`. The task contract fixes *one layer file per
   layer*, so the cut is kept inside each file as `project.*` / id prefix instead
   of as separate files. Same keys, one file; a later split is mechanical. Facts
   therefore land in the *layer* the ledger names, in that layer's single file.
2. **`need` was unfilled in the ledger but is required by the contract.** The
   ledger named `need/need.yaml` as a target yet routed no row to it. I placed the
   root need there (`n1`), derived from L0 items 1–2, `from: product.prod1`, author
   `agent`. It is a genuine derived fact (why the project exists, distinct from the
   product statement of what it is), not an invention of a source claim.
3. **`pain` is left as a declared absence, not invented.** Per `laws.absent` /
   `change.entries.fabricated`, `pain/pain.yaml` holds one fact recording *that no
   source records a sufferer or evidence*; the sufferer is not fabricated. The pain
   fact itself stays unplaceable (U1).
4. **R111** (the store is the data SSOT) is filed under `architecture`, not "result
   layer": the database module is the architecture fact, and the result layer holds
   measurements.

## Reconciliation — source file by source file

Legend: **landed → fact id** (this set) or **landed → named home** (outside the
layer files); **retired**; **unplaceable**. `DUP` rows merged into one home so no
two facts carry the same text.

### `AGENTS.md`
R01→m4 · R02→m35 (DUP) · R03→arch2 (DUP) · R04→m5 · R05→m6 · R06→m7 (DUP) ·
R07→m8 · R08→m9 · R09→m1 (DUP) · R10→render of the project's `AGENTS.yaml` (not a fact of this set).

### `docs/README.md`
R11→prod1 (DUP) · R12→router `docs/README.md` (the SSOT map; a router holds no fact of its own) ·
R13→m2 (DUP) · R14→m3 (DUP) + router · R15→router · R16→res15 (citation) ·
R17→m47 · R18→arch6 (DUP) · R19→`LICENSE` (authored legal document) · R20→**unplaceable** (U2).

### `docs/L0-要求.md`
R21→prod1+prod2 (DUP) · R22→m10 · R23→m11 · R24→m39 (DUP) · R25→prod4 (DUP) ·
R26→prod5 (DUP) · R27→prod6 (DUP) · R28→prod7 (DUP) · R29→m3 (DUP) · R30→m1 (DUP) ·
R31→**retired** (a "待补" meta-note, no fact — `change.upkeep.outdated`).

### `docs/REPORTING.md`
R32→prod8 + arch6 (DUP) · R33→prod9 (DUP) · R34→prod10 (DUP) · R35→prod11 (DUP) ·
R36→prod12 + prod4 (DUP) · R37→prod15 + prod7 (DUP) · R38→prod13 · R39→prod14 ·
R40→m15 (DUP) · R41→m46 (DUP).

### `docs/NAMING.md`
R42→m38 (DUP, DER) · R43→m39 (DUP) · R44→m40 · R45→m41 · R46→m42 · R47→m43 (DUP) ·
R48→m44 (DUP) · R49→m23 (DUP, merged into protocol discipline) · R50→**retired**
(superseded protocol `bfcl-prompt-nothink-greedy`, replaced by native-tools; the
current protocol remains in m44, the history is not carried into the SSOT) ·
R51→m45 (DUP) · R52→m46 (DUP).

### `docs/METHOD.md`
R53→prod3 + m12 · R54→m13 · R55→m14 (DUP) · R56→m45 (DUP) · R57→m16 · R58→m17 ·
R59→m18 (DUP) · R60→m19 · R61→m20 · R62→m21 (DUP) · R63→**retired** (BFCL single/multi-turn,
`testfrac`, `fa-probe` — historical only) · R64→m22 · R65→m23 (DUP) · R66→m7 (DUP) ·
R67→m24 · R68→m25 (DUP) · R69→m26 (DUP) · R70→work record `.scratch/<effort>/` (the 9.5 h
GPU-idle incident is dated evidence, not a current fact).

### `docs/DATABASE.md`
R71→arch1 · R72→m35 (DUP) · R73→arch2 (DUP) · R74→**retired** (the 2026-10-14 dedup
event is dated narrative → work record; the surviving rule is m34) · R75→m34+m35 (DUP) ·
R76→arch3 (DER, kept as the declared data-quality caveat).

### `docs/OPERATIONS.md`
R77→m27+m28 (DUP) · R78→m29 · R79→m30 · R80→work record / environment note (DUP; the
foreign :8834 process is machine state, see U5) · R81→m31 · R82→m32 (DUP) · R83→m33 (DUP) ·
R84→m34 (DUP) · R85→m36 · R86→m37 (DUP).

### `docs/L2-结果.md`
R87→res1+res2 · R88→res3 · R89→res4 · R90→res5 · R91→res6 · R92→res7 · R93→res8 ·
R94→res9 (DUP, DER) · R95→res10 · R96→res11 · R97→res12 (DUP, DER) · R98→res13 ·
R99→res14 (DUP).

### `docs/L3-分析.md`
R100→an1 (from res1,res5) · R101→an2 · R102→an3 · R103→an4 (DUP) · R104→an5 (DUP) ·
R105→an6 · R106→an7 (DUP) · R107→plan7 (DUP).

### `docs/BACKLOG.md`
R108→plan1 (DUP) · R109→plan2, plan3, plan4, plan5, plan6 · R110→**retired** (SKIP
probes m34/m40/m53 produced no loadable candidate and no artifact).

### Store, render and generated outputs
R111→arch1 · R112→arch4 (DER) · R113→arch5 · R114→render `report.html` · R115→render
`figures/report/*.png` · R116→store `.wrapup/bpw_map.json` · R117→store
`.wrapup/loadgate.jsonl` · R118→store `.wrapup/*_summary.jsonl`. These four are the
artifact/store homes, not layer facts.

### Code and supporting files
R119–R130 → the code layer itself (`make_report.py`, `.wrapup/mktables.py`,
`.wrapup/gguf_params.py`, `.wrapup/lmeval_run.py`, `exp.py`, `migrate_db.py`,
`.wrapup/gpu_locked.sh`, `.wrapup/loadgate_cpu.sh`); R131→`LICENSE`; R132→`requirements.txt`;
R133→`.gitignore`; R134→work record `.wrapup/` / `.scratch/`. The code layer is the
script, per the ledger's file-kind table; it is not re-stated inside `docs/`.

## Retired claims (each with its reason — `change.upkeep.retraction`)

| id | claim | why retired |
|---|---|---|
| R31 | "待补" note that user conclusions may be added later | scaffolding, no fact |
| R50 | protocol `bfcl-prompt-nothink-greedy` | superseded by native-tools; current protocol kept in m44 |
| R63 | BFCL single/multi-turn, `testfrac`, `fa-probe` | retired benchmarks, historical only |
| R74 | the 2026-10-14 dedup event (12871→3307) | dated narrative, not a current fact; rule kept in m34 |
| R110 | SKIP probes m34/m40/m53 | detected no loadable candidate, produced no artifact |

## Unplaceable — the three things I could not place

1. **The pain fact (U1).** No source records who was hurt by not knowing how
   settings change scores, or the evidence the pain exists. `change.upkeep.adopt`
   requires the root's pain be filled by asking; as a worker I did not fabricate it.
   `pain/pain.yaml` holds only the declared absence (`p1`).
2. **The operator's own profile (U3).** There is no `PEOPLE.yaml` equivalent: L0
   fixes requirements but nothing records the operator's wording, expertise,
   preferences or the domains he does not care about, so `change.entries.people`
   has no source.
3. **The superseded binary DB snapshots (U4).** `experiments.sqlite.bak34/35/36`
   sit in the repo root. The SSOT model keeps current facts and hard-deletes dead
   ones, and `change.upkeep.archive` demands a marked, outside-SSOT archive; the
   model has no home for kept-but-superseded binary evidence.

Two further entries in `LEDGER.md` were not placeable either, but they are not
facts: **U2** — `check_consistency.py` is named as a gate in `README.md` but does
not exist (a `change.upkeep.resolvable` reference failure, a defect); **U5** — the
foreign process on `:8834` (~6.5 GB VRAM) is a dated machine-state observation, not
a method rule or a result.

## Residual risks / open items

* The checker resolves `docs@1` from `RESEARCH_DOCS_STANDARD` or the absolute
  default `/home/z/vibe/AGENTS.docs.schema.yaml`; on a machine without that policy
  path the check exits 2 and says so.
* 100 facts under 7 layer files is not certified as *exhaustive* against every
  source sub-claim at sentence granularity; it is exhaustive against `LEDGER.md`'s
  R01–R134 / U1–U5, which is the mapping this task supplied.
