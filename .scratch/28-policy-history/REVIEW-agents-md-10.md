## Review — `/home/z/vibe/AGENTS.md` (frozen; nothing outside this one file was opened)

**Verdict: PASS** — 0 P0, 0 P1, 9 P2. No blocking finding.

Structure confirmed first: top-level keys in order `laws, precedence, intent, resources, attention, change, proof`; `laws` holds ten (`ssot, projection, no_op, falsifiable, top_down, derived, absent, controlled, invalidate, authority`); corollaries only under `ssot` (`partition, atomic`) and `falsifiable` (`fail_loud`). The 221-key count was not independently verified (needs the YAML parser; out of scope).

### The document's own checklist (`change.checklist`)
- **One home** — holds, with two residues: the void rule written twice (finding 2); `laws.no_op`'s split test restated at `change.granularity` without `@no_op`.
- **Resolvable** — all 35 `@` occurrences (28 distinct keys) resolve to existing keys. Non-`@` reference `precedence.levels_in_order` "The chain is the one in the docs layout" does not resolve inside this file (finding 3).
- **Sourced** — no stored count of the document's own lists; numerals are behavioural only ("five to ten", "one folder per effort", "one command turning into three"). **F10 fixed.**
- **Declared** — banner line 1 plus `change.render`/`change.files` declare this a render of `AGENTS.yaml`. OK.
- **Sound** — sound at top level; `laws` mixes two mapping members with eight scalars (finding 4).
- **Derived from root** — all ten laws and both corollaries are pointed at with `@`; `change.granularity` restates a law with no pointer.
- **Justified** — no statement found whose deletion would change nothing.

### Findings
1. **P2 `laws.derived`** — "…is **therefore** either generated from its source, or carries no fact of its own". "Therefore" makes it a consequence of `ssot`, yet it is a sibling law. *Criterion: corollary placement.* Fix: nest under `ssot`, or drop "therefore".
2. **P2 `precedence.levels_in_order` + `precedence.specificity`** — "a lower one contradicting a higher one is void" vs "Anything breaking a higher **intent** is void first". One meaning in two places, term drifting (level → intent). *Criterion: one home, one name.* Fix: keep it in `levels_in_order`; cite `@levels_in_order` from `specificity`.
3. **P2 `precedence.levels_in_order`** — "The chain is the one in the docs layout." Unresolvable in this file; `change.chain`/`change.layout` own it. *Criterion: Resolvable.* Fix: `@chain`/`@layout`.
4. **P2 `laws` / `laws.authority`** — eight laws are bare scalars while `ssot`/`falsifiable` carry `_text` + children; `authority` already packs two rules, i.e. "may later need sibling fields", which `change.forward_compatible` says must then live in a field. *Criterion: siblings_only, forward_compatible.* Fix: give `authority` its own `_text`.
5. **P2 `resources.environment.artifacts_home`** — key spelled *artifacts* against every body use of *artefact*; "no file **bare** in the root" leaves "bare" undefined while `change.files` puts four files at the root. *Criterion: one_name; actionability.* Fix: rename; define or drop "bare".
6. **P2 `resources.split.by_logic`, `resources.scheduling.never_block_on_a_resource`** — a fragment borrowing its head from its parent, and a five-word imperative clause though the token exists in its own body ("queue it behind the current holder"); same pattern at `logic_is_physical`, `structure_is_absolute`, `surprise_is_a_signal`. *Criterion: leading word.* Fix: `by_logic` → `logical_level`; → `queue_behind`.
7. **P2 `proof.review.unverified`** — "…and never claim zero unknown defects or runtime enforcement": the coordinate dangles; what "zero"/"claim" distributes over is undecidable. *Criterion: actionability.* Fix: two clauses.
8. **P2 `attention.phases.advance.slice`** vs `attention.delivery.vertical_slice`/`work_package` — one term, two objects (fresh-context working unit vs the artefact a milestone delivers). *Criterion: one_name, term in two senses.* Fix: point `slice` at `@work_package`, or define once.
9. **P2 undefined abbreviations** — `API` (`intent.risk.high_risk`), `env` (`intent.risk.secrets`), `repo` (`change.resumable`). *Criterion: define at first use; F9 residue.* Fix: expand once, as `DAG`/`CI`/`POC`/`SSOT`/`CPU`/`GPU` already are.

### Prior review's ten findings
F1 **fixed** (now a distinct prohibition). F2 **fixed** (no such key). F3 **fixed** (content moved to `change.file_shape`/`current_fact`/`ops`). F4 **fixed**. F5 **fixed** (only `laws.falsifiable → fail_loud`, a declared corollary pointed at by `@fail_loud`). F6 **not fixed** (finding 6). F7 **fixed** (credential sense glossed in place). F8 **partly fixed** (two real rules, still topic-led and unpinned — finding 4). F9 **partly fixed** (finding 9). F10 **fixed**.

### Other named checks
Two contradicting statements: **none found**; closest is the `artifacts_home`/"no file bare in the root" tension (finding 5). Rule stated where the reader will not look: the "key" disambiguation sits in `intent.risk.secrets`, away from the mapping-key uses — acceptable, the marked sense is glossed at its own use. One meaning in two places: finding 2, plus the absence rule at `laws.absent`/`change.fabricated`/`change.say_unknown`, legitimate because both change entries route `@absent`.

### Not verified / limits
- `python3 scripts/render_policy.py --check` was **not run** (no shell in scope); my resolvability check is by eye over the 35 `@` references.
- Paths named by `change.files` (`AGENTS.schema.yaml`, `PEOPLE.yaml`, `docs/`, `.scratch/`, `scripts/render_policy.py`) not resolved — outside the read bound.
- Whether this render matches its SSOT, and the 221-key count, are unverified.
- F1–F10 judged on the current file only; the prior report is outside my read scope, so I verified each named finding's text, not its original wording.

**Reply:** Verdict **PASS** — 0 P0, 0 P1, 9 P2; nothing blocks. Structure confirmed (7 top-level keys in order, 10 laws, 2 corollaries) and all 35 `@` references resolve. Prior findings: F1–F5, F7, F10 fixed; F6, F8, F9 only partly. No blocking finding, so no gist to give; closest candidate is finding 4 (`laws.authority` mixes two rules in a scalar against `forward_compatible`).