import unittest
from pathlib import Path

import yaml


WORKFLOW = Path(__file__).parent.parent / ".github" / "workflows" / "validate.yml"


def workflow_run_commands() -> list[str]:
    data = yaml.safe_load(WORKFLOW.read_text(encoding="utf-8"))
    commands: list[str] = []
    for job in data.get("jobs", {}).values():
        for step in job.get("steps", []):
            run = step.get("run")
            if isinstance(run, str):
                commands.append(run)
    return commands


class CiContractTest(unittest.TestCase):
    def test_ci_runs_deterministic_local_checks(self):
        commands = "\n".join(workflow_run_commands())

        self.assertIn("python -m unittest discover tests", commands)
        self.assertIn("python tests/validate_skills.py", commands)
        self.assertIn("python tests/check_readme_sync.py", commands)

    def test_ci_does_not_run_live_model_or_secret_dependent_steps(self):
        commands = "\n".join(workflow_run_commands()).lower()

        forbidden_fragments = [
            "anthropic_api_key",
            "openai_api_key",
            "claude",
            "openai",
            "gemini",
            "secrets.",
            "curl ",
            "git clone",
        ]
        for fragment in forbidden_fragments:
            with self.subTest(fragment=fragment):
                self.assertNotIn(fragment, commands)


if __name__ == "__main__":
    unittest.main()
