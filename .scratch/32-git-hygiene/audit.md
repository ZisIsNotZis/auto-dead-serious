# Git hygiene audit — milestone 1 package 2 (blocked before repository scan)

- Result: **incomplete and blocked**, not a clean audit.
- Stop reason: no machine-wide exclusive-use window/owner or coordinated admission grant was established. The parent confirmed that the user’s `go` and the one-worker constraint do not imply exclusive machine control. Do not begin the 85-repository status/path/history/content/credential scan until the missing resource authority/evidence is established.
- No repository status, tracked-path, submodule/worktree, history/blob, current-content, historical-content, credential-pattern, or symlink-target marker scan ran. The prepared `audit_repos.py` was not executed. No repository or remote was changed.
- Scope reconciliation: 86 manifest child paths = 83 with HEAD, 2 unborn, 1 unresolved; 85 resolved repositories received only lightweight current HEAD and remote metadata queries. The unresolved pointer was not queried or repaired. No direct Help Agent audit/query was intentionally run. However, the initial root `git status --short --branch` was not configured to ignore submodules, and captured `evidence/root-status.txt` contains ` M helpagent`; that command may have queried Help Agent submodule status. Complete exclusion from indirect status inspection therefore cannot be confirmed. No follow-up was made.
- Root is baseline only: `/home/z/vibe` HEAD `7ace6bf5dd1f23c85fcaf17e5fbbb19913c79d76`; no root hygiene scan ran.
- The vetted scanner availability check found `gitleaks`, `trufflehog`, and `detect-secrets` unavailable. The bounded fallback patterns were not run because the resource stop occurred first.

## Remote-name correction

- `git remote` returned 87 registered remote names across 85 resolved repositories; 85 resolved repositories had at least one name and 0 had no names.
- 84 registered names returned both fetch and push URLs. 3 registered names had neither fetch nor push URL; these are URL-less/incomplete names, not usable GitHub remotes: `/home/z/vibe/dojo` (`origin`), `/home/z/vibe/murderMysteryGame` (`origin`), `/home/z/vibe/pi-keys` (`origin`).
- The manifest's stale aggregate (`1 with no remotes`) is superseded by direct `git remote` names: 87 names and no empty name list; the three entries above have no fetch or push URL. URL endpoint reachability was not tested. The manifest was left unchanged while it was read; its dated follow-up now records this correction and provenance.
- Exact read-only procedure per resolved repository: `git -C <repo> rev-parse --verify HEAD`; for unborn repositories, `git -C <repo> symbolic-ref --quiet HEAD`; `git -C <repo> remote`; and for each returned name only, `git -C <repo> remote get-url --all <name>` and `git -C <repo> remote get-url --push --all <name>`. No fetch or GitHub/API request was made. URL user-info/query/fragment were redacted before persistence.
- Remote evidence: `evidence/remote-only.jsonl` (per-repository commands, exit statuses, current HEAD and sanitized results) and `evidence/remote-only-summary.json` (counts and unchanged manifest hash).

## Repository-by-repository scan state

Every manifest path is listed below. A dash means **not measured**, not zero or clean. Remote names and URL usability are the separate metadata-only result; all hygiene categories remain unscanned.

| Repository | Manifest/current HEAD state | Registered remote names | Registered remotes with both fetch and push URLs | Tracked unstaged | Staged | Untracked nonignored | Ignored | Tracked-but-ignored | Hygiene audit |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| `/home/z/vibe/aps` | `5c87e1d1e966` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/mux` | `7aa19bbbb95b` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/horse_video` | `465b41f74d51` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/huaqiang_video` | `af86cc715f95` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/huaqiang_game` | `77878f00f8dc` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/timecolumn` | `d73a5225c45e` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/npchallenge` | `006033ca36d9` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/vibeos` | `b81f0e248c07` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/vibeos/vendor/hyperframes` | `2ca578f9455c` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/hyperframaker` | `ed4dcf0403f1` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/hyperframaker/vendor/remotion` | `7fc6dea33386` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/hyperframaker/vendor/hyperframes` | `1b86b561273e` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/tutor_private` | `c39847a2a4c2` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/colleague_private` | `300edf162a7d` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/auto_maintain_bench` | `b94c66aa3f8c` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/ideas` | `fbde8f6b5382` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/sys_gal` | `fe9628c5cbdf` | `origin`, `upstream` | 2 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/sys_gal/vendor/chinese-novelist-skill` | `3db1e3be8834` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/drive` | `6f803b4ca0f2` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/ra2` | `ed3712646988` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/ra2/vendor/svg-creator-skill` | `unresolved pointer; not queried` | unknown | — | — | — | — | — | — | not run; unresolved pointer retained |
| `/home/z/vibe/expyssion` | `fbb527c6a8f6` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/pathlm` | `b606d74467c5` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/pelican_bike` | `cc0da5b2eba2` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/learn_draw` | `24693d4b7647` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/learn_draw/vendor/huashu-art-motion` | `f178bd7754a7` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/learn_draw/vendor/huashu-design` | `0830494ecb1c` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/raid_calc` | `01d874f61b01` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/resume_private` | `ff06ff4532eb` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/fat_kakeya_needle` | `93c2740669a3` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/agentic-animation/vendor/remotion` | `357a270803b2` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/agentic-animation/vendor/svg-creator-skill` | `1eb83d602a99` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/agentic-animation/vendor/anthropic` | `3b3fad96af16` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/agentic-animation/vendor/huashu-design` | `0830494ecb1c` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/agentic-animation/vendor/huashu-art-motion` | `f178bd7754a7` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/agentic-animation` | `4213bc40b642` | `origin`, `upstream` | 2 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/mycar` | `cff764536376` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/hfget` | `27fa2be38bca` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/litellmgen` | `0701bd16dc03` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/flashdb` | `7d40cdb55ed9` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/danmaku` | `4382c344e064` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/backseat` | `69d7e0aef9e4` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/pushbus` | `4a3886af5c0d` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/tokenqr` | `487de9e5a95d` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/autofe` | `aaf3a4509321` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/agentworld` | `b318e8f405d1` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/resume_img_gen` | `93369f084745` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/sys_gal_rt` | `32c6c1059a74` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/resume_improve_loop` | `40fad9faea3c` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/lmlayer` | `6f5644cd14d3` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/cuda` | `1d5870f1d19d` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/cvorat` | `32f1a8ea99ad` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/myzcopy` | `1cdbdaa777c8` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/dino.py` | `39536bf1d99d` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/causalmlp` | `a6495d95ed4b` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/fring` | `2b79c9743345` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/treui` | `bae8fa937f10` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/tok` | `1102916e118b` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/myygo` | `a82e1ec1eeb9` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/myminio2` | `c6ac114f35de` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/http_mock` | `7a6c09b68f07` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/cz_noidea` | `79ac1f44dc97` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/beam` | `d0ed13d49dc4` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/ygo` | `b4c10f252caa` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/uv` | `0ea562c36dbf` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/misc` | `fe6f9fb158a0` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/nn` | `e52d2326f079` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/disk` | `0bc874a810f4` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/cz_bert` | `60ccef5f2f9e` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/jpi.fe` | `dc60bfcb0ee8` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/cznn` | `0498a4c6e98b` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/dinoseg` | `b6ffba4f0bb3` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/io_uring-echo-server` | `08a064c6eb42` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/ringsvr` | `ceba00a3ea7d` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/myminio` | `aee639bbd406` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/xywdisk` | `eceac7a764a3` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/retnet` | `739dd39ead47` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/knowledge_net` | `233189629a6f` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/cz_einn` | `16f3f0ca7368` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/neuronloop` | `28a7387a12b0` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/grammar` | `efc4ac6ddd64` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/seq_autoenc` | `d78cf70bc3ca` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/dojo` | `unborn:master` | `origin` | 0 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/murderMysteryGame` | `c00187841495` | `origin` | 0 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/pi-keys` | `unborn:master` | `origin` | 0 | — | — | — | — | — | not run; resource coordination blocker |
| `/home/z/vibe/local_lm_research` | `9c6fb9d4c52a` | `origin` | 1 | — | — | — | — | — | not run; resource coordination blocker |

## Outstanding findings and next action

- No repository can be called clean and no file-specific junk candidate can be classified from this blocked run. Proposed action for each resolved repository is to defer cleanup decisions until the bounded audit is authorized and completed; do not delete or edit paths. For `dojo`, `murderMysteryGame`, and `pi-keys`, later review whether their URL-less `origin` names are intentional; do not add or repair URLs here. For `ra2/vendor/svg-creator-skill`, retain the unresolved state and do not repair it.
- Symlink coverage remains unknown. The prior inventory used no-follow traversal; no follow-up link/`.git` marker search ran under the resource stop. Potential repositories reachable only through symlinked directories are not ruled out, and `helpagent` must remain excluded.
- Local tracking/ahead/behind state, status categories, tracked junk candidates, submodule/worktree state, largest blobs, >100 MiB list, and credential findings are all unmeasured. Remote/unfetched refs and GitHub existence/visibility are also unverified.
- Evidence bounds: `evidence/remote-only.jsonl`, `evidence/remote-only-summary.json`, `evidence/credential-scanner-availability.txt`; ticket and manifest addenda record the stop, reviewer finding, provenance, and missing resource grant. The existing manifest path/HEAD inventory remains the source for the blocked path list.
