## Commands and results (exact, re-run at final revision)

### 1) Baseline capture (before edits)
```
$ for f in AGENTS.md docs/policy/execution.md; do ... sha256sum; done
AGENTS.md: lines=37 bytes=5408 sha256=19c6c4995f84bc67a941d2ca6b14a3364622e2e819f3cd51f56ba32730e98dcc
docs/policy/execution.md: lines=46 bytes=9859 sha256=d84d0b448f2879cf5fd9423b4bb91a2e2ad2a011d725e76cf4e9042dd5c31bde
```

### 2) Final metrics (after edits)
```
AGENTS.md: lines=37 bytes=6281 sha256=ae5987bc16e3a4425ac8d9bba68433b1c95f85a0327e55d87cef2e1c4f6743f5
docs/policy/execution.md: lines=46 bytes=10238 sha256=9b38952dec94de142872bfecfac4de06ad9340dc415ebebd7fb95afc2a4007ca
```

### 3) Scoped baseline->final diff
```
--- .scratch/24-delegation-ssot-context/baseline/AGENTS.md	2026-10-09 19:53:26.493754694 +0800
+++ AGENTS.md	2026-10-09 19:53:29.511686623 +0800
@@ -13,17 +13,17 @@
 - Preserve unrelated/pre-existing work. Never record/commit secrets; contain exposure and arrange rotation. Destruction, history rewriting, material dependency changes, changes to approved contracts/trade-offs, material spending, privacy/legal exposure, and high-risk operations need covering authority; autonomy alone is insufficient. Covered actions need no repeat permission.
 - Bound work, concurrency, depth, review and no-progress attempts by finite limits. Long commands/jobs need a deadline or cancellation path and observable completion through foreground execution, verified notification, or bounded active checks. Detached jobs/records are not continuation.
 - Completion requires full agreed acceptance, revision-bound self-proof and fresh independent review, with limits disclosed. Blocked/unverified acceptance or exhausted resources are not PASS. Do not claim zero unknown defects or runtime enforcement. Technical acceptance does not authorize publication.
-- Communicate task contracts, decisions, evidence and handoffs through durable files, not agent conversations/transcripts. Control signals carry only minimal status/artifact pointers or required authority/infrastructure escalation. Each role reads only what it needs.
+- Communicate task contracts, decisions, evidence and handoffs through durable files, not agent conversations/transcripts. Every task creates or updates a ticket; tickets are the log home for history, provenance and process narrative. All documents, in every form, hold current facts only and are rewritten in place on change: no dated narrative, changelogs, errata, "was A, later B", dashboard timestamps, duplication, stale content or conflicting statements. Control signals carry only minimal status/artifact pointers or required authority/infrastructure escalation. Each role reads only what it needs.
 
 ## Roles
 
-**Main — product owner:** exclusively own user dialogue, intent, authority, confirmed principles, milestones, status/routing and concise delivery. Delegate every substantive task, even small/indivisible work. Never implement or technically verify; unavailable delegation is an infrastructure blocker, not a fallback to direct work. Route inspection and technical acceptance to workers and independent reviewers.
+**Main — product owner (highest-priority role rule):** manage only user dialogue, intent, authority, confirmed principles, milestones, status/routing and concise delivery. Perform no substantive work of any kind — no implementation, no verification, no inspection/review and no document writing — and delegate every task, including all documentation, to a sub agent. This obligation is unconditional and governs whenever this rule is read, regardless of session age or inherited/stale context. Never implement or technically verify; unavailable delegation is an infrastructure blocker, not a fallback to direct work. Route inspection and technical acceptance to workers and independent reviewers.
 
 **Worker — execution:** before changes, record interpretation, scope, inherited acceptance, proof method, options/recommendation and split-versus-leaf decision; never lower acceptance. Self-test and leave revision-bound evidence. A leaf is a cohesive checkable outcome. Split into same-layer siblings with complete coverage, owners, interfaces, dependencies and an integration owner. At context pressure, checkpoint, then split independent remainders or hand an unsplittable remainder to a fresh replacement; do not invent context percentages.
 
 **Reviewer — independent acceptance:** use fresh context, never worker conversation; inspect final scoped artifacts and evidence, not completion claims. Repair material in-scope verifiable defects only with authority/tools; otherwise route a labelled writer fallback. Repair reuses the reviewer's context but makes them a worker, ending independent acceptance authority; the changed result needs another fresh reviewer. PASS needs documented proof, not speculative polish.
 
-Default to fresh narrow workers/reviewers. Worker inheritance is exceptional: session input itself must be necessary and mostly relevant, not a blanket documentation exception. Recursive delegation needs explicit permission, runtime support and the bounds above; never forward an unchanged task indefinitely.
+Default to fresh (non-inherited) context whenever a task is fully specifiable in a compact concrete handoff; inherit context only when a context-free description would cost more than inheriting, for example holistic documentation or policy work. Worker inheritance is exceptional: session input itself must be necessary and mostly relevant, not a blanket documentation exception. Independent review never inherits context. Recursive delegation needs explicit permission, runtime support and the bounds above; never forward an unchanged task indefinitely.
 
 ## Conditional methods
 
--- .scratch/24-delegation-ssot-context/baseline/execution.md	2026-10-09 19:53:26.501754513 +0800
+++ docs/policy/execution.md	2026-10-09 19:53:31.489642009 +0800
@@ -8,7 +8,7 @@
 - Before implementation, inspect task-relevant target/Git state and instructions/records, capture a scoped baseline when attribution matters, and write the worker contract. Resolve routine gaps with evidence and reversible choices. Record unmet criteria/dependencies rather than silently reducing acceptance.
 - Keep cohesive outcomes as leaves, not artificial editing/testing/reporting children. Split siblings at one abstraction layer, each with inputs, outputs, acceptance/proof, owner, interfaces, dependencies and exclusions; map complete parent coverage and assign a worker integration owner. Unequal size is fine; a parent goal beside its substep is not. Parallel writers need disjoint ownership and isolated branches/worktrees; establish interfaces/order before writing and check the combined result against the baseline.
 - On context pressure or resource exhaustion, checkpoint artifacts, revision, decisions, remaining acceptance and next actions. Split independent remainders with coverage/interfaces or route an unsplittable remainder to a fresh replacement under unchanged authority/acceptance. When attempts yield no useful evidence, change the hypothesis/check or route a bounded permitted specialist task; stop repetitive avenues and report incomplete, not an endless loop.
-- Use the project's work-record convention; absent one, use `.scratch/active-work.md` as an entry point. Preserve other entries. Keep unfinished work discoverable: objective/scope/acceptance, owner/status, input/output paths, authority/gates/user availability, decisions, baseline/current revision and dirt, checks/review and covered revision, blockers/next action, and any running-job result/continuation. After a status signal, continue the next authorized step. Remove only this task's active link after independent acceptance and any user gate. On resumption compare records with current target/Git state and rerun stale checks, not session memory.
+- Use the project's work-record convention; absent one, use `.scratch/active-work.md` as an entry point. Preserve other entries in the ticket/work-record ledger only — tickets are append-style, fact documents are not. Keep unfinished work discoverable: objective/scope/acceptance, owner/status, input/output paths, authority/gates/user availability, decisions, baseline/current revision and dirt, checks/review and covered revision, blockers/next action, and any running-job result/continuation. After a status signal, continue the next authorized step. Remove only this task's active link after independent acceptance and any user gate. On resumption compare records with current target/Git state and rerun stale checks, not session memory.
 
 ## Proof and review
 
@@ -26,7 +26,7 @@
 
 ## Documentation
 
-- Keep one authoritative home: human-facing README for overview/use/public design, owning `AGENTS.md` for enforceable shared agent boundaries, this companion for conditional methods, project docs for confirmed product decisions, work records for transient contracts/evidence/handoffs. Optional workspace notes hold unique task-relevant verified layout/commands/environment facts, not repeated rules or a startup requirement. Create documents/automation only for demonstrated need; retain raw provenance only when useful and safe.
+- Keep one authoritative home: human-facing README for overview/use/public design, owning `AGENTS.md` for enforceable shared agent boundaries, this companion for conditional methods, project docs for confirmed product decisions, work records for transient contracts/evidence/handoffs. Every task also creates or updates a ticket, and tickets are the log home for history, provenance and process narrative. Documents of every form hold current facts only and are rewritten in place on change, one home per fact, with no duplication, stale content or conflicting statements. Optional workspace notes hold unique task-relevant verified layout/commands/environment facts, not repeated rules or a startup requirement. Create documents/automation only for demonstrated need; retain raw provenance only when useful and safe.
 - Identify actor, event, action, checkable output and necessary exceptions. Remove repetition and prose that changes no decision/safeguard. Update changed contracts and live owning references with implementation; historical records need no rewrite when still recoverable. Keep policy independent of project facts/docs, model/platform, optional tools/trackers or assumed runtime guarantees.
 - For policy changes, record rationale/options, scoped baseline, core/package size and file count before/after; reread final scoped artifacts, check links/anchors/routing and scoped whitespace. Check concrete affected authority, safety, role, context and compatibility scenarios. Bind proof to final hashes/revision and distinguish documentation checks from untested runtime behavior/configuration. Size reduction must not hide mandatory bulk or remove safeguards.
 
```

### 4) git diff --check (scoped)
```
$ git diff --check -- AGENTS.md docs/policy/execution.md
exit=0
```

### 5) Link/anchor resolution + semantic self-check
```
$ python3 .scratch/24-delegation-ssot-context/validate.py
41/41 checks passed
wrote /home/z/vibe/.scratch/24-delegation-ssot-context/checks.json
exit=0
```

### 6) Index untouched (nothing staged)
```
$ git diff --cached --stat
exit=0 (empty output = nothing staged)
```

## Round 2 — commands and results (exact, re-run at round-2 revision)

### R1) Final metrics (round 2)
```
AGENTS.md: lines=37 bytes=6275 sha256=ca588165e9b80d48e0a02af80db4275f9f3736064049fdf87cf83911ab797e97
docs/policy/execution.md: lines=46 bytes=10086 sha256=bd76a2ff53778fb98979d263d371ebc61e042a893aa59b4b04d941567fe18102
```
(round-1 final was AGENTS.md 6281 / execution.md 10238; round 2 removes 158 bytes,
0 lines)

### R2) Scoped baseline->final diff regenerated
```
$ diff -u .scratch/24-delegation-ssot-context/baseline/AGENTS.md AGENTS.md > AGENTS.baseline-to-final.diff
$ diff -u .scratch/24-delegation-ssot-context/baseline/execution.md docs/policy/execution.md > execution.baseline-to-final.diff
$ cat <both> > baseline-to-final.diff
63 baseline-to-final.diff / 29 AGENTS / 34 execution lines
```

### R3) Semantic self-check + link/anchor + whitespace
```
$ python3 .scratch/24-delegation-ssot-context/validate.py
46/46 checks passed
wrote /home/z/vibe/.scratch/24-delegation-ssot-context/checks.json
exit=0
```
(validate.py updated: A8 literal re-capitalized; B8 pointer to core; B9/B10
verbatim-restatement-absent; B11 one-home-per-fact in core; R1-R5 for notes 1-4)

### R4) Scoped whitespace
```
$ git diff --check -- AGENTS.md docs/policy/execution.md
exit=0
```

### R5) Meaning preservation (each form once)
```
form                               AGENTS exec
one home per fact                  1      0
current facts only                 1      0
rewritten in place                 1      0
tickets are the log home           1      0
dated narrative/changelogs/errata/
  "was A, later B"/dashboard ts.   1      0
duplication/stale/conflicting      1      0
append-style                       0      1
no implementation..document writing 1      0
Unavailable delegation = blocker   1      0
```

### R6) Index untouched (nothing staged)
```
$ git diff --cached --stat
exit=0 (empty output = nothing staged)
```

## Round 3 — commands and results (exact, re-run at round-3 revision)

### R3-1) Round-2 revision reconstruction (attribution baseline)
```
$ patch -o /tmp/.../AGENTS.md .scratch/24-delegation-ssot-context/baseline/AGENTS.md < AGENTS.baseline-to-final.diff
$ patch -o /tmp/.../execution.md .scratch/24-delegation-ssot-context/baseline/execution.md < execution.baseline-to-final.diff
6275 /tmp/.../AGENTS.md
10086 /tmp/.../execution.md
```
(byte counts match round 2's `final-manifest.json`, so the round-2->3 delta below
is attributable.)

### R3-2) Final metrics (round 3)
```
AGENTS.md: lines=37 bytes=6632 sha256=9b28a9b614a6f436e74ad7a16245a62bf70ff539e4d52360c650d709400ad97b
docs/policy/execution.md: lines=46 bytes=10467 sha256=4b18a91e2ce92abdb9df4c0688f13bc537e24c0e482c9cef6258d004337f8c99
```
(round 2 was 6275 / 10086; round-3 delta +357 / +381 = **+738 bytes, 0 lines**)

### R3-3) Scoped baseline->final diffs regenerated
```
$ diff -u .scratch/.../baseline/AGENTS.md AGENTS.md > AGENTS.baseline-to-final.diff
$ diff -u .scratch/.../baseline/execution.md docs/policy/execution.md > execution.baseline-to-final.diff
$ cat <both> > baseline-to-final.diff
30 AGENTS.baseline-to-final.diff / 36 execution.baseline-to-final.diff / 66 baseline-to-final.diff lines
```

### R3-4) Round-2->round-3 diff size
```
$ diff -u <reconstructed round2>/AGENTS.md AGENTS.md | wc -l
23
$ diff -u <reconstructed round2>/execution.md docs/policy/execution.md | wc -l
11
```
(four changed lines total: AGENTS 16/22/26, execution 7)

### R3-5) Semantic self-check + link/anchor + whitespace
```
$ python3 .scratch/24-delegation-ssot-context/validate.py
68/68 checks passed
wrote /home/z/vibe/.scratch/24-delegation-ssot-context/checks.json
exit=0
```
(added D1-D5, E1-E6, F1-F6, G1-G5; all A/B/C/R, six link/anchor pairs and
`git diff --check` still pass)

### R3-6) Scoped whitespace
```
$ git diff --check -- AGENTS.md docs/policy/execution.md
exit=0
```

### R3-7) Meaning preservation (each rule once)
```
form                                     AGENTS exec
one home per fact                        1      0
current facts only                       1      0
rewritten in place on change             1      0
tickets are the log home                 1      0
append-style                             0      1
fork=                                    0      2
Agent-to-agent messages                  1      0
done/not-done                            1      0
Documents other than tickets             1      0
a worker subdivides its own assignment   1      0
```

### R3-8) Index untouched (nothing staged)
```
$ git diff --cached --stat
exit=0 (empty output = nothing staged)
```

### R3-9) Ticket status snapshot refreshed
```
$ git status --porcelain > .scratch/24-delegation-ssot-context/final-status.txt
```
(`final-status.txt` now reflects the round-3 tree: same modified set as round 1
plus the round-2/round-3 `.scratch` workflow files.)

## Round 4 — commands and results (exact, re-run at round-4 revision)

### R4-1) Round-3 revision reconstruction (attribution baseline)
```
$ patch -o /tmp/r3/AGENTS.md   .scratch/.../baseline/AGENTS.md   < AGENTS.baseline-to-final.diff    # round-3 diff as captured at round 3
$ patch -o /tmp/r3/execution.md .scratch/.../baseline/execution.md < execution.baseline-to-final.diff
/tmp/r3/AGENTS.md bytes=6632 sha256=9b28a9b614a6f436e74ad7a16245a62bf70ff539e4d52360c650d709400ad97b
/tmp/r3/execution.md bytes=10467 sha256=4b18a91e2ce92abdb9df4c0688f13bc537e24c0e482c9cef6258d004337f8c99
```
(both match the round-3 manifest, so the round-3→4 delta below is attributable)

### R4-2) Round-3 -> round-4 diff size
```
$ diff -u /tmp/r3/AGENTS.md AGENTS.md | wc -l
11
$ diff -u /tmp/r3/execution.md docs/policy/execution.md | wc -l
11
```
(two changed lines: `AGENTS.md:22`, `execution.md:7`; no other file changed)

### R4-3) Final metrics (round 4)
```
AGENTS.md: lines=37 bytes=6673 sha256=3f6584bcffd82b7e7ba0042558bdc24e479e5fdd4a677252b23654c8b7823003
docs/policy/execution.md: lines=46 bytes=10481 sha256=f6ab19fddbcf4ebcbe67320a8a90c3b4ceccc47d95bb48b3bee81d2186e48286
```
(round 3 was 6632 / 10467; round-4 delta +41 / +14 = **+55 bytes, 0 lines**)

### R4-4) Scoped baseline->final diffs regenerated
```
$ diff -u .scratch/.../baseline/AGENTS.md AGENTS.md > AGENTS.baseline-to-final.diff
$ diff -u .scratch/.../baseline/execution.md docs/policy/execution.md > execution.baseline-to-final.diff
$ cat <both> > baseline-to-final.diff
30 AGENTS.baseline-to-final.diff / 36 execution.baseline-to-final.diff / 66 baseline-to-final.diff lines
```

### R4-5) Semantic self-check + link/anchor + whitespace
```
$ python3 .scratch/24-delegation-ssot-context/validate.py
79/79 checks passed
wrote /home/z/vibe/.scratch/24-delegation-ssot-context/checks.json
exit=0
```
(round-3 checks updated for the new literals — D1 lowercase `split`, D2 core
permitted-only boundary, E3/E4 fork wording — plus added P1–P9 for P2-1/P2-2/P2-3)

### R4-6) Scoped whitespace
```
$ git diff --check -- AGENTS.md docs/policy/execution.md
exit=0
```

### R4-7) Link/anchor + one-home check
```
$ grep -oE '\]\([^)]+\)' AGENTS.md
](docs/policy/execution.md#task-routing)      <- new pointer in Worker role
](docs/policy/execution.md#task-routing)      <- existing Conditional methods link
](docs/policy/execution.md#proof-and-review)
](docs/policy/execution.md#product-decisions)
](docs/policy/execution.md#documentation)
](docs/policy/execution.md#environment)
](docs/policy/execution.md#remote-coordination)
$ grep -nE '^#{1,6} ' docs/policy/execution.md
1:# Conditional operating methods / 5:## Task routing / 13:## Proof and review /
20:## Product decisions / 27:## Documentation / 33:## Environment / 41:## Remote coordination
```
(seven core→companion link occurrences, six distinct anchors — all resolve; the
sibling enumeration now appears only at `execution.md:9`)

### R4-8) Index untouched (nothing staged)
```
$ git diff --cached --stat
exit=0 (empty output = nothing staged)
```

### R4-9) Ticket status snapshot refreshed
```
$ git status --porcelain > .scratch/24-delegation-ssot-context/final-status.txt
```
(`final-status.txt` reflects the round-4 tree.)

## Round 5 — commands and results (exact, re-run at round-5 revision)

### R5-1) Round-4 revision reconstruction (attribution baseline)
```
$ python3 -c "s=open('AGENTS.md').read(); r4=s.replace('defining and recording complete coverage and ownership','defining complete coverage and ownership'); print(len(r4.encode()), __import__('hashlib').sha256(r4.encode()).hexdigest())"
6673 3f6584bcffd82b7e7ba0042558bdc24e479e5fdd4a677252b23654c8b7823003
```
(the reconstruction matches the round-4 manifest, so the round-4→5 delta is
attributable)

### R5-2) Round-4 -> round-5 diff size
```
$ diff -u /tmp/r4-AGENTS.md AGENTS.md | wc -l
11
```
(one changed line, `AGENTS.md:22`: "defining" → "defining and recording";
`docs/policy/execution.md` unchanged)

### R5-3) Final metrics (round 5)
```
AGENTS.md: lines=37 bytes=6687 sha256=488316cbffd9d433d86878dd519b70ed90e56024ab25add1ef9c781ecb1f2065
docs/policy/execution.md: lines=46 bytes=10481 sha256=f6ab19fddbcf4ebcbe67320a8a90c3b4ceccc47d95bb48b3bee81d2186e48286
```
(round 4 was 6673 / 10481; round-5 delta +14 / 0 = **+14 bytes, 0 lines**)

### R5-4) Scoped baseline->final diffs regenerated
```
$ diff -u .scratch/.../baseline/AGENTS.md AGENTS.md > AGENTS.baseline-to-final.diff
$ diff -u .scratch/.../baseline/execution.md docs/policy/execution.md > execution.baseline-to-final.diff
$ cat <both> > baseline-to-final.diff
30 AGENTS.baseline-to-final.diff / 36 execution.baseline-to-final.diff / 66 baseline-to-final.diff lines
```

### R5-5) Semantic self-check + link/anchor + whitespace
```
$ python3 .scratch/24-delegation-ssot-context/validate.py
80/80 checks passed
wrote /home/z/vibe/.scratch/24-delegation-ssot-context/checks.json
exit=0
```
(D2/P6 literals updated to "defining and recording …"; P10 added for the restored
persistence verb)

### R5-6) Scoped whitespace
```
$ git diff --check -- AGENTS.md docs/policy/execution.md
exit=0
```

### R5-7) Link/anchor check (unchanged)
```
$ grep -oE '\]\([^)]+\)' AGENTS.md | sort | uniq -c
      2 ](docs/policy/execution.md#task-routing)   <- round-4 pointer + Conditional methods link
      1 ](docs/policy/execution.md#proof-and-review)
      1 ](docs/policy/execution.md#product-decisions)
      1 ](docs/policy/execution.md#documentation)
      1 ](docs/policy/execution.md#environment)
      1 ](docs/policy/execution.md#remote-coordination)
```
(seven core→companion link occurrences, six distinct anchors — all resolve)

### R5-8) Index untouched (nothing staged)
```
$ git diff --cached --stat
exit=0 (empty output = nothing staged)
```

### R5-9) Ticket status snapshot refreshed
```
$ git status --porcelain > .scratch/24-delegation-ssot-context/final-status.txt
```
(`final-status.txt` reflects the round-5 tree: 32 entries.)
