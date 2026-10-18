"""Check SKILL.md format and metadata; no behavioral evaluation is performed."""

from dataclasses import dataclass, field
import re
import sys
from pathlib import Path

import yaml

SKILLS_DIR = Path(__file__).parent.parent / "skills"

REQUIRED_FRONTMATTER = ["name", "description"]
ALLOWED_EFFORT = {"low", "medium", "high", "xhigh", "max"}
RESERVED_NAMES = {"anthropic", "claude"}
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SOFT_LINE_LIMIT = 300
HARD_LINE_LIMIT = 500


@dataclass
class ValidationResult:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def error(self, category: str, msg: str) -> None:
        self.errors.append(f"[{category}] {msg}")

    def warn(self, category: str, msg: str) -> None:
        self.warnings.append(f"[{category}] {msg}")


def contains_non_latin_script(s: str) -> bool:
    """Return True if the string contains CJK or Cyrillic characters.

    Allows common typographic characters used in English (em dash, arrows, etc.)
    while catching descriptions written in Chinese, Russian, Japanese, etc.
    """
    for c in s:
        cp = ord(c)
        if (
            0x0400 <= cp <= 0x04FF   # Cyrillic
            or 0x3040 <= cp <= 0x309F  # Hiragana
            or 0x30A0 <= cp <= 0x30FF  # Katakana
            or 0x3400 <= cp <= 0x4DBF  # CJK Extension A
            or 0x4E00 <= cp <= 0x9FFF  # CJK Unified Ideographs
        ):
            return True
    return False


def parse_skill(path: Path) -> tuple[dict, str]:
    """Split SKILL.md into frontmatter dict and body string."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    fm = yaml.safe_load(parts[1]) or {}
    if not isinstance(fm, dict):
        return {}, parts[2]
    body = parts[2]
    return fm, body


def validate_skill(skill_dir: Path) -> ValidationResult:
    result = ValidationResult()
    skill_file = skill_dir / "SKILL.md"

    if not skill_file.exists():
        result.error("compatibility", "SKILL.md not found")
        return result

    try:
        fm, body = parse_skill(skill_file)
    except yaml.YAMLError as e:
        result.error("compatibility", f"invalid YAML frontmatter: {e}")
        return result

    for field in REQUIRED_FRONTMATTER:
        if field not in fm:
            result.error("compatibility", f"missing required frontmatter field: '{field}'")

    name = str(fm.get("name", ""))
    if name:
        if name != skill_dir.name:
            result.error("compatibility", f"name must match directory name '{skill_dir.name}'")
        if len(name) > 64:
            result.error("compatibility", "name must not exceed 64 characters")
        if not NAME_RE.fullmatch(name):
            result.error("compatibility", "name must use lowercase letters, numbers, and hyphens only")
        if name in RESERVED_NAMES:
            result.error("compatibility", f"name uses reserved platform word: '{name}'")

    allowed_tools = fm.get("allowed-tools")
    if "allowed-tools" in fm and allowed_tools not in ("", None):
        result.error("skillsmith-policy", "tool permissions require an accepted tool-using skill spec")

    effort = fm.get("effort")
    if effort is not None and str(effort) not in ALLOWED_EFFORT:
        result.error("compatibility", f"invalid effort value: '{effort}'")

    # English-only checks on fields shown in Claude Code UI
    desc = str(fm.get("description", ""))
    if desc and contains_non_latin_script(desc):
        result.warn("reviewer-heuristic", "description contains non-Latin script — use English for reliable auto-invocation")

    if "$ARGUMENTS" not in body:
        result.error("skillsmith-policy", "$ARGUMENTS not found in prompt body — slash command input will be dropped")

    if "## Output Format" not in body:
        result.error("skillsmith-policy", "## Output Format section missing — output structure is undefined")

    line_count = skill_file.read_text(encoding="utf-8").count("\n") + 1
    if line_count > HARD_LINE_LIMIT:
        result.error("skillsmith-policy", f"SKILL.md exceeds 500 lines ({line_count})")
    elif line_count > SOFT_LINE_LIMIT:
        result.warn("reviewer-heuristic", f"SKILL.md is over 300 lines ({line_count}); consider progressive disclosure")

    return result


def main():
    skill_dirs = sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir())
    errors = []
    warnings = []

    if not skill_dirs:
        print("No skills found — add skill directories under skills/")
        sys.exit(1)

    print(f"Validating {len(skill_dirs)} skill(s)...\n")
    for skill_dir in skill_dirs:
        result = validate_skill(skill_dir)
        label = f"skills/{skill_dir.name}/SKILL.md"
        errors.extend(f"  ERROR  {label}: {msg}" for msg in result.errors)
        warnings.extend(f"  WARN   {label}: {msg}" for msg in result.warnings)

    if warnings:
        print("Warnings:")
        for w in warnings:
            print(w)
        print()

    if errors:
        print("Errors:")
        for e in errors:
            print(e)
        print(f"\n{len(errors)} error(s) found. Fix them before merging.")
        sys.exit(1)

    print(f"All {len(skill_dirs)} skill(s) passed validation.")
    if warnings:
        print(f"{len(warnings)} warning(s) — review recommended but not blocking.")


if __name__ == "__main__":
    main()
