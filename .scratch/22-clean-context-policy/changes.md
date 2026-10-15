# Changes and durable rationale

Authority and acceptance are in [contract.md](contract.md). This is a documentation-only implementation of the user's approved design, not a runtime/harness deployment. Compare [implementation.diff](implementation.diff) with the saved starting contents; [final-head.diff](final-head.diff) includes earlier dirty changes and must not be attributed wholly to this task.

## Changed seams

- **Core:** replaced the mandatory applicable-WORKSPACE startup read with already-supplied instruction reuse, fetching only missing applicable instructions, and task/role-scoped project evidence. Policy references resolve from their owning AGENTS, not a child project or shell cwd. Made product-owner main, worker, and independent reviewer boundaries explicit. Main delegates every substantive task and never substitutes its own execution/technical checks for missing infrastructure.
- **Execution:** replaced optional delegation/self-review/direct-parent fallbacks with bounded task dispatch, upfront worker contracts, peer outcome decomposition, technical integration ownership, late splitting or fresh replacement, self-proof, and fresh adversarial acceptance/repair. Reviewer repair is authority/tool-dependent and ends reviewer independence; a read-only reviewer routes a labelled writer fallback. Changed proof receives a new fresh review.
- **Decisions:** retained the baseline's product-centered expression, kickoff questions and authorized autonomy; added conditional end-to-end user slices, concrete review artifacts, POC hypothesis/proof/continue criteria, and a binding gate/waiver distinction. Feedback now explicitly corrects results and traces originating decisions without inventing a user profile.
- **Writing:** kept authoritative sources, one home, placement, executable-rule and portability tests; made fresh acceptance required instead of optional self-review fallback. Required policy proof distinguishes documentation checks from runtime claims.
- **Environment/remote:** retained toolchain, security, preservation, shared-desktop, collision, ownership, bounded observation, and publication safeguards. Removed workspace-document/ticket-layout dependencies and made execution ownership and publication authority explicit. README use is conditional on changing that entry point, not startup.
- **Records:** saved baseline contents/diff/status/size/protected hashes, this upfront contract, attributed changes, structural checks, scenario evidence, final policy hashes, and a user-readable summary. Appended only this task's active entry; retained earlier task records and active-work content unchanged.

## Reversible interpretation choices

1. Keep all five topic names and an owner-relative linked index. Optional means selectively loaded by concrete event/section, not weaker acceptance or a requirement to read the whole package. No bulk companion preload chain was added.
2. Put short invariant role rules in the core and dispatch/review/decomposition methods in execution. A leaf still uses worker proof and independent review; "tiny" exempts invented milestones, not delegation or acceptance.
3. Preserve default review-only authority: discussion/options/review requests are read-only unless execution/repair is explicitly authorized. An authorized workflow may allow reviewer repairs, but cannot manufacture tools or authorize read-only mutation.
4. Separate technical PASS from user-gate approval/publication. The current policy task has no invented user milestone; independent review is its required technical acceptance, and the active item remains pending until that acceptance.
5. Treat insufficient context operationally, not numerically: checkpoint then split true independent remainders or replace the unsplittable worker. There is no platform token threshold or infinite same-task forwarding rule.
6. Treat documentation-only proof as valid for documentation acceptance, with runtime behavior outside this implementation's proof. Untested required acceptance is incomplete; untested out-of-scope runtime is disclosed, not claimed delivered.

## Size and load trade-off

Counts exclude WORKSPACE/README because they are not part of the shippable policy package. Counts are characters/whitespace-delimited words, not asserted context-token measurements.

| Scope | Before characters | After characters | Before words | After words |
|---|---:|---:|---:|---:|
| Core AGENTS.md | 6,694 | 5,609 | 905 | 685 |
| Five companions | 15,943 | 17,280 | 2,235 | 2,268 |
| Whole package | 22,637 | 22,889 | 3,140 | 2,953 |

The core shrank 1,085 characters (16.2%) and 220 words (24.3%). The whole package grew 252 characters (1.1%) but shrank 187 words (6.0%). The execution companion grew for newly required dispatch contracts, coverage/interfaces, replacement, adversarial repair and incomplete-status rules; this is new approved behavior, not relocated philosophy. Old optional-review/direct-main fallbacks and workspace-specific routines were removed rather than copied elsewhere. Character growth is disclosed, not called package shrinkage.

## Attribution and limits

Starting AGENTS/decisions/execution were already dirty. Their existing safety, natural reporting, autonomous choice, continuation, and feedback requirements remain except where the approved redesign supersedes execution roles, startup routing, and optional review. No commits, staging, pushes, runtime configuration, child edits, WORKSPACE/README edits, or prior-task rewrites were performed. Protected hashes and unrelated Git status are checked; child repository contents were not broadly audited. Independent acceptance remains pending, so there is no final policy PASS here.
