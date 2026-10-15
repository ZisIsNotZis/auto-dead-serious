#!/usr/bin/env python3
"""Bounded, read-only Git hygiene audit for the manifest child repositories."""
from __future__ import annotations

import gzip
import hashlib
import heapq
import json
import os
from pathlib import Path
import re
import shlex
import shutil
import stat
import subprocess
import sys
import tempfile
import threading
import time
from urllib.parse import urlsplit

ROOT = Path('/home/z/vibe')
WORK = ROOT / '.scratch/32-git-hygiene'
EVIDENCE = WORK / 'evidence'
REPO_EVIDENCE = EVIDENCE / 'repos'
MANIFEST = WORK / 'manifest.md'
MAX_COMMAND_SECONDS = 300
MAX_FILE_BYTES = 10 * 1024 * 1024
TOP_BLOBS = 50
THRESHOLD = 100 * 1024 * 1024

def decode(value: bytes) -> str:
    return value.decode('utf-8', 'surrogateescape')

def safe_text(value: str) -> str:
    # Redact URL credentials and query/fragment material before evidence persistence.
    value = re.sub(r'(?i)(https?://)[^/@\s]+@', r'\1<redacted>@', value)
    value = re.sub(r'(?i)(https?://[^\s?#]+)[?#][^\s]*', r'\1?<redacted>', value)
    value = re.sub(r'(?<![\w/])[^/@:\s]+@([^/:\s]+):', r'<redacted>@\1:', value)
    return value

def sanitize_url(value: str) -> str:
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
    return safe_text(value)

class AuditError(RuntimeError):
    pass

class Repo:
    def __init__(self, spec: dict, index: int):
        self.spec = spec
        self.path = Path(spec['path'])
        self.rel = str(self.path.relative_to(ROOT))
        self.index = index
        self.commands: list[dict] = []
        self.env = os.environ.copy()
        self.env['GIT_OPTIONAL_LOCKS'] = '0'
        self.env['GIT_TERMINAL_PROMPT'] = '0'
        self.env['GIT_CONFIG_NOSYSTEM'] = self.env.get('GIT_CONFIG_NOSYSTEM', '0')

    def git_args(self, args: list[str]) -> list[str]:
        return ['git', '-C', str(self.path), *args]

    def run(self, args: list[str], *, timeout: int = MAX_COMMAND_SECONDS, check: bool = True) -> bytes:
        command = self.git_args(args)
        try:
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                    timeout=timeout, env=self.env, check=False)
        except subprocess.TimeoutExpired:
            self.commands.append({'command': shlex.join(command), 'result': 'timeout', 'timeout_seconds': timeout})
            raise AuditError(f'command timeout: {shlex.join(command)}')
        self.commands.append({'command': shlex.join(command), 'exit_code': result.returncode})
        if check and result.returncode != 0:
            raise AuditError(f'command failed with exit {result.returncode}: {shlex.join(command)}')
        return result.stdout

    def run_spooled(self, args: list[str], output_path: Path, *, timeout: int = MAX_COMMAND_SECONDS,
                    stdin_path: Path | None = None, check: bool = True) -> int:
        command = self.git_args(args)
        with output_path.open('wb') as out:
            with (stdin_path.open('rb') if stdin_path else open(os.devnull, 'rb')) as inp:
                try:
                    result = subprocess.run(command, stdin=inp, stdout=out, stderr=subprocess.DEVNULL,
                                            timeout=timeout, env=self.env, check=False)
                except subprocess.TimeoutExpired:
                    self.commands.append({'command': shlex.join(command), 'result': 'timeout', 'timeout_seconds': timeout})
                    raise AuditError(f'command timeout: {shlex.join(command)}')
        self.commands.append({'command': shlex.join(command), 'exit_code': result.returncode,
                              'stdout_bytes': output_path.stat().st_size, 'stdout_spooled_then_processed': True})
        if check and result.returncode != 0:
            raise AuditError(f'command failed with exit {result.returncode}: {shlex.join(command)}')
        return result.returncode

    def refs_snapshot(self) -> bytes:
        return self.run(['for-each-ref', '--format=%(refname)%09%(objectname)%09%(upstream)', 'refs/heads', 'refs/remotes', 'refs/tags'])

    def state_snapshot(self) -> tuple[str, bytes]:
        rev = self.run(['rev-parse', '--verify', 'HEAD'], check=False).strip()
        if rev:
            return decode(rev), self.run(['status', '--porcelain=v2', '--branch', '--untracked-files=normal', '--ignored=matching', '-z'])
        symbolic = self.run(['symbolic-ref', '--quiet', 'HEAD'], check=False).strip()
        if not symbolic:
            raise AuditError('HEAD cannot be resolved as a commit or unborn symbolic ref')
        return f'unborn:{decode(symbolic)}', self.run(['status', '--porcelain=v2', '--branch', '--untracked-files=normal', '--ignored=matching', '-z'])

# Pattern values never leave memory. Findings contain only category and location metadata.
PATTERNS = [
    ('private-key-header', re.compile(rb'-----BEGIN (?:RSA |EC |OPENSSH |DSA |PGP )?PRIVATE KEY-----')),
    ('aws-access-key-id', re.compile(rb'\b(?:AKIA|ASIA)[A-Z0-9]{16}\b')),
    ('github-token', re.compile(rb'\b(?:gh[pousr]_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{20,})\b')),
    ('google-api-key', re.compile(rb'\bAIza[0-9A-Za-z_-]{35}\b')),
    ('slack-token', re.compile(rb'\bxox[baprs]-[A-Za-z0-9-]{10,}\b')),
    ('generic-credential-assignment', re.compile(rb'(?i)\b(?:api[_-]?key|access[_-]?token|auth[_-]?token|client[_-]?secret|password|passwd|secret|token)\s*[:=]\s*[\"\']?[^\s\"\'`,;<>]{8,}')),
]

DEP_COMPONENTS = {'node_modules', '.venv', 'venv', 'site-packages', 'dist-packages', '__pycache__', 'bower_components'}
BUILD_COMPONENTS = {'.cache', 'cache', 'build', 'dist', 'target', 'coverage', '.next', '.turbo', 'out'}
BACKUP_COMPONENTS = {'backup', 'backups', 'old', 'archive-backup'}
MODEL_WORDS = {'model', 'models', 'checkpoint', 'checkpoints', 'weights', 'weight', 'ckpt'}
ARCHIVE_SUFFIXES = {'.zip', '.tar', '.gz', '.tgz', '.bz2', '.xz', '.7z', '.rar', '.zst'}
MODEL_SUFFIXES = {'.pt', '.pth', '.ckpt', '.safetensors', '.gguf', '.onnx', '.h5', '.model', '.bin'}
SOURCE_SUFFIXES = {'.py', '.pyi', '.js', '.jsx', '.ts', '.tsx', '.mjs', '.cjs', '.go', '.rs', '.c', '.h', '.cc', '.cpp', '.hpp', '.java', '.kt', '.swift', '.rb', '.php', '.sh', '.bash', '.ps1', '.sql', '.html', '.css', '.scss', '.md', '.rst', '.txt', '.json', '.jsonl', '.yaml', '.yml', '.toml', '.ini', '.cfg', '.xml', '.proto', '.lock', '.gitignore', '.dockerfile'}

def classify(path: str, mode: str = '') -> tuple[str, str]:
    normalized = path.replace('\\', '/').lower()
    parts = [part for part in normalized.split('/') if part]
    name = parts[-1] if parts else normalized
    suffix = Path(name).suffix.lower()
    if any(part in DEP_COMPONENTS for part in parts):
        return 'dependency', suffix or '<extensionless>'
    if any(part in BACKUP_COMPONENTS for part in parts) or name.endswith(('~', '.bak', '.old', '.orig', '.swp')):
        return 'backup', suffix or '<extensionless>'
    if any(word in parts or word in name for word in MODEL_WORDS) or suffix in MODEL_SUFFIXES:
        return 'model', suffix or '<extensionless>'
    if suffix in ARCHIVE_SUFFIXES:
        return 'archive', suffix
    if any(part in BUILD_COMPONENTS for part in parts) or suffix in {'.pyc', '.pyo', '.o', '.obj', '.class', '.so', '.dll', '.dylib'}:
        return 'build', suffix or '<extensionless>'
    if any(part in {'test', 'tests', 'fixture', 'fixtures', 'verification', 'golden'} for part in parts):
        return 'verification', suffix or '<extensionless>'
    if suffix in SOURCE_SUFFIXES or name in {'makefile', 'dockerfile', 'license', 'readme', 'copying'}:
        return 'source', suffix or '<extensionless>'
    if mode == '120000':
        return 'source', '<symlink>'
    if mode == '160000':
        return 'source', '<gitlink>'
    return 'unresolved', suffix or '<extensionless>'

def is_dependency_path(path: str) -> bool:
    return any(part.lower() in DEP_COMPONENTS for part in path.replace('\\', '/').split('/'))

def patterns_for(data: bytes, repo_rel: str, path: str, *, source: str, oid: str | None = None,
                  line_base: int = 1) -> list[dict]:
    found = []
    for line_no, line in enumerate(data.splitlines(), line_base):
        for category, regex in PATTERNS:
            if regex.search(line):
                found.append({'repository': repo_rel, 'path': path, 'source': source,
                              'line': line_no, 'pattern_category': category,
                              'blob_id': oid, 'false_positive_note': 'generic assignment patterns have a higher false-positive rate' if category == 'generic-credential-assignment' else 'pattern match requires human validation; value and line content withheld'})
    return found

def read_manifest() -> list[dict]:
    text = MANIFEST.read_text(encoding='utf-8')
    match = re.search(r'```json\s*(\[.*?\])\s*```', text, re.S)
    if not match:
        raise AuditError('manifest JSON block not found')
    rows = json.loads(match.group(1))
    if len(rows) != 86:
        raise AuditError(f'manifest child count unexpected: {len(rows)}')
    if any(any(part.lower() == 'helpagent' for part in Path(row['path']).parts) for row in rows):
        raise AuditError('manifest unexpectedly contains helpagent; refuse to inspect')
    if any(row['path'] == str(ROOT) for row in rows):
        raise AuditError('manifest unexpectedly contains root repository')
    return rows

def parse_status(raw: bytes) -> tuple[dict, dict]:
    buckets = {'tracked_unstaged': [], 'staged': [], 'untracked_nonignored': [], 'ignored': [], 'tracked_but_ignored': [], 'unmerged': []}
    headers = []
    tokens = raw.split(b'\0')
    i = 0
    while i < len(tokens):
        token = tokens[i]
        i += 1
        if not token:
            continue
        if token.startswith(b'# '):
            headers.append(decode(token))
            continue
        kind = token[:1]
        if kind == b'1':
            fields = token.split(b' ', 8)
            xy, path = decode(fields[1]), decode(fields[8])
            if xy[0] != '.': buckets['staged'].append(path)
            if xy[1] != '.': buckets['tracked_unstaged'].append(path)
            if 'U' in xy: buckets['unmerged'].append(path)
        elif kind == b'2':
            fields = token.split(b' ', 9)
            xy, path = decode(fields[1]), decode(fields[9])
            old = decode(tokens[i]) if i < len(tokens) else None
            if i < len(tokens): i += 1
            if xy[0] != '.': buckets['staged'].append({'path': path, 'renamed_from': old})
            if xy[1] != '.': buckets['tracked_unstaged'].append({'path': path, 'renamed_from': old})
            if 'U' in xy: buckets['unmerged'].append(path)
        elif kind == b'u':
            fields = token.split(b' ', 10)
            path = decode(fields[10])
            buckets['staged'].append(path)
            buckets['tracked_unstaged'].append(path)
            buckets['unmerged'].append(path)
        elif token.startswith(b'? '):
            buckets['untracked_nonignored'].append(decode(token[2:]))
        elif token.startswith(b'! '):
            buckets['ignored'].append(decode(token[2:]))
    counts = {key: len(value) for key, value in buckets.items()}
    return {'headers': headers, 'counts': counts, 'paths': buckets}, buckets

def parse_index(raw: bytes) -> list[dict]:
    entries = []
    for record in raw.split(b'\0'):
        if not record:
            continue
        meta, sep, path = record.partition(b'\t')
        if not sep:
            raise AuditError('unparseable git ls-files --stage record')
        parts = meta.split()
        if len(parts) != 3:
            raise AuditError('unparseable git ls-files stage metadata')
        entries.append({'mode': decode(parts[0]), 'oid': decode(parts[1]), 'stage': decode(parts[2]), 'path': decode(path)})
    return entries

def parse_remote_lines(raw: bytes) -> list[str]:
    return [decode(line) for line in raw.splitlines() if line]

def command_string(repo: Repo, args: list[str]) -> str:
    return shlex.join(repo.git_args(args))

def current_scan(repo: Repo, index_entries: list[dict]) -> dict:
    results = []
    skipped = {'dependency': 0, 'symlink': 0, 'nonregular': 0, 'missing': 0, 'oversize': 0, 'binary': 0, 'read_error': 0}
    scanned = 0
    oid_by_path = {item['path']: item['oid'] for item in index_entries if item['stage'] == '0'}
    for path in oid_by_path:
        if is_dependency_path(path):
            skipped['dependency'] += 1
            continue
        full = repo.path / path
        try:
            st = full.lstat()
        except FileNotFoundError:
            skipped['missing'] += 1
            continue
        except OSError:
            skipped['read_error'] += 1
            continue
        if stat.S_ISLNK(st.st_mode):
            skipped['symlink'] += 1
            continue
        if not stat.S_ISREG(st.st_mode):
            skipped['nonregular'] += 1
            continue
        if st.st_size > MAX_FILE_BYTES:
            skipped['oversize'] += 1
            continue
        try:
            data = full.read_bytes()
        except OSError:
            skipped['read_error'] += 1
            continue
        if b'\0' in data:
            skipped['binary'] += 1
            continue
        scanned += 1
        hits = patterns_for(data, repo.rel, path, source='tracked_worktree', oid='index:' + oid_by_path[path])
        digest = hashlib.sha256(data).hexdigest()
        for hit in hits:
            hit['worktree_content_sha256'] = digest
        results.extend(hits)
    return {'files_scanned': scanned, 'skipped': skipped, 'observations': results,
            'limit_bytes_per_file': MAX_FILE_BYTES}

def do_history(repo: Repo, tempdir: Path) -> dict:
    rev_path = tempdir / 'reachable-objects.txt'
    oid_path = tempdir / 'object-ids.txt'
    meta_path = tempdir / 'object-metadata.txt'
    eligible_path = tempdir / 'eligible-history.jsonl'
    scan_ids_path = tempdir / 'history-scan-ids.txt'
    catout = tempdir / 'history-batch.raw'
    repo.run_spooled(['rev-list', '--objects', '--all', '--reflog'], rev_path)
    with rev_path.open('rb') as rev, oid_path.open('wb') as oidout:
        for line in rev:
            oid = line.rstrip(b'\n').split(b' ', 1)[0]
            if oid:
                oidout.write(oid + b'\n')
    repo.run_spooled(['cat-file', '--batch-check=%(objectname) %(objecttype) %(objectsize)'], meta_path, stdin_path=oid_path)
    heap = []
    threshold_rows = []
    history_candidates = []
    blob_count = 0
    object_count = 0
    eligible_count = 0
    skipped = {'dependency': 0, 'oversize': 0, 'missing_path': 0, 'nonblob': 0}
    with rev_path.open('rb') as rev, meta_path.open('rb') as meta, eligible_path.open('w', encoding='utf-8') as elig, scan_ids_path.open('wb') as scanids:
        for line in rev:
            parsed = line.rstrip(b'\n').split(b' ', 1)
            oid = decode(parsed[0])
            path = decode(parsed[1]) if len(parsed) > 1 else '<no-path-known>'
            md = meta.readline().split()
            object_count += 1
            if len(md) < 3 or md[1] == b'missing':
                raise AuditError(f'missing or malformed reachable object metadata for {oid}')
            objtype, size = decode(md[1]), int(md[2])
            if objtype != 'blob':
                skipped['nonblob'] += 1
                continue
            blob_count += 1
            row = {'object_id': oid, 'path': path, 'size_bytes': size}
            item = (size, object_count, oid, path)
            if len(heap) < TOP_BLOBS:
                heapq.heappush(heap, item)
            elif size > heap[0][0]:
                heapq.heapreplace(heap, item)
            if size > THRESHOLD:
                threshold_rows.append(row)
            category, suffix = classify(path)
            if category != 'source':
                history_candidates.append({'path': path, 'object_id': oid, 'size_bytes': size,
                                           'classification': category, 'file_type': suffix,
                                           'proposed_action': ('review file-specific retention and whether regeneration is documented; do not delete' if category in {'dependency', 'build', 'backup', 'model', 'archive'} else 'manually classify before any later cleanup; do not delete')})
            if path == '<no-path-known>':
                skipped['missing_path'] += 1
                continue
            if is_dependency_path(path):
                skipped['dependency'] += 1
                continue
            if size > MAX_FILE_BYTES:
                skipped['oversize'] += 1
                continue
            elig.write(json.dumps({'object_id': oid, 'path': path, 'size_bytes': size}, ensure_ascii=True) + '\n')
            scanids.write(oid.encode('ascii') + b'\n')
            eligible_count += 1
    if object_count != sum(1 for _ in open(oid_path, 'rb')):
        raise AuditError('rev-list/object metadata count mismatch')
    # Stream eligible blobs from cat-file; raw bytes exist only in process memory.
    observations = []
    binary_count = 0
    scanned_count = 0
    proc = subprocess.Popen(repo.git_args(['cat-file', '--batch']), stdin=scan_ids_path.open('rb'),
                            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, env=repo.env)
    repo.commands.append({'command': command_string(repo, ['cat-file', '--batch']), 'streamed_input_file': str(scan_ids_path.relative_to(WORK)), 'exit_code': 'pending'})
    command_record = repo.commands[-1]
    timed_out = {'value': False}
    def kill_late() -> None:
        timed_out['value'] = True
        try: proc.kill()
        except OSError: pass
    timer = threading.Timer(MAX_COMMAND_SECONDS, kill_late)
    timer.daemon = True
    timer.start()
    try:
        with eligible_path.open('r', encoding='utf-8') as elig:
            for row_text in elig:
                row = json.loads(row_text)
                header = proc.stdout.readline()
                fields = header.rstrip(b'\n').split()
                if len(fields) != 3 or fields[1] != b'blob' or int(fields[2]) != row['size_bytes'] or decode(fields[0]) != row['object_id']:
                    raise AuditError('cat-file batch stream disagrees with object metadata')
                remaining = row['size_bytes']
                chunks = []
                while remaining:
                    chunk = proc.stdout.read(min(1024 * 1024, remaining))
                    if not chunk:
                        raise AuditError('cat-file batch stream ended inside a blob')
                    chunks.append(chunk)
                    remaining -= len(chunk)
                if proc.stdout.read(1) != b'\n':
                    raise AuditError('cat-file batch stream lacks record delimiter')
                data = b''.join(chunks)
                if b'\0' in data:
                    binary_count += 1
                    continue
                scanned_count += 1
                observations.extend(patterns_for(data, repo.rel, row['path'], source='historical_blob', oid=row['object_id']))
        code = proc.wait(timeout=MAX_COMMAND_SECONDS)
    except (subprocess.TimeoutExpired, BrokenPipeError) as ex:
        proc.kill()
        proc.wait()
        raise AuditError('historical cat-file scan timed out or pipe failed') from ex
    finally:
        timer.cancel()
    command_record['exit_code'] = code
    if timed_out['value']:
        command_record['exit_code'] = 'timeout'
        raise AuditError('historical cat-file scan timed out')
    if code != 0:
        raise AuditError(f'historical cat-file scan failed with exit {code}')
    with meta_path.open('rb') as meta:
        metadata_rows = sum(1 for _ in meta)
    if metadata_rows != object_count:
        raise AuditError('cat-file metadata output was truncated')
    return {'object_scope': 'all local refs and reflogs; excludes remote/unfetched refs',
            'object_count_all_types': object_count, 'blob_count': blob_count,
            'top_blobs': [{'object_id': oid, 'path': path, 'size_bytes': size} for size, _, oid, path in sorted(heap, reverse=True)],
            'over_100_mib': sorted(threshold_rows, key=lambda x: (-x['size_bytes'], x['path'], x['object_id'])),
            'over_100_mib_threshold_bytes': THRESHOLD,
            'history_candidates': history_candidates,
            'credential_scan': {'blobs_scanned': scanned_count, 'skipped_binary_blobs': binary_count,
                                'skipped': skipped, 'observations': observations,
                                'limit_bytes_per_blob': MAX_FILE_BYTES},
            'shallow_repository': decode(repo.run(['rev-parse', '--is-shallow-repository']).strip()) == 'true'}

def tracking_info(repo: Repo, branch_raw: bytes) -> list[dict]:
    result = []
    for line in branch_raw.splitlines():
        fields = line.split(b'\t')
        if len(fields) < 3:
            continue
        branch, oid, upstream = map(decode, fields[:3])
        item = {'branch': branch, 'head': oid, 'upstream': upstream or None, 'ahead': None, 'behind': None, 'state': 'no-upstream'}
        if upstream:
            check = repo.run(['rev-parse', '--verify', upstream + '^{commit}'], check=False).strip()
            if check:
                counts = repo.run(['rev-list', '--left-right', '--count', branch + '...' + upstream]).split()
                if len(counts) == 2:
                    item.update({'ahead': int(counts[0]), 'behind': int(counts[1]), 'state': 'known-local-tracking'})
            else:
                item['state'] = 'upstream-not-fetched-or-unresolvable'
        result.append(item)
    return result

def audit_one(spec: dict, index: int) -> dict:
    base = {'manifest_path': spec['path'], 'index': index, 'manifest_head_state': spec['head_state'],
            'manifest_head': spec.get('head'), 'commands': [], 'complete': False}
    if spec['head_state'] == 'unresolved':
        base.update({'state': 'unresolved', 'limitation': 'manifest records an unresolvable .git pointer; no Git command or repair attempted',
                     'manifest_error': spec.get('head_error')})
        return base
    repo = Repo(spec, index)
    base['repository'] = repo.rel
    try:
        head_before, status_before = repo.state_snapshot()
        if spec['head_state'] == 'present':
            expected = spec.get('head')
            if head_before != expected:
                raise AuditError(f'manifest HEAD mismatch: expected {expected}, observed {head_before}')
        else:
            expected_ref = spec.get('head_ref')
            if not head_before.startswith('unborn:') or (expected_ref and head_before.removeprefix('unborn:') != expected_ref):
                raise AuditError(f'manifest unborn ref mismatch: expected {expected_ref}, observed {head_before}')
        base['head_before'] = head_before
        status, _ = parse_status(status_before)
        base['status'] = status
        status_hash = hashlib.sha256(status_before).hexdigest()
        with tempfile.TemporaryDirectory(prefix=f'audit-{index:03d}-', dir=EVIDENCE) as td:
            tempdir = Path(td)
            index_entries = parse_index(repo.run(['ls-files', '--stage', '-z']))
            tracked_ignored_raw = repo.run(['ls-files', '-ci', '--exclude-standard', '-z'])
            tracked_ignored = [decode(p) for p in tracked_ignored_raw.split(b'\0') if p]
            status['paths']['tracked_but_ignored'] = tracked_ignored
            status['counts']['tracked_but_ignored'] = len(tracked_ignored)
            base['tracked_index_count'] = len(index_entries)
            base['index_entries'] = index_entries
            # Candidate files are classified from tracked names, index modes and object IDs only.
            candidates = []
            for ent in index_entries:
                category, file_type = classify(ent['path'], ent['mode'])
                if category != 'source':
                    candidates.append({'path': ent['path'], 'object_id': ent['oid'], 'mode': ent['mode'],
                                       'classification': category, 'file_type': file_type,
                                       'proposed_action': ('review file-specific retention and whether regeneration is documented; do not delete' if category in {'dependency', 'build', 'backup', 'model', 'archive'} else 'manually classify before any later cleanup; do not delete')})
            base['current_candidates'] = candidates
            base['candidate_counts'] = {key: sum(1 for c in candidates if c['classification'] == key) for key in ['dependency','build','backup','model','archive','verification','unresolved']}
            base['current_credential_scan'] = current_scan(repo, index_entries)
            remote_raw = repo.run(['remote'])
            remote_names = parse_remote_lines(remote_raw)
            remote_details = []
            for name in remote_names:
                fetch_raw = repo.run(['remote', 'get-url', '--all', name], check=False)
                fetch_record = repo.commands[-1]
                push_raw = repo.run(['remote', 'get-url', '--push', '--all', name], check=False)
                push_record = repo.commands[-1]
                remote_details.append({'name': name,
                    'fetch_urls': [sanitize_url(decode(x)) for x in fetch_raw.splitlines() if x] if fetch_record['exit_code'] == 0 else [],
                    'fetch_query_exit': fetch_record['exit_code'],
                    'push_urls': [sanitize_url(decode(x)) for x in push_raw.splitlines() if x] if push_record['exit_code'] == 0 else [],
                    'push_query_exit': push_record['exit_code']})
            base['remotes'] = {'names': remote_names, 'count': len(remote_names), 'details': remote_details,
                               'state': 'configured' if remote_names else 'none configured'}
            branch_raw = repo.run(['for-each-ref', '--format=%(refname)%09%(objectname)%09%(upstream)', 'refs/heads'])
            base['local_tracking'] = tracking_info(repo, branch_raw)
            base['refs_before'] = decode(repo.refs_snapshot())
            base['worktrees'] = decode(repo.run(['worktree', 'list', '--porcelain']))
            gm = repo.run(['ls-files', '--error-unmatch', '--', '.gitmodules'], check=False)
            if repo.commands[-1]['exit_code'] == 0:
                base['submodules'] = decode(repo.run(['submodule', 'status']))
            else:
                base['submodules'] = {'state': 'no tracked .gitmodules'}
            if spec['head_state'] == 'present':
                base['history'] = do_history(repo, tempdir)
            else:
                base['history'] = {'state': 'skipped: repository has unborn HEAD', 'credential_scan': {'state': 'skipped: no commit history'}}
            head_after, status_after = repo.state_snapshot()
            refs_after = decode(repo.refs_snapshot())
            remotes_after = parse_remote_lines(repo.run(['remote']))
            remote_details_after = []
            for name in remotes_after:
                fetch_after = repo.run(['remote', 'get-url', '--all', name], check=False)
                fetch_code = repo.commands[-1]['exit_code']
                push_after = repo.run(['remote', 'get-url', '--push', '--all', name], check=False)
                push_code = repo.commands[-1]['exit_code']
                remote_details_after.append({'name': name,
                    'fetch_urls': [sanitize_url(decode(x)) for x in fetch_after.splitlines() if x] if fetch_code == 0 else [],
                    'fetch_query_exit': fetch_code,
                    'push_urls': [sanitize_url(decode(x)) for x in push_after.splitlines() if x] if push_code == 0 else [],
                    'push_query_exit': push_code})
            worktrees_after = decode(repo.run(['worktree', 'list', '--porcelain']))
            if repo.commands[-1]['exit_code'] != 0:
                raise AuditError('worktree state query failed')
            if '.gitmodules' in [e['path'] for e in index_entries if e['stage'] == '0']:
                submodules_after = decode(repo.run(['submodule', 'status']))
            else:
                submodules_after = {'state': 'no tracked .gitmodules'}
            if head_after != head_before:
                raise AuditError(f'HEAD changed during audit: before {head_before}, after {head_after}')
            if hashlib.sha256(status_after).hexdigest() != status_hash:
                raise AuditError('worktree/index status changed during audit; stop for mutation/active-job conflict')
            if refs_after != base['refs_before']:
                raise AuditError('local refs changed during audit; stop for mutation/active-job conflict')
            if remotes_after != remote_names or remote_details_after != remote_details:
                raise AuditError('remote configuration changed during audit; stop for mutation/active-job conflict')
            if worktrees_after != base['worktrees'] or submodules_after != base['submodules']:
                raise AuditError('submodule/worktree state changed during audit; stop for mutation/active-job conflict')
            base['head_after'] = head_after
            base['status_stable'] = True
            base['refs_stable'] = True
            base['complete'] = True
    except AuditError as ex:
        base['blocker'] = str(ex)
        base['complete'] = False
    except Exception as ex:
        base['blocker'] = f'unexpected {type(ex).__name__}; details withheld'
        base['complete'] = False
    base['commands'] = repo.commands
    return base

def write_json_gz(path: Path, value: dict) -> None:
    with path.open('wb') as raw:
        with gzip.GzipFile(fileobj=raw, mode='wb', mtime=0) as out:
            out.write((json.dumps(value, ensure_ascii=True, separators=(',', ':')) + '\n').encode('utf-8'))

def size_text(size: int) -> str:
    return f'{size / (1024 * 1024):.1f} MiB'

def symlink_coverage() -> dict:
    """Check visible symlink targets for repo markers without following helpagent or nested links."""
    result = {'command': "find -P /home/z/vibe -type d -iname helpagent -prune -o -type d -name .git -prune -o -type l -print0",
              'link_count': 0, 'links': [], 'directory_targets_examined': 0, 'markers': [], 'nested_symlinks': [], 'target_searches': [], 'limitations': [],
              'complete': True, 'target_search_limit': 100}
    find_out = EVIDENCE / 'symlink-links.tmp'
    try:
        with find_out.open('wb') as out:
            run = subprocess.run(['find', '-P', str(ROOT), '-type', 'd', '-iname', 'helpagent', '-prune', '-o',
                                  '-type', 'd', '-name', '.git', '-prune', '-o', '-type', 'l', '-print0'],
                                 stdout=out, stderr=subprocess.DEVNULL, timeout=120, check=False)
        if run.returncode != 0:
            result['complete'] = False
            result['limitations'].append({'reason': f'find exited {run.returncode}; symlink inventory incomplete'})
            return result
        links = [Path(decode(p)) for p in find_out.read_bytes().split(bytes([0])) if p]
    except subprocess.TimeoutExpired:
        result['complete'] = False
        result['limitations'].append({'reason': 'symlink inventory find timed out; coverage incomplete'})
        return result
    finally:
        try: find_out.unlink()
        except FileNotFoundError: pass
    targets: dict[str, list[str]] = {}
    for link in links:
        try:
            literal = os.readlink(link)
        except OSError:
            literal = '<readlink-failed>'
        raw_target = Path(literal) if os.path.isabs(literal) else link.parent / literal
        lexical = Path(os.path.abspath(os.path.normpath(str(raw_target))))
        linkrow = {'link': str(link), 'literal_target': literal, 'lexical_target': str(lexical), 'target_kind': 'unknown'}
        result['links'].append(linkrow)
        if any(part.lower() == 'helpagent' for part in lexical.parts):
            linkrow['target_kind'] = 'excluded-helpagent'
            linkrow['target_inspected'] = False
            continue
        cursor = Path(lexical.anchor)
        components = lexical.parts[1:] if lexical.is_absolute() else lexical.parts
        safe = True
        for pos, part in enumerate(components):
            cursor = cursor / part
            try:
                mode = os.lstat(cursor).st_mode
            except FileNotFoundError:
                linkrow['target_kind'] = 'dangling'
                safe = False
                break
            except OSError:
                linkrow['target_kind'] = 'unreadable'
                safe = False
                break
            if stat.S_ISLNK(mode):
                linkrow['target_kind'] = 'symlink-chain-not-followed'
                safe = False
                break
            if pos < len(components) - 1 and not stat.S_ISDIR(mode):
                linkrow['target_kind'] = 'not-a-directory'
                safe = False
                break
            if pos == len(components) - 1:
                if stat.S_ISDIR(mode):
                    linkrow['target_kind'] = 'directory'
                else:
                    linkrow['target_kind'] = 'not-a-directory'
                    safe = False
        if safe and linkrow['target_kind'] == 'directory':
            targets.setdefault(str(lexical), []).append(str(link))
        elif linkrow['target_kind'] in {'symlink-chain-not-followed', 'unreadable'}:
            result['complete'] = False
            result['limitations'].append({'link': str(link), 'reason': f'target {linkrow["target_kind"]}; not dereferenced to avoid an indirect path into helpagent'})
    result['link_count'] = len(result['links'])
    unique_targets = list(targets.items())
    if len(unique_targets) > result['target_search_limit']:
        result['complete'] = False
        for target, associated in unique_targets[result['target_search_limit']:]:
            result['limitations'].append({'link': associated[0], 'reason': 'unique directory target beyond bounded search limit; not searched'})
        unique_targets = unique_targets[:result['target_search_limit']]
    for target, associated in unique_targets:
        command = ['find', '-P', target, '-type', 'd', '-iname', 'helpagent', '-prune', '-o',
                   '(', '-type', 'd', '-name', '.git', '-print0', '-prune', ')', '-o',
                   '(', '-type', 'f', '-name', '.git', '-print0', ')', '-o',
                   '(', '-type', 'l', '-print0', ')']
        outpath = EVIDENCE / f'symlink-target-{result["directory_targets_examined"]:03d}.tmp'
        try:
            with outpath.open('wb') as out:
                run = subprocess.run(command, stdout=out, stderr=subprocess.DEVNULL, timeout=120, check=False)
            target_markers = []
            target_links = []
            if run.returncode != 0:
                result['complete'] = False
                result['limitations'].append({'link': associated[0], 'reason': f'directory marker search exited {run.returncode}'})
            else:
                for entry in (decode(p) for p in outpath.read_bytes().split(bytes([0])) if p):
                    if Path(entry).name == '.git':
                        target_markers.append(entry)
                    else:
                        try: literal_nested = os.readlink(entry)
                        except OSError: literal_nested = '<readlink-failed>'
                        target_links.append({'link': entry, 'literal_target': literal_nested})
            result['markers'].extend(target_markers)
            result['nested_symlinks'].extend(target_links)
            result['target_searches'].append({'target': target, 'links': associated, 'command': shlex.join(command),
                                              'exit_code': run.returncode, 'markers': target_markers,
                                              'nested_symlink_count': len(target_links)})
            if target_links:
                result['complete'] = False
                result['limitations'].append({'link': associated[0], 'reason': f'{len(target_links)} nested symlink(s) found in target tree and not followed; repository markers behind those links remain unknown'})
            result['directory_targets_examined'] += 1
        except subprocess.TimeoutExpired:
            result['complete'] = False
            result['limitations'].append({'link': associated[0], 'reason': 'directory marker search timed out; target coverage incomplete'})
        finally:
            try: outpath.unlink()
            except FileNotFoundError: pass
    result['markers'] = sorted(set(result['markers']))
    return result

def make_report(results: list[dict], manifest_rows: list[dict], symlink: dict | None = None,
                manifest_integrity: tuple[str, bool] | None = None) -> str:
    lines = ['# Git hygiene audit — milestone 1 package 2', '',
             f'- Audit date: {time.strftime("%Y-%m-%dT%H:%M:%S%z")}',
             '- Scope: manifest-listed child repositories only; root is baseline only; `helpagent` was excluded.',
             '- Root baseline only: HEAD `7ace6bf5dd1f23c85fcaf17e5fbbb19913c79d76`; no root repository hygiene scan was run.',
             '- Commands were read-only; no cleanup or repository mutation was performed. Status counts are Git porcelain entries; ignored/untracked directories use Git normal directory collapsing, not recursive file counts.',
             '- Credential scanner tools `gitleaks`, `trufflehog`, and `detect-secrets` were unavailable. Pattern fallback is bounded to tracked regular text files/blobs up to 10 MiB, excluding installed dependency paths, symlinks and binary content.',
             '- Historical refs cover local refs and reflogs only; remote/unfetched refs are not covered. GitHub existence/visibility is unknown because no no-refresh authenticated read-only query was established.',
             '- The existing manifest is not edited by this package. Its remote count includes three failed `origin` lookups; accurate counts below come from per-repository `git remote` names.',
             f'- Manifest SHA-256: `{hashlib.sha256(MANIFEST.read_bytes()).hexdigest()}` at report generation; start/end stability is recorded in `evidence/coverage.json`.', '']
    present = sum(1 for r in results if r.get('manifest_head_state') == 'present')
    unborn = sum(1 for r in results if r.get('manifest_head_state') == 'unborn')
    unresolved = sum(1 for r in results if r.get('manifest_head_state') == 'unresolved')
    completed = sum(1 for r in results if r.get('complete'))
    remote_counts = [r.get('remotes', {}).get('count', 0) for r in results if r.get('manifest_head_state') != 'unresolved' and r.get('remotes')]
    lines += [f'- Manifest reconciliation: {len(manifest_rows)} paths; {present} with HEAD, {unborn} unborn, {unresolved} unresolved; {completed} repository audits complete.',
              f'- Observed configured remote names: {sum(remote_counts)} across {sum(1 for n in remote_counts if n)} resolved repositories; {sum(1 for n in remote_counts if not n)} resolved repositories have no configured remote.',
              '- Remote query per repository: `git -C <repo> remote`, then for each returned name only, `git -C <repo> remote get-url --all <name>` and `git -C <repo> remote get-url --push --all <name>`; URL credentials/query/fragment were redacted before persistence. No fetch was performed.', '',
              '## Repository findings', '',
              '| Repository | HEAD/state | Audit | Unstaged | Staged | Untracked | Ignored | Tracked ignored | Candidates | Remotes | >100 MiB blobs | Credential-pattern matches |',
              '|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|']
    for r in results:
        path = r['manifest_path']
        state = r.get('head_before') or r.get('state') or r['manifest_head_state']
        state_cell = state[:12].replace('|', '\\|')
        st = r.get('status', {}).get('counts', {})
        candidates = sum(r.get('candidate_counts', {}).values())
        remotes = r.get('remotes', {}).get('count', 'unknown')
        over = len(r.get('history', {}).get('over_100_mib', []))
        matches = len(r.get('current_credential_scan', {}).get('observations', [])) + len(r.get('history', {}).get('credential_scan', {}).get('observations', []))
        lines.append(f"| `{path}` | `{state_cell}` | {'complete' if r.get('complete') else 'BLOCKED'} | {st.get('tracked_unstaged', '—')} | {st.get('staged', '—')} | {st.get('untracked_nonignored', '—')} | {st.get('ignored', '—')} | {st.get('tracked_but_ignored', '—')} | {candidates} | {remotes} | {over} | {matches} |")
    lines += ['', '## Candidate review and proposed actions', '']
    for r in results:
        path = r['manifest_path']
        if r.get('manifest_head_state') == 'unresolved':
            lines.append(f'- `{path}` — **unresolved**: manifest records a broken `.git` pointer; no Git query, repair, candidate classification, or audit was attempted. Keep unresolved until separately authorized repair/discovery.')
            continue
        if not r.get('complete'):
            lines.append(f'- `{path}` — **blocked**: {r.get("blocker", "audit not complete")}. Evidence file `{evidence_path(r)}` captures the stopping point; do not treat unrecorded checks as clean.')
        candidates = r.get('current_candidates', [])
        hist = r.get('history', {}).get('history_candidates', [])
        if not candidates and not hist:
            lines.append(f'- `{path}` — no tracked-path or reachable-history junk candidates identified by the naming/type heuristics; no file action proposed. This is not proof of semantic irrelevance.')
            continue
        for source_name, items in [('current tracked', candidates), ('reachable history', hist)]:
            if not items:
                continue
            preview = items[:8]
            rendered = '; '.join(f"`{item['path']}` ({item['classification']}; {item.get('file_type', 'blob')}) — {item['proposed_action']}" for item in preview)
            extra = f'; {len(items) - len(preview)} additional path/object candidates in evidence' if len(items) > len(preview) else ''
            lines.append(f'- `{path}` — {source_name}: {rendered}{extra}. Evidence: `{evidence_path(r)}`.')
    if symlink is not None:
        lines += ['', '## Symlinked-directory coverage check', '',
                  f"- Link entries outside `helpagent`: {symlink.get('link_count', 0)}; resolved physical directory targets examined: {symlink.get('directory_targets_examined', 0)}; `.git` markers found: {len(symlink.get('markers', []))}; target/link gaps: {len(symlink.get('limitations', []))}.",
                  '- The check did not follow nested symlink directories and pruned directories named `helpagent`; it did not audit any newly found repository. See `evidence/symlink-coverage.json` for exact link paths, literal targets, marker results and limitations.']
        if symlink.get('markers'):
            lines += ['- Additional repository-marker candidates (not audited):'] + [f"  - `{m}`" for m in symlink['markers']]
        for limitation in symlink.get('limitations', []):
            lines.append(f"- Coverage limitation: `{limitation.get('link')}` — {limitation.get('reason')}")
    lines += ['', '## Evidence and limits', '',
              '- Full per-repository status paths, candidate metadata, remotes, local tracking state, submodule/worktree state, blob inventories, credential-pattern metadata, command strings and exit statuses are in gzip-compressed JSON records under `evidence/repos/`.',
              '- `evidence/coverage.json` reconciles audit paths/states; `evidence/credential-scanner-availability.txt` records tool availability; `evidence/symlink-coverage.json` records the separate symlink-only coverage check.',
              '- Credentials are never stored. Pattern hits are potential indicators, not confirmed secrets; generic assignment patterns are especially prone to false positives. No values or matching lines are included.',
              '- Current content excludes untracked files, installed dependency locations, symlinks, binaries and files over 10 MiB. History excludes installed dependency locations, binaries, blobs over 10 MiB, and objects not reachable from local refs/reflogs. Remote/unfetched refs and inaccessible/missing objects are not represented.',
              '- No candidate was deleted or edited. Proposed actions are human review questions for a later cleanup package, not cleanup authorization.', '']
    return '\n'.join(lines)

def evidence_path(row: dict) -> str:
    return f"evidence/repos/{row.get('evidence_file', 'missing')}"

def main() -> int:
    REPO_EVIDENCE.mkdir(parents=True, exist_ok=True)
    manifest_hash = hashlib.sha256(MANIFEST.read_bytes()).hexdigest()
    rows = read_manifest()
    results = []
    stop = False
    for idx, spec in enumerate(rows, 1):
        result = audit_one(spec, idx)
        filename = f'{idx:03d}-{re.sub(r"[^A-Za-z0-9._-]+", "_", str(Path(spec["path"]).relative_to(ROOT)))}.json.gz'
        result['evidence_file'] = filename
        write_json_gz(REPO_EVIDENCE / filename, result)
        results.append(result)
        if result.get('blocker'):
            stop = True
            break
    coverage = {'manifest_path_count': len(rows), 'audited_records': len(results),
                'results': [{'path': r['manifest_path'], 'head_state': r['manifest_head_state'], 'complete': r.get('complete', False), 'head': r.get('head_before'), 'evidence': r.get('evidence_file'), 'blocker': r.get('blocker')} for r in results],
                'stopped_on_blocker': stop}
    manifest_unchanged = hashlib.sha256(MANIFEST.read_bytes()).hexdigest() == manifest_hash
    if not manifest_unchanged:
        stop = True
        coverage['manifest_changed_during_audit'] = True
    if stop:
        symlinks = {'complete': False, 'link_count': 0, 'directory_targets_examined': 0, 'markers': [],
                    'limitations': [{'reason': 'not run because the audit stopped on a blocker'}]}
    else:
        symlinks = symlink_coverage()
    (EVIDENCE / 'symlink-coverage.json').write_text(json.dumps(symlinks, indent=2, ensure_ascii=True) + '\n', encoding='utf-8')
    coverage['manifest_sha256'] = manifest_hash
    coverage['manifest_unchanged'] = manifest_unchanged
    coverage['symlink_check_complete'] = symlinks['complete']
    (EVIDENCE / 'coverage.json').write_text(json.dumps(coverage, indent=2, ensure_ascii=True) + '\n', encoding='utf-8')
    (WORK / 'audit.md').write_text(make_report(results, rows, symlinks), encoding='utf-8')
    print(json.dumps({'manifest_paths': len(rows), 'records_written': len(results), 'completed': sum(bool(r.get('complete')) for r in results), 'stopped_on_blocker': stop, 'manifest_unchanged': manifest_unchanged, 'symlink_check_complete': symlinks['complete'], 'symlink_markers': len(symlinks['markers']), 'report': str(WORK / 'audit.md')}, separators=(',', ':')))
    return 2 if stop or len(results) != len(rows) or not symlinks['complete'] else 0

if __name__ == '__main__':
    sys.exit(main())
