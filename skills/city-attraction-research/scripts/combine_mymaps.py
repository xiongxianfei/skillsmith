#!/usr/bin/env python3
"""Combine attraction and dining CSVs on explicit shared Place ID, without guessing identity.

Usage: python combine_mymaps.py attractions_mymaps.csv dining_venues_mymaps.csv OUTPUT_DIR
Default Google My Maps workflow is still TWO independently imported layers; the
combined CSV is a single-layer convenience and uses address/place-name geocoding.
"""
import argparse
import csv
from pathlib import Path

FIELDS = [
    'Place ID', 'Name', 'Map Address', 'Roles', 'Primary Category',
    'Attraction Score', 'Food–Venue Match Score', 'Recommended Foods',
    'Menu Verification Status', 'Latitude', 'Longitude', 'Location Review Status',
    'Attraction ID', 'Venue ID', 'Attraction Source', 'Dining Location Source',
]


def read(path, required):
    with Path(path).open(encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f)
        missing = set(required) - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f'{path}: missing {sorted(missing)}')
        return list(reader)


def write(path, fields, rows):
    with path.open(encoding='utf-8-sig', newline='', mode='w') as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        w.writeheader()
        w.writerows(rows)


def combine(attractions_path, dining_path, output_dir):
    attractions = read(attractions_path, ['Place ID', 'Name', 'Latitude', 'Longitude', 'Primary Category'])
    dining = read(dining_path, ['Place ID', 'Name', 'Map Address', 'Primary Category'])
    places = {}
    a_ids, d_ids = set(), set()
    for row in attractions:
        pid = row['Place ID'].strip()
        if not pid or pid in a_ids:
            raise ValueError(f'duplicate/blank Place ID in attraction file: {pid!r}')
        a_ids.add(pid)
        city, country = row.get('City', ''), row.get('Country', '')
        if not city or not country:
            # Deliberately do not invent a city for an arbitrary dataset.
            combined_address = row['Name']
        else:
            combined_address = f'{row["Name"]}, {city}, {country}'
        places[pid] = {
            'Place ID': pid, 'Name': row['Name'], 'Map Address': combined_address,
            'Roles': 'Attractions', 'Primary Category': row['Primary Category'],
            'Attraction Score': row.get('Attraction Score', row.get('Priority Score','')),
            'Food–Venue Match Score': '', 'Recommended Foods': '', 'Menu Verification Status': '',
            'Latitude': row['Latitude'], 'Longitude': row['Longitude'],
            'Location Review Status': 'confirmed_coordinates_use_separate_attraction_layer_for_exact_pin',
            'Attraction ID': row.get('Attraction ID', ''), 'Venue ID': '',
            'Attraction Source': row.get('Coordinate Source', ''), 'Dining Location Source': '',
        }
    for row in dining:
        pid = row['Place ID'].strip()
        if not pid or pid in d_ids:
            raise ValueError(f'duplicate/blank Place ID in dining file: {pid!r}')
        d_ids.add(pid)
        if pid in places:
            existing = places[pid]
            alat, alon = existing['Latitude'], existing['Longitude']
            dlat, dlon = row.get('Latitude', ''), row.get('Longitude', '')
            if all((alat, alon, dlat, dlon)):
                if abs(float(alat)-float(dlat))>0.0005 or abs(float(alon)-float(dlon))>0.0005:
                    raise ValueError(f'conflicting positions for shared Place ID {pid}')
            existing['Roles'] = 'Attractions; Dining Venues'
            existing['Venue ID'] = row.get('Venue ID', '')
            existing['Food–Venue Match Score'] = row.get('Food–Venue Match Score', '')
            existing['Recommended Foods'] = row.get('Recommended Foods', '')
            existing['Menu Verification Status'] = row.get('Menu Verification Status', '')
            existing['Dining Location Source'] = row.get('Location Source', '')
            existing['Location Review Status'] += '; duplicate physical place merged by verified ID'
        else:
            places[pid] = {
                'Place ID': pid, 'Name': row['Name'], 'Map Address': row['Map Address'],
                'Roles': 'Dining Venues', 'Primary Category': row['Primary Category'],
                'Attraction Score': '',
                'Food–Venue Match Score': row.get('Food–Venue Match Score', ''),
                'Recommended Foods': row.get('Recommended Foods', ''),
                'Menu Verification Status': row.get('Menu Verification Status', ''),
                'Latitude': row.get('Latitude', ''), 'Longitude': row.get('Longitude', ''),
                'Location Review Status': row.get('Geocoding Status', 'address_needs_review'),
                'Attraction ID': '', 'Venue ID': row.get('Venue ID', ''),
                'Attraction Source': '', 'Dining Location Source': row.get('Location Source', ''),
            }
    if len(places) > 2000:
        raise ValueError('Combined map exceeds Google My Maps 2,000-row import limit')
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    write(out/'combined_city_mymaps.csv', FIELDS, list(places.values()))
    return len(places), len(a_ids & d_ids)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('attractions_csv','dining_csv','output_dir'):
        p.add_argument(name)
    a=p.parse_args()
    try: total,shared=combine(a.attractions_csv,a.dining_csv,a.output_dir)
    except ValueError as exc: p.exit(2, f'Error: {exc}\n')
    print(f'Combined {total} physical places, merging {shared} shared ID(s). Review Google location matching before navigation.')

if __name__=='__main__':main()
