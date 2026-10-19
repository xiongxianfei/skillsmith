#!/usr/bin/env python3
"""Validate attraction taxonomy and compute transparent editorial scores. Python stdlib only.

Usage: python scripts/score_and_validate.py INPUT.csv [OUTPUT.csv]
Unrated candidates retain blank scores and tiers. Output defaults to INPUT_scored.csv.
"""
import csv, sys, pathlib

CATEGORIES = {
    'Historical Sites and Architectural Landmarks',
    'Museums, Science, and Learning',
    'Scenic Views and Nature',
    'Local Cuisine and Food Markets',
    'Arts, Crafts, and Cultural Activities',
    'Neighborhoods and Local Life',
    'Sacred Sites and Spirituality',
    'Entertainment, Recreation, and Modern Attractions',
}
WEIGHTS = {'city_distinctiveness':30, 'traveler_relevance':25,
           'experience_quality':20, 'historical_cultural_value':15, 'practical_value':10}
def tier(score):
    return ('Must-Visit Candidate' if score>=80 else
            'Highly Recommended' if score>=60 else 'Optional or Specialist Interest')

def main():
    if len(sys.argv) not in (2,3):
        raise SystemExit('Usage: python score_and_validate.py input.csv [output.csv]')
    src=pathlib.Path(sys.argv[1])
    dst=pathlib.Path(sys.argv[2]) if len(sys.argv)==3 else src.with_name(src.stem+'_scored.csv')
    with src.open(newline='',encoding='utf-8-sig') as h:
        r=csv.DictReader(h); fields=list(r.fieldnames or []); rows=list(r)
    if not fields: raise SystemExit('Input CSV needs a header')
    for required in ['attraction_id','primary_category',*WEIGHTS]:
        if required not in fields: raise SystemExit(f'Missing column: {required}')
    for name in ('weighted_score','priority_tier'):
        if name not in fields: fields.append(name)
    ids=set(); scored=0
    for i,row in enumerate(rows,2):
        ident=row['attraction_id'].strip()
        if not ident or ident in ids: raise SystemExit(f'Row {i}: blank/duplicate attraction_id: {ident!r}')
        ids.add(ident)
        if row['primary_category'].strip() not in CATEGORIES:
            raise SystemExit(f'Row {i}: use full descriptive primary category name, got {row["primary_category"]!r}')
        present=[bool((row.get(k) or '').strip()) for k in WEIGHTS]
        if any(present) and not all(present):
            raise SystemExit(f'Row {i}: provide all five ratings or leave all five blank')
        if all(present):
            vals={}
            for k in WEIGHTS:
                try: n=int(row[k])
                except ValueError: raise SystemExit(f'Row {i}: {k} must be integer 0..5')
                if not 0<=n<=5: raise SystemExit(f'Row {i}: {k} outside 0..5')
                vals[k]=n
            score=sum(WEIGHTS[k]*vals[k] for k in WEIGHTS)/5
            row['weighted_score']=f'{score:.0f}'
            row['priority_tier']=tier(score)
            scored+=1
        else:
            row['weighted_score']=''; row['priority_tier']=''
    with dst.open('w',newline='',encoding='utf-8') as h:
        w=csv.DictWriter(h,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(rows)
    print(f'Validated {len(rows)} attractions; scored {scored}; wrote {dst}')

if __name__=='__main__':main()
