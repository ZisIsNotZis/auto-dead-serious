"""Scoped mechanical evidence and safe policy-check negative controls.

Not semantic acceptance or resource enforcement tests. Fixtures remain in this effort.
"""
from pathlib import Path
import importlib.util
import re
import subprocess
import sys

import jsonschema

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('render_policy', ROOT / 'scripts/render_policy.py')
renderer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(renderer)
source = renderer.read(ROOT / 'AGENTS.yaml')
base = renderer.read(HERE / 'baseline/AGENTS.yaml')
for name in ('AGENTS.schema.yaml', 'AGENTS.docs.schema.yaml'):
    jsonschema.Draft202012Validator.check_schema(renderer.read(ROOT / name))
    print(f'PASS schema definition: {name}')
docs_validator = jsonschema.Draft202012Validator(renderer.read(ROOT / 'AGENTS.docs.schema.yaml'))
docs_validator.validate({'probe': {'_text': 'Measured claim', 'author': 'measurement', 'status': 'current'}})
assert not docs_validator.is_valid({'probe': {'_text': 'Claim', 'author': 'invented'}})
assert not docs_validator.is_valid({'probe': {'_text': 'Claim', 'extra': 'unsupported'}})
print('PASS docs schema positive fixture and invalid-author/unknown-field negative controls')

# Preserve all prior nodes and sibling relative order; source texts may change only at declared homes.
def preservation(before, after, path=''):
    assert set(before) <= set(after), f'removed existing field at {path}'
    assert list(before) == [key for key in after if key in before], f'reordered existing siblings at {path}'
    for key in before:
        if key != '_text':
            preservation(before[key], after[key], f'{path}/{key}')
preservation(base, source)
print('PASS all pre-existing nodes retained and sibling relative order unchanged')
for name in ('AGENTS.schema.yaml', 'AGENTS.docs.schema.yaml'):
    assert (ROOT / name).read_bytes() == (HERE / 'baseline' / name).read_bytes()
assert (ROOT / 'scripts/render_policy.py').read_bytes() == (HERE / 'baseline/render_policy.py').read_bytes()
print('PASS schemas and renderer unchanged from captured dirty baseline')

def at(document, path):
    for key in path.split('.'):
        document = document[key]
    return document
for authority_path in (
    'intent.roles', 'intent.risk', 'precedence',
    'attention.phases._text', 'attention.phases.discussion.wait_for_yes',
    'attention.phases.discussion.interrupt', 'attention.phases.advance',
    'attention.delivery', 'attention.communication.silent_advance',
    'attention.communication.gates_hold',
):
    assert at(base, authority_path) == at(source, authority_path), authority_path
print('PASS existing authority, main-agent delegation, phase entry, silence and user-gate contracts unchanged')
assert '/home/z/.agents' not in (ROOT / 'AGENTS.yaml').read_text()
assert 'SKILL.md' not in (ROOT / 'AGENTS.yaml').read_text()
print('PASS no local skill-path dependency introduced into policy')

rendered = set(renderer.rendered_keys(source))
scenario_refs = set(re.findall(r'@([a-z0-9_]+)', (HERE / 'scenarios.md').read_text()))
assert scenario_refs <= rendered, f'scenario owners missing from rendered policy: {scenario_refs - rendered}'
print(f'PASS all {len(scenario_refs)} distinct scenario/counterexample rule owners resolve in generated view')

fixtures = {
    'valid': ('root:\n  _text: Valid fixture\n', None),
    'duplicate_yaml_key': ('root:\n  _text: First\n  _text: Second\n', 'duplicate key'),
    'duplicate_global_key': ('root:\n  _text: First\n  child:\n    _text: Second\nother:\n  _text: Third\n  child:\n    _text: Fourth\n', 'duplicate key'),
    'missing_text': ('root:\n  child:\n    _text: Child only\n', 'schema:'),
    'dangling_ref': ('root:\n  _text: Fixture @missing\n', 'dangling @ref'),
    'hidden_ref': ('root:\n  _text: Fixture @hidden\n  hidden*:\n    _text: Hidden node\n', 'dangling @ref'),
    'duplicate_text': ('root:\n  _text: Same text\nother:\n  _text: Same text\n', 'two nodes carry the same text'),
    'blank_line': ('root:\n\n  _text: Blank fixture\n', 'blank line'),
    'manual_wrap': ('root:\n  _text: A statement\n    continued manually\n', 'not a single key line'),
    'stale_render': ('root:\n  _text: Current fixture\n', 'out of sync'),
}
for name, (fixture, error) in fixtures.items():
    folder = HERE / 'fixtures' / name
    folder.mkdir(parents=True, exist_ok=True)
    src, out = folder / 'AGENTS.yaml', folder / 'AGENTS.md'
    src.write_text(fixture)
    if name == 'stale_render':
        out.write_text('<!-- generated from AGENTS.yaml - edit that file -->\n```yaml\nroot: Previous fixture\n```\n')
    else:
        out.unlink(missing_ok=True)
    args = [sys.executable, str(ROOT / 'scripts/render_policy.py'), '--source', str(src), '--schema', str(ROOT / 'AGENTS.schema.yaml'), '--out', str(out)]
    if name == 'stale_render':
        args.append('--check')
    result = subprocess.run(args, text=True, capture_output=True)
    (folder / 'result.txt').write_text(f'command: {args!r}\nexit: {result.returncode}\n{result.stdout}{result.stderr}')
    if error is None:
        assert result.returncode == 0, result.stdout + result.stderr
        check = subprocess.run(args + ['--check'], text=True, capture_output=True)
        assert check.returncode == 0, check.stdout + check.stderr
        print('PASS valid fixture render and check')
    else:
        assert result.returncode == 1 and error in result.stdout, (name, result.returncode, result.stdout, result.stderr)
        print(f'PASS safe negative control {name}: rejected with {error!r}')
# --no-index implies a difference exit status; distinguish it from whitespace errors.
diff_evidence = []
for name in ('AGENTS.yaml', 'AGENTS.md'):
    args = ['git', 'diff', '--no-index', '--check', '--', str(HERE / 'baseline' / name), str(ROOT / name)]
    result = subprocess.run(args, text=True, capture_output=True, cwd=ROOT)
    assert result.returncode in (0, 1) and not result.stdout and not result.stderr, (args, result)
    diff_evidence.append(f'command: {args!r}\nexit: {result.returncode}\nstdout: {result.stdout!r}\nstderr: {result.stderr!r}\n')
    print(f'PASS baseline-to-final whitespace check {name}: exit {result.returncode}, no diagnostics (difference exit allowed)')
folder = HERE / 'fixtures' / 'diff-whitespace'
folder.mkdir(parents=True, exist_ok=True)
before, after = folder / 'before.txt', folder / 'after.txt'
before.write_text('plain\n')
after.write_text('plain\ntrailing space \n')
args = ['git', 'diff', '--no-index', '--check', '--', str(before), str(after)]
result = subprocess.run(args, text=True, capture_output=True, cwd=ROOT)
assert result.returncode not in (0, 1) and 'trailing whitespace' in result.stdout, result
negative_evidence = f'command: {args!r}\nexit: {result.returncode}\n{result.stdout}{result.stderr}'
(folder / 'result.txt').write_text(negative_evidence)
(HERE / 'diff-checks.txt').write_text(''.join(diff_evidence) + negative_evidence)
print(f'PASS whitespace negative control: rejected with exit {result.returncode} and trailing-whitespace diagnostic')
print('PASS mechanical evidence complete; semantic independent review and runtime enforcement remain unexercised')
