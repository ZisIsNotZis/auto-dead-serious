#!/usr/bin/env python3
"""Apply the user's AGPL default only to owned child repos with no root license."""
from __future__ import annotations
import json, re, subprocess
from pathlib import Path

ROOT = Path('/home/z/vibe')
WORK = ROOT / '.scratch/32-git-hygiene'
manifest = (WORK / 'manifest.md').read_text(encoding='utf-8')
rows = json.loads(re.search(r'```json\s*(\[.*?\])\s*```', manifest, re.S).group(1))
license_text = (ROOT / 'autofe/LICENSE.md').read_bytes().rstrip(b'\n') + b'\n'
log = WORK / 'evidence/license-batch.jsonl'
records = []
def run(repo, args, timeout=45):
    return subprocess.run(['git','-C',str(repo),*args],cwd=ROOT,text=True,capture_output=True,timeout=timeout,check=False)
for row in rows:
    repo = Path(row['path'])
    parts = {x.casefold() for x in repo.parts}
    if 'helpagent' in parts or 'vendor' in parts or row.get('head_state') in ('unresolved','unborn'):
        continue
    try:
        names = {x.name.casefold() for x in repo.iterdir() if x.is_file()}
    except OSError:
        continue
    if any(n.startswith(('license','copying')) for n in names):
        continue
    if not any(n.startswith('readme') for n in names):
        records.append({'path':str(repo),'action':'skip','reason':'README absent; separate supportable project summary needed'})
        continue
    target = repo / 'LICENSE'
    if target.exists():
        records.append({'path':str(repo),'action':'skip','reason':'license appeared before write'})
        continue
    target.write_bytes(license_text)
    branch = run(repo,['symbolic-ref','--quiet','--short','HEAD'])
    if branch.returncode:
        records.append({'path':str(repo),'action':'file-only','reason':'unborn or detached branch','license':'AGPL-3.0-only'})
        continue
    branch_name = branch.stdout.strip()
    # The saved per-repo status record supplies the exact clean/upstream baseline; no new root/submodule status query.
    name = repo.relative_to(ROOT).as_posix().replace('/','__')
    status_file = WORK / 'status-now' / f'{name}.stdout.txt'
    status_lines = status_file.read_text(encoding='utf-8').splitlines() if status_file.exists() else []
    upstream = next((x.split(' ',2)[2] for x in status_lines if x.startswith('# branch.upstream ')), '')
    ab = next((x.split(' ',2)[2] for x in status_lines if x.startswith('# branch.ab ')), '')
    staged = run(repo,['add','--','LICENSE'])
    if staged.returncode:
        records.append({'path':str(repo),'action':'file-only','reason':'git add failed','license':'AGPL-3.0-only'})
        continue
    commit = run(repo,['commit','--only','-m','Add AGPL-3.0-only license','--','LICENSE'],timeout=90)
    rec={'path':str(repo),'branch':branch_name,'action':'commit','license':'AGPL-3.0-only','commit_exit':commit.returncode,'commit_output':commit.stdout[-1200:],'commit_error':commit.stderr[-400:]}
    if commit.returncode:
        rec['action']='commit-failed'
        records.append(rec)
        continue
    rec['commit']=run(repo,['rev-parse','HEAD']).stdout.strip()
    url=run(repo,['remote','get-url','origin']).stdout.strip()
    is_owner=url.startswith('git@github.com:ZisIsNotZis/') or url.startswith('https://github.com/ZisIsNotZis/')
    if not (upstream and ab == '+0 -0' and is_owner):
        rec['push']='deferred: no synchronized upstream/owner URL in saved status snapshot'
        records.append(rec)
        continue
    push=run(repo,['push','origin',f'HEAD:refs/heads/{branch_name}'],timeout=90)
    rec['push_exit']=push.returncode
    rec['push_output']=push.stdout[-1200:]
    rec['push_error']=push.stderr[-400:]
    records.append(rec)
    log.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in records),encoding='utf-8')
log.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in records),encoding='utf-8')
print(json.dumps({'actions':len(records),'committed':sum(x.get('commit_exit')==0 for x in records),'pushed':sum(x.get('push_exit')==0 for x in records),'deferred':sum('deferred' in x.get('push','') for x in records),'log':str(log.relative_to(ROOT))},ensure_ascii=False))
