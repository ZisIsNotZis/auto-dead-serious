#!/usr/bin/env python3
"""Documentation-only checks; no agent/runtime behavior is exercised."""
from pathlib import Path
import difflib
import hashlib
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
TASK = ROOT / '.scratch/22-clean-context-policy'
POLICY = [Path('AGENTS.md'), *sorted(p.relative_to(ROOT) for p in (ROOT / 'docs/policy').glob('*.md'))]


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT, timeout=10).decode()


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


checks = []
head = git('rev-parse', 'HEAD').strip()
assert head == (TASK / 'baseline/head.txt').read_text().strip(), 'HEAD changed'
checks.append('HEAD unchanged; no commit during implementation')
assert not git('diff', '--cached', '--name-only'), 'Unexpected staged changes'
checks.append('Index has no staged changes (starting status also had none)')
starting_paths = {line[3:] for line in (TASK / 'baseline/starting-status.txt').read_text().splitlines()}
assert set(git('diff', '--name-only').splitlines()) <= {str(p) for p in POLICY} | {'.scratch/active-work.md'} | starting_paths, 'New tracked changes outside policy scope'
checks.append('No newly dirty tracked paths outside policy scope')

protected = json.loads((TASK / 'baseline/protected-sha256.json').read_text())
for name, expected in protected.items():
    assert digest(ROOT / name) == expected, f'Protected file changed: {name}'
old_records = {name for name in protected if name.startswith('.scratch/21-autonomous-work-policy/')}
current_records = {str(p.relative_to(ROOT)) for p in (ROOT / '.scratch/21-autonomous-work-policy').rglob('*') if p.is_file()}
assert old_records == current_records, 'Previous work-record file set changed'
checks.append('WORKSPACE.md, README.md, and all previous policy-task records unchanged')
active_before = (TASK / 'baseline/.scratch/active-work.md').read_bytes()
active_after = (ROOT / '.scratch/active-work.md').read_bytes()
assert active_after.startswith(active_before), 'Existing active entries changed'
assert active_after.count(b'[Clean-context agent policy]') == 1
checks.append('Original active-work content preserved; exactly one task entry appended')

start_status = (TASK / 'baseline/starting-status.txt').read_text().splitlines()
end_status = git('status', '--short').splitlines()
allow = {str(p) for p in POLICY} | {'.scratch/active-work.md', '.scratch/22-clean-context-policy/'}
assert [s for s in start_status if s[3:] not in allow] == [s for s in end_status if s[3:] not in allow], 'Unrelated Git status changed'
checks.append('Unrelated Git status identical to baseline (status check, not child-content audit)')

links = []
for path in POLICY:
    text = (ROOT / path).read_text()
    for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', text):
        assert not re.match(r'[a-z]+://', target), 'Unexpected external policy link'
        resolved = ROOT / target  # owning AGENTS.md directory for this package
        assert resolved.is_file(), f'Missing policy reference: {target}'
        links.append({'source': str(path), 'target': target})
assert {link['target'] for link in links} == {str(p) for p in POLICY if str(p).startswith('docs/policy/')}
assert len(links) == 5, 'Companion index links are not unique/complete'
checks.append('Five unique owner-relative companion links exist and cover the package')

scope = [str(p) for p in POLICY] + ['.scratch/active-work.md', '.scratch/22-clean-context-policy']
whitespace = subprocess.run(['git', 'diff', '--check', '--', *scope], cwd=ROOT, capture_output=True, text=True, timeout=10)
assert whitespace.returncode == 0, whitespace.stdout + whitespace.stderr
# Untracked task records need direct checks as well as the scoped Git check.
for path in [ROOT / '.scratch/active-work.md', *(TASK.glob('*.md'))]:
    for number, line in enumerate(path.read_text().splitlines(), 1):
        assert not line.endswith((' ', '\t')), f'Trailing whitespace: {path}:{number}'
checks.append('Scoped git diff --check passed; active/task Markdown has no trailing whitespace')

before = json.loads((TASK / 'baseline/size.json').read_text())
after = {}
hashes = {}
diff = []
for path in POLICY:
    current = (ROOT / path).read_text()
    starting = (TASK / 'baseline' / path).read_text()
    after[str(path)] = {'lines': len(current.splitlines()), 'words': len(current.split()), 'characters': len(current), 'bytes': (ROOT / path).stat().st_size}
    hashes[str(path)] = digest(ROOT / path)
    diff.extend(difflib.unified_diff(starting.splitlines(keepends=True), current.splitlines(keepends=True), fromfile='starting/' + str(path), tofile='current/' + str(path)))
(TASK / 'implementation.diff').write_text(''.join(diff))
(TASK / 'final-policy-sha256.json').write_text(json.dumps(hashes, indent=2) + '\n')
(TASK / 'final-status.txt').write_text('\n'.join(end_status) + '\n')
report = {
    'kind': 'documentation-only structural/preservation checks; not runtime or independent acceptance',
    'head': head,
    'checks': checks,
    'links': links,
    'before': before,
    'after': after,
    'before_totals': {key: sum(size[key] for size in before.values()) for key in ('lines', 'words', 'characters', 'bytes')},
    'after_totals': {key: sum(size[key] for size in after.values()) for key in ('lines', 'words', 'characters', 'bytes')},
    'policy_sha256': hashes,
}
(TASK / 'validation.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
