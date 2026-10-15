# Delegation / SSOT / context-inheritance policy — self-proof and review packet

Status: implemented; documentation self-checks passed. **Independent acceptance is
pending.** Read the final scoped artifacts, the approved direction in `contract.md`
and this evidence — not the worker conversation. A repair invalidates the affected
proof and requires another fresh reviewer.

## Revision and checks

`final-manifest.json` binds the two live scoped documents to SHA-256 on HEAD
`c82765e`. `baseline/` preserves both pre-edit files; `baseline-to-final.diff`
isolates this task from the earlier uncommitted consolidation; `commands-and-results.md`
holds the exact commands with output.

Reproduce: `python3 .scratch/24-delegation-ssot-context/validate.py` (foreground,
under 60s). Result: **41/41 checks passed**, covering required (A)/(B)/(C) semantics,
the scoped "Preserve other entries" wording, relative-link existence and anchor
resolution for all six `AGENTS.md`→`execution.md` links, and scoped
`git diff --check`. Detailed results: `checks.json`.

| Measure | Baseline | Final | Δ |
| --- | ---: | ---: | ---: |
| `AGENTS.md` lines / bytes | 37 / 5,408 | 37 / 6,281 | 0 / +873 |
| `docs/policy/execution.md` lines / bytes | 46 / 9,859 | 46 / 10,238 | 0 / +379 |

No new sections or files added, so no anchor churn; section headings and all six
core→companion links are unchanged and resolve. `git diff --check` on both files is
clean. Nothing is staged; changes remain in the working tree and are not committed.

## Edits (file:line, final revision)

- `AGENTS.md:16` (shared boundaries, file-communication bullet): adds the ticket
  requirement and the SSOT rule for all documents — current facts only, rewritten
  in place, with the explicit bans (dated narrative, changelogs, errata, "was A,
  later B", dashboard timestamps) and no duplication/staleness/conflict.
- `AGENTS.md:20` (Main role): rewritten to the unconditional form — highest-priority
  role rule; no substantive work of any kind (no implementation, verification,
  inspection/review, document writing); every task including documentation delegated;
  governs regardless of session age or inherited/stale context; only dialogue/intent/
  authority/principles/milestones/status/routing/delivery managed; unavailable
  delegation stays an infrastructure blocker.
- `AGENTS.md:26` (default-context sentence): fresh non-inherited context by default
  for compact specifiable handoffs; inherit only when a context-free description
  would cost more (e.g. holistic documentation/policy work); independent review
  never inherits context.
- `docs/policy/execution.md:11` (task routing): "Preserve other entries" scoped to
  the ticket/work-record ledger only (tickets append-style, fact documents not).
- `docs/policy/execution.md:29` (`Documentation`): every task creates/updates a
  ticket as the log home for history/provenance/process narrative; documents of
  every form hold current facts only, rewritten in place, one home per fact, no
  duplication/staleness/conflict.

## Rationale

See `contract.md`. The enforceable (B) boundary lives in the always-loaded core;
its operational form lives in `execution.md#documentation`; the existing
"Preserve other entries" line was scoped rather than duplicated. Alternatives
(companion-only, or full duplication in both) were rejected for leaving the core
silent or bloating it.

## Scenario check (documentation only)

| Falsifying case | Result |
| --- | --- |
| A model reading only the core still does implementation/verification or writes docs directly | Main rule now forbids all substantive work unconditionally and marks delegation highest-priority. Holds. |
| Long/stale session treats delegation as optional | Rule explicitly governs whenever read, regardless of session age or inherited/stale context. Holds. |
| Model appends a dated changelog/errata to a fact document | Core boundary and `documentation` require current-facts-only, in-place rewrite, with the forbidden forms named. Holds. |
| "Preserve other entries" misapplied to a fact document | Scoped to the ticket/work-record ledger; fact documents are explicitly not append-style. Holds. |
| Independent review reuses worker context | "Independent review never inherits context"; fresh default also stated. Holds. |

These are source/link/whitespace documentation checks, not live agent-behavior
tests. Prose does not enforce tools or guarantee compliance; no claim of zero
unknown defects. Next acceptance step: fresh independent reviewer of the
manifest-bound revision.

---

## Round 2 — follow-up fixes (reviewer notes 1–4)

Status: applied; documentation self-checks re-run (**46/46**). Round-1 evidence
above is preserved unchanged. These four fixes are non-blocking cleanups and
alter no approved acceptance semantic.

### Fixes (file:line, round-2 revision)

1. **Internal redundancy (note 1)** — `AGENTS.md:20`: dropped the restated
   imperative "Never implement or technically verify;", keeping the fuller
   enumeration "no implementation, no verification, no inspection/review and no
   document writing" and the blocker clause, now capitalized ("Unavailable
   delegation is an infrastructure blocker, not a fallback to direct work").
   No safeguard lost; the enumeration is a superset of the dropped clause.
2. **Cross-home duplication (note 2)** — `AGENTS.md:16` now carries the binding
   rule once (added "one home per fact" to the core sentence);
   `docs/policy/execution.md:29` drops the verbatim ticket + current-facts
   restatement and points to the core: "The ticket/log-home and current-facts
   SSOT rules are binding in the core `AGENTS.md` shared boundaries." Every
   distinct fact stays stated once: banned forms, one-home-per-fact, no
   duplication/staleness/conflict, current-facts-only and in-place rewrite are
   in `AGENTS.md:16`; ticket-ledger scoping (append-style) stays at
   `execution.md:11`.
3. **Escape hatch (note 3)** — `docs/policy/execution.md:30`: "historical
   records need no rewrite" qualified to "historical ticket/archived records
   need no rewrite when still recoverable", so the absolute in-place-rewrite
   rule still covers fact documents.
4. **Actor ambiguity (note 4)** — recording acts now attributed to the worker
   role: `AGENTS.md:11` "choose and have workers record"; `execution.md:8` "the
   worker inspects … and records its contract"; `execution.md:22` "workers
   record source, …".

### Round-2 metrics

| Measure | Baseline | Final (round 2) | Round-1 final | Δ vs round 1 |
| --- | ---: | ---: | ---: | ---: |
| `AGENTS.md` lines / bytes | 37 / 5,408 | 37 / 6,275 | 37 / 6,281 | 0 / −6 |
| `docs/policy/execution.md` lines / bytes | 46 / 9,859 | 46 / 10,086 | 46 / 10,238 | 0 / −152 |

Round 2 is net −158 bytes, 0 lines; total does not grow. No file added and the
heading set is unchanged, so no anchor churn. `final-manifest.json` binds
`ca588165…` (`AGENTS.md`) and `bd76a2ff…` (`execution.md`) on HEAD `c82765e`.
`AGENTS.baseline-to-final.diff`, `execution.baseline-to-final.diff` and
`baseline-to-final.diff` were regenerated against the preserved `baseline/`.

### Round-2 checks

`python3 .scratch/24-delegation-ssot-context/validate.py` → **46/46 passed**,
exit 0 (`checks.json`). The self-check was updated for the round-2 wording: A8
literal re-capitalized; B8 asserts the execution pointer to the core rule;
B9/B10 assert the verbatim restatement is gone from execution; B11 checks "one
home per fact" in the core; R1–R5 cover notes 1–4. Link/anchor resolution for
all six `AGENTS.md`→`execution.md` links and scoped `git diff --check` remain
clean (see `commands-and-results.md` round 2).

### Meaning preservation

Each banned form and safeguard appears exactly once in the policy (core unless
noted): dated narrative, changelogs, errata, "was A, later B", dashboard
timestamps, duplication, stale content, conflicting statements, one home per
fact, current facts only, rewritten in place, Every task creates or updates a
ticket, tickets are the log home — all in `AGENTS.md:16`; append-style ticket
ledger scoping in `execution.md:11`. No fact is dropped or duplicated.

These remain documentation checks, not live agent-behavior tests. Independent
acceptance at this revision is still pending a fresh reviewer.

---

## Round 3 — PO-required semantics: (D) subdivision, (E) SMART/fork handoffs, (F) concise messaging, (G) ticket vs fact-document classes

Status: applied; documentation self-checks re-run (**68/68**). Rounds 1–2 above are
preserved unchanged. A fresh independent reviewer is still required; nothing is
committed and nothing is staged.

### Edits (file:line, round-3 revision)

- `AGENTS.md:16` (shared boundaries, communication bullet) — **(G)** scopes the
  universal and names the classes: "Documents other than tickets are fact
  documents: in every form they hold current facts only, one home per fact,
  rewritten in place on change, …", while tickets remain "the log home for
  history, provenance and process narrative". **(F)** adds "Agent-to-agent messages
  stay minimal, with no large prose blocks; results land on disk as documents and
  tickets" and "a report back to Main is a very short description plus
  done/not-done status, never a transcript or restated detail".
- `AGENTS.md:22` (Worker role) — **(D)** makes the worker's own subdivision explicit
  and recordable: "Split a splittable assignment into same-layer siblings,
  **recording** complete coverage, owners, interfaces, dependencies and an
  integration owner."
- `AGENTS.md:26` (default-context paragraph) — **(D)** reconciles the existing
  clause instead of silently granting recursion: "Recursive delegation needs
  explicit permission, runtime support and the bounds above: a worker subdivides
  its own assignment only when granted them; never forward an unchanged task
  indefinitely."
- `docs/policy/execution.md:7` (task routing) — **(E)** "Every assignment is SMART
  — above all specific and actionable — and states its task and acceptance criteria
  (AC). A fresh / non-inherited handoff (`fork=false`) carries the full compact
  contract the child cannot otherwise know: a narrow packet with objective,
  scope/exclusions, authoritative inputs, acceptance/proof, owners, outputs,
  interfaces/dependencies, authority/user gates, stop conditions, finite resource
  limits and an observable status/completion path. An inherited-context handoff
  (`fork=true`) already carries the task, so it designates only the role — you are
  the sub agent; do this work — and proceeds."

### Placement (one home per fact)

| Rule | Home |
| --- | --- |
| (D) worker may subdivide its own assignment, records coverage/owners/interfaces/deps/integration owner, only with explicit permission/runtime/bounds | `AGENTS.md:22` + `AGENTS.md:26` (core boundary); the split method already lives at `execution.md:9` |
| (E) SMART/AC assignment; fresh = `fork=false` full contract; inherited = `fork=true` role-only | `execution.md:7` (dispatch method); `AGENTS.md:26` keeps the fresh-by-default boundary |
| (F) minimal agent messages, no large prose blocks, results on disk as documents and tickets, short done/not-done report to Main | `AGENTS.md:16` (core boundary) |
| (G) tickets = log class (append-style); other documents = fact documents, rewritten in place | `AGENTS.md:16` (classes) + `execution.md:11` (append scoping) |

`fork=` occurs exactly twice, both in `execution.md:7`; "append-style" occurs once,
in `execution.md:11`; no (D)/(E)/(F) rule is restated across the two files.

### Round-3 metrics

| Measure | Baseline | Round 2 | Round 3 | Δ vs round 2 |
| --- | ---: | ---: | ---: | ---: |
| `AGENTS.md` lines / bytes | 37 / 5,408 | 37 / 6,275 | 37 / 6,632 | 0 / +357 |
| `docs/policy/execution.md` lines / bytes | 46 / 9,859 | 46 / 10,086 | 46 / 10,467 | 0 / +381 |

Net round-3 change: **+738 bytes, 0 lines** (+357 in the always-loaded core, +381 in
the conditional companion). The growth is the four mandated semantics: (D) and (F)
are core boundaries, (E) is the dispatch method in the companion, (G) is a
one-clause scoping fix. The three baseline→final diffs were regenerated against the
preserved `baseline/`; `final-metrics.json` and `final-manifest.json` bind
`9b28a9b6…` (`AGENTS.md`, 6,632 B) and `4b18a91e…` (`docs/policy/execution.md`,
10,467 B) on HEAD `c82765e`. No file added and the heading set is unchanged, so no
anchor churn.

### Round-3 checks

`python3 .scratch/24-delegation-ssot-context/validate.py` → **68/68 passed**,
exit 0 (`checks.json`). Added checks D1–D5, E1–E6, F1–F6, G1–G5; all round-1/2
checks (A/B/C/R), link/anchor resolution for all six `AGENTS.md`→`execution.md`
links and scoped `git diff --check` still pass. The added checks assert the
round-3 literals plus the dedup facts: `All documents, in every form` absent,
`append-style` absent from the core, `fork=` exactly twice, `Agent-to-agent
messages` absent from the companion, `subdivides its own assignment` absent from
the companion.

Round 2 was reconstructed by applying `baseline-to-final.diff` to `baseline/`
(`patch -o`); the reconstruction is 6,275 / 10,086 bytes, matching round 2's
manifest, so the round-2→3 delta is attributable. That diff touches exactly four
lines (`AGENTS.md` 16/22/26, `execution.md` 7).

### Scenario check (documentation only)

| Falsifying case | Result |
| --- | --- |
| A sub agent subdivides its task without granted recursion | "a worker subdivides its own assignment only when granted them" plus the surviving "explicit permission, runtime support and the bounds above". Holds. |
| A sub agent splits without recording coverage/owners/interfaces/deps/integration owner | `AGENTS.md:22` requires "recording complete coverage, owners, interfaces, dependencies and an integration owner". Holds. |
| A fresh (`fork=false`) handoff omits AC, scope, inputs, outputs, proof or stop conditions | `execution.md:7` states the AC in the SMART sentence and lists the rest in the packet. Holds. |
| An inherited (`fork=true`) handoff restates the whole task | `execution.md:7`: it "already carries the task, so it designates only the role"; the core still defaults to fresh. Holds. |
| Fork wording contradicts "fresh by default" | Core keeps "Default to fresh (non-inherited) context…"; the fork sentence makes inherited the task-carrying exception. Holds. |
| A literal reader applies in-place rewrite to a ticket | Tickets are named the log home and are not fact documents. Holds. |
| A literal reader appends to a fact document | Fact documents are "rewritten in place on change"; append-style is scoped to the ticket ledger only. Holds. |
| Agents pass a large prose block instead of a report | "Agent-to-agent messages stay minimal, with no large prose blocks"; results land on disk; the report is a short description plus done/not-done. Holds. |

These remain source/link/whitespace documentation checks, not live agent-behavior
tests. Prose does not enforce tool availability or guarantee compliance; no claim of
zero unknown defects. Residual uncertainty: the `fork=true`/`fork=false` spelling is
the host runtime flag the mapping is tied to; a runtime using a different name
would need that one tie updated. Next acceptance step: a fresh independent reviewer
of the manifest-bound revision.

---

## Round 4 — three report-only P2 cleanups (review notes P2-1/P2-2/P2-3)

Status: applied; documentation self-checks re-run (**79/79**). Rounds 1–3 above are
preserved unchanged; one round-3 claim is corrected below. Nothing is committed and
nothing is staged. Round 3 was bound to `9b28a9b6…` (`AGENTS.md`) / `4b18a91e…`
(`execution.md`); round 4 is bound to `3f6584bc…` / `f6ab19fd…` on HEAD `c82765e`.

### Edits (file:line, round-4 revision)

- `AGENTS.md:22` (Worker role) — **P2-2** makes the split permission-gated, matching
  the gate at `AGENTS.md:26`: "**When permitted,** split a splittable assignment into
  same-layer siblings, …". **P2-3** drops the duplicated sibling enumeration and
  points to its one home: "… defining complete coverage and ownership (enumeration in
  [Task routing](docs/policy/execution.md#task-routing))."
- `docs/policy/execution.md:7` (task routing) — **P2-1** removes the contradiction:
  "Every assignment is SMART — above all specific and actionable. A fresh /
  non-inherited handoff (`fork=false`) **states its task and acceptance criteria
  (AC)** and carries the full compact contract …"; and "An inherited-context handoff
  (`fork=true`) already carries the task and AC in context, so it designates only the
  role …". SMART binds every assignment; the explicit task+AC statement is required
  only of the fresh handoff.

### Which note each change closes

| Note | Change | Location |
| --- | --- | --- |
| P2-1 contradiction | SMART for every assignment; task+AC stated by the `fork=false` handoff; `fork=true` already carries task+AC in context | `execution.md:7` |
| P2-2 conditional read | permitted-only qualifier "When permitted" | `AGENTS.md:22` |
| P2-3 duplication + evidence | core enumeration dropped, pointer to `execution.md:9`; this section corrects the round-3 claim | `AGENTS.md:22`, `evidence.md` (this section) |

### One home per fact — corrected claim

Round 3 stated "no (D)/(E)/(F) rule is restated across the two files." That was
**inaccurate**: the sibling enumeration "complete coverage, owners, interfaces,
dependencies and an integration owner" appeared in both `AGENTS.md:22` and
`execution.md:9`. Round 4 removes the core copy; the enumeration now appears **once**,
at `execution.md:9` ("each with inputs, outputs, acceptance/proof, owner, interfaces,
dependencies and exclusions; map complete parent coverage and assign a worker
integration owner"), and the core keeps only the boundary ("complete coverage and
ownership") plus the pointer. No distinct fact is stated twice. The `execution.md:9`
enumeration and the `AGENTS.md:22` pointer are the sole home for those tokens.

### Round-4 metrics

| Measure | Baseline | Round 2 | Round 3 | Round 4 | Δ vs round 3 |
| --- | ---: | ---: | ---: | ---: | ---: |
| `AGENTS.md` lines / bytes | 37 / 5,408 | 37 / 6,275 | 37 / 6,632 | 37 / 6,673 | 0 / +41 |
| `docs/policy/execution.md` lines / bytes | 46 / 9,859 | 46 / 10,086 | 46 / 10,467 | 46 / 10,481 | 0 / +14 |

Net round-4 change: **+55 bytes, 0 lines** — the mandated clarifications (the
permitted-only qualifier, the task+AC re-scoping and the cross-file link to the
enumeration's home). The three baseline→final diffs were regenerated against the
preserved `baseline/`; `final-metrics.json` and `final-manifest.json` bind
`3f6584bc…` (`AGENTS.md`, 6,673 B) and `f6ab19fd…` (`docs/policy/execution.md`,
10,481 B) on HEAD `c82765e`. Headings unchanged, so no anchor churn.

### Round-4 checks

`python3 .scratch/24-delegation-ssot-context/validate.py` → **79/79 passed**, exit 0
(`checks.json`). The round-3 checks were updated for the new literals (D1 lowercase
`split`, D2 core permitted-only boundary, E3/E4 fork wording), and P1–P9 were added
for the three notes: SMART-per-assignment, fresh states task+AC, inherited carries
task+AC in context, the old unconditional phrasing absent, the core split is
permitted-only, the core keeps the coverage/ownership boundary, the core points to
the enumeration, the enumeration is absent from the core, and it lives once in the
companion. All A/B/C/D/E/F/G and round-1/2 checks still pass.

Link/anchor: `AGENTS.md` now has **seven** core→companion link occurrences (the two
`Task routing` links plus the other five), covering the same **six** distinct anchors
`#task-routing`, `#proof-and-review`, `#product-decisions`, `#documentation`,
`#environment`, `#remote-coordination`; all resolve. `git diff --check` on both files
is clean (`exit=0`); nothing is staged.

### Scenario check (documentation only)

| Falsifying case | Result |
| --- | --- |
| An inherited (`fork=true`) child is told "state AC" and restates the task | `execution.md:7` now requires the task+AC statement only of the `fork=false` handoff; the `fork=true` handoff "already carries the task and AC in context" and only designates the role. Holds. |
| A reader sees the unconditional "Split … siblings" and thinks splitting is always allowed | `AGENTS.md:22` is now "When permitted, …", matching the `AGENTS.md:26` gate ("a worker subdivides its own assignment only when granted them"). Either line alone signals the gate. Holds. |
| A reader needs the full sibling enumeration | `AGENTS.md:22` defines "complete coverage and ownership" and links `[Task routing](docs/policy/execution.md#task-routing)`; the enumeration is stated once at `execution.md:9`. Holds. |
| The enumeration is looked for in both files | It is present only at `execution.md:9`; the core copy is gone (P8/P9 checks). Holds. |

These remain source/link/whitespace documentation checks, not live agent-behavior
tests. Prose does not enforce tool availability or guarantee compliance; no claim of
zero unknown defects. Residual uncertainty: the `fork=true`/`fork=false` spelling is
the host runtime flag the mapping is tied to; a runtime using a different name would
need that one tie updated. Next acceptance step: a fresh independent reviewer of the
manifest-bound round-4 revision plus an independent reproduction of the commands.

---

## Round 5 — final polish: persistence verb restored; superseded round-3 rows marked

Status: applied; documentation self-checks re-run (**80/80**). Rounds 1–4 above are
preserved unchanged and their metrics/manifest rows remain those revisions' facts.
Nothing is committed and nothing is staged. Round 4 was bound to `3f6584bc…` /
`f6ab19fd…`; round 5 is bound to `488316cb…` (`AGENTS.md`, 6,687 B) / `f6ab19fd…`
(`docs/policy/execution.md`, 10,481 B) on HEAD `c82765e`.

### Edit (file:line, round-5 revision)

- `AGENTS.md:22` (Worker role) — **P2-A** restores the persistence verb lost in the
  round-4 wording: "When permitted, split a splittable assignment into same-layer
  siblings, **defining and recording** complete coverage and ownership (enumeration
  in [Task routing](docs/policy/execution.md#task-routing))." The single-home
  pointer is kept and the enumeration is still not restated, so round 4's
  one-home-per-fact result is unchanged.

### Round-3 rows superseded by rounds 4–5 (P2-B)

Tickets are append-style, so rounds 1–4 are left verbatim. These rows state the
round-3 revision and no longer describe the current text; what now holds is here:

| Superseded row | Current text (rounds 4–5) |
| --- | --- |
| `evidence.md:163–166` — (D) edit bullet quoting `AGENTS.md:22` as "Split a splittable assignment into same-layer siblings, **recording** complete coverage, owners, interfaces, dependencies and an integration owner." | `AGENTS.md:22`: "When permitted, split … siblings, defining and recording complete coverage and ownership (enumeration in `[Task routing]`)"; the full enumeration is not in the core. |
| `evidence.md:186` — (D) placement row: "worker … records coverage/owners/interfaces/deps/integration owner … `AGENTS.md:22`". | The core records coverage and ownership and points to the enumeration's single home (`execution.md:9`); subdividing is permitted-only (`AGENTS.md:22`/`:26`). |
| `evidence.md:231` — (D) scenario row: "`AGENTS.md:22` requires 'recording complete coverage, owners, interfaces, dependencies and an integration owner'. Holds." | `AGENTS.md:22` requires recording complete coverage and ownership; the enumeration lives once, at `execution.md:9`. The falsifying case still fails, so the row's verdict survives though its citation is superseded. |
| `evidence.md:232` — (E) scenario row: "`execution.md:7` states the AC in the SMART sentence and lists the rest in the packet." | Superseded by the round-4 P2-1 edit: `execution.md:7` makes every assignment SMART and requires the fresh (`fork=false`) handoff — not the SMART sentence — to state its task and AC. Verdict survives. |
| `evidence.md:233` — (E) scenario row quotation "already carries the task, so it designates only the role". | `execution.md:7` now reads "already carries the task and AC in context, so it designates only the role". |
| `evidence.md:260–261` — (P2-3) edit bullet quotation "… defining complete coverage and ownership (enumeration in …)". | Round 5 restores "defining and recording complete coverage and ownership"; pointer and boundary unchanged. |

**Sweep — still holds after rounds 4–5** (checked against the round-5 text): round-3
scenario rows `evidence.md:230`, `:234–237`; the round-4 checks paragraph
(`evidence.md:306–318`: `fork=` twice, enumeration once at `execution.md:9`, core
enumeration absent, seven link occurrences / six anchors); and the round-4 scenario
rows `evidence.md:326–327` (the quoted "complete coverage and ownership" is still a
substring of `AGENTS.md:22`). The round-3 claim "no (D)/(E)/(F) rule is restated"
(`evidence.md:192`, `:280`) was already marked superseded by the round-4
"corrected claim" subsection. Rounds 1–2 rows concern `AGENTS.md:16`/`:20`/`:26` and
`execution.md`, untouched by rounds 4–5.

### Round-5 metrics

| Measure | Baseline | Round 3 | Round 4 | Round 5 | Δ vs round 4 |
| --- | ---: | ---: | ---: | ---: | ---: |
| `AGENTS.md` lines / bytes | 37 / 5,408 | 37 / 6,632 | 37 / 6,673 | 37 / 6,687 | 0 / +14 |
| `docs/policy/execution.md` lines / bytes | 46 / 9,859 | 46 / 10,467 | 46 / 10,481 | 46 / 10,481 | 0 / 0 |

Net round-5 change: **+14 bytes, 0 lines**, all in the always-loaded core. The three
baseline→final diffs were regenerated against the preserved `baseline/` (66 lines,
unchanged shape); `final-metrics.json` and `final-manifest.json` bind `488316cb…` /
`f6ab19fd…` on HEAD `c82765e`. No file or heading added, so no anchor churn.

### Round-5 checks

`python3 .scratch/24-delegation-ssot-context/validate.py` → **80/80 passed**, exit 0
(`checks.json`). Round-5 updates: D2 and P6 literals now require "defining and
recording complete coverage and ownership"; **P10** was added asserting the restored
persistence verb ("recording complete coverage and ownership"). P5, P7 and P8
(permitted-only, pointer present, core enumeration absent) still pass, so neither the
gate nor the one-home result regressed; P2-A's falsifying case (split without
recording) is now caught by P10. All A/B/C/D/E/F/G and P1–P9 checks, link/anchor
resolution for all seven core→companion link occurrences (six distinct anchors) and
scoped `git diff --check` (exit=0) still pass; nothing is staged.

These remain source/link/whitespace documentation checks, not live agent-behavior
tests. Prose does not enforce tool availability or guarantee compliance; no claim of
zero unknown defects. Residual uncertainty: the `fork=true`/`fork=false` spelling is
the host runtime flag the mapping is tied to; a runtime using a different name would
need that one tie updated. Next acceptance step: a fresh independent reviewer of the
manifest-bound round-5 revision plus an independent reproduction of the commands.
