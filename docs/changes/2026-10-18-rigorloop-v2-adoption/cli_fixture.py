#!/usr/bin/env python3
"""Exercise the pinned CLI in temporary projects; never use the live project store.

python -B cli_fixture.py --node /path/to/node24 --cli /path/to/rigorloop/dist/bin/rigorloop.js
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile
import uuid


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--node', required=True)
    parser.add_argument('--cli', required=True)
    args = parser.parse_args()
    node, cli = str(Path(args.node).resolve()), str(Path(args.cli).resolve())
    package = json.loads((Path(cli).parents[2] / 'package.json').read_text())
    assert package['name'] == '@xiongxianfei/rigorloop' and package['version'] == '2.0.0'
    env = dict(os.environ, PATH=str(Path(node).parent) + os.pathsep + os.environ['PATH'])
    version = subprocess.check_output([node, '-p', 'JSON.stringify({node:process.versions.node,sqlite:process.versions.sqlite})'], text=True)
    print('Runtime:', version.strip())
    actor = {'id': 'adoption-fixture', 'role': 'support'}
    change = 'adoption-fixture'

    def envelope(data, revision=None):
        return {'schema_version': 2, 'interface': 'targeted-recording-v2', 'contract': 'rigorloop-records-v4', 'change_id': change, 'expected_revision': revision, 'reads': [], 'input': data}

    def maintenance(data):
        return {'schema_version': 1, 'interface': 'store-maintenance-v1', 'input': data}

    with tempfile.TemporaryDirectory(prefix='skillsmith-rigorloop-proof-') as tmp:
        root = Path(tmp) / 'project'
        restored = Path(tmp) / 'restored'
        root.mkdir(); restored.mkdir()
        identity = json.dumps({'schema_version': 1, 'project_id': str(uuid.uuid4())})
        for p in (root, restored):
            (p / '.rigorloop.json').write_text(identity)
        # Include an unrelated adapter file so preview must preserve existing content too.
        (root / '.agents/skills/unrelated').mkdir(parents=True)
        (root / '.agents/skills/unrelated/SKILL.md').write_text('Unrelated fixture, retain exactly.\n')

        def tree(p):
            return {str(f.relative_to(p)): hashlib.sha256(f.read_bytes()).hexdigest() if f.is_file() else 'directory' for f in p.rglob('*')}

        def run(words, data=None, target=root, failure=False):
            command = [node, cli, *words]
            if words[0] != 'init':
                command += ['--root', str(target)]
            if data is not None:
                command += ['--input', '-']
            command += ['--json'] if words[0] == 'init' else ['--format', 'json']
            result = subprocess.run(command, input=json.dumps(data) if data is not None else None, text=True, capture_output=True, cwd=target, env=env)
            try:
                value = json.loads(result.stdout)
            except json.JSONDecodeError:
                raise AssertionError(f'{words}: invalid response {result.returncode}: {result.stdout[:1000]} {result.stderr[:1000]}')
            if bool(result.returncode) != failure:
                raise AssertionError(f'{words}: unexpected result {result.returncode}: {json.dumps(value)[:4000]}')
            return value

        before = tree(root)
        preview = run(['init', 'codex', '--dry-run'])
        assert tree(root) == before, 'Installer preview wrote destination files'
        print('Installer preview: success; destination paths/bytes unchanged.')
        created = run(['change', 'create', '--change', change], envelope({
            'intent': {'goal': 'Validate disposable CLI behavior', 'scope': 'Temporary fixture only', 'exclusions': ['No real approvals or live-store mutations']},
            'request': {'locator': 'adoption proof TG-3', 'content': 'Exercise storage and recovery using fabricated fixture work', 'captured_by': actor},
            'authority': {'source': 'Reviewed adoption delivery plan', 'allowed': ['Disposable fixture mutations'], 'limits': ['No production state or review judgments'], 'reported_by': actor},
            'activity': {'stage': 'support', 'status': 'in-progress', 'owner': actor, 'reason': 'Temporary qualification fixture'},
            'next_action': None,
        }))
        context = run(['change', 'context', '--change', change])
        # Inspected output shape is part of this pinned-version fixture.
        revision = context['revision']
        action = {'action': 'Check restored context', 'owner': actor, 'rationale': 'Fixture next action'}
        update = envelope({'next_action': action}, revision)
        run(['change', 'update', '--change', change], update)
        rejected = run(['change', 'update', '--change', change], update, failure=True)
        assert any(e['code'] == 'revision-conflict' for e in rejected['errors']), rejected
        current = run(['change', 'context', '--change', change])
        assert current['revision'] != revision
        print('Create/context/update: passed; stale revision rejected.')
        backup = run(['store', 'backup'], maintenance({'scope': {'changes': 'all'}, 'output': str(Path(tmp) / 'backup'), 'actor': actor}))
        integrity = backup['maintenance']['integrity']
        run(['store', 'restore'], maintenance({'backup': str(Path(tmp) / 'backup'), 'expected_backup': integrity, 'expected_store': {'kind': 'absent'}, 'replace': False, 'actor': actor, 'reason': 'Verify recovery in absent disposable store'}), target=restored)
        recovered = run(['change', 'context', '--change', change], target=restored)
        assert recovered['revision'] != current['revision'], 'Restore reused old revision'
        assert 'Check restored context' in json.dumps(recovered), 'Restored handoff missing'
        rejected = run(['change', 'update', '--change', change], envelope({'next_action': None}, current['revision']), target=restored, failure=True)
        assert any(e['code'] == 'revision-conflict' for e in rejected['errors']), rejected
        run(['change', 'update', '--change', change], envelope({'next_action': None}, recovered['revision']), target=restored)
        print('Backup/restore: handoff recovered, old token rejected, fresh context revision accepted.')
        print('No Review, Verification or completion judgment was created. Temporary projects removed on exit.')


if __name__ == '__main__':
    main()
