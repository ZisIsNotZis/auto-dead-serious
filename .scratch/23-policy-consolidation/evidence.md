# Second consolidation — self-proof and review packet

Status: implemented; documentation self-checks passed. **Independent acceptance is pending.** Read the final scoped artifacts, user acceptance/authority in `contract.md`, and this evidence, not the worker conversation. A repair invalidates the affected proof and requires another fresh reviewer.

## Revision and checks

`final-manifest.json` binds the four live scoped documents and active-work record to SHA-256 on HEAD `c82765e53faa60ae04cc3ae4fd1048d1ee5ef953`; four explicitly superseded companions are absent. `baseline/` preserves all nine exact original scoped files, including dirty policy text, plus original status/diff, index state and preservation hashes. `baseline-to-final.diff` isolates this task from prior edits; the Git diff also includes earlier uncommitted policy work.

Reproduce: `python3 .scratch/23-policy-consolidation/validate.py` (30-second foreground bound). Result: **48 checks passed**, including local links/anchors, six exact section routes, retired owning-reference absence, scoped `git diff --check`, dirty-baseline added whitespace, package count/size and preservation. Detailed results: `checks.json`; sizes: `baseline-metrics.json` / `final-metrics.json`.

| Measure | Current baseline | Final |
| --- | ---: | ---: |
| Default core characters / words | 5,609 / 685 | 5,402 / 633 |
| Whole policy characters / words | 22,889 / 2,953 | 15,261 / 1,866 |
| Policy files / companions | 6 / 5 | 2 / 1 |

Core character load falls 3.7%; package load falls 33.3%. No hidden preload: each event links directly to one section, not the entire companion. README/WORKSPACE are not core dependencies.

Inspected final scoped source and baseline-to-final/root-routing diffs. All captured unrelated root tracked artifacts and prior task records retain their original hashes; other worktree/gitlink/untracked status entries and staged diff/HEAD are unchanged. Original `.scratch/active-work.md` remains an exact prefix. No child writes, global configuration changes, staging, commits or publication.

`git submodule status -- drive` completed and reported the existing pinned checkout; `git -C drive status --short` completed with no local changes. These exercise WORKSPACE's new optional inspection commands without changing checkout state. README clone/setup commands were unchanged and not rerun; no quickstart/runtime claim was added.

## Consolidation and retirement rationale

| Current source captured in baseline | Equivalent final home |
| --- | --- |
| AGENTS authority/context, safety, roles and event index | Core retains enforceable boundaries; removes the irrelevant negative filename declaration; allows legitimate task-scoped external evidence and missing applicable instructions. |
| decisions.md | Core autonomy/gates plus `execution.md#product-decisions`: consequential choice provenance/thresholds, tangible slices/POCs, binding gates, feedback correction, PO delivery. |
| execution.md | Core role/safety boundaries plus task-routing/proof-and-review: narrow contracts, sibling coverage/interfaces/integration, late replacement, baseline preservation, revision proof, fresh review/repair and bounded recovery. |
| writing.md | documentation section: authoritative homes, verifiable rules, source provenance, live-reference updates, portable policy, scenario/size/hash proof. |
| environment.md | environment section: target tooling, current authoritative evidence, no security bypass/shared-state surprise, desktop focus, recoverable storage, safe cleanup and tested usage. |
| remote-coordination.md | core explicit discovery trigger plus remote-coordination section: ownership before writes, stale-owner transition, isolation/clean tracker, release/handoff, races/no force-push, bounded observation and ID allocation. |
| WORKSPACE repeated instruction/gate/environment rules | Policy above; WORKSPACE retains actual checkout facts, private slug convention (not a visibility guarantee) and tested optional inspection commands. Static coordination/harness declarations are not durable verified environment facts and did not establish actual ownership/tool availability. |
| README misplaced workspace-rules and agent-rule-as-project-joining references | Correct pointers for people; existing public design/vision remains in README, not portable agent policy. |

All retired files matched their exact captured hashes immediately before deletion. Only the four named policy companions were deleted. Consumers were searched before retirement across live tracked/untracked content, excluding historical scratch. Owning AGENTS/WORKSPACE routes were updated; no live scoped route points to a retired path. Historical scratch records are unchanged and remain recoverable with their original meaning.

**Out-of-scope observations, not introduced owning-link failures:** `resume_private` has two prose source citations to the old remote companion; `learn_draw/WORKSPACE.md` already described that path as absent locally. They are child-project evidence/context, not this package's live owning routes; children were not edited. `README.zh-CN.md` still labels its existing WORKSPACE link as agent rules; the link target exists, but the unchanged label is now imprecise. That root file is outside the authorized README.md/WORKSPACE.md scope. No broad child/root cleanup was performed.

## Concrete scenario walkthroughs (documentation only)

| Scenario / falsifying case | Final rule and observed textual result |
| --- | --- |
| Ancestor isolation: a child task must not preload parent README/WORKSPACE or every method | Core authority/information applies missing root-to-target instructions but limits evidence to task/role; conditional index reads only triggered sections. Already supplied instructions are not reread. Holds. |
| Simple delegation: tiny clear correction tempts main to execute or invent stages | Core main delegates even small/indivisible tasks and never technically verifies. Task-routing keeps a cohesive leaf; product-decisions rejects mandatory tiny-task stages. Holds. |
| Upfront acceptance: implementation starts before options/proof or quietly lowers criteria | Worker core requires interpretation/scope/inherited acceptance/proof/options/split decision before changes; task-routing records unmet criteria instead of reduction. Holds. |
| Split siblings: parent goal beside one mechanical substep, missing integration owner | Core and task-routing require same-layer independently checkable outcomes, complete coverage, child acceptance, interfaces/dependencies/owners and worker integration; artificial editing/testing/reporting splits fail. Holds. |
| Late context pressure: continue blindly, invent a percentage or hand off an unchanged infinite chain | Core checkpoints then splits independent remainders or routes an unsplittable remainder to a fresh replacement. Task-routing preserves revision/remaining acceptance/authority; finite core bounds and no-progress checkpoint prohibit endless continuation. Holds. |
| Reviewer fixes: reuse useful repair context but self-certify resulting revision | Core explicitly permits repair in the reviewer's own context only with authority/tools; they become worker. Proof-and-review requires renewed self-tests and another fresh reviewer; unavailable tools route a labelled writer fallback. Holds. |
| User away: ordinary reversible choices versus an agreed approval gate | Core grants in-scope recorded choices without routine questions; absence is not waiver. Product-decisions requires actual artifact and approval/explicit waiver before dependent gate work; safe independent work continues. Holds. |
| Delegation unavailable: main substitutes direct work or self-review | Main records infrastructure blocker; proof-and-review similarly blocks absent independent review. Neither unavailable proof nor resource exhaustion is PASS. Holds. |
| Out-of-authority action: autonomy used for history rewrite/spending or discussion-only editing | Core distinguishes execution from read-only discussion/review, requires covering authority for high-risk/material changes and pauses only the dependent action. Approved actions need no repeated permission. Holds. |
| Optional data acquisition: task genuinely needs external compatibility evidence or existing project facts | Core permits relevant external evidence and missing applicable instructions; environment checks current authoritative sources when material. No default project-doc dependency or broad external-evidence prohibition. Holds. |
| Uncertain vertical slice/POC: an internal label or promised demo substitutes for user proof | Product-decisions requires actual suitable artifact, hypothesis/proof/continuation criteria for POC and distinguishes internal checkpoints from agreed gates. Holds. |
| Feedback: patch symptoms or invent personality | Product-decisions verifies factual claims, traces originating assumptions, updates necessary confirmed decisions/downstream work only. Holds. |
| Communication and remote state: conversation dumps, implicit locks or arbitrary background promises | Core requires files/minimal control signals and actual bounded completion capabilities. Remote discovery stops competing writes; exclusive fresh ownership, recorded transition/release and bounded observation are explicit. Holds. |

These are source/diff/link/scenario **documentation checks**, not live Pi behavioral tests. No runtime configuration was shipped or tested; prose does not enforce tools or guarantee agent compliance. No claim of zero unknown defects. The next acceptance step is a fresh independent reviewer of the manifest-bound scoped result; main remains PO/routing owner, not technical verifier.
