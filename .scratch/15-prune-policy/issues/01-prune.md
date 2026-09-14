# 01 — Delete the arbitrary caps; prune outdated/redundant policy content

- **Status:** claimed
- **Blocked by:** none
- **Assignee/lock:** agent (pi)
- **Need-review:** yes (policy change)
- **Need-test-cases:** none (policy text; verification = measured delta + citation check + fresh-context review)

## Issue

PO decisions after ticket 14 landed:

1. The character caps in `S1` are arbitrary number-goals, not real constraints — drop them. Replace
   with a measured baseline plus the existing displacement rule, so growth is still visible and
   accountable without a magic number.
2. Authorised: delete policy content that is outdated, redundant, or trivially inferable
   (the file's own `R-DOC.4.1` test: a line that changes no decision over default).

Also carries the one open item from ticket 14 verification: the mirror host list existed in two
homes (`R-ENV.1.3` and `WORKSPACE.md`).

## Acceptance criteria

- [x] `S1` has no character cap; states measuring, displacement-based growth, and delta reporting.
- [x] `R-DOC.6`'s per-file budget no longer claims the policy files (core `S1` governs those).
- [x] Trivially-inferable rules deleted with reasons recorded in Comments.
- [x] Pointer-only stage rules folded into the stage preamble.
- [x] Remote-only material lives outside the always-on reference; core M2/M3 and the trigger table point at its new home.
- [x] One home for the mirror list and for the network observation.
- [x] Rule IDs preserved for everything not deliberately deleted; all citations resolve.
- [x] Size delta measured and recorded; fresh-context review passed or findings fixed.

## Comments

- 2026-09-15 (agent, pi) — Created and claimed on the PO's answers ("(a) no hard cap … (b) … you can delete them").

## Measurements (2026-09-15, `wc -m`)

| Artifact | Before (ticket 14) | After | Delta |
|---|---:|---:|---:|
| `AGENTS.md` (core, always loaded) | 7,992 | 8,090 | +98 (S1 "no cap" rewrite, M2/M3 point at the new file) |
| `docs/policy/reference.md` | 47,994 | 43,401 | **-4,593** |
| `docs/policy/remote-coordination.md` (M2 only) | – (inside reference) | 4,369 | new home for `R-REM.1-6` |
| `WORKSPACE.md` | 2,535 | 2,723 | +188 (gate command now measures all three policy files; one network observation) |
| **Local-mode reading set** (core + reference + WORKSPACE) | 58,521 | **54,214** | **-4,307 (-7.4%)** |
| All files | 58,521 | 58,583 | +62 |

Rules: 108 defined before, **103** after (five deliberately deleted, see below); unresolved
citations: none.

## Deletions and relocations (with reasons)

| Rule | Action | Reason |
|---|---|---|
| `R-DSN.4` config-driven | deleted | restates a competent agent's default; removing it changes no decision |
| `R-DSN.6` just-in-time abstraction | deleted | same class; its content survives in `R-DSN.14` (extraction threshold) |
| `R-DSN.13` architecture | deleted | duplicated `R-DSN.9` + core `I11`; its unique clause (logging plan) folded into `R-DSN.9` |
| `R-STG.4`, `R-STG.5` | deleted | pointer-only rules; folded into the `R-STG` preamble with their `R-DSN.11`/`R-DOC.8` citations |
| `R-REM.1-6` | relocated to `docs/policy/remote-coordination.md` | inert in local mode; the reference now contains only always-applicable rules, and M2 points at the new file |
| `R-DSN.7`, `R-DSN.10`, `R-DSN.12`, `R-DSN.14` | kept, trimmed | review proposed deleting `R-DSN.7/.10/.12/.14` as defaults; kept because each carries a real decision (interface override visibility; script/hook automation; scope-bound safety = no defense-in-depth beyond scope; extract only when 2+ modules need it, which is now the only home of the deleted `R-DSN.6`) |
| mirror host list | one home | the mapping stays in `R-ENV.1.3` (portable, actionable); `WORKSPACE.md` keeps only the dated observation |

## Verification

Fresh-context review of the prune (diff against the pre-prune reference plus a local-mode
completeness check): 17 findings, no content lost beyond the intended deletions. Fixed here:
missing `wc -m` record, gate command still citing the deleted budgets, "everything applies
always" preamble contradicted by remote-marked clauses, `M2` missing its `R-REM.2` pointer,
duplicate scope sentence in the new file, `R-TKT.1.4`/`R-TKT.3` push/branch clauses undecidable
without a remote, `S1` growth needing agreement rather than quiet absorption, `R-BLD.2` citation
after `R-DSN.13` was folded. Verdict after fixes: accept.
