# Research maps — ChatGPT and Google My Maps

Read this file when the user requests a map or map export. Research scores and visit selection remain separate.

## Supported output tiers

1. **Google My Maps CSV is the portable default**: generate `attractions_mymaps.csv` from sourced geographic records using `scripts/export_pins.py`. The export must work with no API key, network, HTML tiles or map renderer.
2. **ChatGPT native pin map is optional**: only request an official host mapping visualization when its capability exists. Use evidence-backed business references or verified location records. If it does not render, do not claim a successful map or repeatedly fabricate widget calls; provide My Maps CSV and a readable place list. A skill is not an API to ChatGPT-specific UI components.
3. **GeoJSON**: retain `attractions.geojson` (or named output) for compatible viewers. Coordinates are WGS84 `[longitude, latitude]`; they are not road route data.
4. **Location review**: `attractions_needs_location_review.csv` lists omitted candidates and their precise issues. Keep the complete scored inventory independent of map coverage.

## Physical place identity and verification

- `attraction_id` identifies a visitor experience; `place_id` identifies one physical location. Do not infer that name equality proves same physical location.
- `location_status` is `verified`, `provisional`, `ambiguous` or `unlocated`. Only `verified` coordinate pairs with their URL and verification date may become precise pins. The exporter rejects invalid/infinite/out-of-range/null-island coordinates and conflicting coordinates for a shared ID.
- `coordinate_precision` should indicate `entrance`, `building`, `site_center` or `area`; if absent, explicitly disclose that an entrance has **not** been confirmed.
- `research_status` (whether the attraction itself is fully researched) is independent from `location_status`. A sourced position does not guarantee current opening/access.
- A district walk or route is not a building pin; leave it unlocated until there is an appropriate meeting point or sourced geometry.
- For cities with a known spatial boundary, use the optional `--bbox minlon,minlat,maxlon,maxlat` to flag out-of-city coordinates in the review report. Never guess geographic bounds.

## Command and files

```sh
python scripts/export_pins.py attraction_inventory.csv attractions.geojson
# Optional source-confirmed geographic envelope:
python scripts/export_pins.py attraction_inventory.csv attractions.geojson --bbox 66.8,39.5,67.2,39.85
```

The script also creates `attractions_mymaps.csv`, `attractions_needs_location_review.csv` and `unlocated_places.csv` next to the GeoJSON. The original optional third positional argument for legacy unlocated CSV remains supported.

## Google My Maps manual import and updates

1. Open https://www.google.com/maps/d/ on desktop, create a map, and add an `Attractions` layer.
2. Import `attractions_mymaps.csv`; select `Latitude` and `Longitude` as location columns, and `Name` as title.
3. Verify imported marker positions, especially entrances and third-party coordinates. Set styles by `Primary Category` or `Priority Tier` if desired.
4. To update an existing layer, **back up the map first**. Use Reimport and merge → Update matching items with `Place ID` from both old and new layers. Google's current behavior can delete old unmatched features and preserve matched custom styles; always inspect before accepting.
5. Do not claim import, successful geocoding, updated styles, or persistent synchronization unless the user or connected map provider confirms it.

Official instructions: https://support.google.com/mymaps/answer/3024836?hl=en (CSV import, up to 2,000 rows, reimport/update matching items).

## Combined attraction and food map

Use the standalone `scripts/combine_mymaps.py` **only when both exported research layer CSVs are available**:

```sh
python scripts/combine_mymaps.py attractions_mymaps.csv dining_venues_mymaps.csv combined_output/
```

It merges only exactly matching, explicitly shared `Place ID` values; it never invents cross-skill identity matches. The combined CSV is a convenience review view with potentially mixed address/coordinate placement. For maximum position accuracy in Google My Maps, **import the two independent layer CSVs**, since attractions use coordinates and dining venues often rely on address matching. If importing the combined single-layer CSV, select `Map Address` and visually review all place-name matches.

Do not include API keys, geocoding, custom Leaflet/Folium HTML maps or direct `tile.openstreetmap.org` calls as automatic defaults. A route map and travel-time calculation belong to `city-itinerary-builder` and need a real routing provider.
