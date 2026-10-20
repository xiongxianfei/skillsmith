#!/usr/bin/env python3
"""Export researched attractions to sourced GeoJSON and Google My Maps CSV.

Usage: python export_pins.py inventory.csv pins.geojson [legacy_unlocated.csv] [--bbox minlon,minlat,maxlon,maxlat]
Writes attractions_mymaps.csv and attractions_needs_location_review.csv beside pins.geojson.
No geocoding, web requests, tile servers, routes, or API keys. Python stdlib only.
"""
import argparse
import csv
import json
import math
from datetime import date
from pathlib import Path
from urllib.parse import quote, urlparse

MAX_MYMAPS_ROWS = 2000
MYMAPS_FIELDS = [
    'Place ID', 'Name', 'City', 'Country', 'Latitude', 'Longitude', 'Primary Category',
    'Attraction Score', 'Priority Tier', 'Geographic Area', 'Secondary Tags',
    'Attraction ID', 'Research Status', 'Location Status', 'Coordinate Precision',
    'Coordinate Source', 'Location Verified At', 'Research Source', 'Google Maps Search',
]
REVIEW_FIELDS = ['Record Type', 'Research ID', 'Place ID', 'Name', 'Reason', 'Follow-up']
REQUIRED = {
    'attraction_id', 'place_id', 'city', 'country', 'name', 'primary_category',
    'latitude', 'longitude', 'location_status', 'location_source_url', 'location_verified_at',
}


def first_source(text):
    return (text or '').split(';')[0].strip()


def safe_text(value):
    """Avoid spreadsheet formula execution in untrusted descriptive fields."""
    value = str(value or '')
    return "'" + value if value.lstrip(' \t\n').startswith(('=', '+', '-', '@', '\t', '\r')) else value


def verify_source(raw_url, raw_date, context):
    uri = first_source(raw_url)
    if urlparse(uri).scheme not in ('https', 'http') or not urlparse(uri).netloc:
        raise ValueError(f'{context}: location source URL required')
    try:
        date.fromisoformat((raw_date or '').strip())
    except ValueError as exc:
        raise ValueError(f'{context}: location verified date must be YYYY-MM-DD') from exc
    return uri


def coords(row, context):
    try:
        lat, lon = float(row['latitude']), float(row['longitude'])
    except (ValueError, TypeError) as exc:
        raise ValueError(f'{context}: verified latitude/longitude must be numeric') from exc
    if not (math.isfinite(lat) and math.isfinite(lon) and -90 <= lat <= 90 and -180 <= lon <= 180):
        raise ValueError(f'{context}: invalid latitude/longitude range')
    if abs(lat) < 1e-12 and abs(lon) < 1e-12:
        raise ValueError(f'{context}: null-island (0,0) is not accepted without separate evidence')
    return lat, lon


def parse_bbox(raw):
    if raw is None:
        return None
    try:
        a, b, c, d = map(float, raw.split(','))
    except ValueError as exc:
        raise ValueError('bbox must be minlon,minlat,maxlon,maxlat') from exc
    if not (-180 <= a < c <= 180 and -90 <= b < d <= 90):
        raise ValueError('invalid bbox extents')
    return a, b, c, d


def write_csv(path, columns, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=columns, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(data)


def export(input_csv, output_geojson, legacy_review=None, bbox=None):
    bbox = parse_bbox(bbox)
    with Path(input_csv).open(newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        missing = REQUIRED - set(reader.fieldnames or [])
        if missing:
            raise ValueError('Missing required columns: ' + ', '.join(sorted(missing)))
        source_rows = list(reader)

    ids = set()
    places = {}
    review = []

    def withhold(row, reason, followup):
        review.append({
            'Record Type': 'Attraction', 'Research ID': row['attraction_id'],
            'Place ID': row['place_id'], 'Name': row['name'],
            'Reason': reason, 'Follow-up': followup,
        })

    for line, row in enumerate(source_rows, 2):
        attr_id = (row['attraction_id'] or '').strip()
        pid = (row['place_id'] or '').strip()
        name = (row['name'] or '').strip()
        if not attr_id or attr_id in ids:
            raise ValueError(f'Row {line}: blank/duplicate attraction_id {attr_id!r}')
        ids.add(attr_id)
        if not pid:
            withhold(row, 'missing_place_id', 'Assign a stable physical place ID.')
            continue
        status = (row['location_status'] or '').strip()
        if status != 'verified':
            withhold(row, 'location_' + (status or 'unlocated'), 'Check the site identity, coordinate precision and source; keep the research entry.')
            continue
        context = f'Row {line} ({name})'
        lat, lon = coords(row, context)
        location_url = verify_source(row['location_source_url'], row['location_verified_at'], context)
        if bbox and not (bbox[0] <= lon <= bbox[2] and bbox[1] <= lat <= bbox[3]):
            withhold(row, 'outside_requested_bbox', 'Confirm intended city or regional scope and corrected coordinates.')
            continue
        if pid in places:
            if places[pid]['latlon'] != (lat, lon):
                raise ValueError(f'{context}: conflicting coordinates for shared place_id {pid}')
            # Distinct attraction experiences can share one pin; retain each research ID in GeoJSON.
            places[pid]['ids'].append(attr_id)
            continue
        places[pid] = {'row': row, 'latlon': (lat, lon), 'ids': [attr_id], 'source': location_url}

    if len(places) > MAX_MYMAPS_ROWS:
        raise ValueError(f'{len(places)} map pins exceed Google My Maps 2,000-row import limit')
    features, csv_rows = [], []
    for pid, p in places.items():
        row, (lat, lon) = p['row'], p['latlon']
        search = f"{row['name']}, {row['city']}, {row['country']}"
        url = 'https://www.google.com/maps/search/?api=1&query=' + quote(search)
        ids_joined = ';'.join(p['ids'])
        props = {
            'place_id': pid, 'name': row['name'], 'primary_category': row['primary_category'],
            'attraction_ids': p['ids'], 'attraction_score': row.get('weighted_score', ''),
            'priority_tier': row.get('priority_tier', ''), 'location_source_url': p['source'],
            'location_verified_at': row['location_verified_at'],
        }
        features.append({'type': 'Feature', 'id': pid,
                         'geometry': {'type': 'Point', 'coordinates': [lon, lat]},
                         'properties': props})
        csv_rows.append({
            'Place ID': safe_text(pid), 'Name': safe_text(row['name']),
            'City': safe_text(row['city']), 'Country': safe_text(row['country']),
            'Latitude': lat, 'Longitude': lon,
            'Primary Category': safe_text(row['primary_category']),
            'Attraction Score': row.get('weighted_score', ''),
            'Priority Tier': safe_text(row.get('priority_tier', '')),
            'Geographic Area': safe_text(row.get('geographic_area', '')),
            'Secondary Tags': safe_text(row.get('secondary_tags', '')),
            'Attraction ID': safe_text(ids_joined),
            'Research Status': safe_text(row.get('research_status', '')),
            'Location Status': 'verified',
            'Coordinate Precision': safe_text(row.get('coordinate_precision', 'site_center_not_entrance_confirmed')),
            'Coordinate Source': p['source'],
            'Location Verified At': row['location_verified_at'],
            'Research Source': first_source(row.get('source_urls', '')),
            'Google Maps Search': url,
        })

    target = Path(output_geojson)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps({'type': 'FeatureCollection', 'features': features}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    write_csv(target.with_name('attractions_mymaps.csv'), MYMAPS_FIELDS, csv_rows)
    write_csv(target.with_name('attractions_needs_location_review.csv'), REVIEW_FIELDS, review)
    # Historical CLI compatibility; old callers expect place_id/name/reason.
    old = Path(legacy_review) if legacy_review else target.with_name('unlocated_places.csv')
    legacy = [{'place_id': r['Place ID'], 'name': r['Name'], 'reason': r['Reason']} for r in review]
    write_csv(old, ['place_id', 'name', 'reason'], legacy)
    return len(places), len(review)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('inventory_csv')
    parser.add_argument('pins_geojson')
    parser.add_argument('legacy_unlocated_csv', nargs='?')
    parser.add_argument('--bbox', default=None, help='Optional geographic bounds minlon,minlat,maxlon,maxlat')
    args = parser.parse_args()
    try:
        mapped, withheld = export(args.inventory_csv, args.pins_geojson, args.legacy_unlocated_csv, args.bbox)
    except ValueError as exc:
        parser.exit(2, f'Error: {exc}\n')
    print(f'Exported {mapped} verified attraction pin(s) and Google My Maps rows; withheld {withheld} research entry/entries')


if __name__ == '__main__':
    main()
