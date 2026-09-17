# 01 — Make policy selective, autonomous, and easy to follow

- **Status:** done
- **Blocked by:** none
- **Assignee:** main orchestrator + delegated writer
- **Need-review:** passed
- **Need-test-cases:** none (policy text; verification = routing audit, citation check, size measurement, diff check, fresh-context review)

## Issue

The current split does not deliver true selective loading: `AGENTS.md` is small, but `docs/policy/reference.md` remains one 43K-character file and the core says every reference rule always applies. Restructure it into a genuinely always-on core plus topic files loaded only by explicit triggers.

The user also set the operating philosophy:

1. Minimize user cognitive load through autonomous execution, not merely shorter prose.
2. Align once on the long-term goal, final outcome, roadmap, philosophy, methodology, and working granularity; then carry the routine workflow without asking for step-by-step permission.
3. Stop only for a blocking serious failure/surprise, an action only the user can perform, a user-facing acceptance milestone, or a material user-owned decision.
4. Never stop merely because one routine step finished or ask whether to continue an already-approved objective.
5. The main AGI preserves context for orchestration, scheduling, decision management, and acceptance. Long or complex execution belongs to subagents; complex validation may itself be delegated. The main remains accountable for synthesis and final acceptance.
6. User-facing reports are plain, specific, and actionable. Every task code is accompanied by a short descriptive name; codes such as D0/C1 never stand alone.
7. Avoid unexplained jargon and do not make the user repeat facts already supplied.
8. Autonomy starts only after the relevant goal, roadmap or milestone, design philosophy, methodology, and working granularity are clear and mutually aligned. Never silently choose among materially different interpretations using reasoning such as “probably X”; surface material ambiguity with the smallest high-information question, while leaving routine implementation discretion autonomous. After alignment, continue until a four-gate interruption condition.

## Acceptance criteria

- [x] `AGENTS.md` contains only genuinely always-on policy plus a deterministic load-routing table.
- [x] Topic files each state when to load, when not to load, and their completion/exit criteria.
- [x] No rule claims unloaded topic files still apply.
- [x] The ordinary approved workflow continues automatically until one of the four user-intervention gates occurs.
- [x] Long/complex work is delegated; the main context is reserved for orchestration and acceptance, with a practical small-task exception.
- [x] User-facing task references pair every code with a descriptive name.
- [x] Reports lead with outcome/action, use plain language, and never ask the user to repeat known context.
- [x] Existing policy meaning is mapped, deliberately retained/rewritten/deleted, with no unresolved citations.
- [x] `WORKSPACE.md` describes the new policy topology and gate commands.
- [x] `wc -m` before/after, `git diff --check`, scoped reread, and fresh-context review are recorded.

## Comments

- 2026-09-15 (main orchestrator, pi) — Created and claimed after the user approved true selective loading and supplied the autonomous-operation philosophy above. Existing unrelated dirty workspace state was present before this ticket and must not be modified.
- 2026-09-15 (delegated writer, pi) — Implemented the approved selective-loading migration without committing, staging, or touching unrelated pre-existing dirty paths. Final acceptance remains review-gated.
- 2026-09-15 (user clarification, recorded by delegated writer) — Alignment on the relevant goal, roadmap or milestone, design philosophy, methodology, and working granularity is the precondition for autonomy; material ambiguity must be surfaced rather than guessed, while routine implementation discretion continues without step-by-step permission.
- 2026-09-15 (delegated writer, pi) — Applied the clarification to the always-on authorization boundary, collaboration question/interpretation rules, and autonomous design rule; reran scoped policy validation. Fresh-context review remains pending.
- 2026-09-17 (fresh-context policy reviewer) — Review verdict: blocked. F4 found that `R-INT.7` still duplicated the always-on first-use/no-bare-code rule retained in `AGENTS.md`; the detailed collaboration checklist otherwise remained correct.
- 2026-09-17 (delegated writer, pi) — Fixed F4 by removing only the duplicate sentence from `R-INT.7`; kept the always-on `AGENTS.md` reporting floor unchanged and preserved the outcome-first, register, medium, pushback, and report-review guidance.
- 2026-09-17 (fresh-context policy reviewer, pi) — Final review of the full selective-loading scope passed with no findings. Verified F4 has one authoritative home, deterministic routing remains intact, all acceptance criteria are satisfied, and the manifest covers every scoped artifact. Reviewed manifest SHA-256 before administrative closeout: `112cd029f5ff044ddb9aa38fce6a98826f5c877cdaac1736c0b14b12ffc461b8`. Verdict: **accept / Merge verdict: OK**.

## Baseline

| Artifact | Characters before |
|---|---:|
| `AGENTS.md` | 8,090 |
| `docs/policy/reference.md` | 43,401 |
| `docs/policy/remote-coordination.md` | 4,369 |
| `WORKSPACE.md` | 2,723 |
| **Total** | **58,583** |

## Implementation ledger

| Previous responsibility | New authoritative home | Treatment |
|---|---|---|
| Always-applicable contract and approval/go-signal rules | `AGENTS.md` | Rewritten as alignment-qualified objective authorization, four intervention gates, always-on safety, delegation ownership, report rule, and deterministic router. |
| `R-INT` | `collaboration.md`; `R-INT.9`–`R-INT.10` in `design.md` | Retained useful IDs; removed per-slice permission, question quotas, and personal profiling. |
| `R-DOC` | `documentation.md` | Retained IDs; corrected source-layer precedence and replaced one-pass monolith disclosure with selective-topic review. |
| `R-TKT`, `R-SES` | `work-management.md`; `R-SES.1.2` in `delegation.md` | Retained statuses and ticket/review mechanics; trivial same-session fixes no longer require a physical ticket; attempt thresholds no longer force user interruption. |
| `R-DEL` | `delegation.md` | Replaced file-count routing and fixed model thresholds with complexity/capability tests; retained parent accountability and safe fallbacks. |
| `R-ENV`, repository `R-REP` | `environment-and-repository.md` | Removed volatile tool rankings and demographic assumptions; retained project-convention, verification, scaffold, and cleanup behavior. |
| `R-DSN`; `R-INT.9`–`R-INT.10` | `design.md` | Retained live IDs and autonomous design analysis; former `R-DSN.4`, `.6`, and `.13` remain retired. |
| `R-BLD`, `R-REP.4` | `build-and-validation.md` | Gates now come from `WORKSPACE.md` with risk-driven additions; evidence and subjective review no longer force user review when a subagent is absent. |
| `R-STG` | deleted | Router replaces the stage-role abstraction; no active policy citation remains. |
| `R-REM` | `remote-coordination.md` | Rewritten as remote-only, event/transition-based coordination with explicit applicability and exit. |
| Core `S1-S5` | `policy-maintenance.md` | Retained as scoped policy admission, size, audit, review, and topology-change rules. |
| `reference.md` | deleted | All retained live definitions migrated before deletion; no forwarding rules remain. |

## Final measurements

| Artifact | Characters after |
|---|---:|
| `AGENTS.md` | 7,559 |
| `WORKSPACE.md` | 2,957 |
| `docs/policy/build-and-validation.md` | 3,652 |
| `docs/policy/collaboration.md` | 5,687 |
| `docs/policy/delegation.md` | 4,476 |
| `docs/policy/design.md` | 4,925 |
| `docs/policy/documentation.md` | 6,508 |
| `docs/policy/environment-and-repository.md` | 5,361 |
| `docs/policy/policy-maintenance.md` | 2,736 |
| `docs/policy/remote-coordination.md` | 3,244 |
| `docs/policy/work-management.md` | 6,266 |
| **Total** | **53,371** |
| **Delta from 58,583 baseline** | **-5,212** |

`AGENTS.md` is 531 characters smaller than the prior core but exceeds the approximate 3,500–5,000 target because the approved alignment boundary, four-column nine-route table, and six applicability semantics remain always-on. Every topic is below the 12,000-character review signal.

## Verification record

| Command | Result |
|---|---|
| `find docs/policy -maxdepth 1 -type f -name '*.md' -print \| sort` | Passed: exactly the nine intended scoped policy files; `reference.md` absent. |
| `wc -m AGENTS.md WORKSPACE.md docs/policy/*.md` | Passed after the alignment clarification: 53,371 characters total, down 5,212 from baseline. |
| Per-file `rg -F -c` for `Load when:`, `Do not load when:`, `Applies while:`, `Exit when:` | Passed: each field occurs exactly once in every topic. |
| `rg -n 'reference\\.md\|R-STG\|applies always\|always applies\|then ask\|wait for approval\|confirm before\|user review gates' AGENTS.md WORKSPACE.md docs/policy` | Passed: no stale topology, retired stage, universal-topic, or unconditional approval phrasing. |
| Initial literal three-file `mutually aligned` count | Failed narrowly: `design.md` used the equivalent phrase “one coherent basis”; no policy defect found. Replaced with the semantic audit below. |
| `rg` alignment audit for `mutually aligned\|one coherent basis`, material interpretations, smallest high-information question, routine discretion, and post-alignment continuation | Passed in `AGENTS.md`, `collaboration.md`, and `design.md`. |
| `rg -o 'R-[A-Z]+(?:\\.[0-9]+(?:\\.[0-9]+)?)?' AGENTS.md WORKSPACE.md docs/policy/*.md` plus definition-resolution script | Passed: 100 specific definitions; no duplicate definition or unresolved active specific citation. |
| `git diff --check` | Passed with no output. |
| `git diff --cached --name-only` | Passed with no output; no files are staged. |
| Full scoped diff reread (`/tmp/vibe-policy-16.diff`) and alignment follow-up reread (`/tmp/vibe-policy-16-alignment.diff`) | Passed: all scoped additions, modifications, deletion, and clarification changes inspected; no unrelated path included. |
| Fresh-context policy review | Pending; `Need-review: yes` remains open and final review is not claimed. |

## Accepted review findings and follow-up fixes

2026-09-17 review scope: the reviewer accepted three blocking findings against the full selective-loading change. The delegated writer fixed them without committing, staging, or modifying child repositories or other unrelated dirty paths.

| Finding | Verified problem | Fix and disposition |
|---|---|---|
| F1 — Deterministic topic routing | Documentation review was both a load trigger and part of the broad read-only exclusion. Build/validation also named every completion claim while excluding documentation-only/read-only work. Delegation and work-management had narrower trigger/exclusion boundary ambiguities. | Added always-on load-over-exclusion precedence; made documentation review an explicit exception to read-only inspection; restricted build/validation completion claims to executable-artifact work; made delegation and work-management exclusions subordinate and disjoint. Audited all nine topic headers; every load/exclusion pair is now disjoint and every four-field header occurs exactly once in order. |
| F2 — Root/child precedence | The core named only the nearest `AGENTS.md`, omitted platform-equivalent `CLAUDE.md`, and did not preserve a root safety/evidence floor against child overrides. `WORKSPACE.md` repeated the incomplete nearest-file wording. | Defined the root-to-leaf instruction chain, same-directory `AGENTS.md`/`CLAUDE.md` handling, deterministic same-directory conflict resolution, nearest-child specialization, and the non-weakenable root safeguards, intervention gates, evidence, and validation floor. Updated `WORKSPACE.md` to match. The child-compatibility audit below found no child edit necessary. |
| F3 — Duplicate reporting authority | Detailed outcome/report behavior was stated in both always-on `AGENTS.md` and `collaboration.md`. | Reduced the core to the indispensable always-on identifier rule: each code's first user-facing use includes a descriptive name and a bare code is forbidden. Detailed outcome-first/report-review behavior remains authoritative in `collaboration.md` under `R-INT.7`. |
| F4 — Duplicate first-use reporting sentence | The prior F3 fix left the first-use/no-bare-code sentence in both the always-on reporting floor and `R-INT.7`, so one behavior still had two authoritative formulations. | Removed only that duplicate sentence from `R-INT.7`. The always-on rule remains unchanged in `AGENTS.md`; `R-INT.7` still owns outcome-first sequencing, plain language, medium choice, actionable pushback, and the report-review checklist. The prior review verdict is blocked and rereview remains required. |

## Child-instruction compatibility audit

- Scope: recursively inspected all 37 current `AGENTS.md`/`CLAUDE.md` paths outside `.git` (29 regular files and 8 symlinks): the 2 root paths plus 35 child paths (28 regular files and 7 symlinks). Hash/size inventory and keyword review covered empty generated-node instructions, immediate child roots, nested HyperFrames vendor instructions, and template instructions.
- Equivalent names: eleven child directories contain both names. Nine pairs are identical or symlinked; the two differing pairs are `hyperframaker/vendor/hyperframes` and `vibeos/vendor/hyperframes`. Under the new rule both differing files apply, with local `AGENTS.md` resolving only same-directory conflicts and nonconflicting `CLAUDE.md` platform detail retained.
- Broad child wording: `mycar/AGENTS.md` says its file wins conflicts, and `raid_calc/AGENTS.md` says product/design truth overrides its local guide. The root chain now qualifies the former to non-floor specialization and the latter to product/design decisions; neither can bypass root safeguards, intervention gates, evidence, or validation. Empty child files inherit the chain rather than erasing it.
- Safety/evidence result: no child instruction authorizes secret disclosure, destructive or history-rewriting action without applicable authority, overwriting unrelated work, or an unsupported completion claim. Child-specific language, project contracts, tests, visual gates, and reporting requirements only specialize or strengthen the root floor. No child file was modified.

## Follow-up measurements

| Artifact | Characters before follow-up | Characters after follow-up | Delta |
|---|---:|---:|---:|
| `AGENTS.md` | 7,559 | 8,401 | +842 |
| `WORKSPACE.md` | 2,957 | 3,090 | +133 |
| `docs/policy/build-and-validation.md` | 3,652 | 3,724 | +72 |
| `docs/policy/collaboration.md` | 5,687 | 5,687 | 0 |
| `docs/policy/delegation.md` | 4,476 | 4,534 | +58 |
| `docs/policy/design.md` | 4,925 | 4,925 | 0 |
| `docs/policy/documentation.md` | 6,508 | 6,540 | +32 |
| `docs/policy/environment-and-repository.md` | 5,361 | 5,361 | 0 |
| `docs/policy/policy-maintenance.md` | 2,736 | 2,736 | 0 |
| `docs/policy/remote-coordination.md` | 3,244 | 3,244 | 0 |
| `docs/policy/work-management.md` | 6,266 | 6,338 | +72 |
| **Total** | **53,371** | **54,580** | **+1,209** |
| **Delta from original 58,583 baseline** |  | **-4,003** |  |

The follow-up growth is the accepted precedence/routing clarification, not new workflow surface. Every topic remains below the 12,000-character review signal.

## Follow-up verification record

| Command / audit | Result |
|---|---|
| `find docs/policy -maxdepth 1 -type f -name '*.md' -print \| sort` | Passed: exactly nine topic files; deleted `reference.md` remains absent. |
| `wc -m AGENTS.md WORKSPACE.md docs/policy/*.md` | Passed: 54,580 characters total; +1,209 from the pre-follow-up selective-loading revision and -4,003 from the original baseline. |
| Header order/count and semantic boundary Python audit over `docs/policy/*.md` | Passed: each of the four fields occurs once and in order in all nine topics; every exclusion is disjoint from its load trigger. |
| Definition/citation Python audit over `AGENTS.md`, `WORKSPACE.md`, and `docs/policy/*.md` | Passed after correcting an audit-script regex typo: 105 unique specific definitions (100 `R-*`, 5 `S*`), 115 citations, no duplicate definitions, no unresolved specific citation. |
| Router/topology Python audit plus policy-file `find` | Passed: nine topic files, nine router entries, no `reference.md`, `R-STG`, or universal-topic stale marker. |
| Recursive child-instruction manifest, SHA-256, pair comparison, and safety/evidence keyword review | Passed: 37 instruction paths audited; two differing same-directory name pairs are deterministically resolved; no child weakening requires a file edit. |
| First-pass header validator | Failed due to a case-sensitive expected-string bug (`Executable` versus lowercase source); corrected validator passed without a policy change. |
| First-pass citation validator | Failed due to an unclosed validator regex group; corrected validator passed without a policy change. |
| First-pass child pair-count assertion | Failed because the expected count omitted one duplicated vendor template pair; the corrected 11-pair child inventory passed and the ticket count was fixed. |
| `git diff --check` | Passed with no output after follow-up policy and ticket edits; final rerun is part of the handoff gate. |
| Full scoped diff reread | Passed on the final policy/ticket content: all scoped tracked diffs and complete untracked policy/ticket/manifest files were inspected; no unrelated path is included. |
| Full-scope manifest/hash including untracked files | Passed: `.scratch/16-policy-selective-loading/review-scope-2026-09-17.sha256` covers root aliases, `WORKSPACE.md`, all topic files, this ticket, and the deleted legacy path marker; its detached digest is reported in the handoff. |
| Follow-up fresh-context review | Blocked: F4 found that the first-use/no-bare-code behavior still appeared in both `AGENTS.md` and `R-INT.7`. The narrow fix below addresses it, but `Need-review: yes` remains open pending rereview. |

## Final narrow review fix

| Artifact | Before F4 fix | After F4 fix | Delta |
|---|---:|---:|---:|
| `AGENTS.md` | 8,401 | 8,401 | 0 |
| `docs/policy/collaboration.md` | 5,687 | 5,525 | -162 |
| All measured policy artifacts | 54,580 | 54,418 | -162 |
| Delta from original 58,583 baseline | -4,003 | -4,165 | -162 |

| Command / audit | Result |
|---|---|
| `rg -ni 'first use in each user-facing message|bare code' AGENTS.md docs/policy/collaboration.md` | Passed: the first-use/no-bare-code requirement appears only in the unchanged always-on reporting floor; `R-INT.7` retains the detailed outcome-first checklist without restating it. |
| Header, definition/citation, and router/topology Python audit | Passed after correcting two validator-only assumptions: all nine topics have the four fields once and in order; 105 specific definitions and 156 citations have no duplicates or unresolved specifics; nine router rows cover nine policy files with no stale legacy/universal marker. |
| `wc -m AGENTS.md WORKSPACE.md docs/policy/*.md` | Passed: 54,418 characters total, 162 fewer than the blocked-review scope and 4,165 fewer than the original baseline. |
| `git diff --check` | Passed with no output. |
| Full narrow diff reread | Passed: the policy edit removes only the duplicate sentence, the ticket records the blocked finding and fix, and no unrelated dirty path is part of this task. |
| Full-scope manifest regeneration and verification | Passed: `.scratch/16-policy-selective-loading/review-scope-2026-09-17.sha256` was regenerated after the fix and verifies all present entries plus the deleted legacy-path marker. |
| Final fresh-context review | Passed: fresh reviewer found no issues, confirmed all acceptance criteria and the full manifest, and returned `Merge verdict: OK`. |
