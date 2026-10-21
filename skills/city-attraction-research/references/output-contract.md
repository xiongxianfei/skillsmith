# Attraction output contract

## Default delivery contract (three files)

Run `python scripts/generate_research.py attraction_inventory.csv OUTPUT_DIR`. It requires Python 3.9+ standard library, the skill's existing scorer/map exporter, and the current [attraction inventory CSV template](../assets/attraction_inventory_template.csv) as input. Existing scoring and mapping commands stay available separately.

- `attractions.json`: `schema_version: "1.0"`, `dataset_type: "attractions"`, `city`, `country`, `attractions[]`, `mapping`. Each attraction retains `attraction_id`, full `primary_category`, `secondary_tags[]`, `ratings` (five integers or nulls), computed `weighted_score` (number or null), `priority_tier` (or null), `place_id`, optional sourced coordinates and status, `estimated_minutes` (integer or null), `source_urls[]`, and other input research metadata. `mapping` records the mapped count, withheld count and withheld reasons.
- `attractions_checklist.csv`: `attraction_id,rank,name,primary_category,weighted_score,priority_tier,estimated_minutes,review_decision,review_notes`. All entries included. Unscored ones have blank rank/score/tier; every initial review decision is `undecided`.
- `attractions_mymaps.csv`: original Google My Maps coordinate export and full descriptive categories, generated only for verified source-backed pins. It may contain only headers when no locations qualify.

Only these three appear in the new default output directory. The legacy `export_pins.py` command continues to generate optional GeoJSON and location-review files when invoked directly. Map warnings are also preserved in the JSON rather than hidden. Reject invalid categories, partial ratings, score mismatches, duplicate attraction IDs, and unsourced `verified` coordinates. No automated research or current map service is implied by the generator; the AI must supply evidence-backed input CSV records first.

## Required narrative outputs

1. City identity (five to seven grounded dimensions).
2. Search coverage and notable unverified candidates; state if inventory is partial.
3. Full primary-category taxonomy with exact descriptive labels.
4. Master ranked table of evaluated entries: name, primary category, key tags, five ratings on request, /100 score, tier, short why-visit rationale and estimated time.
5. Separate itinerary choices for the user's trip duration. Favor geographic continuity and category diversity; never equate the entire research inventory with a mandatory sightseeing schedule.
6. Practical verification section: booking, closures, accessibility, location, source dates.

## Inventory fields

`attraction_id,city,country,name,entry_type,primary_category,secondary_tags,geographic_area,geographic_scope,estimated_minutes,city_distinctiveness,traveler_relevance,experience_quality,historical_cultural_value,practical_value,weighted_score,priority_tier,evidence_confidence,source_urls,verified_date,research_status,related_ids,notes`

- `entry_type`: `place`, `activity`, `event`, or `route`.
- `geographic_scope`: `city`, `near_city`, or `regional`.
- `secondary_tags`: semicolon-separated values in CSV.
- `evidence_confidence`: `high`, `medium`, `low`, or `unverified` and **not** a substitute for the score.
- `source_urls`: multiple URLs separated by semicolons.
- Blank score inputs mean not yet evaluated. Empty `weighted_score` and `priority_tier` remain blank.
- `research_status`: `candidate`, `evaluated`, `needs_verification`, `out_of_scope`.

## Optional geographic export

The CSV may include `place_id,latitude,longitude,location_status,location_source_url,location_verified_at,coordinate_precision` after the existing research fields. A `place_id` is a stable identity for a physical location, potentially shared with the food inventory. Location status is independent from `research_status` and uses `verified`, `provisional`, `ambiguous`, or `unlocated`. A verified coordinate pair requires a source URL and ISO date; `coordinate_precision` can be `entrance`, `building`, `site_center`, or `area`, with unknown precision left explicitly uncertain.

Run `python scripts/export_pins.py attraction_inventory.csv attractions.geojson`. The exporter generates:

- `attractions.geojson`: verified points only, WGS84 longitude/latitude order, without road routes.
- `attractions_mymaps.csv`: Google My Maps layer with `Place ID`, `Name`, `City`, `Country`, `Latitude`, `Longitude`, full `Primary Category`, `Attraction Score`, `Priority Tier`, research/provenance links and location status.
- `attractions_needs_location_review.csv`: withheld entries with concrete reason and follow-up.
- `unlocated_places.csv`: legacy place/name/reason report (backward compatible).

Import into Google My Maps selecting `Latitude` and `Longitude` for location and `Name` for marker labels. A native ChatGPT map is optional; if the host cannot render it, do not present a broken HTML stand-in or claim it was displayed. Follow `references/mapping-and-mymaps.md`. A map pin does not verify opening hours, correct entrance, or a visit booking.

## Release checklist

- All primary categories match the full labels exactly; no letter codes.
- IDs are unique and duplicate place/experience units are resolved.
- Rank only fully rated records; separate pending research.
- No claim of live opening hours, availability, ticket prices or access without evidence.
- Claims about history and recent changes have traceable sources.
- Balanced selection is an *output*, not a forced input into intrinsic scoring.
