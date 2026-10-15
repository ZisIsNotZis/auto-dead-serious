#!/usr/bin/env python3
"""Sequential read-only remote-name inventory, separate from blocked repository scans."""
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import urlsplit

ROOT = Path('/home/z/vibe')
WORK = ROOT / '.scratch/32-git-hygiene'
MANIFEST = WORK / 'manifest.md'
OUT = WORK / 'evidence/remote-only.jsonl'
TIMEOUT = 10

def redact_url(value):
    value = value.strip()
    if '://' in value:
        try:
            parts = urlsplit(value)
            host = parts.hostname or ''
            if parts.port:
                host += f':{parts.port}'
            netloc = ('<redacted>@' if parts.username is not None else '') + host
            return f'{parts.scheme}://{netloc}{parts.path}' + ('?<redacted>' if parts.query else '') + ('#<redacted>' if parts.fragment else '')
        except Exception:
            return '<redacted-unparsed-url>'
    match = re.match(r'^([^/@:\s]+)@([^:\s]+):(.*)$', value)
    if match:
        return f'<redacted>@{match.group(2)}:{match.group(3)}'
    return re.sub(r'(?i)(https?://)[^/@\s]+@', r'\1<redacted>@', value)

def manifest_rows():
    text = MANIFEST.read_text(encoding='utf-8')
    match = re.search(r'```json\s*(\[.*?\])\s*```', text, re.S)
    if not match:
        raise RuntimeError('manifest JSON block absent')
    rows = json.loads(match.group(1))
    if len(rows) != 86:
        raise RuntimeError(f'unexpected manifest count {len(rows)}')
    if any(any(p.lower() == 'helpagent' for p in Path(r['path']).parts) for r in rows):
        raise RuntimeError('helpagent path in manifest; stop')
    return rows

def run(repo, args):
    command = ['git', '-C', repo, *args]
    env = os.environ.copy()
    env['GIT_OPTIONAL_LOCKS'] = '0'
    env['GIT_TERMINAL_PROMPT'] = '0'
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                                timeout=TIMEOUT, env=env, check=False)
    except subprocess.TimeoutExpired:
        return {'command': command, 'exit_code': 'timeout'}, b''
    return {'command': command, 'exit_code': result.returncode}, result.stdout

def main():
    start_manifest_hash = hashlib.sha256(MANIFEST.read_bytes()).hexdigest()
    rows = manifest_rows()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    counts = {'resolved_repositories': 0, 'remote_names': 0, 'repositories_with_remotes': 0, 'repositories_without_remotes': 0}
    records = 0
    blocker = None
    with OUT.open('w', encoding='utf-8') as out:
        for row in rows:
            base = {'path': row['path'], 'manifest_head_state': row['head_state'], 'manifest_head': row.get('head'),
                    'queries': [], 'remote_names': [], 'remotes': [], 'complete': False}
            if row['head_state'] == 'unresolved':
                base['state'] = 'unresolved; no Git query attempted'
                base['limitation'] = row.get('head_error')
                out.write(json.dumps(base, ensure_ascii=True, separators=(',', ':')) + '\n')
                records += 1
                continue
            repo = row['path']
            head_result, head_raw = run(repo, ['rev-parse', '--verify', 'HEAD'])
            base['queries'].append(head_result)
            if head_result['exit_code'] == 0:
                current_head = head_raw.decode('ascii', 'replace').strip()
                if row['head_state'] != 'present' or current_head != row.get('head'):
                    base['blocker'] = f'manifest/current HEAD mismatch: observed {current_head}'
                    blocker = base['blocker']
                    out.write(json.dumps(base, ensure_ascii=True, separators=(',', ':')) + '\n')
                    records += 1
                    break
                base['current_head'] = current_head
            elif row['head_state'] == 'unborn':
                sym_result, sym_raw = run(repo, ['symbolic-ref', '--quiet', 'HEAD'])
                base['queries'].append(sym_result)
                sym = sym_raw.decode('utf-8', 'replace').strip() if sym_result['exit_code'] == 0 else None
                if sym != row.get('head_ref'):
                    base['blocker'] = f'manifest/current unborn ref mismatch: observed {sym}'
                    blocker = base['blocker']
                    out.write(json.dumps(base, ensure_ascii=True, separators=(',', ':')) + '\n')
                    records += 1
                    break
                base['current_head'] = f'unborn:{sym}'
            else:
                base['blocker'] = f'HEAD query failed with exit {head_result["exit_code"]}'
                blocker = base['blocker']
                out.write(json.dumps(base, ensure_ascii=True, separators=(',', ':')) + '\n')
                records += 1
                break
            names_result, names_raw = run(repo, ['remote'])
            base['queries'].append(names_result)
            if names_result['exit_code'] != 0:
                base['blocker'] = f'git remote failed with exit {names_result["exit_code"]}'
                blocker = base['blocker']
                out.write(json.dumps(base, ensure_ascii=True, separators=(',', ':')) + '\n')
                records += 1
                break
            names = [line.decode('utf-8', 'surrogateescape') for line in names_raw.splitlines() if line]
            base['remote_names'] = names
            for name in names:
                detail = {'name': name}
                for mode, args in [('fetch', ['remote', 'get-url', '--all', name]),
                                   ('push', ['remote', 'get-url', '--push', '--all', name])]:
                    query, raw = run(repo, args)
                    base['queries'].append(query)
                    detail[mode + '_query_exit'] = query['exit_code']
                    detail[mode + '_urls'] = [redact_url(line.decode('utf-8', 'replace')) for line in raw.splitlines()] if query['exit_code'] == 0 else []
                    if query['exit_code'] == 'timeout':
                        blocker = f'{mode} URL query timeout for {repo}'
                        base['blocker'] = blocker
                        break
                base['remotes'].append(detail)
                if blocker:
                    break
            base['complete'] = not bool(blocker)
            base['state'] = 'configured' if names else 'none configured'
            counts['resolved_repositories'] += 1
            counts['remote_names'] += len(names)
            counts['repositories_with_remotes'] += int(bool(names))
            counts['repositories_without_remotes'] += int(not names)
            out.write(json.dumps(base, ensure_ascii=True, separators=(',', ':')) + '\n')
            records += 1
            if blocker:
                break
    end_manifest_hash = hashlib.sha256(MANIFEST.read_bytes()).hexdigest()
    summary = {'manifest_paths': len(rows), 'records_written': records, 'resolved_repositories_queried': counts['resolved_repositories'],
               'configured_remote_names': counts['remote_names'], 'repositories_with_remotes': counts['repositories_with_remotes'],
               'repositories_without_remotes': counts['repositories_without_remotes'], 'manifest_sha256_start': start_manifest_hash,
               'manifest_sha256_end': end_manifest_hash, 'manifest_unchanged': start_manifest_hash == end_manifest_hash,
               'blocked': blocker, 'command_timeout_seconds': TIMEOUT,
               'query_procedure': 'git rev-parse --verify HEAD; for unborn, git symbolic-ref --quiet HEAD; git remote; for each returned name, git remote get-url --all NAME and git remote get-url --push --all NAME'}
    (WORK / 'evidence/remote-only-summary.json').write_text(json.dumps(summary, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(summary, separators=(',', ':')))
    return 2 if blocker or records != 86 or start_manifest_hash != end_manifest_hash else 0

if __name__ == '__main__':
    sys.exit(main())
