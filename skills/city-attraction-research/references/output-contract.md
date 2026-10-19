# Attraction output contract

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

## Release checklist

- All primary categories match the full labels exactly; no letter codes.
- IDs are unique and duplicate place/experience units are resolved.
- Rank only fully rated records; separate pending research.
- No claim of live opening hours, availability, ticket prices or access without evidence.
- Claims about history and recent changes have traceable sources.
- Balanced selection is an *output*, not a forced input into intrinsic scoring.
