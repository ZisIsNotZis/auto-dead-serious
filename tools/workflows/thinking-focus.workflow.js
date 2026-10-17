const workerTask = [
  'TASK: add the "focused mental space / economy by default" rules to the project policy. Read /home/z/vibe/AGENTS.md and /home/z/vibe/docs/policy/execution.md fully first. A prior ticket dir .scratch/<NN>-slice-review-selfloop/ may already exist — reuse it if present (append), otherwise create a ticket. Edit ONLY the two policy files plus ticket artifacts.',
  '',
  'Required semantics:',
  '1. Default to the main agent\'s own reasoning budget for every agent, main and sub alike; normally that is the session default (low). Raise the reasoning budget only when the work is genuinely complex or when an agent repeatedly fails. Do not spend high reasoning by default.',
  '2. Focus principle (state it as the reason, not only cost): keep each agent\'s context/mental space small and focused. Prefer splitting work over assigning unrelated tasks to one agent, and avoid needless long reasoning. A bloated or multi-purpose context degrades focus.',
  '3. Sub-agent thinking default should match the main agent\'s default; the builtin worker/reviewer high default is an exception the caller overrides per run (mechanism detail goes in the ticket, not the policy — keep policy model/platform independent).',
  '',
  'Placement: AGENTS.md carries the concise binding boundary; execution.md carries the method (when to raise the budget, how splitting preserves focus) and points to the core rule. State each rule once; current-facts SSOT, no dated narrative.',
  '',
  'PROCESS: write your own acceptance standard in the ticket first, then edit, then self-check against it, iterate until done. Self-test link/anchor and "git diff --check"; record commands+results. Do NOT commit; leave changes unstaged.',
  'Return: file:line summary, self-derived standard and its verification, evidence paths, net size change, residual uncertainty.',
].join('\n');

const w = await runs.run('worker', { agent: 'worker', model: 'deepseek/deepseek-flash:low', task: workerTask });
return { workerOutput: w.output };
