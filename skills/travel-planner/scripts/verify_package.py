#!/usr/bin/env python3
"""Dependency-free structural checks for this portable skill package."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
FRONTMATTER = re.compile(r'^---\n(.*?)\n---\n', re.S)
LINK = re.compile(r'(?<!!)\[[^\]]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)')


def main():
    errors = []
    text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    frontmatter = FRONTMATTER.match(text)
    if frontmatter is None:
        errors.append("missing YAML frontmatter")
    else:
        fields = dict(re.findall(r'^([\w-]+):\s*(.+)$', frontmatter.group(1), re.M))
        name = fields.get("name", "").strip("\"'")
        description = fields.get("description", "").strip("\"'")
        if name != ROOT.name or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or len(name) > 64:
            errors.append("frontmatter name must match the skill directory")
        if not 1 <= len(description) <= 1024:
            errors.append("frontmatter description missing or too long")
    for file in ROOT.rglob("*.md"):
        for target in LINK.findall(file.read_text(encoding="utf-8")):
            if target.startswith(("https://", "http://", "mailto:", "#", "sandbox:")):
                continue
            relative = target.split("#", 1)[0]
            if relative and not (file.parent / relative).resolve().is_file():
                errors.append(f"{file.relative_to(ROOT)}: missing link target {target}")
    required = [
        "README.md", "SOP.md", "references/sop.md", "references/scoring.md",
        "references/data-contracts.md", "references/quality-gates.md",
        "references/research-and-tools.md", "assets/trip-brief.yaml",
        "assets/flight-comparison.csv", "assets/hotel-comparison.csv",
        "assets/itinerary.md", "assets/poi-checklist.csv",
        "scripts/evaluate_itineraries.py", "scripts/test_evaluate.py",
        "examples/samarkand-input.json", "examples/samarkand-case-study.md",
        "examples/samarkand-evaluation.json"
    ]
    for path in required:
        if not (ROOT / path).is_file():
            errors.append(f"missing required skill resource: {path}")
    if errors:
        print("PACKAGE CHECK FAILED")
        for error in errors:
            print(" -", error)
        return 1
    print("PACKAGE CHECK PASSED: metadata, expected files and Markdown links")
    return 0


if __name__ == "__main__":
    sys.exit(main())
