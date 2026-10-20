---
name: local-food-and-dining-research
description: Research and classify a city's local dishes, drinks, and culinary experiences, score foods and venue suitability separately, and link each food to evidence-backed places to try it. Use for must-try food inventories, regional specialty comparisons, food checklists, culinary itineraries, and restaurant-to-dish matching. Run independently or alongside city-attraction-research without duplicating attraction rankings.
metadata:
  version: "1.1.0"
---

# Local Food and Dining Research

Build **two connected but distinct research layers**: (1) foods and drinks, (2) verified venues and food-to-venue recommendations. Do not mistake a famous dish for an endorsed restaurant, and do not treat the full food inventory as a mandate to eat everything. Use **full descriptive primary category names**, never single-letter category codes.

## When to use

- A traveler requests a comprehensive foods-to-try list for a city such as Samarkand.
- A user wants dish classification, city-specific versus national identity, evidence-based ranking criteria, restaurant suggestions, market tastings, or culinary activities.
- A user wants a repeatable culinary database and separate food, venue, and match evaluations.

## Do not use

- For primarily sightseeing attractions or historical-monument ranking: use `city-attraction-research`.
- For medical dietary advice, allergy guarantees, or health claims: do not infer safety from a traditional recipe; obtain relevant qualified information.
- For live restaurant reservations: use a real-time reservation source separately and do not invent times.

## Inputs and assumptions

Use specified city and country, season and dates, preferred foods, dietary restrictions, allergies, alcohol preferences, budget, and meal capacity. When not given, make clear that the baseline is a *balanced, omnivorous first-time visitor* research profile, not a personalized dietary plan. Maintain nonalcoholic alternatives. Never imply a venue can accommodate an allergy without explicit evidence.

## Workflow

1. **Define scope and culinary identity:** Capture city, regional, national, and shared/cross-border culinary influences. Distinguish foods with a documented local preparation from foods that are broadly national; avoid unfounded exclusive-origin claims.
2. **Discover food candidates:** Research local publications, tourism and heritage references, cookery traditions, credible menus, markets, and current reports. Include substantial dishes, bread, snacks, soup, produce, desserts, nonalcoholic drinks, and seasonal specialties. Record names and transliterations as aliases rather than duplicate foods.
3. **Normalize food units:** Each row represents a meaningful dish, drink or food family. Put minor fillings/cuts/variants in `variants` or `secondary_tags`. Give a variation its own row only if technique, cultural role, or eating experience substantially differs.
4. **Classify foods:** Assign exactly one full-name category from `references/food-categories-and-scoring.md`. Add secondary tags and `geographic_identity` (`city_specific_style`, `regional`, `national`, or `shared_cross_border`). Never use single-letter category codes.
5. **Score foods independently of venues:** Use five integer 0–5 ratings and food-specific weights, then derive 0–100 score and priority tier. Unresearched foods remain unscored, not zero. Record editorial rationale and source confidence.
6. **Discover and verify venues:** Maintain venue profiles with names, addresses, type, location, source URLs, verification date, opening/menu uncertainty, accessibility, and status. Search independently for dish-specific evidence. Do not invent actual restaurant existence or attribute dishes on guesswork.
7. **Evaluate food–venue matches separately:** For **each dish–venue pair**, score match quality, preparation evidence, cultural character, practicality, and evidence confidence. The resulting 0–100 **venue suitability for this food** is not a global restaurant rating. If a venue serves multiple dishes, create multiple match rows; do not copy the same score without assessment.
8. **Build selections:** Offer shortlists for 1, 2, 3 and 4+ days or dates supplied. Combine market samples and tea with meals; avoid scheduling multiple substantial meals solely to tick boxes. Consider seasonal availability, meal timing, closures, dietary safety, and geographic clusters.
9. **Deliver and refresh:** Provide a fully categorized food inventory, transparent food scores, a separate food-to-venue match table with evidence status, and an optional practical tasting plan. Recheck current menus and access just before travel. The inventory can remain comprehensive while the visit plan is selective.

## Geographic venue handoff

A dish is **not a map point**. Every map pin represents a researched physical venue and links food matches to that location. Maintain stable `place_id`, `venue_id`, sourced coordinates (when available), clean `map_address` (when using address-based Google My Maps placement), and independent location/menu/operation statuses. For map requests, read [mapping and My Maps reference](references/mapping-and-mymaps.md). Run `python scripts/export_venues_mymaps.py dining_venues.csv foods_scored.csv food_venue_matches.csv output/` when Python/file tools are available; it writes Google My Maps CSV, GeoJSON only for sourced coordinates, and a withheld-location report. **Addresses resolved by Google remain provisional until reviewed**, regardless of venue-match score. Native ChatGPT map display is optional and must never be asserted as visible when unsupported. Avoid downloadable HTML maps with public OpenStreetMap tile URLs. See [the output contract](references/output-contract.md).

For a combined destination-day plan, pass the ranked food inventory, verified venue identities and food–venue matches to [City Itinerary Builder](../city-itinerary-builder/SKILL.md) if installed; it owns meal scheduling, feasible routes and travel materials. This food skill remains independently usable when that sibling skill is absent.

## Cross-skill boundary

`city-attraction-research` owns the attraction category `Local Cuisine and Food Markets` for markets, food walks, and distinctive cooking experiences **as places to visit**. This skill owns individual **foods and drinks**, **venue profiles**, and **dish-to-venue suitability**. Reuse a shared place/venue identifier for overlaps, and keep food /100 scores distinct from attraction /100 scores and venue-match /100 scores. When running independently, do not require the other skill's files.

## Research quality rules

- Source regionality carefully: `Samarkand-style plov` may be city-associated, while generic plov belongs to a wider tradition.
- Cite sources for dish identity and live venue claims; flag uncertain regional attributions, menu items, opening hours, dish availability, and seasonal foods.
- Separate rating criteria from popularity, social-media virality, and generic restaurant review scores.
- Store allergens and dietary information as non-guaranteed indicators; verify ingredients, preparation, and cross-contact directly. Never promise safety.
- Treat no venue score as universal; suitability must name the *particular food/experience*.
- Use full descriptive category names in prose, tables, templates, and structured outputs.

## References

- `references/food-categories-and-scoring.md` — complete food categories, geographic attribution, food and venue-match scoring weights. Read when classifying or scoring.
- `references/output-contract.md` — three-table data contract, matching rules, and quality checks. Read when producing tabular or machine-readable deliverables.
- `assets/food_inventory_template.csv`, `assets/venue_inventory_template.csv`, `assets/food_venue_matches_template.csv` — blank compatible schemas.
- `assets/samarkand_food_starter.csv` — illustrative candidate foods only, not an audited list.
- `references/mapping-and-mymaps.md` — read for venue maps and CSV exports, address review, native-host fallback and Google My Maps import.
- `scripts/export_venues_mymaps.py` — generates `dining_venues_mymaps.csv`, verified-only GeoJSON and review report without geocoding.
- `scripts/score_and_validate.py` — optional CSV validation and scoring with Python standard library. Execute only if Python/file tools are available.
