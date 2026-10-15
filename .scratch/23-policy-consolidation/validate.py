"""Reproduce scoped documentation checks; this does not exercise agent runtime."""
from pathlib import Path
import difflib
import hashlib
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
RECORD = ROOT / '.scratch/23-policy-consolidation'
BASELINE = RECORD / 'baseline'
SCOPED = [
    'AGENTS.md', 'docs/policy/decisions.md', 'docs/policy/environment.md',
    'docs/policy/execution.md', 'docs/policy/remote-coordination.md',
    'docs/policy/writing.md', 'README.md', 'WORKSPACE.md', '.scratch/active-work.md',
]
LIVE = ['AGENTS.md', 'docs/policy/execution.md', 'README.md', 'WORKSPACE.md']
RETIRED = [name for name in SCOPED if name.startswith('docs/policy/') and name not in LIVE]


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT, timeout=20)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def metrics(path):
    data = path.read_bytes()
    text = data.decode()
    return dict(sha256=digest(path), bytes=len(data), characters=len(text),
                words=len(text.split()), lines=len(text.splitlines()))


def anchors(path):
    return {re.sub(r'[^\w\- ]', '', line.lstrip('#').strip().lower()).replace(' ', '-')
            for line in path.read_text().splitlines() if line.startswith('#')}


checks = []


def check(name, condition, detail):
    assert condition, f'{name}: {detail}'
    checks.append(dict(check=name, result='PASS', detail=detail))


before = json.loads((RECORD / 'baseline-metrics.json').read_text())
check('exact original snapshots',
      all(digest(BASELINE / name) == before[name]['sha256'] for name in SCOPED),
      'All nine scoped original files match captured hashes, including all retired companions.')
check('retirement boundary',
      all(not (ROOT / name).exists() for name in RETIRED)
      and sorted(p.name for p in (ROOT / 'docs/policy').iterdir()) == ['execution.md'],
      'Only four explicitly superseded companions retired; one operational companion remains.')
for saved, label in [('unrelated-tracked-hashes.json', 'unrelated tracked artifacts'),
                     ('prior-record-hashes.json', 'prior scratch records')]:
    originals = json.loads((BASELINE / saved).read_text())
    check(label, all((digest(ROOT / name) if (ROOT / name).is_file() else None) == expected
                     for name, expected in originals.items()),
          f'{len(originals)} captured paths unchanged.')
check('index preservation', git('diff', '--cached', '--binary') == (BASELINE / 'index.diff').read_bytes(),
      'Staged diff unchanged; no staging/commit/publication performed.')
check('HEAD preservation', git('rev-parse', 'HEAD') == (BASELINE / 'head.txt').read_bytes(),
      'HEAD unchanged.')
check('other active entries', (ROOT / '.scratch/active-work.md').read_bytes().startswith(
      (BASELINE / '.scratch/active-work.md').read_bytes()),
      'Original active-work bytes preserved as exact prefix; only this task appended.')


def unrelated_status(data):
    return [line for line in data.decode().splitlines()
            if line[3:] not in SCOPED and line[3:] != '.scratch/23-policy-consolidation/']


current_status = git('status', '--short')
check('unrelated worktree status', unrelated_status(current_status) == unrelated_status(
      (BASELINE / 'status.txt').read_bytes()),
      'Other tracked/gitlink/untracked status entries unchanged; children not written.')
(RECORD / 'final-status.txt').write_bytes(current_status)

links = []
for name in LIVE + ['.scratch/active-work.md']:
    owner = ROOT / name
    for target in re.findall(r'\]\(([^)]+)\)', owner.read_text()):
        if re.match(r'\w+://|mailto:', target):
            continue
        filename, _, anchor = target.partition('#')
        destination = owner.parent / filename if filename else owner
        check(f'link {name} -> {target}', destination.exists(), 'Local target exists.')
        if anchor:
            check(f'anchor {name} -> {target}', anchor in anchors(destination), 'Target heading exists.')
        links.append(dict(source=name, target=target))
core = (ROOT / 'AGENTS.md').read_text()
retired_pattern = re.compile(r'(?:decisions|environment|remote-coordination|writing)\.md')
check('live owning retired references', all(not retired_pattern.search((ROOT / n).read_text()) for n in LIVE),
      'No live owning policy or scoped root documentation points at retired paths.')
core_links = re.findall(r'\]\(([^)]+)\)', core)
check('section-only conditional routing', len(core_links) == 6 and all(
      x.startswith('docs/policy/execution.md#') for x in core_links),
      'Six exact event-to-section links; no companion preload or further reading chain.')
check('no negative filename dependencies', not re.search(r'WORKSPACE|README', core),
      'Core neither advertises optional project filenames nor depends on them.')

whitespace = git('diff', '--check', '--', *SCOPED)
check('scoped git diff whitespace', not whitespace, 'git diff --check exits zero without output.')
changes = []
for name in SCOPED:
    old = (BASELINE / name).read_text().splitlines(keepends=True)
    new = (ROOT / name).read_text().splitlines(keepends=True) if (ROOT / name).exists() else []
    delta = list(difflib.unified_diff(old, new, fromfile=f'baseline/{name}', tofile=name))
    check(f'baseline-added whitespace {name}', all(
        not line[1:].rstrip('\n').endswith((' ', '\t'))
        for line in delta if line.startswith('+') and not line.startswith('+++')),
        'No newly introduced trailing whitespace relative to dirty baseline.')
    changes.extend(delta)
(RECORD / 'baseline-to-final.diff').write_text(''.join(changes))
(RECORD / 'scoped-final-git.diff').write_bytes(git('diff', '--', *SCOPED))

final = {name: metrics(ROOT / name) for name in LIVE}
for key, paths in [('core', ['AGENTS.md']), ('package', LIVE[:2])]:
    final[key] = {field: sum(final[name][field] for name in paths)
                  for field in ['bytes', 'characters', 'words', 'lines']}
    final[key]['files'] = len(paths)
check('default core size', final['core']['characters'] < before['core']['characters'],
      f"{before['core']['characters']} -> {final['core']['characters']} characters.")
check('package size and count', final['package']['characters'] < before['package']['characters']
      and final['package']['files'] == 2,
      f"{before['package']['characters']} -> {final['package']['characters']} characters; 6 -> 2 files.")
(RECORD / 'final-metrics.json').write_text(json.dumps(final, indent=2) + '\n')
manifest = {'head': git('rev-parse', 'HEAD').decode().strip(),
            'files': {name: digest(ROOT / name) for name in LIVE + ['.scratch/active-work.md']},
            'retired': RETIRED, 'proof_type': 'documentation self-check, not runtime/independent acceptance'}
(RECORD / 'final-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
(RECORD / 'checks.json').write_text(json.dumps({'revision': manifest, 'checks': checks,
      'links': links}, indent=2) + '\n')
print(json.dumps({'checks_passed': len(checks), 'core': final['core'], 'package': final['package'],
                  'head': manifest['head']}, indent=2))
