# Itinerary outputs and quality contract

## Canonical source and artifacts

Read the user-provided/constructed `itinerary.json` as **the only factual itinerary record**. When Python execution is available, run `scripts/build_trip_materials.py` to validate and produce:

| File | Meaning |
| --- | --- |
| `selected_places.geojson` | Verified selected pins, unique by place ID, not a complete research pin map |
| `verified_routes.geojson` | **Only** sourced geographic route geometry; empty layer if unavailable |
| `unlocated_places.csv` | Selected physical places withheld from precise mapping |
| `practical_checklist.csv` | All chronological itinerary blocks with planned/completed/skipped and booking states |
| `itinerary_timeline.html` | Local-time chronological day-by-day cards |
| `itinerary_infographic.html` | Typography-based graphical daily plan; no fabricated imagery or facts |
| `printable_travel_guide.html` | Printer-friendly HTML schedule; use browser Print → Save as PDF when needed |
| `navigation.md` | External destination links only for sourced coordinates |
| `validation_report.json` | Counts of itinerary blocks, mappable places, unlocated places, sourced route geometries |

The three HTML documents are self-contained (inline CSS, no CDN). They remain readable offline, but external navigation links need a functioning map application/network. Geographic basemap tiles and full navigation are deliberately **not** embedded. Render the GeoJSON using a suitable provider if a visual map is requested and supported.

## Validation boundaries

Validator checks input schema essentials, IANA zone, date/time formatting, sorted/nonoverlapping blocks, unique IDs, place references, coordinate ranges, sourced geometry/metrics and whether sourced durations fit the available transfer interval. It **cannot** independently confirm a restaurant opening time, route reliability, flight arrival, venue accessibility, or the truth of an external source. A `valid=true` file means **structurally consistent**, not **booked** or **all assumptions verified**.

Before releasing a plan, confirm critical opening hours, reservations, local travel and traveler constraints with sources. If tools are absent, give readable text and structured data plus explicit omissions.

## Regression scenarios

- Unknown or ambiguous location → not mapped; still listed in unlocated report.
- Two research records for the same market → one selected physical pin.
- No routing service → empty `verified_routes.geojson`, no invented time.
- Verified journey longer than calendar gap → reject plan.
- Schedule change → regenerate timeline/guide/infographic from revised canonical JSON, never edit outputs separately.
- Booking pending → display pending, never confirmed.
