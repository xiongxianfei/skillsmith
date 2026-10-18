"""Deterministic contract checks for the bilingual vocabulary-mastery skill."""

import re
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "vocabulary-mastery" / "SKILL.md"

DOMAINS = (
    "Phonetics",
    "Phonology",
    "Morphology",
    "Lexicon",
    "Syntax",
    "Semantics",
    "Pragmatics",
    "Discourse",
    "Information Structure",
    "Prosody",
)


class VocabularyMasteryContractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = SKILL.read_text(encoding="utf-8")
        cls.template = cls.source.split("## Output Format", 1)[1]

    def test_skill_instructions_are_english_only(self):
        # Do not rely on Chinese characters inside the prompt to trigger
        # Chinese-language generation. The runtime output may use Chinese.
        non_english_scripts = re.compile(
            r"[\u0400-\u04ff\u3040-\u30ff\u3400-\u9fff\uac00-\ud7af]"
        )
        self.assertIsNone(non_english_scripts.search(self.source))

    def test_english_version_precedes_chinese_version(self):
        en = self.template.index("**Part 1: English Reference**")
        zh = self.template.index("**Part 2: Simplified Chinese Reference**")
        self.assertLess(en, zh)

    def test_two_full_ten_dimension_templates(self):
        en, zh = self.template.split("**Part 2: Simplified Chinese Reference**", 1)
        for n, domain in enumerate(DOMAINS, start=1):
            with self.subTest(domain=domain):
                self.assertIn(f"**{n}. {domain}**", en)
                self.assertIn(f"**{n}. <Chinese heading for {domain}>**", zh)

        for heading in ("Word Overview", "Knowledge Connections", "Recall Prompts", "Answers"):
            with self.subTest(section=heading):
                self.assertIn(f"**{heading}**", en)
                self.assertIn(f"**<Chinese heading for {heading}>**", zh)

        self.assertIn("same English illustration", zh)
        self.assertIn("same English example", zh)

    def test_both_parts_have_three_prompts_and_answers(self):
        en, zh = self.template.split("**Part 2: Simplified Chinese Reference**", 1)
        for segment in (en, zh):
            self.assertIn("question one", segment)
            self.assertIn("question two", segment)
            self.assertIn("question three", segment)
            self.assertIn("answer one", segment)
            self.assertIn("answer two", segment)
            self.assertIn("answer three", segment)

    def test_safety_and_complete_two_version_behavior(self):
        self.assertIn("$ARGUMENTS", self.source)
        self.assertIn("Always output both full versions", self.source)
        self.assertIn("self-contained", self.source)
        self.assertIn("Do not fabricate", self.source)
        self.assertIn("without actual audio", self.source.lower())


if __name__ == "__main__":
    unittest.main()
