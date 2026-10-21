#!/usr/bin/env python3
"""Generate three default food/dining files from the existing three research CSVs.

Usage: python generate_research.py FOODS.csv VENUES.csv MATCHES.csv OUT_DIR [--overwrite]
Preserves legacy score_and_validate.py and export_venues_mymaps.py commands.
Python standard library only; no live menu checks or geocoding.
"""
import argparse
import csv
import json
import os
import tempfile
from pathlib import Path

from export_venues_mymaps import export, safe_text
from score_and_validate import CATEGORIES, FOOD_WEIGHTS, MATCH_WEIGHTS

OUTPUTS = ('food_research.json', 'foods_checklist.csv', 'dining_venues_mymaps.csv')
CHECKLIST = ('food_id', 'rank', 'name', 'primary_category', 'geographic_identity',
             'food_score', 'priority_tier', 'review_decision', 'review_notes')


def split_items(s):
    return [x.strip() for x in (s or '').split(';') if x.strip()]


def load_csv(path, required):
    with Path(path).open(newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        fields = list(reader.fieldnames or [])
        missing = set(required) - set(fields)
        if missing:
            raise ValueError(f'{path}: missing columns {sorted(missing)}')
        return fields, list(reader)


def check_ids(rows, key, title):
    ids = set()
    for line, row in enumerate(rows, 2):
        ident = (row.get(key) or '').strip()
        if not ident or ident in ids:
            raise ValueError(f'{title} row {line}: blank or duplicate {key}')
        ids.add(ident)
    return ids


def compute(row, weights, score_key, line):
    values = [(row.get(key) or '').strip() for key in weights]
    if any(values) and not all(values):
        raise ValueError(f'Row {line}: {score_key} requires all five ratings')
    if not any(values):
        if (row.get(score_key) or '').strip():
            raise ValueError(f'Row {line}: {score_key} exists without ratings')
        return {k: None for k in weights}, None
    ratings = {}
    for field, value in zip(weights, values):
        try:
            number = int(value)
        except ValueError as exc:
            raise ValueError(f'Row {line}: {field} must be integer 0..5') from exc
        if not 0 <= number <= 5:
            raise ValueError(f'Row {line}: {field} must be integer 0..5')
        ratings[field] = number
    score = sum(weights[k] * v for k, v in ratings.items()) / 5
    supplied = (row.get(score_key) or '').strip()
    if supplied:
        try:
            matches = float(supplied) == score
        except ValueError:
            matches = False
        if not matches:
            raise ValueError(f'Row {line}: {score_key} conflicts with calculated ratings')
    return ratings, score


def food_tier(score):
    return ('Must-Try Candidate' if score >= 80 else 'Highly Recommended'
            if score >= 60 else 'Optional or Specialist Interest')


def write_csv(path, fields, rows):
    with Path(path).open('w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(rows)


def make_record(row, rating_fields, ratings, score_key, score):
    record = {k: v for k, v in row.items() if k not in (*rating_fields, score_key, 'source_urls',
                                                           'aliases', 'secondary_tags', 'variants')}
    record['ratings'] = ratings
    record[score_key] = score
    record['source_urls'] = split_items(row.get('source_urls'))
    for field in ('aliases', 'secondary_tags', 'variants'):
        if field in row:
            record[field] = split_items(row.get(field))
    return record


def generate(foods_csv, venues_csv, matches_csv, outdir, overwrite=False):
    outdir = Path(outdir)
    if not overwrite and any((outdir / name).exists() for name in OUTPUTS):
        raise FileExistsError('Default outputs exist; use a new directory or --overwrite')
    food_fields, foods = load_csv(foods_csv, ['food_id', 'name', 'primary_category', *FOOD_WEIGHTS])
    venue_fields, venues = load_csv(venues_csv, ['venue_id', 'name', 'city', 'country', 'address', 'source_urls', 'verified_date'])
    match_fields, matches = load_csv(matches_csv, ['match_id', 'food_id', 'venue_id', 'menu_status', *MATCH_WEIGHTS])
    food_ids = check_ids(foods, 'food_id', 'Foods')
    venue_ids = check_ids(venues, 'venue_id', 'Venues')
    check_ids(matches, 'match_id', 'Matches')
    normalized_foods, normalized_matches = [], []
    cities = {((v.get('city') or '').strip(), (v.get('country') or '').strip()) for v in venues}
    cities.update(((f.get('city') or '').strip(), (f.get('country') or '').strip())
                  for f in foods if (f.get('city') or '').strip() and (f.get('country') or '').strip())
    if len(cities) > 1:
        raise ValueError('One research run may contain only one city/country')
    city_country = next(iter(cities), (None, None))
    for line, row in enumerate(foods, 2):
        if (row.get('primary_category') or '').strip() not in CATEGORIES:
            raise ValueError(f'Foods row {line}: invalid full primary_category')
        if not (row.get('name') or '').strip():
            raise ValueError(f'Foods row {line}: name required')
        ratings, score = compute(row, FOOD_WEIGHTS, 'food_score', line)
        row['food_score'] = '' if score is None else f'{score:g}'
        row['priority_tier'] = '' if score is None else food_tier(score)
        record = make_record(row, FOOD_WEIGHTS, ratings, 'food_score', score)
        record['priority_tier'] = row['priority_tier'] or None
        normalized_foods.append(record)
    for line, row in enumerate(matches, 2):
        if row['food_id'] not in food_ids or row['venue_id'] not in venue_ids:
            raise ValueError(f'Matches row {line}: missing referenced food_id or venue_id')
        ratings, score = compute(row, MATCH_WEIGHTS, 'venue_suitability_score', line)
        if score is not None:
            if (row.get('menu_status') or '').strip() not in ('verified', 'plausible_needs_confirmation'):
                raise ValueError(f'Matches row {line}: scored match requires supported menu status')
            if not (row.get('source_urls') or '').strip():
                raise ValueError(f'Matches row {line}: scored match needs dish-specific source evidence')
        row['venue_suitability_score'] = '' if score is None else f'{score:g}'
        normalized_matches.append(make_record(row, MATCH_WEIGHTS, ratings, 'venue_suitability_score', score))
    normalized_venues = []
    for row in venues:
        r = dict(row)
        r['source_urls'] = split_items(row.get('source_urls'))
        normalized_venues.append(r)
    # Food scores and venue-pair scores remain separate.
    ranked = sorted(normalized_foods, key=lambda f: (f['food_score'] is None,
                    -(f['food_score'] or 0), f['food_id']))
    checklist = []
    for food in ranked:
        score = food['food_score']
        checklist.append({
            'food_id': safe_text(food['food_id']),
            'rank': len(checklist)+1 if score is not None else '',
            'name': safe_text(food['name']),
            'primary_category': safe_text(food['primary_category']),
            'geographic_identity': safe_text(food.get('geographic_identity', '')),
            'food_score': '' if score is None else f'{score:g}',
            'priority_tier': food['priority_tier'] or '',
            'review_decision': 'undecided', 'review_notes': '',
        })
    outdir.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=outdir.parent) as temp:
        tmp = Path(temp)
        stage = tmp / 'stage'
        stage.mkdir()
        mapdir = tmp / 'map'
        mapdir.mkdir()
        food_input = tmp / 'foods.csv'
        match_input = tmp / 'matches.csv'
        food_out_fields = list(dict.fromkeys(food_fields + ['food_score', 'priority_tier']))
        match_out_fields = list(dict.fromkeys(match_fields + ['venue_suitability_score']))
        write_csv(food_input, food_out_fields, foods)
        write_csv(match_input, match_out_fields, matches)
        mapped, withheld, precise = export(venues_csv, food_input, match_input, mapdir)
        with (mapdir / 'dining_needs_location_review.csv').open(newline='', encoding='utf-8-sig') as f:
            warnings = list(csv.DictReader(f))
        result = {'schema_version': '1.0', 'dataset_type': 'food_and_dining',
                  'city': city_country[0], 'country': city_country[1],
                  'foods': normalized_foods, 'venues': normalized_venues,
                  'food_venue_matches': normalized_matches,
                  'mapping': {'mapped': mapped, 'withheld': withheld,
                              'verified_coordinates': precise, 'needs_location_review': warnings}}
        (stage / 'food_research.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        write_csv(stage / 'foods_checklist.csv', CHECKLIST, checklist)
        (stage / 'dining_venues_mymaps.csv').write_bytes((mapdir / 'dining_venues_mymaps.csv').read_bytes())
        outdir.mkdir(parents=True, exist_ok=True)
        for name in OUTPUTS:
            os.replace(stage / name, outdir / name)
    return len(foods), len(venues), len(matches), mapped, withheld


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('foods_csv')
    parser.add_argument('venues_csv')
    parser.add_argument('matches_csv')
    parser.add_argument('output_dir')
    parser.add_argument('--overwrite', action='store_true')
    args = parser.parse_args()
    try:
        stats = generate(args.foods_csv, args.venues_csv, args.matches_csv,
                         args.output_dir, args.overwrite)
    except (OSError, ValueError) as exc:
        parser.exit(2, f'Error: {exc}\n')
    print(f'Generated three food files: {stats[0]} foods, {stats[1]} venues, '
          f'{stats[2]} matches, {stats[3]} map places, {stats[4]} withheld')


if __name__ == '__main__':
    main()
