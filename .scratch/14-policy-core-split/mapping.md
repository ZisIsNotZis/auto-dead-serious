# Rule coverage map — old `AGENTS.md` (108 rules) → new home

Destination keys: **CORE** (`AGENTS.md`), **R-xxx** (`docs/policy/reference.md` section),
**WS** (`WORKSPACE.md`), **DEL** (deleted, reason given).

## Intro + index

| Old | Destination | Note |
|---|---|---|
| Intro L3 (portable, precedence, token-efficiency, map-not-pipeline) | CORE intro + S4 | precedence collapse fixed; "copy unchanged" vs "tighten" resolved by M1/M3 + R-REP.1.1 |
| `DOCUMENT` mnemonic index L5–18 | DEL | wrong pointers (D→Collaboration 4/11, O→Collaboration 9), documented as non-authoritative, duplicated the headers; replaced by the trigger table |

## Collaboration 1–11

| Old | Destination |
|---|---|
| 1 User & roles | CORE I1 + R-INT.1 |
| 2 Audience | R-INT.2 |
| 3 Goal / pressure | R-INT.3 |
| 4 Ask, 4.1 budget, 4.2 scope | R-INT.4, R-INT.4.1, R-INT.4.2 |
| 5 Process guidance / triage | R-INT.5 |
| 6 Responsibility | CORE I4 + R-INT.6 |
| 7 Report, 7.1 registers, 7.2 medium, 7.3 pushback, 7.4 self-review | R-INT.7–7.4 + CORE I12 |
| 8 Go-signal / recording regimes | CORE I2 + R-INT.8 |
| 9 Flexibility | R-INT.9 |
| 9.1 L1/L2 change rules | R-DOC.10.4 (L1-verbatim conflict fixed) |
| 9.2 amendments / routing around | CORE S2, S3, S5 (blanket escape removed; routing-around is now ticket + review + tier rule) |
| 10 Projection map | R-INT.10 |
| 11 Do it for the user | R-INT.11 |

## Documentation 1–11

| Old | Destination |
|---|---|
| 1 Supreme + write regimes (a)–(d) | CORE I5 + R-DOC.1 |
| 2 Before-code | R-DOC.2 |
| 3 SSOT | R-DOC.3 |
| 4 Clarity, 4.1 checklist | R-DOC.4, R-DOC.4.1 (rubric kept verbatim for reviewers; exemption test added) |
| 5 Formalize / S.M.A.R.T. | R-DOC.5 (exemption boundary made operational) |
| 6 Structure, 6.1 markdown style, 6.2 size economy | R-DOC.6, R-DOC.6.1 + CORE S1 (honest budget, `wc -m`, delete-not-reword) |
| 7 Level | R-DOC.7 |
| 8 Philosophy capture | R-DOC.8 |
| 9 People | R-DOC.9 |
| 10 Layers 10.1–10.4 | R-DOC.10–10.4 (L1 + comment vs design truth resolved) |
| 11 Routing | R-DOC.11 (WORKSPACE.md exception moved into the rule itself) |

## Tickets & git 1–6

| Old | Destination |
|---|---|
| 1 Tickets + micro-fix | R-TKT.1 (+ policy files excluded from micro-fix: CORE S3) |
| 1.1 Layout / ordinals / slugs | R-TKT.1.1 (local: ordinals from disk; remote: R-REM.5) |
| 1.2 Status | R-TKT.1.2 |
| 1.3 Fields | R-TKT.1.3 |
| 1.4 Commits / triage order / inbox | R-TKT.1.4 |
| 2 Locks, heartbeat, takeover, worktrees, no-remote fallback | R-REM.1, R-REM.2 (remote only) |
| 3 Branching | R-TKT.3 (local: one commit/concern → main; wider → branch) + R-REM.2 for races |
| 4 Review | R-TKT.2 (review record artifact added; rejection cycle bounded) |
| 5 Matt Pocock layout / tracker | R-TKT.4 (self-sufficiency) + R-REM.6 (tracker = remote) |
| 6 Sync 6.1–6.4 | R-TKT.1.1 (local ordinals) + R-REM.3, R-REM.4, R-REM.5 (remote) |

## Sessions & tools 1–13

| Old | Destination |
|---|---|
| 1 Bootstrap, 1.1 serialization, 1.2 compaction, 1.3 cognitive load | R-SES.1, 1.1, 1.2, 1.3 |
| 2 Focus / park / user-unavailable | R-SES.2 (all stop thresholds collected here; `Dear <owner>:` → `Parked-on-user:`) |
| 3 Delegation / fan-out / patience / kill protocol / slots | R-DEL.1, R-DEL.2, R-DEL.3, R-DEL.4 |
| 4 Subagent models | R-DEL.5 (+ "lowest-cost model the harness exposes" resolution rule) |
| 5 Self-knowledge / escalation | R-DEL.6 (+ no-stronger-model fallback) |
| 6 Tool autonomy, 6.1 modern tooling, 6.2 sudo, 6.3 China, 6.4 verify | R-ENV.1–1.4 (preference orderings kept; dated external facts → WS) |
| 7 Info gathering, 7.1 minimal skills | R-ENV.2, R-ENV.3 |
| 8 Skill learning | R-ENV.4 |
| 9 Roles / challenge-yourself / critique framing | R-DEL.7, R-DEL.8 |
| 10 Cleanup | R-REP.5 |
| 11 Time economy | CORE I10 + R-SES.3 |
| 12 Proper tools | R-ENV.5 |
| 13 Orchestration ladder | R-DEL.10 |

## Repository files 1–5

| Old | Destination |
|---|---|
| 1 Scaffold, 1.1 deployment | R-REP.1, R-REP.1.1 |
| 2 README | R-REP.2 |
| 3 .gitignore | R-REP.3 |
| 4 Commits + gate bar + secrets | CORE I7 + R-REP.4 (command list + first-party warning waiver added) |
| 5 Naming / preserve | R-REP.6 (branch conflict with R-REP.5 resolved) |

## Part II stages

| Old | Destination |
|---|---|
| Part II intro (map, not pipeline, default walks) | CORE T + R-STG preamble |
| Stage 0.1 end users, 0.2 tickets-as-channel, 0.3 untrusted | R-INT.12, R-TKT.1 (+ R-REM for fleet channel), CORE I6 + R-INT.13 |
| Stage 1 PO 1–2 | R-STG.1 |
| Stage 2 CM 1–2 | R-STG.2 |
| Stage 3 UX 1–2 | R-STG.3 |
| Stage 4 Design 1–14 | R-DSN.1–14 (R-DSN.11 gains a non-trivial definition + offline path) |
| Stage 5 Build 1–7 | R-BLD.1–7; L166→R-BLD.1 (docs item made satisfiable), L167→R-BLD.2, L168→R-BLD.3, L169→R-BLD.4, L170→R-BLD.5, L171→R-BLD.6, L172→R-BLD.7 + R-DEL.9 |

## Deleted outright (with reason)

| Old | Reason |
|---|---|
| Mnemonic index | wrong, non-authoritative, duplicates headers |
| Duplicated approval-list restatements (L24/25/78/99) | one home = CORE I1 |
| Duplicated stall thresholds (L42/92/95/96/171 → five numbers) | one home = R-SES.2, others cite |
| Duplicated delegation test (L93/L96/L74) | one home = CORE I9 + R-DEL.1 |
| Duplicated fresh-context/leak rules (L81/167/172) | one home = R-DEL.8; others cite |
| Duplicated won't-error/root-cause (L161/167/171) | one home = R-DSN.9 + R-BLD.6 |
| Duplicated git/sync mechanics (L79/84/85/87) | one home = R-REM.2/3/5 |
| Stage 1–3 restatements of Part I | collapsed into R-STG pointers |
| "Collab 7.1" broken citation, bare "6.3" in intro | citation scheme fixed (CORE S4) |
| Model tiers / harness pairings / dated `verified 2026-08` | ephemeral → WORKSPACE.md (except the invariant resolution rule in R-DEL.5) |

## Files

| File | Role |
|---|---|
| `AGENTS.md` | core, always in context |
| `docs/policy/reference.md` | on-demand detail, sections R-* |
| `WORKSPACE.md` | project knowledge + coordination mode declaration |
