## Review
Verdict: **OK with notes** — no correctness or contradiction defect found. 16 compaction candidates, each measured against the file's own tests: `@no_op` (":11 a rule saying what the model already does is too fine", "a statement earns its place only by changing a decision") and `@cut_repetition` (":204 Keep every meaning in one home"). Path for every finding: `/home/z/vibe/AGENTS.md`.

**Deletions — statement fails @no_op because the model already does it, or the fact already has a home**

1. **P1** `:229` `single_variable: Change one thing per comparison and hold every other condition equal. @controlled` — `:17 controlled` says this word for word. Cost: a second home for a cited law plus ~14 tokens per read.
2. **P1** `:230` `rerun: Rerun the checks a change invalidated, and re-examine what it did not mean to change. @invalidate` — `:18 invalidate` already contains "including the parts it did not mean to change". Cost: same duplicate-home waste.
3. **P1** `:70` `Storing and using keys is common sense - env or a secret manager, never committed.` — the file itself calls it common sense, so it changes no decision; only the tail ("Do not ask just because a credential appeared…") does. Cost: ~15 tokens of default behaviour.
4. **P2** `:77` `efficiency._text: Reduce errors, raise efficiency, save the user's time.` — aspiration with no decision; keep the second sentence, which is the reason.
5. **P2** `:45` `scope._text: … Perfect does not mean doing everything.` — restatement of "Depth beats breadth" inside the same node.
6. **P2** `:97` `commits: … A commit is local and reversible.` — git semantics a model holds; the branch/merge rule is the real content.
7. **P2** `:78` `defect_surface: … each of them lowers the chance and the cost of a mistake.` — restates the node name; the four verbs are the rule.
8. **P2** `:153` `tldr: TLDR. Lead with a summary…` — the id is already the word, and "lead with a summary" duplicates `:152 conclusion_only` "Give the conclusion".
9. **P2** `:64` `worker: Finish with full effort and prove it.` — `:219 proof._text` already owns "Work must be independently provable".
10. **P2** `:257` `subagent_scope: … so it does not do what it should not.` — purpose clause the model holds from "scope plus its tool list and limits".

**Collapses — a sentence spending tokens to gesture at a word the model holds**

1. **P1** `:63` `delegation: … no substantive work at all - no implementation, no checking, no review, no document writing.` → **nothing** (the list gestures at a point the preceding clause already makes).
2. **P1** `:223` `completion: The burden of completion sits on the one doing the work.` → **burden**; the operative content is the remainder of the line.
3. **P2** `:27` `levels_in_order: … and a lower one contradicting a higher one is void.` → **void**.
4. **P2** `:175` `no_mood_labels: … A statement's weight is derived from those at judgement time, not stored as a mood.` → **mood**; sentence one already carries the rule.
5. **P2** `:164` `match_user: … without infantilising …` → **match**.
6. **P2** `:152` `conclusion_only: … but keep it readable …` → **conclusion**.

**Limits**
- Read once, line numbers from that read; no diff or other path, so I cannot tell injected fact from render boilerplate, and did not compare `AGENTS.yaml`.
- Did not run `python3 scripts/render_policy.py --check` (":202"); no write, no commit. Nothing here is a correctness blocker — all items are token cost and duplicate homes.

---
**Reply**

Verdict: OK with notes (compaction only); 10 deletions + 6 collapses, 3 + 2 of them P1; nothing blocking.
Delete first: `:229 single_variable` (duplicate of `:17 controlled`), `:230 rerun` (duplicate of `:18 invalidate`), `:70 secrets` opening clause — the file calls it common sense.
Collapse first: `:63 delegation` → **nothing**, `:223 completion` → **burden**, `:27 levels_in_order` → **void**.