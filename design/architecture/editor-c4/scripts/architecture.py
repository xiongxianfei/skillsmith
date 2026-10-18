#!/usr/bin/env python3
"""Portable D2/C4 formatting, consistency checks, and SVG rendering.

No third-party Python libraries. Run from any working directory:
  python3 design/architecture/editor-c4/scripts/architecture.py format
  python3 design/architecture/editor-c4/scripts/architecture.py check
  python3 design/architecture/editor-c4/scripts/architecture.py render
"""
from __future__ import annotations
import argparse
from pathlib import Path
import re
import shutil
import subprocess
import sys

ARCH = Path(__file__).resolve().parents[1]
VIEWS = ARCH / 'views'
IMAGES = ARCH / 'diagrams'
CORE_VIEWS = ('context', 'container')


def all_sources():
    return [ARCH / 'model.d2'] + sorted(VIEWS.glob('*.d2'))


def preflight() -> bool:
    d2 = shutil.which('d2')
    if not d2:
        print('ERROR: D2 CLI not on PATH. Install from https://d2lang.com/tour/install', file=sys.stderr)
        return False
    print('Using D2:', subprocess.run([d2, '--version'], capture_output=True, text=True).stdout.strip())
    return True


def run(args: list[str]) -> bool:
    print('+ ' + ' '.join(args), flush=True)
    try:
        result = subprocess.run(args, check=False)
        if result.returncode:
            print(f'ERROR: command returned exit status {result.returncode}', file=sys.stderr)
            return False
        return True
    except OSError as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return False


def policy_check() -> bool:
    problems = []
    for filename in ['model.d2', 'views/context.d2', 'views/container.d2']:
        if not (ARCH / filename).is_file():
            problems.append(f'missing required file: {filename}')
    if not problems:
        model = (ARCH / 'model.d2').read_text(encoding='utf-8')
        if not re.search(r'^\s*\w+\s*->\s*[\w.]+\s*:', model, re.M):
            problems.append('model.d2 should define at least one directed labeled relationship')
        for name in CORE_VIEWS:
            view = (VIEWS / f'{name}.d2').read_text(encoding='utf-8')
            if not re.search(r'^\s*\.\.\.@\.\./model(?:\.d2)?\s*$', view, re.M):
                problems.append(f'{name}.d2 must import the common model via ...@../model')
            if 'suspend' not in view or 'unsuspend' not in view:
                problems.append(f'{name}.d2 must select model elements with suspend/unsuspend')
            # D2 globs include arrows in the selector; exclude these on purpose.
            for line_no, line in enumerate(view.splitlines(), 1):
                s = line.strip()
                if '->' in s and not s.startswith('(') and not s.startswith('#'):
                    problems.append(f'{name}.d2:{line_no}: add structural edges to model.d2, not a C4 view')
    if problems:
        for p in problems:
            print('POLICY ERROR:', p, file=sys.stderr)
        return False
    print('Basic C4 source-of-truth policy checks passed (not full semantic validation).')
    return True


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('action', choices=['format', 'check', 'render'])
    args = p.parse_args()

    if not policy_check():
        return 1
    files = all_sources()
    if not files:
        print('ERROR: No D2 sources found', file=sys.stderr)
        return 1
    if not preflight():
        return 2

    if args.action == 'format':
        return 0 if run(['d2', 'fmt', *map(str, files)]) else 1

    if args.action == 'check':
        for f in files:
            if not run(['d2', 'validate', str(f)]):
                return 1
        if not run(['d2', 'fmt', '--check', *map(str, files)]):
            print('Run the format action and commit the changes.', file=sys.stderr)
            return 1
        # An SVG render tests more than parser validation and catches import/layout errors.
        import tempfile
        with tempfile.TemporaryDirectory(prefix='c4-d2-check-') as tmp:
            for src in sorted(VIEWS.glob('*.d2')):
                if not run(['d2', '--layout=elk', str(src), str(Path(tmp) / (src.stem + '.svg'))]):
                    return 1
        print('Check complete: formatting, syntax, and rendering passed.')
        return 0

    IMAGES.mkdir(exist_ok=True)
    for src in sorted(VIEWS.glob('*.d2')):
        if not run(['d2', '--layout=elk', str(src), str(IMAGES / (src.stem + '.svg'))]):
            return 1
    print(f'Rendered {len(list(VIEWS.glob("*.d2")))} diagram(s) into {IMAGES}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
