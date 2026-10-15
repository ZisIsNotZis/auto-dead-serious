const workerTask = [
  'ROUND 4: close the three report-only P2 notes from the round-3 independent review, without regressing any acceptance semantic. Edit ONLY /home/z/vibe/AGENTS.md and /home/z/vibe/docs/policy/execution.md. Read both fully first. Round 3 revision is bound to sha256 9b28a9b6… (AGENTS) / 4b18a91e… (execution).',
  '',
  'P2-1 (execution.md:7, contradiction): "Every assignment … states its task and acceptance criteria (AC)" reads as if it also binds an inherited-context handoff, contradicting the next sentence. Qualify explicitly: state that SMART/specific-and-actionable applies to every assignment, but the explicit task+AC statement is required for a fresh (fork=false) handoff; an inherited-context (fork=true) handoff already carries task and AC in context, so it designates only the role and proceeds.',
  '',
  'P2-2 (AGENTS.md:22 vs :26, conditional read): AGENTS.md:22 says "Split a splittable assignment into same-layer siblings" unconditionally, while :26 gates it on explicit permission/runtime/bounds. Make :22 read as permitted-only (qualifier or a short pointer to the gate) so either line alone gives the same guidance.',
  '',
  'P2-3 (duplication + inaccurate evidence): AGENTS.md:22 re-enumerates "complete coverage, owners, interfaces, dependencies and an integration owner", which also appears at execution.md:9. Prefer one home: in AGENTS.md:22 keep only the core boundary (a worker may split when permitted and must define complete coverage/ownership) and point to execution.md:9 for the enumeration; OR, if the core must stay self-contained, keep the enumeration once and correct evidence.md so it no longer claims no cross-file duplication. Whichever is chosen, the policy as a whole must state every distinct fact once and evidence.md must be accurate.',
  '',
  'Constraints:',
  '- Concise; no net size growth if avoidable; do not drop or weaken any accepted rule.',
  '- Ticket dir /home/z/vibe/.scratch/24-delegation-ssot-context/: APPEND a round-4 section; preserve rounds 1-3.',
  '- Re-run validate.py, link/anchor checks and "git diff --check"; regenerate diffs, metrics and final-manifest.json; correct any inaccurate evidence claim.',
  '- Do NOT commit; leave changes unstaged.',
  '',
  'Return: file:line summary, which P2 each closes, evidence paths, net size change, residual uncertainty. Do not claim PASS; a fresh review and an independent command reproduction follow.',
].join('\n');

const reviewTask = [
  'Fresh independent RE-REVIEW after round 4. Do not rely on worker claims: read /home/z/vibe/AGENTS.md and /home/z/vibe/docs/policy/execution.md fully, the diff, and evidence under /home/z/vibe/.scratch/24-delegation-ssot-context/.',
  '',
  'Confirm all prior acceptance criteria still hold:',
  '1. Main unconditional highest-priority: no implementation/verification/inspection/document writing; every task including documentation delegated; binds regardless of session age/inherited context; unavailable delegation is an infrastructure blocker.',
  '2. Every task creates/updates a ticket; tickets are the log home; append-style for tickets only.',
  '3. Non-ticket documents hold current facts only, one home per fact, rewritten in place; banned list; no duplication/staleness/conflict.',
  '4. "Preserve other entries" scoped to the ticket ledger.',
  '5. Fresh context by default; inherit only when a context-free description costs more; independent review never inherits.',
  '6. (D) a worker may split its own assignment only when granted permission/runtime/bounds, with coverage/owners/interfaces/dependencies/integration owner recorded.',
  '7. (E) assignments are SMART/specific-and-actionable; fresh handoffs carry the explicit task+AC and full compact contract; inherited handoffs do not restate the task and only designate the role.',
  '8. (F) agent-to-agent messages stay minimal with no large prose blocks; valuable results land on disk as documents/tickets; report to Main is a short description plus done/not-done.',
  '9. (G) ticket vs fact-document classes are explicitly disjoint.',
  '10. Concise, no weakened boundaries; relative links/anchors resolve; revision-bound evidence is internally consistent.',
  '',
  'Verify the three round-3 P2 notes are CLOSED or explicitly justified: (P2-1) no reader can make a fork handoff restate the task; (P2-2) AGENTS.md:22 and :26 agree read alone; (P2-3) every distinct fact is stated once and evidence.md is accurate.',
  '',
  'Falsify: a model reading only the changed text (a) passes an under-specified fresh task, (b) restates the whole task to a fork child, (c) dumps a long report to Main, (d) applies in-place rewrite to a ticket or append-style to a fact document. Report PASS/FAIL per criterion, the three P2 statuses, before/after size, and material defects with file:line. Do NOT repair.',
].join('\n');

const verifyTask = [
  'Independent command reproduction after round 4. READ and RUN commands only; do NOT edit, create or delete anything.',
  'Run exactly and report raw output for each:',
  '1. cd /home/z/vibe && sha256sum AGENTS.md docs/policy/execution.md',
  '2. cd /home/z/vibe && python3 .scratch/24-delegation-ssot-context/validate.py; echo EXIT=$?',
  '3. cd /home/z/vibe && git diff --check -- AGENTS.md docs/policy/execution.md; echo EXIT=$?',
  '4. cd /home/z/vibe && git status --short AGENTS.md docs/policy/execution.md; git diff --cached --stat',
  '5. cd /home/z/vibe && wc -l -c AGENTS.md docs/policy/execution.md; git rev-parse HEAD',
  'Then read /home/z/vibe/.scratch/24-delegation-ssot-context/final-manifest.json and state whether the observed sha256 values and byte/line counts match it. Report raw evidence only, state any mismatch explicitly, do not judge policy content.',
].join('\n');

const w = await runs.run('worker4', { agent: 'worker', task: workerTask });
const r = await runs.run('review4', { agent: 'reviewer', task: reviewTask });
const v = await runs.run('verify4', { agent: 'worker', task: verifyTask });
return { workerOutput: w.output, reviewOutput: r.output, verifyOutput: v.output };
