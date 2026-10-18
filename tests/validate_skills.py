"""Check each public skill entrypoint and Agent Skills frontmatter constraints."""
import re
import sys
from pathlib import Path
import yaml

SKILLS_DIR = Path(__file__).parent.parent / "skills"
REQUIRED_FRONTMATTER = ("name", "description")
NAME_PATTERN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")


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

    name = metadata.get("name")
    if isinstance(name, str) and name.strip():
        if len(name) > 64 or not NAME_PATTERN.fullmatch(name):
            errors.append("'name' must be 1-64 lowercase letters, digits, or single hyphens")
        if name != skill_dir.name:
            errors.append(f"'name' ({name}) must match directory ({skill_dir.name})")

    description = metadata.get("description")
    if isinstance(description, str) and len(description) > 1024:
        errors.append("'description' exceeds 1024 characters")

    compatibility = metadata.get("compatibility")
    if compatibility is not None:
        if not isinstance(compatibility, str) or not compatibility.strip() or len(compatibility) > 500:
            errors.append("'compatibility' must be a non-empty string of at most 500 characters")

    extra = metadata.get("metadata")
    if extra is not None:
        if not isinstance(extra, dict) or not all(isinstance(k, str) and isinstance(v, str) for k, v in extra.items()):
            errors.append("'metadata' must map string keys to string values")
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

    print(f"Checking Agent Skills entrypoints for {len(skill_dirs)} skill(s)...\n")
    errors = []
    for skill_dir in skill_dirs:
        label = f"skills/{skill_dir.name}/SKILL.md"
        errors.extend(f"  ERROR  {label}: {message}" for message in validate_skill(skill_dir))

    if errors:
        print("\n".join(errors))
        print(f"\n{len(errors)} error(s) found. Fix them before merging.")
        return 1

    print(f"All {len(skill_dirs)} skill(s) passed metadata checks.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
