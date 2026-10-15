#!/usr/bin/env python3
"""Render the audit's explicit resource-blocked state from work-record evidence only."""
import json
from pathlib import Path
import re

ROOT = Path('/home/z/vibe')
WORK = ROOT / '.scratch/32-git-hygiene'

def load_manifest():
    text = (WORK / 'manifest.md').read_text(encoding='utf-8')
    match = re.search(r'```json\s*(\[.*?\])\s*```', text, re.S)
    if not match:
        raise RuntimeError('manifest JSON block absent')
    rows = json.loads(match.group(1))
    if len(rows) != 86:
        raise RuntimeError(f'unexpected manifest path count: {len(rows)}')
    if any(any(part.lower() == 'helpagent' for part in Path(row['path']).parts) for row in rows):
        raise RuntimeError('helpagent is in manifest; refuse to render as scoped')
    return rows

def main():
    rows = load_manifest()
    remote_rows = [json.loads(line) for line in (WORK / 'evidence/remote-only.jsonl').read_text(encoding='utf-8').splitlines()]
    if len(remote_rows) != 86:
        raise RuntimeError(f'expected 86 remote evidence rows, got {len(remote_rows)}')
    by_path = {row['path']: row for row in remote_rows}
    if set(by_path) != {row['path'] for row in rows}:
        raise RuntimeError('remote evidence paths do not reconcile with manifest')
    resolved = [row for row in remote_rows if row['manifest_head_state'] != 'unresolved']
    remotes = [(row['path'], remote) for row in resolved for remote in row['remotes']]
    names = sum(len(row['remote_names']) for row in resolved)
    usable = sum(bool(item['fetch_urls']) and bool(item['push_urls']) for _, item in remotes)
    url_less = [(path, item['name']) for path, item in remotes if not item['fetch_urls'] and not item['push_urls']]
    lines = [
        '# Git hygiene audit — milestone 1 package 2 (blocked before repository scan)',
        '',
        '- Result: **incomplete and blocked**, not a clean audit.',
        '- Stop reason: no machine-wide exclusive-use window/owner or coordinated admission grant was established. The parent confirmed that the user’s `go` and the one-worker constraint do not imply exclusive machine control. Do not begin the 85-repository status/path/history/content/credential scan until the missing resource authority/evidence is established.',
        '- No repository status, tracked-path, submodule/worktree, history/blob, current-content, historical-content, credential-pattern, or symlink-target marker scan ran. The prepared `audit_repos.py` was not executed. No repository or remote was changed.',
        '- Scope reconciliation: 86 manifest child paths = 83 with HEAD, 2 unborn, 1 unresolved; 85 resolved repositories received only lightweight current HEAD and remote metadata queries. The unresolved pointer was not queried or repaired. `helpagent` was not inspected.',
        '- Root is baseline only: `/home/z/vibe` HEAD `7ace6bf5dd1f23c85fcaf17e5fbbb19913c79d76`; no root hygiene scan ran.',
        '- The vetted scanner availability check found `gitleaks`, `trufflehog`, and `detect-secrets` unavailable. The bounded fallback patterns were not run because the resource stop occurred first.',
        '',
        '## Remote-name correction',
        '',
        f'- `git remote` returned {names} registered remote names across {len(resolved)} resolved repositories; {sum(bool(row["remote_names"]) for row in resolved)} resolved repositories had at least one name and {sum(not row["remote_names"] for row in resolved)} had no names.',
        f'- {usable} registered names returned both fetch and push URLs. {len(url_less)} registered names had neither fetch nor push URL; these are URL-less/incomplete names, not usable GitHub remotes: ' + ', '.join(f'`{path}` (`{name}`)' for path, name in url_less) + '.',
        '- The earlier manifest counted failed URL lookups as if they were configured URLs and said one repository had no remotes. Direct names show 87 names and no empty name list; the three entries above have no usable URL. The manifest was left unchanged while it was read; its dated follow-up now records this correction and provenance.',
        '- Exact read-only procedure per resolved repository: `git -C <repo> rev-parse --verify HEAD`; for unborn repositories, `git -C <repo> symbolic-ref --quiet HEAD`; `git -C <repo> remote`; and for each returned name only, `git -C <repo> remote get-url --all <name>` and `git -C <repo> remote get-url --push --all <name>`. No fetch or GitHub/API request was made. URL user-info/query/fragment were redacted before persistence.',
        '- Remote evidence: `evidence/remote-only.jsonl` (per-repository commands, exit statuses, current HEAD and sanitized results) and `evidence/remote-only-summary.json` (counts and unchanged manifest hash).',
        '',
        '## Repository-by-repository scan state',
        '',
        'Every manifest path is listed below. A dash means **not measured**, not zero or clean. Remote names and URL usability are the separate metadata-only result; all hygiene categories remain unscanned.',
        '',
        '| Repository | Manifest/current HEAD state | Registered remote names | Usable fetch/push URLs | Tracked unstaged | Staged | Untracked nonignored | Ignored | Tracked-but-ignored | Hygiene audit |',
        '|---|---|---|---:|---:|---:|---:|---:|---:|---|',
    ]
    for manifest_row in rows:
        row = by_path[manifest_row['path']]
        if row['manifest_head_state'] == 'unresolved':
            state = 'unresolved pointer; not queried'
            remote_names = 'unknown'
            usable_here = '—'
            audit_state = 'not run; unresolved pointer retained'
        else:
            head = row.get('current_head') or 'current HEAD not verified'
            state = ('unborn:' + head.rsplit('/', 1)[-1]) if head.startswith('unborn:') else head[:12]
            remote_names = ', '.join(f'`{name}`' for name in row['remote_names']) if row['remote_names'] else '(none)'
            usable_here = sum(bool(item['fetch_urls']) and bool(item['push_urls']) for item in row['remotes'])
            audit_state = 'not run; resource coordination blocker'
        lines.append(f"| `{manifest_row['path']}` | `{state}` | {remote_names} | {usable_here} | — | — | — | — | — | {audit_state} |")
    lines += [
        '',
        '## Outstanding findings and next action',
        '',
        '- No repository can be called clean and no file-specific junk candidate can be classified from this blocked run. Proposed action for each resolved repository is to defer cleanup decisions until the bounded audit is authorized and completed; do not delete or edit paths. For `dojo`, `murderMysteryGame`, and `pi-keys`, later review whether their URL-less `origin` names are intentional; do not add or repair URLs here. For `ra2/vendor/svg-creator-skill`, retain the unresolved state and do not repair it.',
        '- Symlink coverage remains unknown. The prior inventory used no-follow traversal; no follow-up link/`.git` marker search ran under the resource stop. Potential repositories reachable only through symlinked directories are not ruled out, and `helpagent` must remain excluded.',
        '- Local tracking/ahead/behind state, status categories, tracked junk candidates, submodule/worktree state, largest blobs, >100 MiB list, and credential findings are all unmeasured. Remote/unfetched refs and GitHub existence/visibility are also unverified.',
        '- Evidence bounds: `evidence/remote-only.jsonl`, `evidence/remote-only-summary.json`, `evidence/credential-scanner-availability.txt`; ticket and manifest addenda record the stop, reviewer finding, provenance, and missing resource grant. The existing manifest path/HEAD inventory remains the source for the blocked path list.',
        '',
    ]
    (WORK / 'audit.md').write_text('\n'.join(lines), encoding='utf-8')
    print(json.dumps({'manifest_paths': len(rows), 'remote_evidence_paths': len(remote_rows), 'registered_remote_names': names,
                      'usable_fetch_push_urls': usable, 'url_less_names': len(url_less), 'hygiene_scans_run': 0,
                      'report': str(WORK / 'audit.md')}, separators=(',', ':')))

if __name__ == '__main__':
    main()
