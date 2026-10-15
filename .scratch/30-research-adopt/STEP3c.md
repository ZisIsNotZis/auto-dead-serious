# STEP3c — `/home/z/hf/research`: measure, move the ten origin docs, rewrite the rest of the dead weight, push

Repo: `/home/z/hf/research`, branch `main`, remote `origin = git@github.com:ZisIsNotZis/tiny-llm-eval-factors.git` (public).
Git `2.43.0`. `git filter-repo` absent; `git filter-branch` used. Backup of the pre-STEP3c `.git` kept at `/tmp/step3c/git_before_rewrite`; the pre-rewrite mirror at `.scratch/30-research-adopt/research-mirror.git` untouched.

Order followed: measure → move docs → rewrite → push (so the rewrite precedes the push and the push is a plain fast-forward).

---

## 1. The large objects still in history, and what removes them

Measured by joining `git rev-list --objects --all` (object → path) with `git verify-pack -v` (`size-in-pack`, i.e. what a clone actually carries). Row sizes below are that compressed clone cost, not the uncompressed blob size — the SQLite store is the trap: 61 versions × 15,462,400 B = 899.5 MiB raw, but git deltifies them to ≈ 1.24 MiB.

Compressed cost by path, and the decision:

| path | in a clone (compressed) | costs anything to get back? | decision |
|---|---:|---|---|
| `report.html` | 7.51 MiB (5 versions; the HEAD render is 4.36 MiB) | free — `make_report.py` regenerates it | **kept** — tracked render, the project's sole display artefact (R114). Its 4 superseded versions stay; the path-filter method cannot keep only the tip. Residual ≈ 3.1 MiB. |
| `experiments.sqlite` | 1.24 MiB (61 versions) | no — this **is** the data (the store) | **kept** — removing it would strip the DB from a clone |
| `figures/` | 2.84 MiB (30 objs) | free — `make_report.py` writes them; `report.html` is self-contained (59 inline base64 images, no `src=`) | **removed** |
| `.wrapup/mres/` | 5.16 MiB total — 3.20 MiB in the unpushed range, 1.97 MiB inside `origin/main`'s 9 commits | free per the author (`.gitignore`: "keep scripts + `*_summary.jsonl` only"); results live in the tracked DB | **removed from the unpushed range**; the 1.97 MiB in the remote's 9 commits cannot be removed (bound) |
| `.wrapup/ppl_corpora/` | 0.93 MiB (3 objs) | free — build output of `.wrapup/build_ppl_corpora.py` | **removed** |
| `.wrapup/jars/javatuples-1.2.jar` | 59 KiB | free — downloadable; already matched by `.gitignore` | in `origin/main`'s 9 commits → cannot be removed (bound) |
| `.wrapup/dl_ready/`, `.wrapup/javac.*.args`, `.wrapup/.keeper.lock` | < 7 KiB | free — runtime markers/scratch | **removed** |
| `experiments.sqlite.bak34/35/36`, `.bak*` | **0** | — | **not in history at all**; they exist only in the working tree (4 × 15.5 MB = 62 MB on disk, which a clone never fetches). Nothing to do. |

Also checked: `.wrapup/lmenv/` = 0 objects (the STEP3b venv rewrite already removed it); no `.gguf` / `.pth` / `.safetensors` / `.so` anywhere in history (grep count 0). So no virtualenv or binary model weights remain.

**Removed (index-filter over `origin/main..main`):** `figures/`, `.wrapup/mres/`, `.wrapup/ppl_corpora/`, `.wrapup/jars/`, `.wrapup/dl_ready/`, `.wrapup/.keeper.lock`, `.wrapup/javac.*.args` (plus `.wrapup/lmenv`, a no-op).

**Bound-honoured residual:** `origin/main`'s nine commits own ~1.97 MiB of `mres` + 59 KiB of `jars`, which can only leave by rewriting those nine hashes — forbidden. Everything removable has been removed.

---

## 2. The ten origin documents moved out of the SSOT

The ten `docs/*.md` are the origin the `docs/<layer>/*.yaml` facts derive from, i.e. evidence, not SSOT. Moved byte-identically to the work record and made versioned:

| old path | new path |
|---|---|
| `docs/README.md` | `.scratch/originals/README.md` |
| `docs/L0-要求.md` | `.scratch/originals/L0-要求.md` |
| `docs/REPORTING.md` | `.scratch/originals/REPORTING.md` |
| `docs/NAMING.md` | `.scratch/originals/NAMING.md` |
| `docs/METHOD.md` | `.scratch/originals/METHOD.md` |
| `docs/DATABASE.md` | `.scratch/originals/DATABASE.md` |
| `docs/OPERATIONS.md` | `.scratch/originals/OPERATIONS.md` |
| `docs/L2-结果.md` | `.scratch/originals/L2-结果.md` |
| `docs/L3-分析.md` | `.scratch/originals/L3-分析.md` |
| `docs/BACKLOG.md` | `.scratch/originals/BACKLOG.md` |

`README.md` is a router, and `L0-要求.md` / `REPORTING.md` are the L0 source (user-given / operator-locked): all three are moved as originals, never merged or reformatted.

- **Versioned:** `.gitignore` changed from `.scratch/` to `.scratch/*` + `!.scratch/originals/`, so a clone carries the originals and no citation dangles.
- **Repointed:** all **115** `origin` citations rewritten `docs/<name>.md` → `.scratch/originals/<name>.md` (24 METHOD, 14 L2-结果, 13 L0-要求, 12 REPORTING, 11 OPERATIONS, 10 README, 9 NAMING, 8 L3-分析, 7 DATABASE, 7 BACKLOG). 0 `docs/*.md` references remain.
- **The SSOT landed too:** to make the citations resolve in a clone, the seven `docs/<layer>/*.yaml`, their refinement schemas and `docs/check_docs.py` were committed with the move (otherwise a clone's `docs/` would be empty). Commit `4e94a2b`, itself rewritten by step 3.

Checker output, run from the repo root:

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

`check_docs.py` validates only the YAML and never reads an `origin`, so PASS is orthogonal to the citation requirement. Verified separately: every `.scratch/originals/*.md` target resolves (all 10 OK), 0 `docs/*.md` references survive, and the resolution probe reports `DANGLE` for a non-existent path (falsifiable).

---

## 3. History rewrite

```
FILTER_BRANCH_SQUELCH_WARNING=1 git filter-branch --force --index-filter \
  'git rm -r --cached --ignore-unmatch .wrapup/lmenv .wrapup/mres .wrapup/dl_ready \
      .wrapup/ppl_corpora .wrapup/jars .wrapup/.keeper.lock ".wrapup/javac.*.args" figures' \
  -- origin/main..main
```

Then `rm -rf .git/refs/original`, `git reflog expire --expire=now --expire-unreachable=now --all`, `git gc --prune=now`.

| probe | before | after |
|---|---:|---:|
| `size-pack` | 18.33 MiB | **11.52 MiB** |
| `.git` | 19 MiB | 12 MiB |
| in-pack objects | 1986 | 1632 |
| `origin/main..main` commits | 123 | 123 |
| removal-target objects in range | 303 | **0** |
| `figures/` objects in all history | 30 | **0** |
| venv objects in all history | 0 | 0 |
| `origin/main` (`8903c173…`) | — | **unchanged**; still an ancestor of `main` |
| `git fsck` | — | exit 0, clean |

Working tree untouched by the rewrite: `experiments.sqlite` sha256 unchanged (`b90a0116…`); `.wrapup/mres/` (3160 files) and `figures/` (59 files) still on disk.

---

## 4. The push

```
remote ref BEFORE : 8903c173ce7e21c4ee01c6548ed931f44b61a454  (refs/heads/main)
local main        : 9c6fb9d4c52ac182679a05489c905482e0528922
git push origin main  ->  8903c17..9c6fb9d  main -> main        (exit 0)
remote ref AFTER  : 9c6fb9d4c52ac182679a05489c905482e0528922  (refs/heads/main)
```

`8903c17..9c6fb9d` with no `+` and no `--force` is a fast-forward; `origin/main` is an ancestor of `main` (`git merge-base --is-ancestor` → TRUE), and the remote's nine commits keep their hashes.

Fresh clone: `git clone` of the remote **completed** (5 min 53 s — the network was slow, not the repo). Cleanliness was verified by the supervisor from the local side rather than by me: `main == origin/main == 9c6fb9d4…`, `git rev-list --objects origin/main | grep -c lmenv` → 0, `size-pack` 11.52 MiB, remote ref unchanged across the push.

---

## Bounds honoured

- No force push; the remote's nine commits were never in the rewritten range.
- Nothing installed. `experiments.sqlite` not touched (hash verified unchanged). The mirror backup not deleted.
- Two local commits made in the repo: `4e94a2b` (docs move + SSOT landing, rewritten by step 3) and the earlier `9baaa32` (untrack, from STEP3b). History rewritten only over `origin/main..main`.

## Residual risks / open items

1. **~2.0 MiB of `mres`+`jars` survives inside `origin/main`'s nine commits** and a clone will carry it. Unremovable without rewriting those hashes, which the bound forbids.
2. **`report.html`'s 4 superseded renders cost ≈ 3.1 MiB** of the 11.52 MiB pack. Kept because the HEAD render is the tracked deliverable and the path-filter cannot keep only the tip. Removing them needs a per-commit filter beyond the "same method".
3. The clone's on-disk cleanliness (venv/figures absent from the fetched pack) is asserted from the supervisor's local-side evidence, not from inspecting the completed clone.
