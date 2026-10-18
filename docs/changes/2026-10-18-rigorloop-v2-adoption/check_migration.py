#!/usr/bin/env python3
"""Audit this migration's retained bytes, explicit coverage and active references."""
import argparse
import hashlib
import json
from pathlib import Path
import re

CHANGE = Path('docs/changes/2026-10-18-rigorloop-v2-adoption')


def digest(data):
    return hashlib.sha256(data).hexdigest()


def anchors(text):
    text = re.sub(r'```.*?```', '', text, flags=re.S)
    found = set(re.findall(r'<a id="([^"]+)"', text))
    counts = {}
    for heading in re.findall(r'^#{1,6}\s+(.+)$', text, re.M):
        slug = re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
        count = counts.get(slug, 0)
        found.add(slug + (f'-{count}' if count else ''))
        counts[slug] = count + 1
    return found


def audit(root):
    errors = []
    manifest = json.loads((root / CHANGE / 'migration-manifest.json').read_text())
    def require(condition, message):
        if not condition:
            errors.append(message)
    for old in ('specs', 'docs/architecture'):
        require(not (root / old).exists(), f'retired root still exists: {old}')
    require(len(manifest['sources']) == 21, 'source inventory is not 21 files')
    expected = set()
    for src in manifest['sources']:
        p = root / src['snapshot']
        require(p.is_file(), f'missing snapshot: {p}')
        if not p.is_file():
            continue
        require(digest(p.read_bytes()) == src['sha256'], f'snapshot changed: {p}')
        for i, block in enumerate(re.split(r'\n\s*\n', p.read_text().strip())):
            expected.add((src['source'], i, digest(block.encode())))
    actual = set()
    for entry in manifest['paragraphs']:
        key = (entry['source'], entry['paragraph'], entry['sha256'])
        require(key not in actual, f'duplicate paragraph disposition: {key}')
        actual.add(key)
        require(entry['disposition'] in ('retained', 'reconciled', 'historical', 'superseded'), f'unresolved disposition: {key}')
        require(bool(entry['rationale']), f'missing rationale: {key}')
        dest, _, fragment = entry['target'].partition('#')
        p = root / dest
        require(p.is_file(), f'missing destination: {entry["target"]}')
        if p.is_file():
            if fragment:
                require(fragment in anchors(p.read_text()), f'missing anchor: {entry["target"]}')
            if entry.get('retained_text'):
                require(entry['retained_text'] in p.read_text(), f'retained clause missing: {key}')
    require(actual == expected, f'paragraph coverage mismatch: missing={len(expected-actual)} extra={len(actual-expected)}')
    for name, sha in manifest['protected'].items():
        p = root / name
        require(p.is_file() and digest(p.read_bytes()) == sha, f'product boundary changed: {name}')
    principles = (root / 'AGENTS.md').read_text().split('## Core Engineering Principles', 1)[1]
    require(digest(principles.encode()) == manifest['agent_principles_sha256'], 'user engineering principles changed')
    active = list((root / 'design').rglob('*.md'))
    snapshots = {root / src['snapshot'] for src in manifest['sources']}
    active += [p for p in (root / 'docs').rglob('*.md')
               if p not in snapshots and 'sources' not in p.relative_to(root).parts]
    active += [root / p for p in ('README.md', 'CONTRIBUTING.md', 'CONSTITUTION.md', 'AGENTS.md', 'CLAUDE.md', 'docs/workflows.md', 'docs/project-map.md', 'docs/plan.md')]
    active = sorted(set(active))
    for p in active:
        if not p.exists():
            errors.append(f'missing active document: {p}')
            continue
        text = re.sub(r'```.*?```', '', p.read_text(), flags=re.S)
        for target in re.findall(r'\]\(([^)]+)\)', text):
            if target.startswith(('http:', 'https:', 'mailto:', 'app:')):
                continue
            name, _, fragment = target.partition('#')
            dest = p.parent / name if name else p
            require(dest.exists(), f'broken link: {p.relative_to(root)} -> {target}')
            if fragment and dest.is_file() and dest.suffix == '.md':
                require(fragment in anchors(dest.read_text()), f'broken fragment: {p.relative_to(root)} -> {target}')
    return errors, len(expected)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[3])
    args = parser.parse_args()
    errors, count = audit(args.root.resolve())
    for error in errors:
        print('ERROR:', error)
    if errors:
        raise SystemExit(1)
    print(f'Migration audit passed: 21 snapshots, {count} paragraph dispositions, protected product bytes and active links/fragments.')
    print('Semantic mappings still require independent review; this audit does not approve them.')
