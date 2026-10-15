## Review

**Merge verdict: BLOCK — restore one explicit authority boundary before adopting this policy.** The remaining changes match the requested direction.

### Correct
- **Autonomous implementation:** `AGENTS.md:11–13` and `docs/policy/decisions.md:5` front-load consequential questions, then allow justified in-scope decisions—including unspecified product details during full delegation.
- **Readable, product-centered reporting:** `AGENTS.md:15` and `docs/policy/decisions.md:9` explain user effects through confirmed goals and scenarios, with technical identifiers serving as supporting references.
- **Critical handling of guidance:** `docs/policy/decisions.md:8` distinguishes preferences from factual claims and proposed solutions, and updates the highest necessary authoritative layer plus affected downstream material—not mechanically every layer.
- **Real continuation mechanisms:** `AGENTS.md:21` and `docs/policy/execution.md:14` require observable results and verified continuation, without assuming a particular harness.
- **Optional specialists and bounded research:** `docs/policy/execution.md:9,16,28` provides safe fallback work and a diminishing-returns stopping rule.

### Finding: P0 — Material spending no longer has an explicit authorization gate
**Location:** `AGENTS.md:13,20`; `docs/policy/decisions.md:6`; affected reference in `docs/policy/environment.md:5`.

The diff removes the root’s explicit user-owned boundary for material cost, privacy, legal exposure, and operations. Its replacement requires staying within “granted authority,” but does not establish which of those effects require separate authorization. The remaining safeguard enumerates destructive actions, dependency consequences, and changes to approved contracts or trade-offs—not standalone material spending.

Meanwhile, the new consequential-choice guidance treats recurring costs as choices to highlight and record. `environment.md:5` still routes material cost and privacy consequences to the root user-decision boundary, whose explicit classification has disappeared.

**Concrete scenario:** An absent user delegates a feature without granting spending authority. Upgrading an already configured service to a materially more expensive recurring tier need not introduce a dependency, destructive action, or change an explicitly approved product contract. The revised policy no longer clearly distinguishes that expense from a consequential in-scope choice to record and execute.

**Smallest fix:** Retain an explicit root safeguard that material spending and material privacy, legal, or high-risk operational effects require authority covering those effects; autonomy or absence alone does not supply it. Spending already covered by granted authority should proceed without another checkpoint. Continue independent work while any genuinely unapproved action is deferred.

### Scenario checks

| Scenario | Result |
|---|---|
| Absent user; unspecified in-scope product detail | Choose, record consequential assumptions, verify, continue (`AGENTS.md:13`). |
| Ordinary technical ambiguity | Research or experiment, choose a reversible direction; no permission gate (`decisions.md:5`). |
| Unapproved recurring expense | **Boundary omission above.** |
| Pre-agreed demo checkpoint | Honor it for dependent work; continue independent work (`execution.md:15`). |
| Erroneous factual suggestion versus taste | Test facts; respect goals and preferences (`decisions.md:8`). |
| Optional worker unavailable | Safe parent execution or documented self-review (`execution.md:28`). |
| Detached job without notification | Not a continuation mechanism; foreground results or active bounded checks required (`execution.md:14`). |
| Research diminishing returns | Assess expected new evidence and stop repetitive work (`execution.md:16`). |

### Validation and limits
Reviewed the exact working-tree diff twice and read the five named policy files plus `WORKSPACE.md`. Companion references resolve; the material-cost boundary is a **semantic reference regression**, not a missing path. No edits or delegation performed.

Shell checks were unavailable. The parent should run the required scoped `git diff --check` and record before/after character counts under `docs/policy/writing.md:8`. This review does not attest to committed ranges or runtime wake behavior.