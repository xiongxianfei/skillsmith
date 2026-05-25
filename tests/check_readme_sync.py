"""Report README drift for skill table, slash commands, and install URLs."""

from dataclasses import dataclass, field
import re
import sys
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).parent.parent
SKILLS_DIR = REPO_ROOT / "skills"
README_PATH = REPO_ROOT / "README.md"
CANONICAL_REPO = "xiongxianfei/skillsmith"
STALE_REPO = "xiongxianfei/ai-skills"

TABLE_ROW_RE = re.compile(r"^\|\s*\[([a-z0-9][a-z0-9-]*)\]\(skills/\1/SKILL\.md\)\s*\|", re.MULTILINE)
SLASH_COMMAND_RE = re.compile(r"(?<![\w:/])`?/([a-z0-9][a-z0-9-]*)`?")


@dataclass
class ReadmeSyncResult:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def error(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)


def parse_skill_frontmatter(skill_file: Path) -> dict:
    text = skill_file.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    data = yaml.safe_load(parts[1]) or {}
    return data if isinstance(data, dict) else {}


def load_skills(skills_dir: Path) -> dict[str, str]:
    skills: dict[str, str] = {}
    for skill_dir in sorted(path for path in skills_dir.iterdir() if path.is_dir()):
        metadata = parse_skill_frontmatter(skill_dir / "SKILL.md")
        name = str(metadata.get("name") or skill_dir.name)
        description = str(metadata.get("description") or "").strip()
        skills[name] = description
    return skills


def parse_table_skills(readme_text: str) -> set[str]:
    return set(TABLE_ROW_RE.findall(readme_text))


def parse_slash_commands(readme_text: str) -> set[str]:
    return set(SLASH_COMMAND_RE.findall(readme_text))


def check_install_instructions(readme_text: str, result: ReadmeSyncResult) -> None:
    normalized = readme_text.lower()
    if STALE_REPO in normalized:
        result.warn(f"stale install instructions reference {STALE_REPO}")
    if CANONICAL_REPO not in normalized:
        result.warn(f"README install instructions do not reference {CANONICAL_REPO}")


def check_readme_sync(repo_root: Path = REPO_ROOT) -> ReadmeSyncResult:
    result = ReadmeSyncResult()
    skills_dir = repo_root / "skills"
    readme_path = repo_root / "README.md"

    if not skills_dir.exists():
        result.error(f"{skills_dir} not found")
        return result
    if not readme_path.exists():
        result.error(f"{readme_path} not found")
        return result

    skills = load_skills(skills_dir)
    expected = set(skills)
    readme_text = readme_path.read_text(encoding="utf-8")

    table_skills = parse_table_skills(readme_text)
    missing_table = sorted(expected - table_skills)
    extra_table = sorted(table_skills - expected)
    if missing_table:
        result.warn("missing README skill table entries: " + ", ".join(missing_table))
    if extra_table:
        result.warn("extra README skill table entries: " + ", ".join(extra_table))

    commands = parse_slash_commands(readme_text)
    missing_commands = sorted(expected - commands)
    extra_commands = sorted(commands - expected)
    if missing_commands:
        result.warn("missing README slash commands: " + ", ".join(f"/{name}" for name in missing_commands))
    if extra_commands:
        result.warn("extra README slash commands: " + ", ".join(f"/{name}" for name in extra_commands))

    check_install_instructions(readme_text, result)
    return result


def main() -> int:
    result = check_readme_sync(REPO_ROOT)

    if result.warnings:
        print("README sync warnings:")
        for warning in result.warnings:
            print(f"  WARN  {warning}")
        print()

    if result.errors:
        print("README sync errors:")
        for error in result.errors:
            print(f"  ERROR {error}")
        return 1

    if not result.warnings:
        print("README sync check passed.")
    else:
        print(f"README sync check completed with {len(result.warnings)} warning(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
