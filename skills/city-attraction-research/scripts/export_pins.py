#!/usr/bin/env python3
"""Export sourced city attraction pins, without geocoding or routing.

Usage: python export_pins.py inventory.csv pins.geojson [unlocated.csv]
Requires standard library only. Coordinates must be verified before they are plotted.
"""
import csv
import json
import sys
from pathlib import Path


def main():
    if len(sys.argv) not in (3, 4):
        raise SystemExit('Usage: python export_pins.py inventory.csv pins.geojson [unlocated.csv]')
    source, output = Path(sys.argv[1]), Path(sys.argv[2])
    missing_path = Path(sys.argv[3]) if len(sys.argv) == 4 else output.with_name('unlocated_places.csv')
    verified, pending = {}, {}
    with source.open(newline='', encoding='utf-8-sig') as handle:
        reader = csv.DictReader(handle)
        required = {'attraction_id', 'place_id', 'name', 'primary_category', 'latitude', 'longitude', 'location_status', 'location_source_url', 'location_verified_at'}
        if not required.issubset(set(reader.fieldnames or [])):
            raise SystemExit('Missing required columns: '+', '.join(sorted(required - set(reader.fieldnames or []))))
        for line, row in enumerate(reader, 2):
            pid = row['place_id'].strip()
            name = row['name'].strip()
            status = row['location_status'].strip() or 'unlocated'
            if not pid:
                pending[f'row-{line}'] = {'place_id':'','name':name,'reason':'place_id missing'}
                continue
            if status != 'verified':
                if pid not in verified:
                    pending.setdefault(pid, {'place_id':pid,'name':name,'reason':'location '+status})
                continue
            try:
                lat, lon = float(row['latitude']), float(row['longitude'])
            except (ValueError, TypeError):
                raise SystemExit(f'Row {line}: verified coordinates must be numeric')
            if not (-90 <= lat <= 90 and -180 <= lon <= 180):
                raise SystemExit(f'Row {line}: coordinates out of range')
            if not (row['location_source_url'].strip() and row['location_verified_at'].strip()):
                raise SystemExit(f'Row {line}: verified coordinates need source and verification date')
            feature={'type':'Feature','id':pid,'geometry':{'type':'Point','coordinates':[lon,lat]},'properties':{'name':name,'place_id':pid,'primary_category':row['primary_category'],'attraction_id':row['attraction_id'],'priority_tier':row.get('priority_tier',''),'source_url':row['location_source_url']}}
            if pid in verified and verified[pid]['geometry']['coordinates'] != feature['geometry']['coordinates']:
                raise SystemExit(f'Row {line}: conflicting verified coordinates for place_id {pid}')
            verified.setdefault(pid, feature)
            pending.pop(pid, None)
    features, missing = list(verified.values()), list(pending.values())
    output.parent.mkdir(parents=True, exist_ok=True)
    missing_path.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps({'type':'FeatureCollection','features':features},indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    with missing_path.open('w',encoding='utf-8',newline='') as handle:
        w=csv.DictWriter(handle,fieldnames=['place_id','name','reason'])
        w.writeheader();w.writerows(missing)
    print(f'Exported {len(features)} verified pin(s); withheld {len(missing)} unverified entry/entries')


if __name__ == '__main__':
    main()
