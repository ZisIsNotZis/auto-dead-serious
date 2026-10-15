## Review — `/home/z/vibe/AGENTS.md` (256 lines: banner, one fenced YAML block, 7 top-level keys in the stated order; `laws` = 10 laws, 4 of them expanding into corollaries)

**Verdict: BLOCK.** Checklist Q1 (one home), Q3 (sourced) and Q7 (justified) fail; Q6 passes with one gap. No contradicting pair found. 1 blocking + 9 non-blocking findings.

### Checklist (the document's own, `change.checklist` AGENTS.md:176)
- **One home: FAIL** — AGENTS.md:156 is verbatim AGENTS.md:150, and AGENTS.md:14 restates AGENTS.md:6.
- **Resolvable: PASS** — all 26 `@` references resolve to keys that exist; the only unresolved item is the command `python3 scripts/render_policy.py --check` (176), which scope forbade checking.
- **Sourced: FAIL** — two counts of their own enumeration are stored in prose: "all four lower the chance and the cost of a mistake" (84) and "The four are never mixed." (184).
- **Declared: PASS** — line 1 declares this file a render of `AGENTS.yaml` and names where the edit belongs; `change.render`, `change.files`, `change.write_only` agree.
- **Sound structure: PASS** — every node is one physical line (only lines 1, 2, 256 lack a `:`), no blank lines, nesting uniform; the one depth variance is noted under question 3 below.
- **Derived from the root: PASS with one gap** — `laws.authority` (23) states a topic, not a rule derived through a story.
- **Justified: FAIL** — sentence 3 of AGENTS.md:11 and the whole of AGENTS.md:156 survive their own delete test.

### Findings
**Blocking**
- **F1, one home — `attention.delivery.invent_no_gate` (AGENTS.md:156):** "Invent no stage or gate for a tiny, clear task, and never relabel ordinary ad hoc work as a milestone to dodge review." is character-for-character `attention.delivery.milestone` (AGENTS.md:150). Violates checklist Q1, `laws.ssot._text` ("Every fact has exactly one main home"), `change.cut_repetition`, and fails `laws.no_op`'s own test. Fix: delete one copy, keeping the name that describes the rule — `milestone` promises the opposite of its text and collides with `milestone_list`.

**Non-blocking**
- **F2, one home/justified — `laws.projection.order` (11):** the node states its rule twice ("An edit never reorders them, because the order carries meaning and a reordering diff buries the change it arrived with. An edit never reorders siblings, because…"). Fix: drop the last sentence.
- **F3, one home — `laws.no_op.stable_key` (14)** "decided by a stable key, the part of the work it serves" restates `laws.ssot._text` (6) "decided by the decision it serves"; its first clause is ssot's mechanism and only its second is no_op's test, so half its content sits under the wrong parent. Fix: leave the home mechanism in ssot._text, keep only the empirical half here.
- **F4, leading word — `laws.projection.order` (11):** bare `order` borrows its head from `projection` and collides with `precedence.source_order` (30) and `precedence.levels_in_order` (31), so `@order` would be ambiguous. Fix: name the concept (`sibling_order`).
- **F5, set of one — `laws.projection.order` and `laws.no_op.stable_key`:** single-member sets that nothing points at — no `@order`, no `@stable_key` anywhere, while `@partition` (92), `@atomic` (200) and `@fail_loud` (89) are referenced. `laws.no_op`: "a split earns its place only when it changes what the model would do". Fix: inline, or reference.
- **F6, sentence keys —** `intent.decisions.principles_are_not_authority` and `intent.decisions.milestones_are_fixed` are full declarative sentences where the rename allows none; `intent.roles.main_delegates` is a subject+verb clause. Fix: `no_authority`, `fixed`, `delegates`.
- **F7, one term in two senses — `intent.risk.secrets`:** "key" means a credential, while `laws.ssot.partition` (7), `laws.no_op.stable_key` (14), `change.resolvable` (186) and `change.field_admission` (203) use key for a mapping/partition key, and neither sense is defined. Violates `resources.efficiency.one_name` (87) and `change.field_admission`. Fix: say credential.
- **F8, not actionable — `laws.authority` (23):** "Whose word wins, and what may not be done without consent." states no rule and points nowhere, while `change.file_kind` requires a router to point at the file that owns each fact. Fix: state the rule, or `@precedence.source_order` and `@intent.risk.high_risk`.
- **F9, undefined abbreviation —** first use not expanded: API (74), CPU/GPU (`start_early`), env (`intent.risk.secrets`), repo (`cleanup_check`), while CI, DAG, POC, TLDR and SSOT are expanded, so the file's own `intent.user_model.user_language` rule ("Define any term you introduce at its first use") is unevenly applied.
- **F10, stored count —** "all four" (84) and "The four" (184) store the size of their own list; `laws.derived` (19) says a count is generated from its source or carries no fact. Fix: refer to the set, not its size.

### The four asked
1. **Leading words:** only two named keys are full sentences (F6) and `order` is the one whose sense depends on its parent (F4); the rest are single strong tokens or two-word noun phrases (ssot, atomic, top_down, absent, invalidate, waste, commits, deadline, baseline).
2. **The tree:** `ssot > partition` and `ssot > atomic` are real (partition states ssot's own home-decision mechanism; atomic's addressability is what makes an `@`-reference possible, which ssot._text requires). `no_op > stable_key` is half real (F3). `projection > order` rests on assertion — its stated reason ("a reordering diff buries the change", 11) is diff legibility, not the graph-to-tree cost `projection._text` (10) names — so that is the one arguable invented edge. Reachability: all ten laws are pointed at (`@ssot` 176, `@projection` 178, `@no_op` 199, `@falsifiable` 224, `@top_down` 176, `@derived` 187, `@absent` 188/211, `@controlled` 226, `@invalidate` 227, `@authority` 30/74); `@order` and `@stable_key` are not. No leaf law is merely a consequence of another; the closest call is `laws.controlled` (21), which specialises falsifiable but carries its own action.
3. **Sibling sets:** no set mixes a rule with a sub-branch. All-branch: `intent` (6), `resources` (6), `attention` (3), `proof` (3). All-rule: `precedence` (9), `change` (39). `laws` (3) holds 4 branches and 6 leaves, but all ten values are of one kind — a law — so `laws.ssot.partition` is satisfied; it is the only place depth varies. Sets of one: `projection > order`, `no_op > stable_key`, and `falsifiable > fail_loud` (that one justified by `@fail_loud`).
4. **Previous blockers:** (a) **FIXED** — what the reader sees, lines 1–256, is one fenced YAML block in which every node is one physical line; the only colon-less lines are the banner (1) and the two fences (2, 256), so `laws.atomic` (8) is now true of the file. (b) **FIXED** — `intent` (35) has exactly six children (objective, user_model, scope, decisions, roles, risk), every one a sub-branch carrying its own `_text`, with no bare rule among them.

### Not verified / limits
- The 223-key figure was not independently counted (search output truncates at 100 matches); arithmetic over 256 lines minus the banner, two fences and 31 `_text` nodes gives 222 named keys — inference, possibly off by one.
- `python3 scripts/render_policy.py --check` (176) was neither run nor located; opening it was out of scope, so its existence and green state are unknown.
- `@`-reference completeness was checked only against the 26 `@` occurrences inside this file; a source written as prose rather than `@key` would escape the check.
- Judgements of "sourced" elsewhere rest on this file being read once at launch; no other revision, schema, renderer, `docs/`, `.scratch/` or history was opened.

### Reply
**Verdict: BLOCK** — 1 blocking + 9 non-blocking findings; 3 of 7 checklist questions fail (one home, sourced, justified).
Blocking gist: `attention.delivery.invent_no_gate` (line 156) is a verbatim duplicate of `attention.delivery.milestone` (line 150), so the fact has two homes in one file and fails the document's own `laws.ssot` and `laws.no_op` tests.
Both previous blockers are genuinely fixed, not reworded: the file the reader sees is one node per physical line, and `intent`'s children are six sub-branches of one kind.
Tree and leading words mostly hold; the weak points are `laws.projection.order` (duplicated rule, parent-dependent name, nothing references it) and `laws.no_op.stable_key` (half its content belongs to `ssot`).