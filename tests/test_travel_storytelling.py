"""Offline consistency tests for the authored storytelling demonstration.

These checks do not prove historical truth, narrative quality or host behavior.
Run: python -m unittest discover -s tests -p 'test_travel_storytelling.py' -v
"""
import json
import re
import unittest
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills' / 'travel-storytelling-guide'
DEMO = SKILL / 'examples' / 'samarkand'


class StorytellingExampleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((DEMO / 'stories.json').read_text(encoding='utf-8'))
        cls.markdown = (DEMO / 'guided_commentary.md').read_text(encoding='utf-8')

    def test_scope_and_existing_subject_ids(self):
        self.assertEqual(self.data['schema_version'], '1.0')
        self.assertEqual(self.data['language'], 'en')
        pairs = {(s['subject_type'], s['subject_id']) for s in self.data['stories']}
        self.assertEqual(pairs, {('attraction', 'SAM-A001'), ('food', 'SAM-F001')})
        self.assertEqual(len(self.data['stories']), 2)
        for story in self.data['stories']:
            self.assertEqual(story['subject_id'], story['research_input']['id_value'])

    def test_ids_and_evidence_references(self):
        sources = self.data['sources']
        source_ids = {s['source_id'] for s in sources}
        self.assertEqual(len(sources), len(source_ids))
        story_ids = {s['story_id'] for s in self.data['stories']}
        self.assertEqual(len(story_ids), len(self.data['stories']))
        for story in self.data['stories']:
            claims = {c['claim_id']: c for c in story['claims']}
            self.assertEqual(len(claims), len(story['claims']))
            for claim in claims.values():
                self.assertIn(claim['kind'], {'documented', 'interpretation', 'tradition', 'disputed'})
                self.assertTrue(claim['source_ids'])
                self.assertTrue(set(claim['source_ids']) <= source_ids)
            for mode in ('pre_trip', 'on_location'):
                self.assertTrue(story[mode]['claim_ids'])
                self.assertTrue(set(story[mode]['claim_ids']) <= set(claims))

    def test_source_provenance_is_explicit(self):
        for source in self.data['sources']:
            uri = urlparse(source['url'])
            self.assertEqual(uri.scheme, 'https')
            self.assertTrue(uri.netloc)
            date.fromisoformat(source['checked_at'])
            self.assertIn(source['access'], {'page_read', 'indexed_excerpt', 'user_supplied'})
            self.assertTrue(source['supports'])
            self.assertIn(source['url'], self.markdown)

    def test_readable_output_preserves_exact_prose(self):
        for story in self.data['stories']:
            self.assertIn(story['story_id'], self.markdown)
            for mode in ('pre_trip', 'on_location'):
                self.assertEqual(self.markdown.count(story[mode]['text']), 1)
            for claim in story['claims']:
                self.assertIn(claim['claim_id'], self.markdown)

    def test_lengths_and_speech_estimates(self):
        for story in self.data['stories']:
            for mode, lower, upper in [('pre_trip', 150, 250), ('on_location', 300, 450)]:
                part = story[mode]
                count = len(re.sub(r'\[[^\]]*\]', '', part['text']).split())
                self.assertEqual(count, part['word_count'])
                self.assertTrue(lower <= count <= upper)
            spoken = story['on_location']
            self.assertEqual(spoken['assumed_words_per_minute'], 130)
            self.assertEqual(spoken['estimated_minutes'], round(spoken['word_count'] / 130, 1))

    def test_spoken_text_has_no_citation_markup_or_urls(self):
        for story in self.data['stories']:
            text = story['on_location']['text']
            self.assertNotIn('https://', text)
            self.assertNotIn('', text)
            for claim in story['claims']:
                self.assertNotIn(claim['claim_id'], text)

    def test_food_not_assigned_an_invented_place_or_venue(self):
        story = next(s for s in self.data['stories'] if s['subject_type'] == 'food')
        self.assertIsNone(story['place_id'])
        self.assertIsNone(story['venue_id'])
        self.assertTrue(story['limitations'])
        self.assertIn('If you choose to taste', story['on_location']['text'])

    def test_skill_local_markdown_links_exist(self):
        for path in (SKILL / 'SKILL.md', SKILL / 'references' / 'storytelling-guidelines.md'):
            text = path.read_text(encoding='utf-8')
            for target in re.findall(r'\]\(([^)]+)\)', text):
                if '://' not in target and not target.startswith('#'):
                    self.assertTrue((path.parent / target.split('#')[0]).exists(), target)


if __name__ == '__main__':
    unittest.main()
