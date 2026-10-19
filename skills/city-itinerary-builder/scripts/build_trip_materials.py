#!/usr/bin/env python3
"""Validate one canonical itinerary and render portable planning artifacts.

Usage: python build_trip_materials.py trip.json [output_directory]
Dependencies: Python 3.9+ standard library only. Never geocodes or routes.
"""
import csv
import html
import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import quote
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

KINDS = {'arrival', 'departure', 'attraction', 'food', 'rest', 'transfer', 'appointment', 'lodging', 'other'}
STATES = {'planned', 'selected', 'completed', 'skipped'}
BOOKINGS = {'confirmed', 'pending', 'unverified', 'not_required'}
CLOCK = re.compile(r'^(?:[01]\d|2[0-3]):[0-5]\d$')


def fail(message):
    raise ValueError(message)


def iso(value, context):
    try:
        parsed = date.fromisoformat(value)
        if parsed.isoformat() != value:
            fail(f'{context}: expected YYYY-MM-DD')
        return parsed
    except (TypeError, ValueError):
        fail(f'{context}: expected valid YYYY-MM-DD')


def minutes(value, context):
    if not isinstance(value, str) or not CLOCK.fullmatch(value):
        fail(f'{context}: expected HH:MM local 24-hour time')
    h, m = map(int, value.split(':'))
    return 60 * h + m


def coords_ok(lat, lon):
    return (type(lat) in (int, float) and type(lon) in (int, float)
            and -90 <= lat <= 90 and -180 <= lon <= 180)


def verify(data):
    if data.get('version') != '1.0':
        fail('version must equal 1.0')
    trip = data.get('trip') or {}
    for key in ('id', 'city', 'country', 'timezone'):
        if not isinstance(trip.get(key), str) or not trip[key].strip():
            fail(f'trip.{key} is required')
    try:
        ZoneInfo(trip['timezone'])
    except (ZoneInfoNotFoundError, ValueError):
        fail('trip.timezone must be a valid IANA time zone')
    begin, finish = iso(trip.get('start_date'), 'trip.start_date'), iso(trip.get('end_date'), 'trip.end_date')
    if finish < begin:
        fail('trip end_date before start_date')
    if not isinstance(data.get('places'), list) or not isinstance(data.get('days'), list) or not isinstance(data.get('legs', []), list):
        fail('places, days and legs must be arrays')

    places = {}
    for n, place in enumerate(data['places'], 1):
        pid = place.get('place_id')
        if not isinstance(pid, str) or not pid or pid in places:
            fail(f'place {n}: missing/duplicate place_id')
        if not isinstance(place.get('name'), str) or not place['name']:
            fail(f'place {pid}: name is required')
        status = place.get('location_status', 'unlocated')
        if status not in {'verified', 'provisional', 'unlocated'}:
            fail(f'place {pid}: bad location_status')
        lat, lon = place.get('latitude'), place.get('longitude')
        if (lat is None) != (lon is None):
            fail(f'place {pid}: latitude and longitude must both be supplied or both be null')
        if lat is not None and not coords_ok(lat, lon):
            fail(f'place {pid}: invalid coordinate pair')
        if status == 'verified' and (lat is None or not place.get('location_source_url') or not place.get('location_verified_at')):
            fail(f'place {pid}: verified location requires coordinates and sourced verification date')
        if status == 'unlocated' and lat is not None:
            fail(f'place {pid}: unlocated status cannot contain coordinates')
        places[pid] = place

    if not data['days']:
        fail('days must contain at least one planned day')
    blocks = {}
    seen_dates = set()
    for day in data['days']:
        d = iso(day.get('date'), 'day.date')
        if d in seen_dates:
            fail(f'duplicate day {d}')
        seen_dates.add(d)
        if not begin <= d <= finish:
            fail(f'day {d}: outside trip date range')
        if not isinstance(day.get('blocks'), list):
            fail(f'day {d}: blocks must be array')
        prev = None
        for block in day['blocks']:
            bid = block.get('block_id')
            if not isinstance(bid, str) or not bid or bid in blocks:
                fail(f'day {d}: duplicate or missing block_id')
            a, b = minutes(block.get('start'), f'block {bid} start'), minutes(block.get('end'), f'block {bid} end')
            if b <= a:
                fail(f'block {bid}: end must be after start on same day')
            if prev is not None and a < prev:
                fail(f'day {d}: overlapping or unsorted blocks (at {bid})')
            prev = b
            if block.get('kind') not in KINDS:
                fail(f'block {bid}: unsupported kind')
            if block.get('state', 'planned') not in STATES:
                fail(f'block {bid}: unsupported state')
            if block.get('booking_status', 'unverified') not in BOOKINGS:
                fail(f'block {bid}: unsupported booking_status')
            if not isinstance(block.get('title'), str) or not block['title']:
                fail(f'block {bid}: title is required')
            if block.get('place_id') is not None and block['place_id'] not in places:
                fail(f'block {bid}: unknown place_id')
            blocks[bid] = (d, a, b, block)

    for n, leg in enumerate(data.get('legs', []), 1):
        first, second = leg.get('from_block_id'), leg.get('to_block_id')
        if first not in blocks or second not in blocks or first == second:
            fail(f'leg {n}: unknown or identical block endpoint')
        d1, _, end1, _ = blocks[first]
        d2, start2, _, _ = blocks[second]
        if d1 != d2 or start2 < end1:
            fail(f'leg {n}: endpoints must be nonoverlapping blocks on same day')
        if leg.get('mode') not in {'walking', 'driving', 'cycling', 'transit', 'other'}:
            fail(f'leg {n}: bad travel mode')
        dur, dist, geom = leg.get('duration_minutes'), leg.get('distance_meters'), leg.get('route_geometry')
        if dur is not None and (type(dur) not in (float, int) or dur <= 0):
            fail(f'leg {n}: invalid duration_minutes')
        if dist is not None and (type(dist) not in (float, int) or dist < 0):
            fail(f'leg {n}: invalid distance_meters')
        if any(v is not None for v in (dur, dist, geom)):
            if not (leg.get('source_url') and leg.get('verified_at')):
                fail(f'leg {n}: metrics or route geometry require source_url and verified_at')
        if dur is not None and dur > start2 - end1:
            fail(f'leg {n}: sourced journey exceeds time between blocks')
        if geom is not None:
            if not isinstance(geom, dict) or geom.get('type') != 'LineString':
                fail(f'leg {n}: route_geometry must be a LineString')
            points = geom.get('coordinates')
            if not isinstance(points, list) or len(points) < 2 or any(not isinstance(p, list) or len(p) < 2 or not coords_ok(p[1], p[0]) for p in points):
                fail(f'leg {n}: malformed sourced geometry')
    return places


def write_csv(path, fieldnames, rows):
    with path.open('w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def page(title, body, extra=''):
    styles = '''body{font:16px system-ui,Arial,sans-serif;color:#142233;max-width:900px;margin:30px auto;padding:0 20px;line-height:1.5}h1,h2{letter-spacing:-.03em}header{border-bottom:3px solid #142233;margin-bottom:25px}table{width:100%;border-collapse:collapse;margin:16px 0 30px}td,th{padding:12px 8px;border-bottom:1px solid #ddd;text-align:left;vertical-align:top}.muted{color:#637082}.card{border:1px solid #ddd;border-radius:14px;padding:15px;margin:12px 0}.time{font-weight:700;white-space:nowrap}.pill{font-size:.8em;padding:2px 7px;border-radius:10px;background:#ebeff3}a{color:#18558f}@media print{body{margin:0;max-width:none}.card{break-inside:avoid}a{text-decoration:none}}'''
    return '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+html.escape(title)+'</title><style>'+styles+extra+'</style></head><body>'+body+'</body></html>'


def render(data, dest):
    places = verify(data)
    dest.mkdir(parents=True, exist_ok=True)
    trip=data['trip']
    title=f"{trip['city']} — {trip['start_date']} to {trip['end_date']}"
    escape=html.escape
    selected = set()
    pins, unmapped, checks, nav, guide, cards = [], [], [], [], [], []
    for day in data['days']:
        d=day['date']
        rows=[]
        columns=[]
        for block in day['blocks']:
            pid=block.get('place_id')
            place=places.get(pid)
            name=block['title']
            booking=block.get('booking_status','unverified')
            state=block.get('state','planned')
            if pid and state != 'skipped':
                selected.add(pid)
            checks.append({'date':d,'time':block['start'],'block_id':block['block_id'],'title':name,'kind':block['kind'],'state':state,'booking_status':booking,'place_id':pid or ''})
            link=''
            if state != 'skipped' and place and place.get('location_status')=='verified':
                lat,lon=place['latitude'],place['longitude']
                url='https://www.google.com/maps/dir/?api=1&destination='+quote(f'{lat},{lon}',safe='')
                link='<a href="'+escape(url,quote=True)+'">Open navigation</a>'
                nav.append(f"- {block['start']} {name}: {url}")
            elif pid and state != 'skipped':
                nav.append(f"- {block['start']} {name}: location not verified; navigation link withheld")
            subtitle=f"{block['kind']} · {state} · booking: {booking}"
            if block.get('notes'):
                subtitle+=' · '+str(block['notes'])
            rows.append('<tr><td class="time">'+escape(block['start'])+'–'+escape(block['end'])+'</td><td><strong>'+escape(name)+'</strong><div class="muted">'+escape(subtitle)+'</div></td><td>'+link+'</td></tr>')
            columns.append('<div class="card"><div class="time">'+escape(block['start'])+'–'+escape(block['end'])+'</div><strong>'+escape(name)+'</strong><div class="muted">'+escape(subtitle)+'</div>'+link+'</div>')
        guide.append('<h2>'+escape(d)+'</h2><table><thead><tr><th>Local time</th><th>Activity</th><th>Location</th></tr></thead><tbody>'+''.join(rows)+'</tbody></table>')
        cards.append('<h2>'+escape(d)+'</h2>'+''.join(columns))
    for pid in sorted(selected):
        place=places[pid]
        status=place.get('location_status','unlocated')
        if status=='verified':
            pins.append({'type':'Feature','id':pid,'geometry':{'type':'Point','coordinates':[place['longitude'],place['latitude']]},'properties':{'name':place['name'],'place_id':pid,'primary_category':place.get('primary_category',''), 'address':place.get('address') or '', 'location_source_url':place['location_source_url']}})
        else:
            unmapped.append({'place_id':pid,'name':place['name'],'location_status':status,'reason':'coordinates not verified for precise plotting'})
    routes=[]
    for index,leg in enumerate(data.get('legs',[]),1):
        if leg.get('route_geometry') is not None:
            routes.append({'type':'Feature','id':f'leg-{index}','geometry':leg['route_geometry'],'properties':{'from_block_id':leg['from_block_id'],'to_block_id':leg['to_block_id'],'mode':leg['mode'],'duration_minutes':leg.get('duration_minutes'),'distance_meters':leg.get('distance_meters'),'source_url':leg['source_url']}})
    (dest/'selected_places.geojson').write_text(json.dumps({'type':'FeatureCollection','features':pins},indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    (dest/'verified_routes.geojson').write_text(json.dumps({'type':'FeatureCollection','features':routes},indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    write_csv(dest/'unlocated_places.csv',['place_id','name','location_status','reason'],unmapped)
    write_csv(dest/'practical_checklist.csv',['date','time','block_id','title','kind','state','booking_status','place_id'],checks)
    (dest/'navigation.md').write_text('# Navigation for '+title+'\n\nOnly verified locations receive links. Links open a navigation app; they are not verified journeys.\n\n'+'\n'.join(nav)+'\n',encoding='utf-8')
    label='<header><h1>'+escape(title)+'</h1><p class="muted">Planning status: '+escape(trip.get('status','draft'))+' · local timezone: '+escape(trip['timezone'])+' · source itinerary version: '+escape(data['version'])+'</p></header>'
    foot='<p class="muted">Planning aid only. Verify operating hours, travel times, bookings and access before travel. Unverified locations are intentionally excluded from map pins.</p>'
    (dest/'printable_travel_guide.html').write_text(page('Printable Travel Guide',label+''.join(guide)+foot),encoding='utf-8')
    (dest/'itinerary_timeline.html').write_text(page('Itinerary Timeline',label+''.join(cards)+foot),encoding='utf-8')
    infographic='<section class="summary"><p>'+escape(str(len(data['days'])))+' day(s) · '+escape(str(len(checks)))+' itinerary block(s) · '+escape(str(len(pins)))+' mapped locations</p></section>'
    (dest/'itinerary_infographic.html').write_text(page('Itinerary Infographic',label+infographic+''.join(cards)+foot,'.summary{background:#e7edf5;padding:10px 20px;border-radius:12px}.card{border-left:5px solid #194872;background:#f9fbfc}'),encoding='utf-8')
    (dest/'validation_report.json').write_text(json.dumps({'valid':True,'blocks':len(checks),'selected_places':len(selected),'mapped_places':len(pins),'unlocated_places':len(unmapped),'sourced_route_geometries':len(routes)},indent=2)+'\n',encoding='utf-8')
    return len(checks),len(pins),len(unmapped),len(routes)


def main():
    if len(sys.argv) not in (2,3):
        print('Usage: python build_trip_materials.py trip.json [output_directory]',file=sys.stderr)
        return 2
    try:
        path=Path(sys.argv[1]);data=json.loads(path.read_text(encoding='utf-8'))
        output=Path(sys.argv[2]) if len(sys.argv)==3 else path.with_name(path.stem+'_materials')
        counts=render(data,output)
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print('Validation failed: '+str(exc),file=sys.stderr)
        return 1
    print('Validated and created travel materials at '+str(output)+' (blocks, mapped, unlocated, routed: '+', '.join(map(str,counts))+')')
    return 0

if __name__=='__main__':
    sys.exit(main())
