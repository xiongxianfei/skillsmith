"""Focused three-file delivery tests. Run from repo root:
python -m unittest discover -s tests -p 'test_minimal_research_outputs.py' -v
Uses stdlib only; no network or mapping service.
"""
import csv
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ATTRACTIONS = ROOT / 'skills/city-attraction-research/scripts/generate_research.py'
FOOD = ROOT / 'skills/local-food-and-dining-research/scripts/generate_research.py'


def write_csv(path, rows):
    fields = list(rows[0])
    with path.open('w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fields)
        writer.writeheader()
        writer.writerows(rows)


def read_csv(path):
    with path.open(newline='', encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))


def attraction(**changes):
    row = dict(attraction_id='A1', place_id='P1', city='Samarkand', country='Uzbekistan',
               name='Registan Square', primary_category='Historical Sites and Architectural Landmarks',
               city_distinctiveness='5', traveler_relevance='5', experience_quality='5',
               historical_cultural_value='5', practical_value='4', weighted_score='',
               priority_tier='', secondary_tags='tilework;Silk Road', source_urls='https://example.org/history',
               estimated_minutes='90', latitude='39.65', longitude='66.98', location_status='verified',
               location_source_url='https://example.org/coords', location_verified_at='2026-10-21',
               research_status='evaluated')
    row.update(changes)
    return row


def food(**changes):
    row = dict(food_id='F1', name='Samarkand plov', primary_category='Rice, Grains, and Substantial Staples',
               local_distinctiveness='5', cultural_significance='5', culinary_distinctiveness='5',
               general_traveler_relevance='5', availability='5', food_score='', priority_tier='',
               source_urls='https://example.org/food', geographic_identity='city_specific_style',
               secondary_tags='rice;regional', aliases='osh', variants='')
    row.update(changes)
    return row


def venue(**changes):
    row = dict(venue_id='V1', place_id='P2', city='Samarkand', country='Uzbekistan',
               name='Plov House', address='Ibn Sino Street 12', map_address='Ibn Sino Street 12',
               source_urls='https://example.org/restaurant', verified_date='2026-10-21',
               location_status='unlocated', verification_status='name_and_specialty_supported',
               latitude='', longitude='', location_source_url='', location_verified_at='')
    row.update(changes)
    return row


def match(**changes):
    row = dict(match_id='M1', food_id='F1', venue_id='V1', menu_status='plausible_needs_confirmation',
               signature_food_match='5', preparation_experience='5', cultural_character='5',
               practicality='5', evidence_confidence='4', venue_suitability_score='',
               source_urls='https://example.org/restaurant-menu')
    row.update(changes)
    return row


class MinimalOutputs(unittest.TestCase):
    def setUp(self):
        d = tempfile.TemporaryDirectory()
        self.addCleanup(d.cleanup)
        self.root = Path(d.name)
        self.a_csv = self.root / 'attractions.csv'
        self.f_csv = self.root / 'foods.csv'
        self.v_csv = self.root / 'venues.csv'
        self.m_csv = self.root / 'matches.csv'
        write_csv(self.a_csv, [attraction()])
        write_csv(self.f_csv, [food()])
        write_csv(self.v_csv, [venue()])
        write_csv(self.m_csv, [match()])

    def run_attr(self, *extra):
        return subprocess.run([sys.executable, str(ATTRACTIONS), str(self.a_csv),
                               str(self.root / 'attraction_out'), *extra], capture_output=True, text=True)

    def run_food(self, *extra):
        return subprocess.run([sys.executable, str(FOOD), str(self.f_csv), str(self.v_csv),
                               str(self.m_csv), str(self.root / 'food_out'), *extra],
                              capture_output=True, text=True)

    def test_attraction_three_files_scores_and_map(self):
        write_csv(self.a_csv, [attraction(), attraction(attraction_id='A2',place_id='P3',
                      name='Mahalla walk',city_distinctiveness='',traveler_relevance='',
                      experience_quality='',historical_cultural_value='',practical_value='',
                      latitude='',longitude='',location_status='unlocated',location_source_url='',
                      location_verified_at='')])
        done = self.run_attr()
        self.assertEqual(done.returncode, 0, done.stderr)
        out = self.root / 'attraction_out'
        self.assertEqual({p.name for p in out.iterdir()},
                         {'attractions.json','attractions_checklist.csv','attractions_mymaps.csv'})
        doc = json.loads((out / 'attractions.json').read_text())
        self.assertEqual(len(doc['attractions']),2)
        self.assertEqual(doc['attractions'][0]['weighted_score'],98)
        self.assertIsNone(doc['attractions'][1]['weighted_score'])
        self.assertEqual(doc['mapping']['mapped'],1)
        self.assertEqual(doc['mapping']['withheld'],1)
        self.assertEqual(read_csv(out/'attractions_checklist.csv')[1]['rank'],'')
        self.assertEqual(read_csv(out/'attractions_mymaps.csv')[0]['Place ID'],'P1')

    def test_attraction_rejects_partial_ratings(self):
        write_csv(self.a_csv,[attraction(practical_value='')])
        result=self.run_attr()
        self.assertNotEqual(result.returncode,0)
        self.assertFalse((self.root/'attraction_out'/'attractions.json').exists())

    def test_attraction_rejects_stale_score(self):
        write_csv(self.a_csv,[attraction(weighted_score='99')])
        result=self.run_attr()
        self.assertNotEqual(result.returncode,0)
        self.assertIn('does not match',result.stderr)

    def test_attraction_output_safely_quotes_spreadsheet_formula(self):
        write_csv(self.a_csv,[attraction(name='=SUM(1,2)')])
        result=self.run_attr()
        self.assertEqual(result.returncode,0,result.stderr)
        name=read_csv(self.root/'attraction_out'/'attractions_checklist.csv')[0]['name']
        self.assertTrue(name.startswith("'="))

    def test_food_three_files_and_provisional_address(self):
        write_csv(self.f_csv,[food(),food(food_id='F2',name='Non',primary_category='Breads and Baked Pastries',
                      local_distinctiveness='',cultural_significance='',culinary_distinctiveness='',
                      general_traveler_relevance='',availability='')])
        result=self.run_food()
        self.assertEqual(result.returncode,0,result.stderr)
        out=self.root/'food_out'
        self.assertEqual({p.name for p in out.iterdir()},
                         {'food_research.json','foods_checklist.csv','dining_venues_mymaps.csv'})
        doc=json.loads((out/'food_research.json').read_text())
        self.assertEqual(doc['foods'][0]['food_score'],100)
        self.assertIsNone(doc['foods'][1]['food_score'])
        self.assertEqual(doc['food_venue_matches'][0]['venue_suitability_score'],98)
        self.assertEqual(doc['mapping']['mapped'],1)
        row=read_csv(out/'dining_venues_mymaps.csv')[0]
        self.assertEqual(row['Menu Verification Status'],'plausible_needs_confirmation')
        self.assertEqual(row['Location Status'],'address_based_provisional')
        self.assertEqual(row['Food–Venue Match Score'],'98')
        self.assertEqual(read_csv(out/'foods_checklist.csv')[1]['rank'],'')

    def test_food_no_score_remains_blank(self):
        write_csv(self.m_csv,[match(signature_food_match='',preparation_experience='',
                  cultural_character='',practicality='',evidence_confidence='')])
        result=self.run_food()
        self.assertEqual(result.returncode,0,result.stderr)
        row=read_csv(self.root/'food_out'/'dining_venues_mymaps.csv')[0]
        self.assertEqual(row['Food–Venue Match Score'],'')

    def test_food_rejects_broken_relation(self):
        write_csv(self.m_csv,[match(venue_id='no-such-venue')])
        result=self.run_food()
        self.assertNotEqual(result.returncode,0)
        self.assertIn('missing referenced',result.stderr)

    def test_food_rejects_unsupported_scored_match(self):
        write_csv(self.m_csv,[match(menu_status='not_yet_researched')])
        result=self.run_food()
        self.assertNotEqual(result.returncode,0)

    def test_food_rejects_unsupported_source(self):
        write_csv(self.m_csv,[match(source_urls='')])
        result=self.run_food()
        self.assertNotEqual(result.returncode,0)

    def test_existing_files_require_overwrite_flag(self):
        self.assertEqual(self.run_attr().returncode,0)
        self.assertNotEqual(self.run_attr().returncode,0)
        self.assertEqual(self.run_attr('--overwrite').returncode,0)
        self.assertEqual(self.run_food().returncode,0)
        self.assertNotEqual(self.run_food().returncode,0)
        self.assertEqual(self.run_food('--overwrite').returncode,0)


if __name__=='__main__': unittest.main()
