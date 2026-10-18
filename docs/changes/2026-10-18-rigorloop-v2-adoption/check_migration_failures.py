#!/usr/bin/env python3
"""Prove that the migration audit detects loss, using only disposable copies."""
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
spec = importlib.util.spec_from_file_location('migration_audit', HERE / 'check_migration.py')
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)
manifest = json.loads((HERE / 'migration-manifest.json').read_text())
with tempfile.TemporaryDirectory(prefix='skillsmith-migration-negative-') as tmp:
    root = Path(tmp) / 'repo'
    shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns('.git', '.agents', '.rigorloop', '__pycache__', '.codex'))
    errors, _ = audit.audit(root)
    assert not errors, errors
    def reject(path, replacement, expected):
        p = root / path
        original = p.read_bytes()
        try:
            if replacement is None:
                p.unlink()
            else:
                p.write_bytes(replacement)
            errors, _ = audit.audit(root)
            assert any(expected in e for e in errors), (expected, errors)
        finally:
            p.write_bytes(original)
        print('Negative check passed:', expected)
    reject(manifest['sources'][0]['snapshot'], None, 'missing snapshot')
    retained = next(e for e in manifest['paragraphs'] if e.get('retained_text') and len(e['retained_text']) > 120 and e['retained_text'].startswith('R'))
    target = retained['target'].partition('#')[0]
    reject(target, None, 'missing destination')
    changed = (root / target).read_text().replace(retained['retained_text'], 'Deliberately missing retained clause.', 1)
    reject(target, changed.encode(), 'retained clause missing')
print('All negative cases rejected; source workspace unchanged.')
