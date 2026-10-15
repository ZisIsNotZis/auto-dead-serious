#!/usr/bin/env python3
"""Run the authorized one-at-a-time, non-Help-Agent child status command."""
from __future__ import annotations
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from datetime import datetime, timezone

ROOT = Path('/home/z/vibe')
WORK = ROOT / '.scratch/32-git-hygiene'
MANIFEST = WORK / 'manifest.md'
OUT = WORK / 'status-now'
OUT.mkdir(parents=True, exist_ok=True)
text = MANIFEST.read_text(encoding='utf-8')
block = re.search(r'```json\s*(\[.*?\])\s*```', text, re.S)
if not block:
    raise SystemExit('manifest JSON block not found')
rows = json.loads(block.group(1))
records = []
for row in rows:
    repo = Path(row['path'])
    parts = {part.casefold() for part in repo.parts}
    if 'helpagent' in parts:
        continue
    state = row.get('head_state')
    if state == 'unresolved':
        records.append({'path': str(repo), 'manifest_state': state, 'result': 'unknown: unresolved pointer not queried'})
        continue
    if state not in ('present', 'unborn'):
        records.append({'path': str(repo), 'manifest_state': state, 'result': 'unknown: unrecognized manifest state'})
        continue
    name = repo.relative_to(ROOT).as_posix().replace('/', '__') or 'root'
    prefix = OUT / name
    cmd = ['git', '-C', str(repo), 'status', '--porcelain=v2', '--branch', '--untracked-files=normal', '--ignored=matching', '--ignore-submodules=dirty']
    env = os.environ.copy()
    env['GIT_OPTIONAL_LOCKS'] = '0'
    started = datetime.now(timezone.utc).astimezone().isoformat()
    try:
        result = subprocess.run(cmd, cwd=ROOT, env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30, check=False)
    except subprocess.TimeoutExpired as exc:
        record = {'path': str(repo), 'manifest_state': state, 'manifest_head': row.get('head'), 'command': 'GIT_OPTIONAL_LOCKS=0 ' + ' '.join(cmd), 'started': started, 'result': 'timeout', 'timeout_seconds': 30}
        prefix.with_suffix('.stdout.partial').write_bytes(exc.stdout or b'')
        prefix.with_suffix('.stderr.partial').write_bytes(exc.stderr or b'')
        records.append(record)
        (OUT / 'summary.jsonl').write_text(''.join(json.dumps(x, ensure_ascii=False) + '\n' for x in records), encoding='utf-8')
        sys.stderr.write(json.dumps(record, ensure_ascii=False) + '\n')
        raise SystemExit(124)
    stdout_path = Path(str(prefix) + '.stdout.txt')
    stderr_path = Path(str(prefix) + '.stderr.txt')
    stdout_path.write_text(result.stdout, encoding='utf-8')
    stderr_path.write_text(result.stderr, encoding='utf-8')
    lines = result.stdout.splitlines()
    branch_oid = next((line.split(' ', 2)[2] for line in lines if line.startswith('# branch.oid ')), None)
    branch_head = next((line.split(' ', 2)[2] for line in lines if line.startswith('# branch.head ')), None)
    entries = [line for line in lines if line.startswith(('1 ', '2 ', 'u ', '? '))]
    tracked = [line for line in entries if line.startswith(('1 ', '2 ', 'u '))]
    staged = sum(1 for line in tracked if len(line.split(' ', 2)) > 1 and line.split(' ', 2)[1][0] != '.')
    unstaged = sum(1 for line in tracked if len(line.split(' ', 2)) > 1 and line.split(' ', 2)[1][1] != '.')
    renamed = sum(1 for line in entries if line.startswith('2 '))
    untracked = sum(1 for line in entries if line.startswith('? '))
    ignored = sum(1 for line in lines if line.startswith('! '))
    expected = row.get('head') if state == 'present' else '(initial)'
    match = branch_oid == expected
    clean = result.returncode == 0 and match and not entries
    record = {'path': str(repo), 'manifest_state': state, 'manifest_head': expected, 'branch_oid': branch_oid, 'branch_head': branch_head, 'command': 'GIT_OPTIONAL_LOCKS=0 ' + ' '.join(cmd), 'started': started, 'returncode': result.returncode, 'stdout': stdout_path.relative_to(ROOT).as_posix(), 'stderr': stderr_path.relative_to(ROOT).as_posix(),  'stdout_bytes': len(result.stdout.encode()), 'stderr_bytes': len(result.stderr.encode()), 'status_entries': len(entries), 'staged_entries': staged, 'unstaged_entries': unstaged, 'renamed_entries': renamed, 'untracked_entries': untracked, 'ignored_entries': ignored, 'head_matches_manifest': match, 'result': 'clean' if clean else ('state-drift' if not match else ('command-failed' if result.returncode else 'changes-present'))}
    records.append(record)
    (OUT / 'summary.jsonl').write_text(''.join(json.dumps(x, ensure_ascii=False) + '\n' for x in records), encoding='utf-8')
    print(json.dumps(record, ensure_ascii=False))
    if result.returncode != 0 or not match:
        raise SystemExit(result.returncode or 3)
print(f'completed={sum(1 for r in records if r.get("returncode") == 0)} unresolved={sum(1 for r in records if r.get("result", "").startswith("unknown"))} helpagent_paths_queried=0')
