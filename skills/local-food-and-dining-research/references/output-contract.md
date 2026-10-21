# Food and dining output contract

## Default delivery contract (three files)

Run `python scripts/generate_research.py foods.csv venues.csv matches.csv OUTPUT_DIR`. It uses the skill's existing CSV schemas, scoring constants, and venue map exporter. The command requires Python 3.9+ standard library only and does not geocode or check live menus.

- `food_research.json`: `schema_version: "1.0"`, `dataset_type: "food_and_dining"`, `foods[]`, `venues[]`, `food_venue_matches[]`, `mapping`. Each food contains stable `food_id`, full `primary_category`, geographic identity, tags/aliases/variants, five `ratings`, computed `food_score` (number or null), priority tier, and source evidence. Each venue retains its `venue_id`, physical `place_id`, address and verification fields. Each food–venue pair retains its independent five `ratings`, `venue_suitability_score` (or null), `menu_status` and dish-specific sources. `mapping` records mapped and withheld venues and precise-coordinate count.
- `foods_checklist.csv`: `food_id,rank,name,primary_category,geographic_identity,food_score,priority_tier,review_decision,review_notes`. All foods included; unscored items have blank rank/score/tier and all initial review decisions are `undecided`.
- `dining_venues_mymaps.csv`: existing My Maps import format, only for documented locations. Address matches remain provisional until visually checked; no venue score is substituted for a food score, and unscored pair scores stay blank.

Only the three files appear in the new default output directory. The existing `score_and_validate.py` and `export_venues_mymaps.py` commands remain optional and continue to generate their historical files. Reject duplicate IDs, invalid food categories, partial ratings, inconsistent scores, broken food–venue references, and scored matches with unsupported menu status or missing dish-specific source. Do not invent missing locations or food availability.

## Required deliverables

1. Culinary identity: specific local traditions versus regional/national/shared foods.
2. Complete candidate food inventory, organized under full category names; distinct dish variants are not inflated into separate meals without a reason.
3. Food rankings (food score /100; separate score tiers), with rationale and stated traveler baseline.
4. Venue research and a dish-to-venue table: name, matched food, evidence confidence/menu status, venue suitability **for that food** /100, location, and timing cautions.
5. Selective 1-, 2-, 3-, and 4+-day tasting suggestions; avoid excessive meals.
6. Seasonal, dietary, allergen, source, and opening-hours uncertainty.

## Existing source CSV formats (inputs and optional legacy commands)

### Foods: `food_inventory_template.csv`
`food_id,city,country,name,aliases,primary_category,secondary_tags,variants,geographic_identity,local_distinctiveness,cultural_significance,culinary_distinctiveness,general_traveler_relevance,availability,food_score,priority_tier,seasonality,dietary_flags,allergen_flags,evidence_confidence,source_urls,verified_date,research_status,notes`

### Venues: `venue_inventory_template.csv`
`venue_id,city,country,name,venue_type,address,geographic_area,geo_scope,published_rating,opening_information,verification_status,source_urls,verified_date,notes`

A venue may additionally include `place_id,latitude,longitude,location_status,location_source_url,location_verified_at,map_address,coordinate_precision` after the base CSV fields. `map_address` is a clean, **manually checked candidate address** for Google My Maps, not a coordinate claim. `place_id` identifies the physical location; `venue_id` identifies a venue entity. Address-only pins remain `address_based_provisional` and need a manual visual check after My Maps geocoding. Coordinate precision, place verification, research status, operational status and menu status are separate concerns. Match records reference venue IDs; multiple foods can share one physical `place_id`.

Venues are separately researched identities/profiles. Scores tied to a specific food live in the match table, never as one supposedly universal global venue score.

### Matches: `food_venue_matches_template.csv`
`match_id,food_id,venue_id,specific_variant,signature_food_match,preparation_experience,cultural_character,practicality,evidence_confidence,venue_suitability_score,menu_status,best_time,source_urls,verified_date,notes`

- Use stable unique IDs; a food can have many venue matches and vice versa.
- `secondary_tags`, `source_urls`, `aliases`, and `variants` use semicolons as CSV separators.
- An unverified menu or unavailable dish must not be represented as a confirmed match.
- An unrated food or match has blank rating fields and score; unknown is never zero.

## Optional direct Google My Maps dining export command

Run `python scripts/export_venues_mymaps.py dining_venues.csv foods_scored.csv food_venue_matches.csv output/`. This independently produces:

- `dining_venues_mymaps.csv`: physical venues with `Place ID`, `Venue ID`, `Name`, `City`, `Country`, `Map Address`, full descriptive `Primary Category`, `Recommended Foods`, **pair-specific** `Food–Venue Match Score`, `Menu Verification Status`, `Geocoding Status`, source and review date. Unscored matches remain blank; an unknown dish is never marked verified.
- `dining_venues.geojson`: precise pins **only** for verified source-backed coordinate pairs.
- `dining_needs_location_review.csv`: missing/ambiguous/unsupported venue positions and the needed follow-up.

To import, choose **`Map Address`** (not partially blank Latitude/Longitude columns) as Google My Maps location field and `Name` as label. Google geocoding is not proof of branch identity: manually review all imported venues. A native ChatGPT map can be offered if the host supports it, but is not required or guaranteed. Follow `references/mapping-and-mymaps.md`. No custom downloadable HTML map is required.

## Crosswalk and QA

- Food venue can share a real place identifier with a record in city-attraction research; never force identical attraction and venue-match scores.
- Look for duplicates due to spellings and transliterations: `somsa/samsa`, `non/nan`, etc.
- Confirm current venue existence and menu before a booking or definite recommendation.
- If sources are not available, provide a draft candidate list and explicit verification flags, not fabricated certainty.
- Do not falsely present a national dish as a unique city invention.
- Food preference, safety and personal appeal are post-research filters, not revisions of a city's culinary significance.
