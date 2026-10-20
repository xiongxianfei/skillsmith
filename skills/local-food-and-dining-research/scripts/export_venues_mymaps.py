#!/usr/bin/env python3
"""Export researched dining venues and supported food matches to Google My Maps.

Usage: python export_venues_mymaps.py venues.csv foods.csv matches.csv OUTPUT_DIR
No geocoding, web traffic, restaurant availability checks, or external dependencies.
Rows with sourced addresses remain PROVISIONAL until user checks pins in My Maps.
"""
import argparse
import csv
import json
import math
import re
from datetime import date
from pathlib import Path
from urllib.parse import quote, urlparse

MAX_MYMAPS_ROWS = 2000
MYMAPS_FIELDS = [
    'Place ID', 'Venue ID', 'Name', 'City', 'Country', 'Map Address', 'Primary Category',
    'Recommended Foods', 'Food–Venue Match Score', 'Menu Verification Status',
    'Geocoding Status', 'Location Status', 'Latitude', 'Longitude',
    'Location Source', 'Source Checked At', 'Dish Evidence',
    'Visitor Note', 'Google Maps Search',
]
REVIEW_FIELDS = ['Record Type', 'Research ID', 'Place ID', 'Name', 'Reason', 'Follow-up']


def load_csv(path, required):
    with Path(path).open(newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        missing = set(required) - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f'{path}: missing columns {sorted(missing)}')
        return list(reader)


def first_source(value):
    return (value or '').split(';')[0].strip()


def safe_text(value):
    text = str(value or '')
    return "'" + text if text.lstrip(' \n\t').startswith(('=', '+', '-', '@', '\t', '\r')) else text


def valid_source_date(source, when):
    parsed = urlparse(first_source(source))
    if parsed.scheme not in ('http', 'https') or not parsed.netloc:
        return False
    try:
        date.fromisoformat((when or '').strip())
    except ValueError:
        return False
    return True


def latlon(row, context):
    try:
        lat, lon = float(row.get('latitude', '') or ''), float(row.get('longitude', '') or '')
    except ValueError as exc:
        raise ValueError(f'{context}: verified coordinates must be numeric') from exc
    if not (math.isfinite(lat) and math.isfinite(lon) and -90 <= lat <= 90 and -180 <= lon <= 180):
        raise ValueError(f'{context}: invalid coordinate range')
    if lat == 0 and lon == 0:
        raise ValueError(f'{context}: null-island (0,0) cannot represent a verified venue without review')
    return lat, lon


def address_is_clean(address):
    """Conservative fallback: not a geocoder, only a basic ambiguity screen."""
    a = (address or '').strip()
    if len(a) < 9 or not re.search(r'\d', a):
        return False
    if any(x in a.lower() for x in ('(', ')', 'uncertain', 'unknown', 'possibly', 'other sources', ' / ', 'near ', ' area', 'approx')):
        return False
    return True


def write_csv(path, fields, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', newline='', encoding='utf-8-sig') as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        w.writeheader()
        w.writerows(rows)


def export(venues_csv, foods_csv, matches_csv, outdir):
    venues = load_csv(venues_csv, ['venue_id', 'name', 'city', 'country', 'address', 'source_urls', 'verified_date'])
    foods = load_csv(foods_csv, ['food_id', 'name'])
    matches = load_csv(matches_csv, ['match_id', 'venue_id', 'food_id', 'menu_status', 'venue_suitability_score'])
    foodnames = {}
    for row in foods:
        f_id = row['food_id'].strip()
        if not f_id or f_id in foodnames:
            raise ValueError(f'duplicate/blank food_id {f_id!r}')
        foodnames[f_id] = row['name']
    matches_by_venue = {}
    match_ids = set()
    for row in matches:
        mid, fid, vid = row['match_id'].strip(), row['food_id'].strip(), row['venue_id'].strip()
        if not mid or mid in match_ids:
            raise ValueError(f'duplicate/blank match_id {mid!r}')
        match_ids.add(mid)
        if fid not in foodnames:
            raise ValueError(f'{mid}: unknown food_id {fid}')
        matches_by_venue.setdefault(vid, []).append(row)
    ids = set()
    places = {}
    review = []
    features = []

    def withhold(row, reason, followup):
        review.append({'Record Type': 'Dining Venue', 'Research ID': row['venue_id'],
                       'Place ID': row.get('place_id', ''), 'Name': row['name'],
                       'Reason': reason, 'Follow-up': followup})

    for line, row in enumerate(venues, 2):
        vid, name = row['venue_id'].strip(), row['name'].strip()
        if not vid or vid in ids:
            raise ValueError(f'Row {line}: duplicate/blank venue_id {vid!r}')
        ids.add(vid)
        pid = (row.get('place_id') or '').strip()
        if not pid:
            withhold(row, 'missing_place_id', 'Identify the physical venue and assign stable place_id.')
            continue
        status = (row.get('location_status') or 'unlocated').strip()
        source = first_source(row.get('location_source_url')) or first_source(row.get('source_urls'))
        source_date = (row.get('location_verified_at') or '').strip() or row.get('verified_date', '').strip()
        verified_coords = status == 'verified'
        point = None
        if verified_coords:
            point = latlon(row, f'Row {line} {name}')
            if not valid_source_date(row.get('location_source_url'), row.get('location_verified_at')):
                raise ValueError(f'Row {line} {name}: verified coordinates require location source and YYYY-MM-DD')

        # An explicitly reviewed map_address is preferred. Otherwise allow only clean, sourced street addresses.
        reviewed_address = (row.get('map_address') or '').strip()
        if reviewed_address and not address_is_clean(reviewed_address):
            withhold(row, 'ambiguous_map_address', 'Replace annotations or incomplete address with a full sourced address.')
            continue
        if not reviewed_address:
            raw_address = (row.get('address') or '').strip()
            if address_is_clean(raw_address) and ('branch' not in row.get('verification_status', '').lower()):
                reviewed_address = raw_address
        if not reviewed_address and verified_coords:
            # For a named, verified physical pin without a street address, My Maps may resolve its name.
            reviewed_address = f"{name}, {row['city']}, {row['country']}"
            placement_status = 'provider_name_lookup_needs_review'
        elif reviewed_address:
            placement_status = 'address_geocoded_by_google_needs_visual_review'
        else:
            withhold(row, 'missing_or_ambiguous_address', 'Confirm exact venue branch and clean full street address before importing.')
            continue
        if not valid_source_date(source, source_date):
            withhold(row, 'missing_location_provenance', 'Record published map/address source and YYYY-MM-DD verification date.')
            continue
        if not verified_coords and status not in ('provisional', 'unlocated', 'ambiguous', ''):
            withhold(row, 'unrecognized_location_status', 'Use verified, provisional, unlocated or ambiguous.')
            continue

        full_address = reviewed_address
        if row.get('city', '').lower() not in full_address.lower():
            full_address += ', ' + row['city']
        if row.get('country', '').lower() not in full_address.lower():
            full_address += ', ' + row['country']
        matched = matches_by_venue.get(vid, [])
        pairs = []
        for m in matched:
            status_menu = (m.get('menu_status') or 'not_yet_researched').strip()
            # Never imply a dish is confirmed when match has no supporting source.
            if status_menu not in ('verified', 'plausible_needs_confirmation'):
                continue
            if not first_source(m.get('source_urls')) and not first_source(row.get('source_urls')):
                continue
            name_food = foodnames[m['food_id']]
            score_s = (m.get('venue_suitability_score') or '').strip()
            if score_s:
                try: score = float(score_s)
                except ValueError as exc: raise ValueError(f'Invalid pair score for {m["match_id"]}') from exc
                if not (math.isfinite(score) and 0 <= score <= 100):
                    raise ValueError(f'Invalid pair score range for {m["match_id"]}')
            pairs.append((name_food, score_s, status_menu, first_source(m.get('source_urls'))))
        foods_list = '; '.join(sorted({q[0] for q in pairs}))
        scores = [float(q[1]) for q in pairs if q[1]]
        best = f'{max(scores):g}' if scores else ''
        menu = ('plausible_needs_confirmation' if any(x[2]=='plausible_needs_confirmation' for x in pairs)
                else 'verified' if pairs else 'not_yet_researched')
        url = 'https://www.google.com/maps/search/?api=1&query=' + quote(f'{name}, {full_address}')
        item = {
            'Place ID': safe_text(pid), 'Venue ID': safe_text(vid), 'Name': safe_text(name),
            'City': safe_text(row['city']), 'Country': safe_text(row['country']),
            'Map Address': safe_text(full_address),
            'Primary Category': 'Local Cuisine and Food Markets',
            'Recommended Foods': safe_text(foods_list),
            'Food–Venue Match Score': best,
            'Menu Verification Status': menu,
            'Geocoding Status': placement_status,
            'Location Status': 'verified_coordinates' if verified_coords else 'address_based_provisional',
            'Latitude': point[0] if point else '', 'Longitude': point[1] if point else '',
            'Location Source': source, 'Source Checked At': source_date,
            'Dish Evidence': '; '.join(sorted({q[3] for q in pairs if q[3]})),
            'Visitor Note': safe_text(row.get('notes', '')),
            'Google Maps Search': url,
        }
        if pid in places:
            old = places[pid]
            if old['Map Address'] != item['Map Address']:
                raise ValueError(f'Venues share place_id {pid} but have conflicting address records')
            old['Venue ID'] += ';' + vid
            if item['Recommended Foods']:
                old['Recommended Foods'] = '; '.join(sorted({*old['Recommended Foods'].split('; '), *item['Recommended Foods'].split('; ')} - {''}))
            if item['Food–Venue Match Score'] and (not old['Food–Venue Match Score'] or float(old['Food–Venue Match Score']) < float(item['Food–Venue Match Score'])):
                old['Food–Venue Match Score'] = item['Food–Venue Match Score']
            if item['Menu Verification Status'] == 'plausible_needs_confirmation':
                old['Menu Verification Status'] = item['Menu Verification Status']
            continue
        places[pid] = item
        if point:
            features.append({'type': 'Feature', 'id': pid,
                'geometry': {'type': 'Point', 'coordinates': [point[1], point[0]]},
                'properties': {'place_id': pid, 'name': name, 'venue_id': vid,
                               'menu_verification_status': menu, 'location_source_url': source}})

    unknown_venue_matches = set(matches_by_venue) - ids
    if unknown_venue_matches:
        raise ValueError(f'Matches refer to unknown venue IDs: {sorted(unknown_venue_matches)}')
    if len(places) > MAX_MYMAPS_ROWS:
        raise ValueError(f'{len(places)} venues exceed Google My Maps 2,000-row import limit')
    out = Path(outdir)
    out.mkdir(parents=True, exist_ok=True)
    write_csv(out / 'dining_venues_mymaps.csv', MYMAPS_FIELDS, list(places.values()))
    write_csv(out / 'dining_needs_location_review.csv', REVIEW_FIELDS, review)
    (out / 'dining_venues.geojson').write_text(json.dumps({'type': 'FeatureCollection', 'features': features}, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    return len(places), len(review), len(features)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('venues_csv')
    p.add_argument('foods_csv')
    p.add_argument('matches_csv')
    p.add_argument('outdir')
    a = p.parse_args()
    try:
        mapped, withheld, coords_count = export(a.venues_csv, a.foods_csv, a.matches_csv, a.outdir)
    except ValueError as exc:
        p.exit(2, f'Error: {exc}\n')
    print(f'Exported {mapped} Google My Maps dining venue(s) ({coords_count} verified coordinate point(s)); withheld {withheld}')


if __name__ == '__main__':
    main()
