"""Focused contract tests for the portable itinerary builder.

Run from any working directory: python -m unittest discover -s tests -v
"""
import copy
import importlib.util
import json
import pathlib
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('build_trip_materials', ROOT / 'scripts' / 'build_trip_materials.py')
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)
SAMPLE = json.loads((ROOT / 'assets' / 'samarkand_itinerary_example.json').read_text(encoding='utf-8'))


class TripMaterialsTest(unittest.TestCase):
    def sample(self):
        return copy.deepcopy(SAMPLE)

    def test_unlocated_places_do_not_become_pins_or_routes(self):
        with tempfile.TemporaryDirectory() as td:
            counts = module.render(self.sample(), pathlib.Path(td))
            self.assertEqual(counts, (2, 0, 2, 0))
            features = json.loads((pathlib.Path(td) / 'selected_places.geojson').read_text())['features']
            self.assertEqual(features, [])
            self.assertIn('location not verified', (pathlib.Path(td) / 'navigation.md').read_text())

    def test_verified_coordinate_maps_once(self):
        trip = self.sample()
        for index, place in enumerate(trip['places']):
            place.update(latitude=40.0 + index, longitude=65.0 + index,
                         location_status='verified', location_source_url='https://example.org/verified', location_verified_at='2026-11-01')
        with tempfile.TemporaryDirectory() as td:
            self.assertEqual(module.render(trip, pathlib.Path(td)), (2, 2, 0, 0))
            geo = json.loads((pathlib.Path(td) / 'selected_places.geojson').read_text())
            self.assertEqual(geo['features'][0]['geometry']['coordinates'], [65.0, 40.0])
            self.assertEqual(len(geo['features']), 2)
            self.assertIn('api=1&destination=', (pathlib.Path(td) / 'navigation.md').read_text())

    def test_rejects_overlapping_blocks(self):
        trip = self.sample()
        trip['days'][0]['blocks'][1]['start'] = '10:00'
        with self.assertRaisesRegex(ValueError, 'overlapping'):
            module.verify(trip)

    def test_rejects_unsourced_route_metrics(self):
        trip = self.sample()
        trip['legs'][0]['duration_minutes'] = 10
        with self.assertRaisesRegex(ValueError, 'require source_url'):
            module.verify(trip)

    def test_rejects_journey_longer_than_gap(self):
        trip = self.sample()
        trip['legs'][0].update(duration_minutes=70, source_url='https://example.org/routing', verified_at='2026-11-01')
        with self.assertRaisesRegex(ValueError, 'exceeds time'):
            module.verify(trip)

    def test_sourced_geometry_is_retained_not_invented(self):
        trip = self.sample()
        trip['legs'][0].update(duration_minutes=35, source_url='https://example.org/routing',
            verified_at='2026-11-01', route_geometry={'type':'LineString','coordinates':[[65,40],[65.01,40.01]]})
        with tempfile.TemporaryDirectory() as td:
            self.assertEqual(module.render(trip,pathlib.Path(td)), (2,0,2,1))
            geom = json.loads((pathlib.Path(td)/'verified_routes.geojson').read_text())['features'][0]['geometry']
            self.assertEqual(geom,trip['legs'][0]['route_geometry'])

    def test_location_marked_verified_needs_source(self):
        trip = self.sample()
        trip['places'][0].update(location_status='verified',latitude=39.0,longitude=67.0)
        with self.assertRaisesRegex(ValueError, 'requires coordinates and sourced'):
            module.verify(trip)

    def test_no_unsupported_state_claims(self):
        trip = self.sample()
        trip['days'][0]['blocks'][0]['booking_status']='booked'
        with self.assertRaisesRegex(ValueError,'unsupported booking_status'):
            module.verify(trip)


if __name__=='__main__':
    unittest.main()
