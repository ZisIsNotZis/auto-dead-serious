# REVIEW-render-3 — independent execution of the renderer's checks

**Verdict: PASS** (no blocking finding). All four revisions match, `--check` exits 0, and every mandated failure mode fires with exit 1. Two non-blocking check gaps and one non-blocking diagnostics issue are recorded below; both gaps are unreachable with the shipped SSOT as it stands today.
All mutation happened in `/tmp/rev3v`; nothing under `/home/z/vibe` was modified (only this report was written).

## 1. Revision check (executed)
`cd /home/z/vibe && md5sum AGENTS.yaml AGENTS.md scripts/render_policy.py AGENTS.schema.yaml`
```
c52a61864fed9afecf2a3b3037649d24  AGENTS.yaml        <- matches
be70e5e2fe1723d806573bb99e9336f8  AGENTS.md          <- matches
a4e521b408d0729588076c9d82f717de  scripts/render_policy.py  <- matches
d2f0e0900d6c5a1ae3f44d023824781a  AGENTS.schema.yaml <- matches
```
Sandbox copy at `/tmp/rev3v` (script in `scripts/`, siblings `AGENTS.yaml`/`AGENTS.schema.yaml`) reproduced `checks passed; AGENTS.md matches AGENTS.yaml.` / `exit=0` from the pristine copies.

## 2. `--check` on the real artifact (executed)
`python3 /home/z/vibe/scripts/render_policy.py --check`
```
checks passed; AGENTS.md matches AGENTS.yaml.
EXIT=0
```

## 3. Defect matrix (each case = clean re-copy of the SSOT, one edit, then `--check`)

| # | defect injected | exit | message |
|---|---|---|---|
| 1 | duplicate key in one mapping | 1 | `AGENTS.yaml: duplicate key 'trust_is_earned' (first seen at line 6) (line 8)` |
| 2 | `@ref` to a nonexistent key | 1 | `checks failed: - dangling @ref (not rendered into AGENTS.md): zzz_missing_key` |
| 3 | `@ref` to the hidden key `emphasis_by_evidence` | 1 | `checks failed: - dangling @ref (not rendered into AGENTS.md): emphasis_by_evidence` |
| 4 | manually wrapped line (folded, still valid YAML) | 1 | `checks failed: - AGENTS.yaml:110: not a single key line (manual wrap?)` |
| 5 | blank line | 1 | `checks failed: - AGENTS.yaml:5: blank line` |
| 6a | uppercase letter in a key | 1 | `AGENTS.yaml:108: not a single key line (manual wrap?)` + `schema: 'One_name_one_thing' does not match any of the regexes…at ['resources','efficiency']` + `bad key shape: /resources/efficiency/One_name_one_thing` |
| 6b | space in a key | 1 | same three checks with `one name one thing` |
| 7 | node whose `_text` is removed | 1 | `schema: None is not of type 'object' at ['precedence','trust_is_earned']` + `node without _text: /precedence/trust_is_earned` |
| 8 | SSOT edit, no re-render | 1 | `AGENTS.md is out of sync with AGENTS.yaml; re-run the renderer.` |
| 9 | same key name in a *different* mapping (global uniqueness) | 1 | `checks failed: - duplicate key: order` |
| 10 | manual wrap inside AGENTS.md | 1 | `checks failed: - AGENTS.md:10: not a single key line (manual wrap?)` |
| 11 | blank line inside AGENTS.md | 1 | `checks failed: - AGENTS.md:6: blank line` |

Cases 10-11 show the layout check really is applied to the generated file, not only the SSOT. **No mandated defect passed the checks.** Cases 1 and 9 are caught by two different mechanisms (parse-time duplicate rejection for one mapping, a global `Counter` for cross-mapping reuse) — both fire.

## 4. Independent verification of AGENTS.md alone (executed, own commands)
`python3` one-shot over `/home/z/vibe/AGENTS.md` — counts, a line-shape regex `^( +)?(?:_text|[a-z][a-z0-9_]*):(?: \S.*)?$`, `@ref` extraction, a canonical `safe_dump` re-dump of the fenced body, and a from-scratch re-render of the SSOT (drop `*` keys, collapse text-only nodes):
```
file lines: 205 | blank lines: 0 | non-single-key lines: [] | hidden-key leak ('*'): []
refs: 5 (distinct) | refs with no matching key in AGENTS.md: []
canonical re-dump == body (wrap detector): True
independent re-render == body: True
```
So, by commands independent of the script: every rendered line is a single key line, there are no blank lines, no manual wrap (a folded line would not survive the canonical re-dump), no hidden key leaked, all 5 `@ref` targets (`@fact_record`, `@attention`, `@hard_delete`, `@resources`, `@silent_advance`) exist as keys, and the file is byte-identical to my own re-render.

## 5. Findings

### F1 — non-blocking — `render_policy.py:159` (`rendered = {k for k in keys if not k.endswith("*")}`) vs `render()` at `:161-177`
Claim violated: "every `@ref` names a key that is actually written to AGENTS.md."
`rendered` is computed from key *names*, not from the subtree the renderer actually emits. A key that is a **descendant of a hidden (`*`) node** never lands in AGENTS.md, yet its name is in `rendered`, so a ref to it is accepted.
Reproduction (executed, sandbox): add `hidden_child` under `emphasis_by_evidence*` and a `@hidden_child` ref, then run in write mode:
```
python3 /tmp/rev3v/scripts/render_policy.py
checks passed; wrote /tmp/rev3v/AGENTS.md (205 lines).   exit=0
```
and the same tree under `--check` reports only `AGENTS.md is out of sync`, never a dangling ref. Severity non-blocking: the shipped SSOT has exactly one hidden key (`AGENTS.yaml:246`, text-only, no children), so the gap is currently unreachable. Fix shape: compute `rendered` from the same recursion `render()` uses (a key is rendered only if no ancestor ends in `*`).

### F2 — non-blocking — `render_policy.py:37` (`REF_RE = re.compile(r"(?<![\w@])@([a-z0-9_]+)")`)
A ref that is not all-lowercase is not recognised as a ref at all, so no check ever sees it. Executed: appending `@HARD_DELETE` to a `_text` and running write mode gives `checks passed; wrote … exit=0`. A reader of AGENTS.md would find no such key. Low severity (the correct spelling `@hard_delete` does exist and resolves), but a mistyped ref is silently unchecked.

### F3 — non-blocking — `render_policy.py:147-150` (`main()` parses before it lints)
`doc, schema = read(SRC), read(SCHEMA)` runs before `check_layout(SRC)`, and only `yaml.constructor.ConstructorError` is caught, so any other YAML error escapes as a traceback. Executed: a same-indent continuation line gives a `Traceback … line 150 … read(SRC)` (exit 1) rather than the clean `:N: not a single key line (manual wrap?)` message. The defect is still caught (exit 1) — only the diagnostic is lost. Consequence: for YAML-invalid input the layout checker never runs, so a "wrap" that happens to parse as `key: value` is only caught by the parser. Recommend catching `yaml.YAMLError` and running `check_layout` first.

### Checked and found sound
No claimed check is missing: all six docstring claims map to live code (`jsonschema.validate`; `UniqueKeyLoader` + global `Counter`; `KEY_RE` + schema regex; the `@ref` set-difference; `check_layout` on both files; the `--check` byte comparison). No dead code found — every helper, regex alternative and parameter is reachable. The renderer's own guard `assert yaml.safe_load(body) == expected` is real and would fire on round-trip loss. `render()` runs in both modes, so a write-mode render is still preceded by the full check set.

## 6. Not verified / limits
- The malformed-**schema** path (`jsonschema.SchemaError` escaping the `except ValidationError`) was reasoned from code only; **not run**. Same for the "wrap that parses as indented `key: value`" masquerade — reasoned from code, not executed.
- Only the first `ValidationError` is ever reported (`validator.validate` raises on first hit) — observed in case 6a; not probed further.
- Single environment only (`python3` + installed `jsonschema`/`yaml`); no version matrix, no CRLF/trailing-whitespace variants beyond cases above.
- Read exactly four files; no `docs/`, `.scratch/`, other projects or dotfiles were opened, and no repository sweep was run.
