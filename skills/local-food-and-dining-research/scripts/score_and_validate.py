#!/usr/bin/env python3
"""Check food/venue/match CSV relationships and calculate transparent scores.

Usage: python scripts/score_and_validate.py FOODS.csv VENUES.csv MATCHES.csv [OUTPUT_DIR]
Missing ratings remain blank. Does not connect to the internet. Python standard library only.
"""
import csv, pathlib, sys

CATEGORIES = {
    'Rice, Grains, and Substantial Staples',
    'Breads and Baked Pastries',
    'Dumplings and Noodles',
    'Grilled and Meat Specialties',
    'Soups and Stews',
    'Produce, Salads, and Accompaniments',
    'Sweets and Desserts',
    'Traditional Drinks',
}
FOOD_WEIGHTS = {'local_distinctiveness':30,'cultural_significance':25,
                'culinary_distinctiveness':20,'general_traveler_relevance':15,'availability':10}
MATCH_WEIGHTS = {'signature_food_match':35,'preparation_experience':25,
                 'cultural_character':15,'practicality':15,'evidence_confidence':10}

def load(path):
    with pathlib.Path(path).open(encoding='utf-8-sig',newline='') as f:
        r=csv.DictReader(f)
        if not r.fieldnames: raise SystemExit(f'No header in {path}')
        return list(r),list(r.fieldnames)

def check_ids(rows,key,label):
    ids=set()
    for line,row in enumerate(rows,2):
        ident=(row.get(key) or '').strip()
        if not ident or ident in ids: raise SystemExit(f'{label} row {line}: blank/duplicate {key}: {ident!r}')
        ids.add(ident)
    return ids

def score_rows(rows,fields,weights,outfield,label):
    for field in [*weights]:
        if field not in fields: raise SystemExit(f'{label}: missing column {field}')
    if outfield not in fields: fields.append(outfield)
    n=0
    for line,row in enumerate(rows,2):
        vals=[(row.get(k) or '').strip() for k in weights]
        if any(vals) and not all(vals):
            raise SystemExit(f'{label} row {line}: all five ratings required or all blank')
        if all(vals):
            parsed=[]
            for x in vals:
                try: v=int(x)
                except ValueError: raise SystemExit(f'{label} row {line}: rating must be integer')
                if not 0<=v<=5: raise SystemExit(f'{label} row {line}: rating outside 0..5')
                parsed.append(v)
            total=sum(w*v for w,v in zip(weights.values(),parsed))/5
            row[outfield]=f'{total:.0f}'
            n+=1
        else: row[outfield]=''
    return n

def write(rows,fields,path):
    with path.open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(rows)

def main():
    if len(sys.argv) not in (4,5):
        raise SystemExit('Usage: python score_and_validate.py foods.csv venues.csv matches.csv [output_dir]')
    foods,foodfields=load(sys.argv[1]); venues,venuefields=load(sys.argv[2]); matches,matchfields=load(sys.argv[3])
    foodids=check_ids(foods,'food_id','foods');venueids=check_ids(venues,'venue_id','venues');check_ids(matches,'match_id','matches')
    for n,row in enumerate(foods,2):
        if row.get('primary_category','').strip() not in CATEGORIES:
            raise SystemExit(f'foods row {n}: use full descriptive category name, got {row.get("primary_category")!r}')
    for n,row in enumerate(matches,2):
        if row.get('food_id') not in foodids: raise SystemExit(f'matches row {n}: food_id not found')
        if row.get('venue_id') not in venueids: raise SystemExit(f'matches row {n}: venue_id not found')
    foodn=score_rows(foods,foodfields,FOOD_WEIGHTS,'food_score','foods')
    if 'priority_tier' not in foodfields:foodfields.append('priority_tier')
    for row in foods:
        if row['food_score']:
            score=float(row['food_score']);row['priority_tier']=('Must-Try Candidate' if score>=80 else 'Highly Recommended' if score>=60 else 'Optional or Specialist Interest')
        else:row['priority_tier']=''
    matchn=score_rows(matches,matchfields,MATCH_WEIGHTS,'venue_suitability_score','matches')
    for line,row in enumerate(matches,2):
        if row['venue_suitability_score'] and row.get('menu_status') not in ('verified','plausible_needs_confirmation'):
            raise SystemExit(f'matches row {line}: a scored match requires verified or explicitly provisional menu_status')
    out=pathlib.Path(sys.argv[4]) if len(sys.argv)==5 else pathlib.Path('.')
    out.mkdir(parents=True,exist_ok=True)
    write(foods,foodfields,out/'foods_scored.csv')
    write(venues,venuefields,out/'venues_checked.csv')
    write(matches,matchfields,out/'food_venue_matches_scored.csv')
    print(f'Validated {len(foods)} foods ({foodn} scored), {len(venues)} venues, {len(matches)} matches ({matchn} scored). Wrote {out}')

if __name__=='__main__':main()
