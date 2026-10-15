const workerTask = [
  'FOLLOW-UP fixes to the policy change in /home/z/vibe/AGENTS.md and /home/z/vibe/docs/policy/execution.md.',
  'An independent review passed all acceptance criteria but left four non-blocking notes. Apply the smallest fix for each; preserve every acceptance semantic; prefer net size reduction.',
  '',
  '1. Internal redundancy (AGENTS.md:20): "no implementation, no verification, no inspection/review and no document writing" is restated by the retained "Never implement or technically verify". Drop one of the two.',
  '2. Cross-home duplication (AGENTS.md:16 vs execution.md Documentation bullet): the ticket + SSOT sentences are near-verbatim in two homes. Keep ONE authoritative statement of the binding rule (in AGENTS.md); in execution.md keep only the documentation-specific method plus a pointer to the core rule, not a verbatim restatement. Do not drop any distinct fact from the policy as a whole: the explicit banned forms, one-home-per-fact, and no duplication/staleness/conflict must still be stated once somewhere.',
  '3. Escape hatch (execution.md:30): "historical records need no rewrite when still recoverable" sits beside the absolute all-documents-rewritten-in-place rule and could exempt a history-bearing document. Qualify it to ticket/archived records.',
  '4. Actor ambiguity: execution.md task-routing ("write the worker contract"), execution.md product-decisions ("record source ..."), and AGENTS.md:11 ("choose and record") name recording acts without attributing them to a subagent. Add attribution only where it is concise; skip if it would bloat.',
  '',
  'Constraints:',
  '- Net line/byte count must NOT grow; prefer reduction. The AGENTS.md core must stay self-contained for its binding rule.',
  '- Verify no meaning is lost: every banned form and every safeguard from the current revision must still appear once in the policy.',
  '- Ticket dir is /home/z/vibe/.scratch/24-delegation-ssot-context/ (round 1). APPEND a round-2 section; preserve round-1 evidence. Update baseline-to-final.diff, final metrics and manifest, and re-run the ticket validate.py plus the link/anchor check.',
  '- Do NOT commit; leave changes in the working tree.',
  '',
  'Return file:line summary of each fix, the round-1 note it closes, evidence paths, and residual uncertainty. Do not claim PASS; a fresh review follows.',
].join('\n');

const reviewTask = [
  'Fresh independent RE-REVIEW of the round-2 fixes to /home/z/vibe/AGENTS.md and /home/z/vibe/docs/policy/execution.md. Do not rely on worker claims; read both files fully, the diff, and the ticket evidence under /home/z/vibe/.scratch/24-delegation-ssot-context/.',
  '',
  'Verify that ALL round-1 acceptance criteria still hold:',
  '1. Main is unconditional/highest-priority: no implementation, verification, inspection/review or document writing; every task including documentation delegated; binds regardless of session age/inherited context; unavailable-delegation stays a blocker.',
  '2. Every task creates/updates a ticket; tickets are the log home (append OK).',
  '3. All document forms = SSOT, current facts only, rewritten in place; banned forms explicitly listed; no duplication/staleness/conflict; one home per fact; history only in tickets.',
  '4. "Preserve other entries" scoped to the ticket/work-record ledger only.',
  '5. Fresh context by default for compact specifiable handoffs; inherit only when a context-free description costs more; independent review never inherits.',
  '6. Concise, no bloat, no contradiction, no weakened safety/authority/evidence boundaries.',
  '7. Relative markdown links/anchors in the changed files resolve.',
  '8. Revision-bound evidence exists and is consistent.',
  '',
  'Also confirm each round-1 note is closed or explicitly justified: (a) no internal redundancy in the Main rule; (b) the ticket+SSOT fact is stated once with no distinct fact lost across AGENTS.md and execution.md; (c) the "historical records need no rewrite" line no longer exempts history-bearing documents; (d) actor ambiguity addressed or acceptably bounded.',
  '',
  'Attempt to falsify: construct a model reading ONLY the changed text that still implements directly, or still writes append-only/dated documents. Report before/after size to confirm no growth.',
  '',
  'Report PASS/FAIL per criterion, each round-1 note as closed/open, and material defects with file:line. Do NOT repair.',
].join('\n');

const w = await runs.run('worker2', { agent: 'worker', task: workerTask });
const r = await runs.run('review2', { agent: 'reviewer', task: reviewTask });
return { workerOutput: w.output, reviewOutput: r.output };
