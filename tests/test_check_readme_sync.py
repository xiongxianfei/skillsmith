import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent))
import check_readme_sync


SKILL_TEMPLATE = """---
name: {name}
description: >
  {description}
---

$ARGUMENTS

## Output Format
"""


def write_skill(root: Path, name: str, description: str | None = None) -> None:
    skill_dir = root / "skills" / name
    skill_dir.mkdir(parents=True)
    (skill_dir / "SKILL.md").write_text(
        SKILL_TEMPLATE.format(name=name, description=description or f"Use this skill whenever {name} is needed."),
        encoding="utf-8",
    )


def readme_for(names: list[str], install_repo: str = "xiongxianfei/Skillsmith") -> str:
    rows = "\n".join(
        f"| [{name}](skills/{name}/SKILL.md) | `/{name}` | Use this skill whenever {name} is needed. |"
        for name in names
    )
    commands = ", ".join(f"`/{name}`" for name in names)
    return f"""# Skillsmith

## Skills

| Skill | Claude Command | Description |
|-------|---------------|-------------|
{rows}

## Installation

```bash
curl -sSL https://raw.githubusercontent.com/{install_repo}/main/install.sh | bash
git clone https://github.com/{install_repo}
```

Restart Claude Code after installing — skills are available immediately as {commands}.
"""


def write_readme(root: Path, content: str) -> None:
    (root / "README.md").write_text(content, encoding="utf-8")


class ReadmeSyncTest(unittest.TestCase):
    def run_check(self, readme: str, skill_names: list[str] | None = None):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name in skill_names or ["alpha", "beta"]:
                write_skill(root, name)
            write_readme(root, readme)

            return check_readme_sync.check_readme_sync(root)

    def test_complete_readme_is_in_sync(self):
        result = self.run_check(readme_for(["alpha", "beta"]))

        self.assertEqual([], result.errors)
        self.assertEqual([], result.warnings)

    def test_missing_skill_table_row_is_reported(self):
        result = self.run_check(readme_for(["alpha"]))

        self.assertIn("missing README skill table entries", "\n".join(result.warnings))
        self.assertIn("beta", "\n".join(result.warnings))

    def test_extra_skill_table_row_is_reported(self):
        result = self.run_check(readme_for(["alpha", "beta", "ghost"]))

        self.assertIn("extra README skill table entries", "\n".join(result.warnings))
        self.assertIn("ghost", "\n".join(result.warnings))

    def test_missing_slash_command_is_reported(self):
        readme = readme_for(["alpha", "beta"]).replace("`/beta`", "`beta`")

        result = self.run_check(readme)

        self.assertIn("missing README slash commands", "\n".join(result.warnings))
        self.assertIn("/beta", "\n".join(result.warnings))

    def test_extra_slash_command_is_reported(self):
        readme = readme_for(["alpha", "beta"]) + "\nTry `/ghost` for old behavior.\n"

        result = self.run_check(readme)

        self.assertIn("extra README slash commands", "\n".join(result.warnings))
        self.assertIn("/ghost", "\n".join(result.warnings))

    def test_stale_install_url_is_reported(self):
        result = self.run_check(readme_for(["alpha", "beta"], install_repo="xiongxianfei/ai-skills"))

        self.assertIn("stale install instructions", "\n".join(result.warnings))
        self.assertIn("ai-skills", "\n".join(result.warnings))

    def test_current_skillsmith_install_url_passes(self):
        result = self.run_check(readme_for(["alpha", "beta"], install_repo="xiongxianfei/Skillsmith"))

        self.assertEqual([], result.errors)
        self.assertEqual([], result.warnings)


if __name__ == "__main__":
    unittest.main()
