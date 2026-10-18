"""Check required skill files and metadata; no behavioral evaluation is performed."""

import re
import sys
from pathlib import Path

import yaml

SKILLS_DIR = Path(__file__).parent.parent / "skills"
REQUIRED_FRONTMATTER = ("name", "description")


def validate_skill(skill_dir: Path) -> list[str]:
    try:
        text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        return [f"cannot read SKILL.md: {error}"]

    frontmatter = re.match(r"\A---[ \t]*\n(.*?)^---[ \t]*(?:\n|$)", text, re.S | re.M)
    if frontmatter is None:
        return ["YAML frontmatter must start the file and be enclosed by standalone '---' lines"]

    try:
        metadata = yaml.safe_load(frontmatter.group(1))
    except yaml.YAMLError as error:
        return [f"invalid YAML frontmatter: {error}"]
    if not isinstance(metadata, dict):
        return ["YAML frontmatter must be a mapping"]

    errors = []
    for field in REQUIRED_FRONTMATTER:
        value = metadata.get(field)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"'{field}' must be a non-empty string")
    return errors


def main() -> int:
    try:
        skill_dirs = sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir())
    except OSError as error:
        print(f"Cannot read skills directory: {error}")
        return 1
    if not skill_dirs:
        print("No skills found — add skill directories under skills/")
        return 1

    print(f"Checking required files and metadata for {len(skill_dirs)} skill(s)...\n")
    errors = []
    for skill_dir in skill_dirs:
        label = f"skills/{skill_dir.name}/SKILL.md"
        errors.extend(f"  ERROR  {label}: {message}" for message in validate_skill(skill_dir))

    if errors:
        print("\n".join(errors))
        print(f"\n{len(errors)} error(s) found. Fix them before merging.")
        return 1

    print(f"All {len(skill_dirs)} skill(s) passed required checks.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
