#!/usr/bin/env python3
"""Create a D2/C4 starter package without overwriting existing project files."""
import argparse
from pathlib import Path
import shutil
import sys

TEMPLATE = Path(__file__).resolve().parents[1] / "assets" / "project-template"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd(), help="Repository root")
    parser.add_argument("--target", type=Path, default=Path("architecture"),
                        help="Destination directory RELATIVE to --repo")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    repo = args.repo.resolve()
    target_arg = args.target
    if not repo.is_dir() or not TEMPLATE.is_dir():
        print("ERROR: repository or bundled template directory is missing", file=sys.stderr)
        return 2
    if target_arg.is_absolute() or target_arg == Path("."):
        print("ERROR: --target must be a non-root, relative directory", file=sys.stderr)
        return 2
    target = (repo / target_arg).resolve()
    try:
        target.relative_to(repo)
    except ValueError:
        print("ERROR: --target must remain inside the repository", file=sys.stderr)
        return 2
    new_count = old_count = 0
    for source in sorted(TEMPLATE.rglob("*")):
        if not source.is_file():
            continue
        destination = target / source.relative_to(TEMPLATE)
        try:
            destination.resolve().relative_to(repo)
        except ValueError:
            print(f"ERROR: file path escapes repository: {destination}", file=sys.stderr)
            return 2
        label = destination.relative_to(repo)
        if destination.exists() or destination.is_symlink():
            print(f"PRESERVE {label}")
            old_count += 1
            continue
        print(f"CREATE   {label}")
        if not args.dry_run:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, destination)
        new_count += 1
    print(f'{"Planned" if args.dry_run else "Created"}: {new_count}; preserved: {old_count}')
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
