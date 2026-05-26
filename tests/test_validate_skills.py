import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent))
import validate_skills


VALID_FRONTMATTER = """---
name: sample-skill
description: >
  Use this skill whenever a user needs a focused sample output.
argument-hint: sample input
---

**Input:**
$ARGUMENTS

## Output Format

- Result
"""


def write_skill(root: Path, name: str, content: str = VALID_FRONTMATTER) -> Path:
    skill_dir = root / name
    skill_dir.mkdir(parents=True)
    (skill_dir / "SKILL.md").write_text(content, encoding="utf-8")
    return skill_dir


class ValidateSkillsTest(unittest.TestCase):
    def validate_one(self, skill_name: str, content: str = VALID_FRONTMATTER):
        with tempfile.TemporaryDirectory() as tmp:
            skill_dir = write_skill(Path(tmp), skill_name, content)
            return validate_skills.validate_skill(skill_dir)

    def test_missing_skill_file_is_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_dir = Path(tmp) / "sample-skill"
            skill_dir.mkdir()

            result = validate_skills.validate_skill(skill_dir)

        self.assertIn("SKILL.md not found", "\n".join(result.errors))

    def test_invalid_yaml_frontmatter_is_error(self):
        content = VALID_FRONTMATTER.replace("name: sample-skill", "name: [sample-skill")

        result = self.validate_one("sample-skill", content)

        self.assertIn("invalid YAML frontmatter", "\n".join(result.errors))

    def test_missing_required_frontmatter_fields_are_errors(self):
        cases = {
            "name": "name: sample-skill\n",
            "description": "description: >\n  Use this skill whenever a user needs a focused sample output.\n",
            "argument-hint": "argument-hint: sample input\n",
        }

        for field, text in cases.items():
            with self.subTest(field=field):
                result = self.validate_one("sample-skill", VALID_FRONTMATTER.replace(text, ""))

                self.assertIn(field, "\n".join(result.errors))

    def test_valid_skill_without_effort_passes_without_warning(self):
        result = self.validate_one("sample-skill")

        self.assertEqual([], result.errors)
        self.assertEqual([], result.warnings)

    def test_invalid_effort_value_is_error_when_present(self):
        content = VALID_FRONTMATTER.replace(
            "argument-hint: sample input",
            "argument-hint: sample input\neffort: ultra",
        )

        result = self.validate_one("sample-skill", content)

        self.assertIn("invalid effort value: 'ultra'", "\n".join(result.errors))

    def test_non_empty_allowed_tools_requires_tool_using_spec(self):
        content = VALID_FRONTMATTER.replace(
            "argument-hint: sample input",
            "argument-hint: sample input\nallowed-tools: Bash",
        )

        result = self.validate_one("sample-skill", content)

        self.assertIn("tool permissions require an accepted tool-using skill spec", "\n".join(result.errors))

    def test_missing_allowed_tools_is_valid(self):
        result = self.validate_one("sample-skill")

        self.assertEqual([], result.errors)

    def test_skill_name_must_match_directory_and_syntax(self):
        content = VALID_FRONTMATTER.replace("name: sample-skill", "name: Bad_Name")

        result = self.validate_one("bad-name", content)
        error_text = "\n".join(result.errors)

        self.assertIn("name must match directory name 'bad-name'", error_text)
        self.assertIn("name must use lowercase letters, numbers, and hyphens only", error_text)

    def test_reserved_skill_name_is_error(self):
        content = VALID_FRONTMATTER.replace("name: sample-skill", "name: claude")

        result = self.validate_one("claude", content)

        self.assertIn("name uses reserved platform word: 'claude'", "\n".join(result.errors))

    def test_name_longer_than_64_characters_is_error(self):
        long_name = "a" * 65
        content = VALID_FRONTMATTER.replace("name: sample-skill", f"name: {long_name}")

        result = self.validate_one(long_name, content)
        error_text = "\n".join(result.errors)

        self.assertIn("name", error_text)
        self.assertIn("64", error_text)

    def test_missing_body_contracts_are_errors(self):
        content = VALID_FRONTMATTER.replace("$ARGUMENTS", "input").replace("## Output Format", "## Result")

        result = self.validate_one("sample-skill", content)
        error_text = "\n".join(result.errors)

        self.assertIn("$ARGUMENTS not found", error_text)
        self.assertIn("## Output Format section missing", error_text)

    def test_non_latin_metadata_is_warning(self):
        content = VALID_FRONTMATTER.replace(
            "description: >\n  Use this skill whenever a user needs a focused sample output.",
            "description: 中文",
        )

        result = self.validate_one("sample-skill", content)

        self.assertEqual([], result.errors)
        self.assertIn("description contains non-Latin script", "\n".join(result.warnings))

    def test_length_warning_and_error(self):
        warning_body = "\n".join(f"line {i}" for i in range(295))
        warning_content = VALID_FRONTMATTER + "\n" + warning_body
        warning_result = self.validate_one("sample-skill", warning_content)

        self.assertEqual([], warning_result.errors)
        self.assertIn("SKILL.md is over 300 lines", "\n".join(warning_result.warnings))

        error_body = "\n".join(f"line {i}" for i in range(505))
        error_content = VALID_FRONTMATTER + "\n" + error_body
        error_result = self.validate_one("sample-skill", error_content)

        self.assertIn("SKILL.md exceeds 500 lines", "\n".join(error_result.errors))


if __name__ == "__main__":
    unittest.main()
