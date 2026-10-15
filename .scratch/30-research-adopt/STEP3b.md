# STEP3b — `/home/z/hf/research`: back up, rewrite the unpushed range, reclaim 3.52 GiB

Repo: `/home/z/hf/research`, branch `main`, remote `git@github.com:ZisIsNotZis/tiny-llm-eval-factors.git` (public GitHub).
Git: `git version 2.43.0`. `git filter-repo` absent; `git filter-branch` present at `/usr/lib/git-core/git-filter-branch`.
Run at 2026-10-14 ~19:57–19:59 +08:00.

> Note: the task text named the remote `…/tiny-llm-ebooks…`; `git remote -v` says `…/tiny-llm-eval-factors.git`. Per the task, `git remote -v` is authoritative — that is the remote used (and never touched).

## TLDR

- The venv is **0** objects of `origin/main`'s history and **79,682** of `origin/main..main` — re-confirmed. So the bloat is entirely in the unpushed range.
- A verified mirror backup exists outside the repo; the unpushed 122 commits were rewritten (index-filter) to drop `.wrapup/lmenv`; the remote's 9 commits keep their hashes.
- `.git` went **3.6 GiB → 19 MiB** (3,799,114,358 → 19,302,175 bytes, reclaimed **3.52 GiB**).
- The push would be a plain fast-forward; **no `git push` was run**.

---

## 1. Measurement re-confirmed (the stop condition did not trigger)

| probe | result |
|---|---:|
| `git rev-list --objects origin/main \| grep -c '\.wrapup/lmenv'` | **0** |
| `git rev-list --objects origin/main..main \| grep -c '\.wrapup/lmenv'` | **79,682** |
| `git rev-list --count origin/main` | 9 |
| `git rev-list --count main` | 131 |
| `git rev-list --count origin/main..main` | 122 |

The venv appears **nowhere** in `origin/main`'s history, so the rewrite of the unpushed range is sufficient and **no force push is needed** — the stop condition for step 1 did not apply.

## 2. Backup (made and verified before anything else)

- Path: **`/home/z/vibe/.scratch/30-research-adopt/research-mirror.git`** (outside the repo; `/home/z/vibe` is on `/`, 183 GB free).
- Command: `git clone --mirror --no-hardlinks /home/z/hf/research <backup>` — `--no-hardlinks` forces a true copy, so the two `.git` dirs are independent (verified: every pack file has `links=1` on both sides, distinct inodes).
- Verification:
  - `git -C <backup> rev-list --count --all` → **131** (matches the source; `origin/main` is a 9-commit subset).
  - `git -C <backup> fsck --no-progress` → **clean, exit 0**.
  - `git -C <backup> rev-list --objects --all | grep -c '\.wrapup/lmenv'` → **79,682** (the venv history is preserved).
  - refs: `main = 0efda6f9c0fac6da2f1e7a691bdab57f4178a3b3`, `origin/main = 8903c173ce7e21c4ee01c6548ed931f44b61a454` — the pre-rewrite tip.
  - Size 3.6 GiB (3,799,011,787 bytes).
  - Re-verified **after** the source `git gc` — still 131 commits, 79,682 venv objects, `main` still `0efda6f9c`, `fsck` clean.
- **Retained** until the report is accepted.

## 3. Rewrite — unpushed range only

```
FILTER_BRANCH_SQUELCH_WARNING=1 git filter-branch --force --index-filter \
  'git rm -r --cached --ignore-unmatch .wrapup/lmenv' -- origin/main..main
```

`--index-filter` is the fast form (no tree checkout per commit); the range `origin/main..main` excludes the remote's commits. Took **44 s**.

| probe after rewrite | result |
|---|---|
| `git rev-parse main` | `9baaa32b085772133212c1a40f7d2bba638a233e` (rewritten) |
| `git rev-parse origin/main` | `8903c173ce7e21c4ee01c6548ed931f44b61a454` (unchanged) |
| `git rev-list --count origin/main..main` | 122 (structure preserved; no `--prune-empty`) |
| venv objects in `origin/main..main` | **0** |
| first child of `origin/main`'s parent | still `8903c173…` (boundary intact) |
| `main` tip tree | `0dce6afe28ccb164b47860d6c0f7003b7c2d6c6a` — identical to the old tip's tree |
| per-commit scan `git ls-tree -r <c> -- .wrapup/lmenv` over all 122 | 0 hits |

The remote's nine commits keep their hashes (only `refs/heads/main` was rewritten; `refs/original/refs/heads/main` → `0efda6f9c` was the only backup ref).

## 4. Space reclaimed

```
rm -rf .git/refs/original
git reflog expire --expire=now --expire-unreachable=now --all
git gc --prune=now
```

| metric | before | after |
|---|---:|---:|
| `.git` (`du -sb`) | 3,799,114,358 B (**3.6 GiB**) | 19,302,175 B (**19 MiB**) |
| `size-pack` | 3.52 GiB | 18.33 MiB |
| `in-pack` objects | 81,374 | 1,986 |
| packs | 2 | 1 |
| loose objects | 294 (17.99 MiB) | 0 |

**Reclaimed 3,779,812,183 bytes = 3.52 GiB.** Largest remaining object is a 15.4 MB SQLite blob; the 375 MB `libcublasLt.so` and the rest of the venv are gone.

## 5. Proof of the result

1. **`.git` size before/after** — 3.6 GiB → 19 MiB (table above).
2. **Venv gone from history** — `git rev-list --objects --all | grep -c '\.wrapup/lmenv'` = **0**; `git log --all --oneline -- .wrapup/lmenv` = **0** lines; no reflog entry references the old commit.
3. **`git fsck --no-progress`** — **exit 0, no output** (clean).
4. **Working tree intact** — `.wrapup/lmenv` still on disk (8.9 GiB); `git ls-files` = 409 tracked files, **0 missing on disk**; `git status --porcelain` = the same 8 untracked entries as before (the `docs/<layer>/` YAML dirs + `docs/check_docs.py`); tip tree hash unchanged (`0dce6afe`). `experiments.sqlite` (15,462,400 B, mtime Oct 14 06:54) and `docs/check_docs.py` untouched; the 14 `docs/*/*.yaml` untouched.
5. **Fast-forward gate** — `git merge-base --is-ancestor origin/main main` → **TRUE** (exit 0). The push would fast-forward, not force.
6. **Ten `docs/*.md` byte-identical** — `sha256sum -c` on all ten (plus root `AGENTS.md`) → **all OK**; hashes match `BASELINE.txt` recorded at 2026-10-14T11:31:11Z.
7. **`python3 docs/check_docs.py`** — **PASS** (exit 0).

## Bounds honoured

- **No `git push`. Remote untouched.** Nothing installed.
- `experiments.sqlite`, the ten `.md` files, and `docs/*/*.yaml` untouched.
- Scope: only `.wrapup/lmenv` removed from the unpushed history (the named change). Other regenerable paths that commit `0efda6f9c` untracked (`mres`, `dl_ready`, `ppl_corpora`, `jars`, old `experiments.sqlite` blobs, `report.html`) remain in that history — they are now negligible (the whole pack is 18.33 MiB), so no widening was needed.
- Write locations: `/home/z/hf/research/.git` (rewrite + gc) and this report. Backup kept.

## The push command NOT run

```
git push origin main
```

No `--force` and no `--force-with-lease`: `origin/main` is an ancestor of the new `main`, so this is an ordinary fast-forward. It was **not** executed and the remote was never contacted.

## Evidence files

- `/tmp/step3b_before.txt` — pre-rewrite sizes, hashes, commit list.
- `/tmp/step3b_docs_before.txt` — pre-rewrite `sha256sum` of the ten docs + `AGENTS.md`.
- `/home/z/vibe/.scratch/30-research-adopt/research-mirror.git` — the backup.
