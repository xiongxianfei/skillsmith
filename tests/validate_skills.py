"""Validate skills in the skills/ directory against deterministic rules."""

from dataclasses import dataclass, field
import re
import sys
from pathlib import Path

import yaml

SKILLS_DIR = Path(__file__).parent.parent / "skills"
EVALS_DIR = Path(__file__).parent / "evals" / "skills"

REQUIRED_FRONTMATTER = ["name", "description"]
ALLOWED_EFFORT = {"low", "medium", "high", "xhigh", "max"}
RESERVED_NAMES = {"anthropic", "claude"}
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SOFT_LINE_LIMIT = 300
HARD_LINE_LIMIT = 500
BASELINE_FILE = "grandfathered-skills.yaml"
REQUIRED_EVAL_CATEGORIES = {"normal", "indirect-trigger"}
EDGE_EVAL_CATEGORIES = {"edge", "safety", "failure", "non-trigger", "misuse"}
HIGH_RISK_EVAL_CATEGORIES = {"safety", "misuse"}


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


def load_yaml_file(path: Path) -> tuple[dict, str | None]:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as e:
        return {}, f"invalid YAML: {e}"
    if not isinstance(data, dict):
        return {}, "YAML root must be a mapping"
    return data, None


def validate_grandfathering_baseline(skills_root: Path, evals_root: Path) -> tuple[ValidationResult, set[str]]:
    result = ValidationResult()
    baseline_path = evals_root / BASELINE_FILE
    grandfathered: set[str] = set()

    if not baseline_path.exists():
        result.error("skillsmith-policy", f"{baseline_path} not found")
        return result, grandfathered

    data, yaml_error = load_yaml_file(baseline_path)
    if yaml_error:
        result.error("skillsmith-policy", f"{BASELINE_FILE} {yaml_error}")
        return result, grandfathered

    if data.get("version") != 1:
        result.error("skillsmith-policy", f"{BASELINE_FILE} version must be 1")

    for field in ("created_for_change", "source", "grandfathered_skills"):
        if field not in data:
            result.error("skillsmith-policy", f"{BASELINE_FILE} missing required field: '{field}'")

    entries = data.get("grandfathered_skills", [])
    if not isinstance(entries, list):
        result.error("skillsmith-policy", f"{BASELINE_FILE} grandfathered_skills must be a list")
        return result, grandfathered

    valid_entries: list[str] = []
    for index, entry in enumerate(entries):
        if not isinstance(entry, str):
            result.error("skillsmith-policy", f"{BASELINE_FILE} grandfathered_skills[{index}] must be a string")
            continue
        valid_entries.append(entry)

    if valid_entries != sorted(valid_entries):
        result.error("skillsmith-policy", f"{BASELINE_FILE} grandfathered_skills must be sorted lexicographically")

    for entry in valid_entries:
        if "/" in entry or "\\" in entry or entry.startswith("."):
            result.error("skillsmith-policy", f"{BASELINE_FILE} entries must be bare skill directory names: '{entry}'")
            continue
        grandfathered.add(entry)

    if len(grandfathered) != len(valid_entries):
        result.error("skillsmith-policy", f"{BASELINE_FILE} contains duplicate grandfathered skill names")

    existing_skills = {path.name for path in skills_root.iterdir() if path.is_dir()} if skills_root.exists() else set()
    for skill_name in sorted(grandfathered - existing_skills):
        result.error("skillsmith-policy", f"{BASELINE_FILE} lists '{skill_name}', but skills/{skill_name}/ does not exist")

    return result, grandfathered


def validate_cases_file(skill_name: str, cases_path: Path) -> ValidationResult:
    result = ValidationResult()
    data, yaml_error = load_yaml_file(cases_path)
    label = f"tests/evals/skills/{skill_name}/cases.yaml"

    if yaml_error:
        result.error("skillsmith-policy", f"{label} {yaml_error}")
        return result

    if data.get("version") != 1:
        result.error("skillsmith-policy", f"{label} version must be 1")

    scenarios = data.get("scenarios")
    if not isinstance(scenarios, list) or not scenarios:
        result.error("skillsmith-policy", f"{label} scenarios must be a non-empty list")
        return result

    categories: set[str] = set()
    for index, scenario in enumerate(scenarios, start=1):
        if not isinstance(scenario, dict):
            result.error("skillsmith-policy", f"{label} scenario {index} must be a mapping")
            continue

        scenario_id = scenario.get("id") or f"#{index}"
        category = scenario.get("category")
        if isinstance(category, str):
            categories.add(category)
        else:
            result.error("skillsmith-policy", f"{label} scenario {scenario_id} missing category")

        if not scenario.get("prompt") and not scenario.get("situation"):
            result.error("skillsmith-policy", f"{label} scenario {scenario_id} needs prompt or situation")

        expected_behavior = scenario.get("expected_behavior")
        if not isinstance(expected_behavior, str) or not expected_behavior.strip():
            result.error("skillsmith-policy", f"{label} scenario {scenario_id} needs expected_behavior")

    missing = sorted(REQUIRED_EVAL_CATEGORIES - categories)
    for category in missing:
        result.error("skillsmith-policy", f"{label} missing required eval category: {category}")

    if categories.isdisjoint(EDGE_EVAL_CATEGORIES):
        result.error("skillsmith-policy", f"{label} needs one edge, safety, failure, non-trigger, or misuse scenario")

    if data.get("high_risk") is True:
        safety_notes = data.get("safety_notes")
        if not isinstance(safety_notes, str) or not safety_notes.strip():
            result.error("skillsmith-policy", f"{label} high_risk fixtures need safety_notes")
        if categories.isdisjoint(HIGH_RISK_EVAL_CATEGORIES):
            result.error("skillsmith-policy", f"{label} high_risk fixtures need a safety or misuse eval scenario")

    return result


def validate_eval_fixtures(skills_root: Path = SKILLS_DIR, evals_root: Path = EVALS_DIR) -> ValidationResult:
    result = ValidationResult()
    baseline_result, grandfathered = validate_grandfathering_baseline(skills_root, evals_root)
    result.errors.extend(baseline_result.errors)
    result.warnings.extend(baseline_result.warnings)

    if not skills_root.exists():
        result.error("compatibility", f"{skills_root} not found")
        return result

    grandfathered_without_cases = []
    skill_names = sorted(path.name for path in skills_root.iterdir() if path.is_dir())
    for skill_name in skill_names:
        cases_path = evals_root / skill_name / "cases.yaml"
        if not cases_path.exists():
            if skill_name in grandfathered:
                grandfathered_without_cases.append(skill_name)
            else:
                result.error("skillsmith-policy", f"skills/{skill_name} is not grandfathered and lacks tests/evals/skills/{skill_name}/cases.yaml")
            continue

        cases_result = validate_cases_file(skill_name, cases_path)
        result.errors.extend(cases_result.errors)
        result.warnings.extend(cases_result.warnings)

    if grandfathered_without_cases:
        result.warn(
            "reviewer-heuristic",
            "grandfathered skills without eval fixtures: " + ", ".join(grandfathered_without_cases),
        )

    return result


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

    eval_result = validate_eval_fixtures(SKILLS_DIR, EVALS_DIR)
    errors.extend(f"  ERROR  evals: {msg}" for msg in eval_result.errors)
    warnings.extend(f"  WARN   evals: {msg}" for msg in eval_result.warnings)

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
