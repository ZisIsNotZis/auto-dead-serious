# STEP3 — `/home/z/hf/research`: untrack the virtualenv, measure a rewrite, judge the ten docs

Repo: `/home/z/hf/research`, branch `main`, remote `git@github.com:ZisIsNotZis/tiny-llm-eval-factors.git` (public GitHub).
Git here: `git version 2.43.0`.
This file is a report for part 2 and part 3; part 1 was acted on and committed locally.

## 0. Headline

- **Tracked paths: 79,661 → 409.** The virtualenv `.wrapup/lmenv/` alone was 78,667 of them (98.8% of the index).
- **A history rewrite would reclaim ≈ 3.53 GiB**, of which **≈ 3.51 GiB (99.8%) is the virtualenv**. The SQLite store looks huge (61 versions, 899.5 MiB raw) but costs only ≈ 5.7 MiB on disk because git deltifies it.
- **None of the ten `docs/*.md` can be retired now**: all ten are cited by path in YAML `origin` (115 citations). A dangling origin is a defect. The checker `docs/check_docs.py` never reads the `.md` at all, so the origin strings are the only thing holding them.

---

## 1. Untracking (done, local commit, no push)

Commit: **`0efda6f9c`** — "Untrack regenerable artifacts that should never have been versioned", on `main`, **not pushed** (`git status -sb` → `## main...origin/main [ahead 122]`). Index-only: `git rm -r --cached`; every working-tree file is still on disk (`.wrapup/lmenv` still 8.9 GiB, `.wrapup/mres` 1.3 GiB, etc.).

### What came out (79,252 paths)

| Path | Count | Why it costs nothing to get back |
|---|---:|---|
| `.wrapup/lmenv/` | 78,667 | lm-eval virtualenv, missed by the sibling-venv rules. `python3 -m venv .wrapup/lmenv` + `pip install lm_eval[vllm]`; exact resolve is recorded in `.wrapup/lmenv_install.log`. |
| `.wrapup/mres/` | 556 | Raw per-panel eval artifacts; `.gitignore` already declared them regenerable ("keep scripts + `*_summary.jsonl` only") but they were never removed from the index. |
| `.wrapup/dl_ready/` | 12 | Download-completion markers written by `.wrapup/dl_*.sh` (`echo … > dl_ready/$file.ready`). |
| `.wrapup/jars/` | 1 | Downloaded third-party dependency jar (`javatuples-1.2.jar`); already matched by the existing `.gitignore` rule. |
| `.wrapup/ppl_corpora/` | 3 | Generated corpora; build output of `.wrapup/build_ppl_corpora.py` (from local caches, no network). |
| `.wrapup/.keeper.lock` | 1 | GPU keeper lock — runtime state. |
| `.wrapup/javac.*.args` | 12 | `javac` invocation scratch. |

**Kept deliberately** (records/sources, not build output): all `*.sh` / `*.py` scripts, `*_summary.jsonl` and other `.jsonl`, `*.out` run logs, `CAMPAIGN*.txt`, `bpw_map.json`/`MOE`/probe JSON. `.wrapup/lmeshim/lm_eval_cli.py` is source, kept.

### `.gitignore` extended

```
.wrapup/lmenv/          # added to the wrap-up dirs block
.wrapup/dl_ready/       # added
.wrapup/ppl_corpora/    # added
.wrapup/.keeper.lock    # added
.wrapup/javac.*.args    # added
```
`.wrapup/mres/` and `.wrapup/jars/` already had rules (lines 24, 26) — untracking was the missing half. Verified: `git check-ignore -v --no-index .wrapup/lmenv/bin/python3` → `.gitignore:18:.wrapup/lmenv/`.

### Reproduction

```
git ls-files | wc -l                                   # 79661  (before)
git rm -r --cached --quiet .wrapup/lmenv .wrapup/mres .wrapup/jars \
    .wrapup/dl_ready .wrapup/ppl_corpora .wrapup/.keeper.lock '.wrapup/javac.*.args'
git add .gitignore && git commit
git ls-files | wc -l                                   # 409    (after)
```

**Untracking alone reclaims no history and shrinks no clone** — it only stops the index from tracking the files. The 3.5 GiB is reclaimed only by a rewrite (part 2, not done).

---

## 2. What a history rewrite would reclaim (measured, not acted on)

`.git` = 3.6 GiB on disk; `git count-objects -vH` → `size-pack 3.52 GiB`, `in-pack 81,374`, `2 packs`, loose `17.99 MiB`.

Method: `git rev-list --objects --all` → object list; `git verify-pack -v` on both packs joined to paths; loose objects sized with `stat`. **Raw** = uncompressed unique-blob bytes across all versions; **on-disk** = packed `size-in-pack` for packed objects plus the actual loose-file size for loose ones (the number a rewrite + `git gc --prune=now` frees).

| Path family | blobs | raw (all versions) | on-disk now | reclaimable by rewrite |
|---|---:|---:|---:|---:|
| virtualenv `.wrapup/lmenv/` | 72,179 | 7.83 GiB | 3,593.16 MiB packed | **≈ 3.51 GiB** |
| SQLite store + backups `experiments.sqlite*` | 61 | 899.5 MiB | 0.62 MiB packed + 5.11 MiB loose | **≈ 5.7 MiB** |
| generated report + figures (`report.html`, `figures/`) | 35 | 15.0 MiB | 11.00 MiB loose (0 packed) | **≈ 11.0 MiB** |
| everything else | 1,499 | 54.2 MiB | 6.65 MiB packed + 0.75 MiB loose | **≈ 7.4 MiB** |
| loose commits/trees (93 objs, remainder of loose) | — | — | ≈ 1.1 MiB loose | ≈ 1.1 MiB |
| **total** | 73,774 | — | — | **≈ 3.53 GiB** |

Two facts worth stating:

- The pack is **99.8% the virtualenv**. Its single largest object is `lmenv/lib/python3.12/site-packages/nvidia/cu13/lib/libcublasLt.so.13` — 541.6 MB raw, 374.9 MB packed, alone ~10% of the repo.
- The SQLite store is a **trap**: 61 versions × 15,462,400 B = 899.5 MiB raw, but git keeps 48 of them as deltas (0.62 MiB) and only 13 loose (5.11 MiB). Purging it from history buys ~6 MiB, **not** 900 MB. Its real cost today is in the **working tree / checkout** (4 backups × 15.5 MB = 62 MB on disk), which a rewrite does not touch.

### Tooling reality (checked, contradicts the brief's assumption)

- `git filter-repo` — **ABSENT** (`git filter-repo` → "not a git command"; `python3 -c 'import git_filter_repo'` → ImportError).
- `git filter-branch` — **PRESENT** at `/usr/lib/git-core/git-filter-branch` (git 2.43.0). It prints the usual "glut of gotchas" warning. So a rewrite **could** be run without installing anything, though filter-repo is the correct tool.
- Remote is a **public GitHub** repo. A rewrite changes **all 130 commit hashes** and requires `git push --force`, which breaks every existing clone/fork. Outward and irreversible → needs consent (`resources.work_areas.pushes`, `resources.work_areas.untrack`).

### Exact commands (NOT run)

Preferred, needs install (not done — installing is out of bounds):
```
pip install git-filter-repo
git filter-repo --force \
  --path .wrapup/lmenv --path .wrapup/mres --path .wrapup/dl_ready \
  --path .wrapup/ppl_corpora --path .wrapup/jars \
  --path experiments.sqlite --path-glob 'experiments.sqlite.bak*' \
  --path report.html --path figures \
  --invert-paths
git remote add origin git@github.com:ZisIsNotZis/tiny-llm-eval-factors.git   # filter-repo drops origin
```

Available now (filter-branch, discouraged):
```
git filter-branch --force --prune-empty --tag-name-filter cat \
  --index-filter 'git rm -r --cached --ignore-unmatch .wrapup/lmenv .wrapup/mres \
      .wrapup/dl_ready .wrapup/ppl_corpora .wrapup/jars \
      experiments.sqlite report.html figures' \
  -- --all
rm -rf .git/refs/original .git/logs
git reflog expire --expire=now --all
git gc --prune=now --aggressive
```

Then, and only with consent: `git push --force origin main` (plus `--tags` if tags exist). Note `--path-glob 'experiments.sqlite.bak*'` is required because the `.bak34/35/36` backups were committed historically and are only *currently* untracked/ignored; likewise `figures/` has historical blobs though it is ignored today.

---

## 3. Which of the ten `docs/*.md` can be retired

Ten docs, citation counts from `grep -rhoP 'docs/[^\s;"（(]+\.md' docs/*/*.yaml`:

| doc | origin citations | facts now live in |
|---|---:|---|
| `docs/METHOD.md` | 24 | `docs/method/method.yaml` |
| `docs/L2-结果.md` | 14 | `docs/result/result.yaml` |
| `docs/L0-要求.md` | 13 | `docs/product/product.yaml`, `docs/need/need.yaml` |
| `docs/REPORTING.md` | 12 | `docs/product/product.yaml` |
| `docs/OPERATIONS.md` | 11 | `docs/method/method.yaml` |
| `docs/README.md` | 10 | the `docs/<layer>/` tree itself (its SSOT table is the layout) |
| `docs/NAMING.md` | 9 | `docs/method/method.yaml` |
| `docs/L3-分析.md` | 8 | `docs/result/result.yaml` |
| `docs/DATABASE.md` | 7 | `docs/architecture/architecture.yaml` |
| `docs/BACKLOG.md` | 7 | `docs/plan/plan.yaml` |
| **total** | **115** | |

**Binding mechanism (checked).** `docs/check_docs.py` validates only the seven YAML layer files against their schemas — it never opens a `.md`. No tracked `.py`/`.sh` outside `docs/` references any of the ten. So the *only* things that break when a `.md` is deleted are (a) the `origin` strings in `docs/*/*.yaml`, and (b) `docs/README.md`'s own index table.

**Verdict.**

- **Can be retired now: none.** All ten are cited by path in YAML `origin` (7–24 each). Deleting any leaves dangling origin strings — the defect the brief names. Retirement is blocked until those origins are repointed, which is a `docs/*/*.yaml` edit outside this change's write bounds.
- **Safe to retire once origins are repointed** (content fully carried by the YAML layers): `METHOD.md`, `NAMING.md`, `OPERATIONS.md`, `DATABASE.md`, `BACKLOG.md`, `L2-结果.md`, `L3-分析.md`, and `README.md`. `README.md` is a *router* (index/SSOT table), so if it goes its routing role must move into the tree first.
- **Should not be deleted even then**: `L0-要求.md` and `REPORTING.md`. They are L0 — user-given / operator-locked — i.e. the *source* the YAML derives from, so they are origin, not a redundant copy; an origin pointing at them is a genuine citation. Keep them, or move them to an archive marked no-longer-trustworthy (`change.upkeep.archive`), never hard-delete as a "duplicate".

Inference: the content-coverage judgement in the two bullets above is my reading of the docs against the YAML; the citation counts and the checker's scope are measured facts.

---

## Bounds honoured

- **No `git push`** (`ahead 122`, remote untouched). **No history rewrite. Nothing installed.**
- `experiments.sqlite`, the ten `.md`, `docs/*/*.yaml`, `docs/check_docs.py` untouched.
- Writes made: `/home/z/hf/research/.gitignore`, the untracking `git rm --cached` index change, one local commit `0efda6f9c`, and this report.
- The untracked `docs/<layer>/` YAML additions were left untracked.
