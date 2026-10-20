"""Focused stdlib regression tests for portable attraction and dining map exports.

Run: python -m unittest discover -s tests -p 'test_research_mymaps.py' -v
These tests are independent of live geocoders and map providers.
"""
import csv
import importlib.util
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

ROOT = Path(__file__).resolve().parents[1]

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

attractions = load('attractions_export', ROOT / 'skills/city-attraction-research/scripts/export_pins.py')
dining = load('dining_export', ROOT / 'skills/local-food-and-dining-research/scripts/export_venues_mymaps.py')
combined = load('combined_export', ROOT / 'skills/city-attraction-research/scripts/combine_mymaps.py')

A_FIELDS = 'attraction_id,place_id,city,country,name,primary_category,latitude,longitude,location_status,location_source_url,location_verified_at,weighted_score,priority_tier,geographic_area,secondary_tags,source_urls,research_status'.split(',')
V_FIELDS = 'venue_id,place_id,city,country,name,address,map_address,latitude,longitude,location_status,location_source_url,location_verified_at,source_urls,verified_date,verification_status,notes'.split(',')
F_FIELDS = 'food_id,name'.split(',')
M_FIELDS = 'match_id,venue_id,food_id,menu_status,venue_suitability_score,source_urls'.split(',')

def write(path, fields, rows):
    with Path(path).open('w', encoding='utf-8-sig',newline='') as f:
        w = csv.DictWriter(f,fieldnames=fields)
        w.writeheader();w.writerows(rows)

def read(path):
    with Path(path).open(encoding='utf-8-sig',newline='') as f:
        return list(csv.DictReader(f))

def a(**kwargs):
    base = dict(attraction_id='A1',place_id='P1',city='Samarkand',country='Uzbekistan',name='Registan',primary_category='Historical Sites and Architectural Landmarks',latitude='39.655',longitude='66.975',location_status='verified',location_source_url='https://example.com/location',location_verified_at='2026-10-19',weighted_score='98',priority_tier='Must-Visit Candidate',geographic_area='Center',secondary_tags='architecture',source_urls='https://example.com/research',research_status='evaluated')
    base.update(kwargs)
    return base

def v(**kwargs):
    base = dict(venue_id='V1',place_id='P2',city='Samarkand',country='Uzbekistan',name='Plov house',address='Ibn Sino Street 12',map_address='Ibn Sino Street 12',latitude='',longitude='',location_status='unlocated',location_source_url='',location_verified_at='',source_urls='https://example.com/venue',verified_date='2026-10-19',verification_status='name_and_specialty_supported',notes='Serving hours need confirmation')
    base.update(kwargs);return base

def m(**kwargs):
    base=dict(match_id='M1',venue_id='V1',food_id='F1',menu_status='plausible_needs_confirmation',venue_suitability_score='94',source_urls='https://example.com/dish')
    base.update(kwargs);return base

class ExportTests(unittest.TestCase):
    def setUp(self):
        self.tmp=TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)
        self.acin=self.root/'attractions.csv'
        self.vcin=self.root/'venues.csv'
        self.fin=self.root/'foods.csv'
        self.mcin=self.root/'matches.csv'
        write(self.acin,A_FIELDS,[a()])
        write(self.vcin,V_FIELDS,[v()])
        write(self.fin,F_FIELDS,[{'food_id':'F1','name':'Samarkand plov'}])
        write(self.mcin,M_FIELDS,[m()])

    def test_attraction_geojson_mymaps_and_no_invented_coordinates(self):
        mapped, withheld=attractions.export(self.acin,self.root/'attractions.geojson')
        self.assertEqual((mapped,withheld),(1,0))
        doc=json.loads((self.root/'attractions.geojson').read_text())
        self.assertEqual(doc['features'][0]['geometry']['coordinates'],[66.975,39.655])
        row=read(self.root/'attractions_mymaps.csv')[0]
        self.assertEqual(row['Primary Category'],'Historical Sites and Architectural Landmarks')
        self.assertEqual(row['Attraction Score'],'98')
        self.assertEqual(row['Place ID'],'P1')

    def test_attraction_unknown_remains_in_review_not_on_map(self):
        write(self.acin,A_FIELDS,[a(),a(attraction_id='A2',place_id='P3',name='Neighborhood walk',latitude='',longitude='',location_status='unlocated',location_source_url='',location_verified_at='')])
        self.assertEqual(attractions.export(self.acin,self.root/'attractions.geojson'),(1,1))
        self.assertEqual(read(self.root/'attractions_needs_location_review.csv')[0]['Research ID'],'A2')

    def test_attraction_duplicate_research_id_rejected(self):
        write(self.acin,A_FIELDS,[a(),a(place_id='P3',name='Other')])
        with self.assertRaisesRegex(ValueError,'duplicate attraction_id'):
            attractions.export(self.acin,self.root/'attractions.geojson')

    def test_attraction_conflicting_shared_place_rejected(self):
        write(self.acin,A_FIELDS,[a(),a(attraction_id='A2',longitude='66.980')])
        with self.assertRaisesRegex(ValueError,'conflicting coordinates'):
            attractions.export(self.acin,self.root/'attractions.geojson')

    def test_attraction_verified_point_requires_source_date(self):
        write(self.acin,A_FIELDS,[a(location_source_url='')])
        with self.assertRaisesRegex(ValueError,'location source URL'):
            attractions.export(self.acin,self.root/'attractions.geojson')

    def test_attraction_bbox_flags_wrong_region(self):
        self.assertEqual(attractions.export(self.acin,self.root/'attractions.geojson',bbox='66,39,67,40'),(1,0))
        self.assertEqual(attractions.export(self.acin,self.root/'attractions.geojson',bbox='56,39,57,40'),(0,1))

    def test_dining_address_based_venue_and_provisional_menu(self):
        mapped,withheld,geos=dining.export(self.vcin,self.fin,self.mcin,self.root)
        self.assertEqual((mapped,withheld,geos),(1,0,0))
        row=read(self.root/'dining_venues_mymaps.csv')[0]
        self.assertIn('Ibn Sino Street 12',row['Map Address'])
        self.assertEqual(row['Food–Venue Match Score'],'94')
        self.assertEqual(row['Recommended Foods'],'Samarkand plov')
        self.assertEqual(row['Menu Verification Status'],'plausible_needs_confirmation')
        self.assertIn('needs_visual_review',row['Geocoding Status'])

    def test_dining_no_score_remains_blank(self):
        write(self.mcin,M_FIELDS,[m(venue_suitability_score='')])
        dining.export(self.vcin,self.fin,self.mcin,self.root)
        self.assertEqual(read(self.root/'dining_venues_mymaps.csv')[0]['Food–Venue Match Score'],'')

    def test_dining_uncertain_branch_is_withheld(self):
        write(self.vcin,V_FIELDS,[v(map_address='',address='Near market / various branches',verification_status='branch_or_menu_needs_confirmation')])
        self.assertEqual(dining.export(self.vcin,self.fin,self.mcin,self.root),(0,1,0))
        self.assertEqual(read(self.root/'dining_needs_location_review.csv')[0]['Reason'],'missing_or_ambiguous_address')

    def test_dining_verified_coordinates_require_provenance(self):
        write(self.vcin,V_FIELDS,[v(location_status='verified',latitude='39.66',longitude='66.98')])
        with self.assertRaisesRegex(ValueError,'verified coordinates require location source'):
            dining.export(self.vcin,self.fin,self.mcin,self.root)

    def test_verified_dining_geojson_keeps_lon_lat(self):
        write(self.vcin,V_FIELDS,[v(location_status='verified',latitude='39.66',longitude='66.98',location_source_url='https://example.com/map',location_verified_at='2026-10-19')])
        self.assertEqual(dining.export(self.vcin,self.fin,self.mcin,self.root),(1,0,1))
        doc=json.loads((self.root/'dining_venues.geojson').read_text())
        self.assertEqual(doc['features'][0]['geometry']['coordinates'],[66.98,39.66])

    def test_combined_merges_shared_place_id_without_double_marker(self):
        attractions.export(self.acin,self.root/'attractions.geojson')
        write(self.vcin,V_FIELDS,[v(place_id='P1',map_address='Ibn Sino Street 12')])
        dining.export(self.vcin,self.fin,self.mcin,self.root)
        total, shared=combined.combine(self.root/'attractions_mymaps.csv',self.root/'dining_venues_mymaps.csv',self.root)
        self.assertEqual((total,shared),(1,1))
        row=read(self.root/'combined_city_mymaps.csv')[0]
        self.assertEqual(row['Roles'],'Attractions; Dining Venues')
        self.assertEqual(row['Attraction Score'],'98')
        self.assertEqual(row['Food–Venue Match Score'],'94')

    def test_combined_unrelated_places_remain_two(self):
        attractions.export(self.acin,self.root/'attractions.geojson')
        dining.export(self.vcin,self.fin,self.mcin,self.root)
        self.assertEqual(combined.combine(self.root/'attractions_mymaps.csv',self.root/'dining_venues_mymaps.csv',self.root),(2,0))

    def test_csv_spreadsheet_formula_injection_guard(self):
        write(self.acin,A_FIELDS,[a(name='=SUM(1,2)')])
        attractions.export(self.acin,self.root/'attractions.geojson')
        self.assertTrue(read(self.root/'attractions_mymaps.csv')[0]['Name'].startswith("'="))

if __name__=='__main__':unittest.main()
