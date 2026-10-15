const workerTask = [
  'TASK: two deliverables. Read /home/z/vibe/AGENTS.md and /home/z/vibe/docs/policy/execution.md fully first.',
  '',
  '(A) POLICY CHANGE — review cadence + worker self-loop. Edit ONLY /home/z/vibe/AGENTS.md and /home/z/vibe/docs/policy/execution.md.',
  'Required semantics:',
  '1. Independent review is a VERTICAL-SLICE gate, not a per-task/per-subtask gate. Each vertical slice gets at least one fresh independent review before the slice is declared complete; the exact timing within the slice is flexible. Define "vertical slice" as a bounded end-to-end user outcome, consistent with the existing Product decisions wording.',
  '2. Within a slice, the worker runs a self-loop: first derive and record its own acceptance standard, then execute, then check the result against that standard, and iterate until done. Do NOT require a separate independent review for every task or sub-task.',
  '3. Work with no corresponding vertical slice (for example record/policy/documentation-only work) gets independent review only when the user explicitly asks for one.',
  '4. Reconcile with existing rules without weakening them: keep revision-bound self-proof, fresh independent review, "never accept the repairer\'s own verdict", and all safety/authority/evidence boundaries intact. State that a self-test is the in-slice loop and is NOT independent acceptance; the slice-gate reviewer remains independent.',
  '5. Concise; state each rule once (AGENTS.md = binding boundary, execution.md = method/pointer); facts as current SSOT, no dated narrative.',
  '',
  '(B) Record the verified subagent-parameter fact in the ticket (NOT in the policy — keep policy model/platform independent):',
  '- Thinking is controlled ONLY by the model suffix: exact provider/id plus :off|minimal|low|medium|high|xhigh|max. The dispatch "thinking" field is ignored on dispatch (watchdog.configure only).',
  '- Builtin worker/reviewer frontmatter defaults thinking to high; children otherwise inherit the parent session model.',
  '- Preferred fix for doc-edit children: pass the model suffix per run, e.g. model: "deepseek/deepseek-flash:medium". Alternatives: edit agent frontmatter (environment change) or define a custom low-thinking agent. Note that /home/z/.pi/agent/extensions/agents/worker.md declares a model that was NOT applied.',
  '- Evidence: subagent({action:"models"}) output and guide topic=tool-reference (model param row).',
  '',
  'PROCESS (apply the new rule to this very task): first write down your own acceptance standard in the ticket, then make the edits, then self-check against that standard, and iterate until it passes. Leave revision-bound evidence.',
  '',
  'Constraints: create ticket dir /home/z/vibe/.scratch/<next-unused-NN>-slice-review-selfloop/. Self-test link/anchor and whitespace ("git diff --check"); record commands+results. Do NOT commit; leave changes unstaged.',
  'Return: file:line summary, the self-derived standard and its verification, evidence paths, net size change, residual uncertainty.',
].join('\n');

const w = await runs.run('worker', { agent: 'worker', task: workerTask });
return { workerOutput: w.output };
