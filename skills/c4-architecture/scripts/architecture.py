#!/usr/bin/env python3
"""Format, validate and render a D2/C4 architecture package (Python 3.9+ and D2 0.7+)."""
import argparse
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


def execute(command):
    print("+ " + " ".join(map(str, command)), flush=True)
    try:
        result = subprocess.run([str(x) for x in command], check=False)
    except OSError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return False
    if result.returncode:
        print(f"ERROR: command returned {result.returncode}", file=sys.stderr)
        return False
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["format", "check", "render"])
    parser.add_argument("--root", type=Path, required=True,
                        help="Architecture package containing model.d2 and views/")
    args = parser.parse_args()
    root = args.root.resolve()
    model = root / "model.d2"
    views_dir = root / "views"
    core = [views_dir / "context.d2", views_dir / "container.d2"]
    if not model.is_file() or not all(p.is_file() for p in core):
        print(f"ERROR: {root} needs model.d2 and views/context.d2 + container.d2", file=sys.stderr)
        return 2
    sources = [model] + sorted(views_dir.glob("*.d2"))
    d2 = shutil.which("d2")
    if not d2:
        print("ERROR: D2 CLI not installed; https://d2lang.com/tour/install", file=sys.stderr)
        return 2

    if args.action == "format":
        return 0 if execute([d2, "fmt"] + sources) else 1
    if args.action == "check":
        for path in sources:
            if not execute([d2, "validate", path]):
                return 1
        if not execute([d2, "fmt", "--check"] + sources):
            print("Run format and commit changed .d2 files.", file=sys.stderr)
            return 1
        # Compilation catches errors missed by syntax-only validation.
        with tempfile.TemporaryDirectory(prefix="skillsmith-c4-") as temp:
            for path in sources[1:]:
                if not execute([d2, path, Path(temp) / (path.stem + ".svg")]):
                    return 1
        print("D2 syntax, formatting and test render checks passed. Human architecture review remains required.")
        return 0

    diagrams = root / "diagrams"
    diagrams.mkdir(exist_ok=True)
    for path in sources[1:]:
        if not execute([d2, path, diagrams / (path.stem + ".svg")]):
            return 1
    print(f"Rendered {len(sources) - 1} view(s) to {diagrams}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
