const workerTask = [
  'TASK: Extend the project policy with three PO-required semantics. Edit ONLY /home/z/vibe/AGENTS.md and /home/z/vibe/docs/policy/execution.md. This is round 3; round 2 fixes are already in the working tree. Read both files fully first; preserve all existing acceptance semantics and keep wording concise (prefer no net core-size growth).',
  '',
  '(D) Subagents may further subdivide their own task: a sub agent that judges its assignment splittable may split it into same-layer siblings, subject to explicit permission, runtime support and the existing depth/bounds rules. It must record complete coverage, owners, interfaces, dependencies and an integration owner. Reconcile this with the existing clause "Recursive delegation needs explicit permission, runtime support and the bounds above"; do not silently grant recursion.',
  '',
  '(E) SMART, specific-and-actionable assignment, differentiated by context mode:',
  '- Every assignment must be SMART, above all specific and actionable: state what the task is and its acceptance criteria (AC).',
  '- Fresh / non-inherited handoff (fork=false): carry the full compact contract the child cannot otherwise know — objective, scope/exclusions, acceptance/AC, inputs, outputs, proof, stop conditions.',
  '- Inherited-context handoff (fork=true): the inherited context already carries the task, so do not restate it. The handoff only designates the role — you are the sub agent; do this work — and proceeds.',
  '- Use the existing "fresh / inherited context" vocabulary; tie it once to the fork flag so the mapping is explicit. This must not contradict "fresh by default".',
  '',
  '(F) Concise inter-agent communication:',
  '- Agent-to-agent messages stay minimal; do not pass large prose blocks between agents.',
  '- Valuable results land on disk as documents and tickets.',
  '- A report back to Main carries only a very short description plus done / not-done status; no transcripts and no restated detail.',
  '',
  '(G) Resolve the round-2 P2 ambiguity: AGENTS.md:16 says "All documents, in every form, hold current facts only ... rewritten in place", but a ticket is also a document and is append-style (execution.md:11). Make the two classes explicit so a literal reader cannot apply in-place rewrite to tickets nor append-style to fact documents; smallest fix is to scope the universal (e.g. fact/other documents) and name tickets as the log class.',
  '',
  'Constraints:',
  '- Concise; state each rule once; do not duplicate across AGENTS.md and execution.md (AGENTS.md holds the binding boundary, execution.md the method/pointer).',
  '- Ticket dir: /home/z/vibe/.scratch/24-delegation-ssot-context/. APPEND a round-3 section; preserve rounds 1-2.',
  '- Re-run the ticket validate.py plus link/anchor and "git diff --check"; update the diff, metrics and manifest. Report net size change.',
  '- Do NOT commit.',
  '',
  'Return file:line summary, evidence paths, net size change, residual uncertainty. Do not claim PASS; a fresh review follows.',
].join('\n');

const reviewTask = [
  'Fresh independent RE-REVIEW after round 3. Do not rely on worker claims: read /home/z/vibe/AGENTS.md and /home/z/vibe/docs/policy/execution.md fully, the diff, and evidence under /home/z/vibe/.scratch/24-delegation-ssot-context/.',
  '',
  'First confirm the round-1 acceptance criteria still hold: Main unconditional highest-priority delegation (no implementation/verification/inspection/document writing, all work delegated, context-age binding, unavailable-delegation blocker); every task creates/updates a ticket as log home; all document forms = SSOT current-facts rewritten in place with the banned list and no duplication/staleness/conflict; "Preserve other entries" scoped to the ticket ledger; fresh context by default with inheritance only when a context-free description costs more and review never inherits; concise and no weakened boundaries; links/anchors resolve; revision-bound evidence.',
  '',
  'Then verify the round-3 additions:',
  '(D) A sub agent may subdivide its own task into same-layer siblings within explicit permission/runtime/bounds, with coverage, owners, interfaces, dependencies and an integration owner recorded.',
  '(E) Assignments are SMART/specific-and-actionable; fresh handoffs (fork=false) carry the full compact contract; inherited-context handoffs (fork=true) do not restate the task and only designate the role; the mapping uses the existing fresh/inherited vocabulary and does not contradict fresh-by-default.',
  '(F) Agent-to-agent messages stay minimal with no large prose blocks; valuable results land on disk as documents/tickets; reports to Main are a one-line description plus done/not-done status.',
  '(G) The round-2 ambiguity is resolved: the current-facts/rewrite-in-place rule and the append-style ticket class are explicitly disjoint, so a literal reader cannot apply in-place rewrite to tickets nor append-style to fact documents.',
  '',
  'Falsification attempts: construct a model reading only the changed text that (a) passes an under-specified task to a fresh child, (b) restates the whole task to a fork child, or (c) dumps a long report to Main. Report PASS/FAIL per criterion and per round-3 item, before/after size, and material defects with file:line. Do NOT repair.',
].join('\n');

const w = await runs.run('worker3', { agent: 'worker', task: workerTask });
const r = await runs.run('review3', { agent: 'reviewer', task: reviewTask });
return { workerOutput: w.output, reviewOutput: r.output };
