#!/usr/bin/env python3
"""Generate the three default attraction deliverables from one researched CSV.

Usage: python generate_research.py attraction_inventory.csv OUT_DIR [--overwrite]
Existing score_and_validate.py and export_pins.py CLIs are unchanged and optional.
Python standard library only. No online geocoding or map-tile requests.
"""
import argparse
import csv
import json
import os
import tempfile
from pathlib import Path

from export_pins import export, safe_text
from score_and_validate import CATEGORIES, WEIGHTS, tier

OUTPUTS = ('attractions.json', 'attractions_checklist.csv', 'attractions_mymaps.csv')
CHECKLIST = ('attraction_id', 'rank', 'name', 'primary_category', 'weighted_score',
             'priority_tier', 'estimated_minutes', 'review_decision', 'review_notes')
GEO = ('place_id', 'latitude', 'longitude', 'location_status',
       'location_source_url', 'location_verified_at')


def read_csv(path):
    with Path(path).open('r', newline='', encoding='utf-8-sig') as f:
        r = csv.DictReader(f)
        fields = list(r.fieldnames or [])
        required = {'attraction_id', 'name', 'city', 'country', 'primary_category', *WEIGHTS}
        if not required.issubset(fields):
            raise ValueError(f'Missing attraction columns: {sorted(required - set(fields))}')
        return fields, list(r)


def split_items(s):
    return [s.strip() for s in (s or '').split(';') if s.strip()]


def rating_score(row, line):
    inputs = [(row.get(key) or '').strip() for key in WEIGHTS]
    if any(inputs) and not all(inputs):
        raise ValueError(f'Row {line}: all five ratings or none required')
    if not any(inputs):
        if (row.get('weighted_score') or '').strip():
            raise ValueError(f'Row {line}: score without complete ratings')
        return {name: None for name in WEIGHTS}, None
    ratings = {}
    for name, value in zip(WEIGHTS, inputs):
        try:
            number = int(value)
        except ValueError as exc:
            raise ValueError(f'Row {line}: {name} must be integer 0..5') from exc
        if number < 0 or number > 5:
            raise ValueError(f'Row {line}: {name} must be integer 0..5')
        ratings[name] = number
    score = sum(WEIGHTS[name] * value for name, value in ratings.items()) / 5
    current = (row.get('weighted_score') or '').strip()
    if current:
        try:
            correct = float(current) == score
        except ValueError:
            correct = False
        if not correct:
            raise ValueError(f'Row {line}: supplied weighted_score does not match five ratings')
    return ratings, score


def nullable_number(value, field, line):
    if not str(value or '').strip():
        return None
    try:
        number = float(value)
    except ValueError as exc:
        raise ValueError(f'Row {line}: invalid {field}') from exc
    valid = (-90 <= number <= 90) if field == 'latitude' else (-180 <= number <= 180)
    if not valid:
        raise ValueError(f'Row {line}: out-of-range {field}')
    return number


def transform(fields, rows):
    records, scored_rows = [], []
    ids = set()
    cities = set()
    for line, source in enumerate(rows, 2):
        row = dict(source)
        ident = (row.get('attraction_id') or '').strip()
        if not ident or ident in ids:
            raise ValueError(f'Row {line}: empty or duplicate attraction_id')
        ids.add(ident)
        if (row.get('primary_category') or '').strip() not in CATEGORIES:
            raise ValueError(f'Row {line}: invalid full primary_category')
        city = (row.get('city') or '').strip()
        country = (row.get('country') or '').strip()
        if not city or not country or not (row.get('name') or '').strip():
            raise ValueError(f'Row {line}: city, country and name required')
        cities.add((city, country))
        if len(cities) > 1:
            raise ValueError('One research run may contain only one city/country')
        ratings, score = rating_score(row, line)
        for key in GEO:
            row.setdefault(key, '')
        for key in ('source_urls', 'secondary_tags', 'estimated_minutes', 'research_status'):
            row.setdefault(key, '')
        lat = nullable_number(row['latitude'], 'latitude', line)
        lon = nullable_number(row['longitude'], 'longitude', line)
        if (lat is None) != (lon is None):
            raise ValueError(f'Row {line}: partial latitude/longitude pair')
        duration = (row.get('estimated_minutes') or '').strip()
        if duration:
            try:
                duration = int(duration)
            except ValueError as exc:
                raise ValueError(f'Row {line}: estimated_minutes must be integer') from exc
            if duration < 0:
                raise ValueError(f'Row {line}: estimated_minutes must be >= 0')
        else:
            duration = None
        row['weighted_score'] = '' if score is None else f'{score:g}'
        row['priority_tier'] = '' if score is None else tier(score)
        scored_rows.append(row)
        record = {k: v for k, v in row.items() if k not in (*WEIGHTS, 'weighted_score',
                   'priority_tier', 'source_urls', 'secondary_tags', 'latitude', 'longitude',
                   'estimated_minutes')}
        record.update(ratings=ratings, weighted_score=score, priority_tier=row['priority_tier'] or None,
                      source_urls=split_items(row['source_urls']),
                      secondary_tags=split_items(row['secondary_tags']),
                      latitude=lat, longitude=lon, estimated_minutes=duration)
        records.append(record)
    return records, scored_rows, (next(iter(cities)) if cities else (None, None))


def write_csv(path, fields, rows):
    with Path(path).open('w', newline='', encoding='utf-8-sig') as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        w.writeheader()
        w.writerows(rows)


def generate(input_csv, outdir, overwrite=False):
    outdir = Path(outdir)
    if not overwrite and any((outdir / name).exists() for name in OUTPUTS):
        raise FileExistsError('Default outputs exist; use a new directory or --overwrite')
    fields, source_rows = read_csv(input_csv)
    records, scored_rows, city_country = transform(fields, source_rows)
    outdir.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=outdir.parent) as temp:
        temp = Path(temp)
        stage = temp / 'stage'
        stage.mkdir()
        mapping = temp / 'map'
        mapping.mkdir()
        export_fields = list(dict.fromkeys(fields + list(GEO) + ['weighted_score', 'priority_tier',
                                                   'source_urls', 'secondary_tags', 'research_status']))
        scored_input = temp / 'scored.csv'
        write_csv(scored_input, export_fields, scored_rows)
        mapped, withheld = export(scored_input, mapping / 'pins.geojson')
        with (mapping / 'attractions_needs_location_review.csv').open(newline='', encoding='utf-8-sig') as f:
            warnings = list(csv.DictReader(f))
        ranked = sorted(records, key=lambda x: (x['weighted_score'] is None,
                         -(x['weighted_score'] or 0), x['attraction_id']))
        checklist = []
        for entry in ranked:
            score = entry['weighted_score']
            checklist.append({
                'attraction_id': safe_text(entry['attraction_id']),
                'rank': len(checklist)+1 if score is not None else '',
                'name': safe_text(entry['name']),
                'primary_category': safe_text(entry['primary_category']),
                'weighted_score': '' if score is None else f'{score:g}',
                'priority_tier': entry['priority_tier'] or '',
                'estimated_minutes': '' if entry['estimated_minutes'] is None else entry['estimated_minutes'],
                'review_decision': 'undecided', 'review_notes': '',
            })
        result = {'schema_version': '1.0', 'dataset_type': 'attractions',
                  'city': city_country[0], 'country': city_country[1],
                  'attractions': records, 'mapping': {'mapped': mapped, 'withheld': withheld,
                  'needs_location_review': warnings}}
        (stage / 'attractions.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        write_csv(stage / 'attractions_checklist.csv', CHECKLIST, checklist)
        (stage / 'attractions_mymaps.csv').write_bytes((mapping / 'attractions_mymaps.csv').read_bytes())
        outdir.mkdir(parents=True, exist_ok=True)
        for name in OUTPUTS:
            os.replace(stage / name, outdir / name)
    return len(records), mapped, withheld


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('attraction_inventory_csv')
    parser.add_argument('output_dir')
    parser.add_argument('--overwrite', action='store_true')
    args = parser.parse_args()
    try:
        total, mapped, withheld = generate(args.attraction_inventory_csv, args.output_dir, args.overwrite)
    except (OSError, ValueError) as exc:
        parser.exit(2, f'Error: {exc}\n')
    print(f'Generated three attraction files: {total} records, {mapped} map pins, {withheld} withheld locations')


if __name__ == '__main__':
    main()
