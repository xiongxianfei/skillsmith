# Food and dining output contract

## Required deliverables

1. Culinary identity: specific local traditions versus regional/national/shared foods.
2. Complete candidate food inventory, organized under full category names; distinct dish variants are not inflated into separate meals without a reason.
3. Food rankings (food score /100; separate score tiers), with rationale and stated traveler baseline.
4. Venue research and a dish-to-venue table: name, matched food, evidence confidence/menu status, venue suitability **for that food** /100, location, and timing cautions.
5. Selective 1-, 2-, 3-, and 4+-day tasting suggestions; avoid excessive meals.
6. Seasonal, dietary, allergen, source, and opening-hours uncertainty.

## Three required tables

### Foods: `food_inventory_template.csv`
`food_id,city,country,name,aliases,primary_category,secondary_tags,variants,geographic_identity,local_distinctiveness,cultural_significance,culinary_distinctiveness,general_traveler_relevance,availability,food_score,priority_tier,seasonality,dietary_flags,allergen_flags,evidence_confidence,source_urls,verified_date,research_status,notes`

### Venues: `venue_inventory_template.csv`
`venue_id,city,country,name,venue_type,address,geographic_area,geo_scope,published_rating,opening_information,verification_status,source_urls,verified_date,notes`

Venues are separately researched identities/profiles. Scores tied to a specific food live in the match table, never as one supposedly universal global venue score.

### Matches: `food_venue_matches_template.csv`
`match_id,food_id,venue_id,specific_variant,signature_food_match,preparation_experience,cultural_character,practicality,evidence_confidence,venue_suitability_score,menu_status,best_time,source_urls,verified_date,notes`

- Use stable unique IDs; a food can have many venue matches and vice versa.
- `secondary_tags`, `source_urls`, `aliases`, and `variants` use semicolons as CSV separators.
- An unverified menu or unavailable dish must not be represented as a confirmed match.
- An unrated food or match has blank rating fields and score; unknown is never zero.

## Crosswalk and QA

- Food venue can share a real place identifier with a record in city-attraction research; never force identical attraction and venue-match scores.
- Look for duplicates due to spellings and transliterations: `somsa/samsa`, `non/nan`, etc.
- Confirm current venue existence and menu before a booking or definite recommendation.
- If sources are not available, provide a draft candidate list and explicit verification flags, not fabricated certainty.
- Do not falsely present a national dish as a unique city invention.
- Food preference, safety and personal appeal are post-research filters, not revisions of a city's culinary significance.
