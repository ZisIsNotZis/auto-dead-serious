VERDICT: PASS — all 3 newly-closed cases fire and all 11 regression cases still fire; pristine sandbox exits 0.
md5 match: AGENTS.yaml c52a6186…, AGENTS.md be70e5e2…, render_policy.py f39afe43…, AGENTS.schema.yaml d2f0e090… all match the stated revisions.
Pristine: exit 0, "checks passed; AGENTS.md matches AGENTS.yaml."
Cases fired: 14/14 (baseline + F1–F3 + R1–R11); every case returned exit 1 with a clean message, no traceback.
Nothing failed to fire. I could not write the report file (path is under read-only /home/z/vibe, no write tool) — full report is inline below.

# REPORT — independent execution verification of scripts/render_policy.py (run from /tmp sandboxes, /home/z/vibe untouched)

## Method / revisions
Copied the four artifacts to fresh sandboxes; ran `python3 scripts/render_policy.py --check` per case with the exit code captured by Python. Verified hashes match the revisions given: AGENTS.yaml c52a61864fed9afecf2a3b3037649d24, AGENTS.md be70e5e2fe1723d806573bb99e9336f8, render_policy.py f39afe434e01bb73855e03bca1f2cd56, AGENTS.schema.yaml d2f0e0900d6c5a1ae3f44d023824781a.

## Case table (case / injected defect / exit / message)
| case | injected defect | exit | message |
|---|---|---|---|
| baseline | none (pristine) | 0 | checks passed; AGENTS.md matches AGENTS.yaml. |
| F1 | key `ledger` as child of hidden `emphasis_by_evidence*`, referenced `@ledger` | 1 | dangling @ref (not rendered into AGENTS.md): ledger |
| F2 | `@hard_delete` written `@HARD_DELETE` | 1 | dangling @ref (not rendered into AGENTS.md): HARD_DELETE |
| F3 | line `broken: [1, 2` (YAML-invalid) | 1 | AGENTS.yaml:362: blank line + AGENTS.yaml: YAML error (line 364): expected ',' or ']', but got '<stream end>' — no traceback |
| R1 | duplicate `_text` in one mapping | 1 | AGENTS.yaml: YAML error (line 6): duplicate key '_text' (first seen at line 5) |
| R2 | `@fact_record` → `@no_such_key` | 1 | dangling @ref … no_such_key |
| R3 | `@attention` → `@emphasis_by_evidence` | 1 | dangling @ref … emphasis_by_evidence |
| R4 | continuation line at same indent (manual wrap) | 1 | AGENTS.yaml:6: not a single key line (manual wrap?) (+ YAML error line 7) |
| R5 | blank first line | 1 | AGENTS.yaml:1: blank line |
| R6 | key `verify_the_fact` → `VerifyTheFact` | 1 | AGENTS.yaml:8: not a single key line (manual wrap?) + schema regex at ['precedence'] + bad key shape: /precedence/VerifyTheFact |
| R7 | key `own_inference` → `own inference` | 1 | AGENTS.yaml:12: not a single key line + schema regex + bad key shape: /precedence/own inference |
| R8 | removed `_text` of `own_inference` | 1 | schema: None is not of type 'object' at ['precedence','own_inference'] + node without _text: /precedence/own_inference |
| R9 | `commitment:` → `resources:` (name reused in a 2nd mapping) | 1 | duplicate key: resources |
| R10 | SSOT text edited, no re-render | 1 | AGENTS.md is out of sync with AGENTS.yaml; re-run the renderer. |
| R11 | blank line + wrapped line inside AGENTS.md | 1 | AGENTS.md:3: blank line + AGENTS.md:5: not a single key line (manual wrap?) |

The three previously-open gaps are genuinely closed: hidden-subtree keys are excluded from `rendered_keys` (F1), `REF_RE` matches uppercase so a non-rendered `@HARD_DELETE` dangles (F2), and the parser is wrapped in `except yaml.YAMLError` with a `problem_mark`-based line number, so malformed YAML reports cleanly (F3).

## Independent AGENTS.md-only check (my own commands, not the script)
Lines 205; blank lines 0; non-key lines 0; distinct textual keys 179; refs found 5 — attention, fact_record, hard_delete, resources, silent_advance — every one present as a key (refs_missing = []). Consistent with the script's pristine PASS.

## Checks found dead, missing or bypassable
- No required check is dead or bypassable in the executed set.
- Overlap (not a defect): an uppercase key or a key containing a space is caught primarily by the layout regex in `check_layout`, reported as "not a single key line (manual wrap?)", and only secondarily by the snake_case `KEY_RE` check. The snake_case check does fire, but the first-seen message is the layout one.
- Duplicate-key detection is implemented in the YAML loader, so it surfaces under "YAML error:" rather than the "duplicate key:" wording from `check()`; it is still clean and correct.

## Not verified / limits
- Only `--check` mode run; write mode, the `assert yaml.safe_load(body) == expected` render guard, and the missing-AGENTS.md path were not exercised.
- Hidden-node exclusion executed only at depth 1 (F1/R3); deeper inheritance was confirmed by reading `rendered_keys`, not run.
- Schema check exercised only for missing `_text` and bad key names, not for wrong value types or extra fields.
- Single Python/jsonschema/YAML environment; no CI or cross-version run.
- Report file not written to /home/z/vibe/.scratch/28-policy-history/REVIEW-render-4.md — that tree is read-only here and no write tool is available; the runtime should persist this response there.