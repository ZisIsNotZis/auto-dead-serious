const items = args.paths.map(path => ({path, packet: '/home/z/vibe/.tmp/catalogue-fast-inputs/' + path + '.json'}));
const results = await runs.all(items.map(item => ({
  key: 'score-' + item.path,
  label: 'Score ' + item.path,
  agent: 'catalogue-score-one',
  model: 'github_copilot/gpt-6-luna:high',
  cwd: '/home/z/vibe',
  context: 'fresh',
  timeoutMs: 600000,
  output: 'fast/' + item.path + '.json',
  task: 'Rate only ' + item.path + '. Read exactly this supplied packet: ' + item.packet + '. Return the concise numeric JSON contract. Do not open any other file.'
})));
return results.map((result, i) => ({path: items[i].path, ...result}));
