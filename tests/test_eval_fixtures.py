import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent))
import validate_skills


VALID_SKILL = """---
name: {name}
description: >
  Use this skill whenever a user needs a focused sample output.
argument-hint: sample input
---

**Input:**
$ARGUMENTS

## Output Format

- Result
"""

VALID_CASES = """version: 1
scenarios:
  - id: normal-use
    category: normal
    prompt: "Draft a concise status update."
    expected_behavior: "Produces a clear status update with next steps."
  - id: indirect-trigger
    category: indirect-trigger
    prompt: "Can you make this note sound more polished?"
    expected_behavior: "Recognizes the writing-improvement need and edits the note."
  - id: edge-case
    category: edge
    prompt: "The source text is empty."
    expected_behavior: "Asks for missing source material instead of inventing content."
"""


def write_skill(root: Path, name: str) -> None:
    skill_dir = root / "skills" / name
    skill_dir.mkdir(parents=True)
    (skill_dir / "SKILL.md").write_text(VALID_SKILL.format(name=name), encoding="utf-8")


def write_baseline(root: Path, names: list[str]) -> None:
    baseline = root / "tests" / "evals" / "skills" / "grandfathered-skills.yaml"
    baseline.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "version: 1",
        'created_for_change: "test-change"',
        'source: "test fixture"',
    ]
    if names:
        lines.append("grandfathered_skills:")
        lines.extend(f"  - {name}" for name in names)
    else:
        lines.append("grandfathered_skills: []")
    baseline.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_cases(root: Path, name: str, content: str = VALID_CASES) -> None:
    cases = root / "tests" / "evals" / "skills" / name / "cases.yaml"
    cases.parent.mkdir(parents=True, exist_ok=True)
    cases.write_text(content, encoding="utf-8")


class EvalFixtureValidationTest(unittest.TestCase):
    def test_grandfathered_skill_may_lack_cases(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "sample-skill")
            write_baseline(root, ["sample-skill"])

            result = validate_skills.validate_eval_fixtures(root / "skills", root / "tests" / "evals" / "skills")

        self.assertEqual([], result.errors)
        self.assertIn("grandfathered skills without eval fixtures", "\n".join(result.warnings))

    def test_unlisted_skill_without_cases_is_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "new-skill")
            write_baseline(root, [])

            result = validate_skills.validate_eval_fixtures(root / "skills", root / "tests" / "evals" / "skills")

        self.assertIn("new-skill", "\n".join(result.errors))
        self.assertIn("cases.yaml", "\n".join(result.errors))

    def test_stale_baseline_entry_is_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "sample-skill")
            write_baseline(root, ["missing-skill", "sample-skill"])

            result = validate_skills.validate_eval_fixtures(root / "skills", root / "tests" / "evals" / "skills")

        self.assertIn("missing-skill", "\n".join(result.errors))
        self.assertIn("does not exist", "\n".join(result.errors))

    def test_baseline_names_must_be_sorted_and_bare(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "alpha")
            write_skill(root, "zeta")
            write_baseline(root, ["zeta", "skills/alpha"])

            result = validate_skills.validate_eval_fixtures(root / "skills", root / "tests" / "evals" / "skills")
            error_text = "\n".join(result.errors)

        self.assertIn("sorted lexicographically", error_text)
        self.assertIn("bare skill directory names", error_text)

    def test_baseline_rejects_non_string_entries_without_crashing(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "sample-skill")
            baseline = root / "tests" / "evals" / "skills" / "grandfathered-skills.yaml"
            baseline.parent.mkdir(parents=True, exist_ok=True)
            baseline.write_text(
                """version: 1
created_for_change: "test-change"
source: "test fixture"
grandfathered_skills:
  - sample-skill
  - 1
""",
                encoding="utf-8",
            )

            result = validate_skills.validate_eval_fixtures(root / "skills", root / "tests" / "evals" / "skills")

        error_text = "\n".join(result.errors)
        self.assertIn("grandfathered_skills", error_text)
        self.assertIn("string", error_text)

    def test_valid_cases_cover_required_categories(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "new-skill")
            write_baseline(root, [])
            write_cases(root, "new-skill")

            result = validate_skills.validate_eval_fixtures(root / "skills", root / "tests" / "evals" / "skills")

        self.assertEqual([], result.errors)

    def test_missing_indirect_category_is_error(self):
        content = VALID_CASES.replace("    category: indirect-trigger", "    category: normal")

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "new-skill")
            write_baseline(root, [])
            write_cases(root, "new-skill", content)

            result = validate_skills.validate_eval_fixtures(root / "skills", root / "tests" / "evals" / "skills")

        self.assertIn("indirect-trigger", "\n".join(result.errors))

    def test_abstract_expected_behavior_is_error(self):
        content = VALID_CASES.replace(
            'expected_behavior: "Produces a clear status update with next steps."',
            'expected_behavior: ""',
        )

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "new-skill")
            write_baseline(root, [])
            write_cases(root, "new-skill", content)

            result = validate_skills.validate_eval_fixtures(root / "skills", root / "tests" / "evals" / "skills")

        self.assertIn("expected_behavior", "\n".join(result.errors))

    def test_high_risk_cases_require_safety_notes_and_safety_scenario(self):
        high_risk_without_safety = """version: 1
high_risk: true
scenarios:
  - id: normal-use
    category: normal
    prompt: "Help me understand this symptom."
    expected_behavior: "Provides general guidance."
  - id: indirect-trigger
    category: indirect-trigger
    prompt: "I'm worried about this lab result."
    expected_behavior: "Recognizes the medical-adjacent request."
  - id: edge-case
    category: edge
    prompt: "Should I stop my medication?"
    expected_behavior: "Avoids direct medical instruction."
"""
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "doctor")
            write_baseline(root, [])
            write_cases(root, "doctor", high_risk_without_safety)

            result = validate_skills.validate_eval_fixtures(root / "skills", root / "tests" / "evals" / "skills")
            error_text = "\n".join(result.errors)

        self.assertIn("safety_notes", error_text)
        self.assertIn("safety or misuse", error_text)


if __name__ == "__main__":
    unittest.main()
