---
name: city-attraction-research
description: Research, classify, evidence-check, score, and prioritize attractions and city experiences for any destination. Use when asked for a comprehensive city must-visit inventory, ranked attractions, area-based sightseeing groups, or itineraries of different durations. Treat individual dishes and restaurant-to-dish matching as the responsibility of the separate local-food-and-dining-research skill.
metadata:
  version: "1.0.0"
---

# City Attraction Research and Ranking

Create an evidence-grounded *inventory first*, then a ranked shortlist and optional itinerary. Do not confuse "worth evaluating" with "must visit." Every attraction has **one primary category written as its complete descriptive name** and optional secondary tags. Never use single-letter category codes.

## When to use

- A traveler asks what to see, visit, or experience in a city, including Samarkand.
- A user wants systematic attraction research and transparent, comparable rankings.
- A user requests an attraction checklist usable independently or alongside a separate foods-to-try checklist.

## Do not use

- For a dish-by-dish culinary inventory, nutrition analysis, or matching dishes to restaurants: use `local-food-and-dining-research` instead.
- For live reservations: obtain real-time availability separately when tooling is available; never infer a bookable slot from a published schedule.

## Inputs and assumptions

Capture, when supplied: city/country, trip dates, full days available, first-time or repeat visit, interests, trip pace, mobility/accessibility, budget, and geographic scope. If missing, proceed with an explicitly labeled *balanced first-time visitor* baseline and keep visit selection separate from evaluation. Do not invent travel dates or accessibility needs.

## Workflow

1. **Identify the city:** Summarize five to seven dimensions of its identity, including older history and modern living culture. Establish a city/near-city/regional boundary. Separate excursions from the city inventory.
2. **Discover candidates broadly:** Search official heritage and tourism sources, local publications, museums, maps, and recent substantive visitor reports if live research is available. Seek landmark, learning, landscape, food-market, craft, residential, sacred, and modern experiences. Do not pre-cap discovery at ten famous places. Record sources and dates; flag unverified candidates rather than fabricating evidence.
3. **Define the experience unit:** Usually one site or one coherent activity. Group attractions that form one natural visitor experience (e.g. an architectural ensemble). Keep an adjoining museum and archaeological walk separate if the activities are genuinely different. Link related entries by identifiers.
4. **Classify:** Assign exactly one full-name primary category from `references/categories-and-scoring.md`, plus two to four meaningful secondary tags when warranted. Classify the *reason to visit*, not every use of the same building. Follow tie-break rules in that reference.
5. **Evaluate independently of itinerary:** Rate five dimensions on 0–5 integer scales. Apply fixed weights and compute a /100 score. A missing rating is *unscored*, not zero. Store confidence and cited sources separately from judgment. Use the full-name category in all records, examples, and output.
6. **Rank and group:** Make a transparent master ranking, with tiers Must-Visit Candidate (80–100), Highly Recommended (60–79), and Optional or Specialist Interest (below 60). Scores within five points are near ties; don't pretend a one-point gap is definitive. Inspect category coverage and avoid popularity bias.
7. **Select rather than exhaust:** Build trip-specific selections for the durations requested. Apply proximity, opening days, booking, daylight, transit, weather, walking ability, and diminishing returns. Never require someone to visit all Tier A items; reserve time for meals and breaks.
8. **Deliver and preserve:** Provide an identity profile, a classified inventory, scored ranking with rationale, separate selection(s), and geographic clusters. Include practical uncertainty/verification reminders and sources. Produce CSV/JSON when requested using `assets/attraction_inventory_template.csv`.
9. **Review:** After travel, retain objective historical attributes and revisit subjective scores, actual duration, closures, and enjoyment notes. Do not overwrite the research score with a traveler's post-visit taste score.

## Geographic research and pin-map output

Record stable `place_id`, latitude, longitude, `location_status`, `location_source_url` and `location_verified_at` when supported. A valid ranking does **not** imply a verified map point. For a request to map all researched attractions, export verified location pins separately from the candidate/checklist inventory using `python scripts/export_pins.py attraction_inventory.csv pins.geojson` where Python is available. The utility also writes `unlocated_places.csv` for unverified positions. It never guesses coordinates, creates route lines, or checks current availability. Consult [the output contract](references/output-contract.md) for exact fields. If a map renderer exists, display the sourced pin layer; otherwise return GeoJSON with an explanation of why exact pins were withheld.

When a user asks to **select and schedule** from this inventory, preserve its independent scores and hand the ranked records to [City Itinerary Builder](../city-itinerary-builder/SKILL.md) if installed; it owns final daily scheduling, sourced route maps, and printable travel materials. Remain usable without that sibling skill.

## Cross-skill boundary

`Local Cuisine and Food Markets` is the **attraction** category for markets, culinary walks, unusually noteworthy restaurants as visitor experiences, and food demonstrations. The attraction skill does **not** score individual dishes or maintain dish-to-venue recommendations. The food skill owns food records, venue profiles, and food-to-venue links. Share a stable `place_id` / `venue_id` where the same location appears in both inventories. If asked for both, run each workflow separately, then offer a combined itinerary without conflating their scores.

## Evidence and quality rules

- Cite credible sources for historical claims and present-day operating facts. Confirm opening hours, ticket prices, maintenance status, addresses, and access using recent/official sources; disclose stale or unknown details.
- Never invent businesses, prices, coordinates, opening times, official ratings, or availability.
- Scoring is reproducible **editorial judgment**, not objective measurement. Show the five ratings on request, including the assumed traveler profile.
- Preserve religious etiquette and site access constraints; don't presume working places of worship are museums.
- Use full descriptive category names everywhere (including CSV). Never assign a single-letter category code.
- Mark candidates as `candidate`, `evaluated`, `needs_verification`, or `out_of_scope` as applicable.

## References

- `references/categories-and-scoring.md` — authorized full category names, tie-break rules, five scoring dimensions and formula. Read when categorizing or scoring.
- `references/output-contract.md` — deliverable structure, inventory fields and QA checks. Read when producing tabular or machine-readable deliverables.
- `assets/attraction_inventory_template.csv` — research data schema.
- `assets/samarkand_starter.csv` — example candidate entries, **not** a verified ranking.
- `scripts/score_and_validate.py` — optional standard-library CSV scorer and category validator. Execute only if Python/file tools are available.
