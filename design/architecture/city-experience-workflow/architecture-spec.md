# City experience workflow — architecture specification (proposed for review)

## Goal

Let travelers use independent city-attraction and food-research skills to build ranked checklists, then use a separate city-itinerary-builder to select a feasible subset using arrival/departure, existing commitments, hotel context, and sourced route data. Distinguish discovery pins, selected itinerary pins, sourced routes, infographic-style schedule views, and real navigation.

## Implemented in this proposal

- Two existing portable research skills refined with optional place IDs and location provenance; the attraction skill gains a standard-library verified-pin GeoJSON exporter.
- New `city-itinerary-builder` with portable instructions, canonical JSON example, Python validation/rendering and focused regression tests.
- Revised `travel-planner` handoff: retains trip-wide commitments, flights, accommodation, booking authorization and audits.
- Full descriptive attraction category names replace obsolete four-code POI categories.

**Not implemented:** geocoding, tile hosting, external routing providers, turn-by-turn navigation, transactions, background services, or persistent hosted state. HTML outputs are static; exported GeoJSON requires a suitable map viewer.

## Simplified research delivery contract (proposed refinement)

The two research skills remain independent and each produces **three default files**, replacing the previously contemplated 14/17-file package plan:

- City attractions: `attractions.json`, `attractions_checklist.csv`, `attractions_mymaps.csv`.
- Local food and dining: `food_research.json`, `foods_checklist.csv`, `dining_venues_mymaps.csv`.

Each canonical JSON contains all researched candidates, numeric or null weighted scores, independent location/menu statuses, full descriptive categories, stable entity/place IDs and sources; the other two files are derived. Existing scoring CLI, direct GeoJSON/My Maps exporters and location-review reports remain available **on request**, with their established flags and output formats unchanged. The itinerary builder reads these two canonical JSONs directly; no separate research package manifests, checksums, workbook or handoff files are required. This narrows the default user experience without restricting the research inventory or retiring proven map exports. File-producing hosts should run the bundled stdlib generators; unsupported file generation must be reported as partial rather than claimed successful.

## Boundary and context

The traveler supplies requirements and research or checklists to an external assistant host. The host can load any one of three passive packaged skills and may use separately connected mapping/routing providers. Skillsmith does not run a backend or grant provider permissions. The builder accepts pasted, manually verified lists if its research siblings are unavailable.

## Data and invariants

- **Identity:** stable `place_id` for physical locations, separate attraction IDs, food IDs, venue IDs and itinerary block IDs; shared markets appear once as map locations.
- **Category:** full descriptive primary category with secondary tags, separate research ranking from itinerary choice.
- **Geography:** separate latitude/longitude and `verified`, `provisional`, `unlocated` status, source and verification date. Precise pin export only for verified locations.
- **Time:** trip IANA time zone and local dated time blocks, confirmed bookings remain distinct from planned activities.
- **Route:** provider-sourced GeoJSON `LineString`, mode, duration/distance, source URL and observation date. Unknown routes retain null geometry and metrics.
- **Outputs:** map GeoJSON layers, unlocated CSV, timeline, infographic-style HTML, printable HTML guide, navigation links, practical checklist, validation report.

## Dual-platform research mapping refinement (implementation proposed for review)

The Samarkand prototype successfully imported **14 sourced coordinate-based attraction markers and five address-based dining venues into two Google My Maps layers**, as observed by the user. ChatGPT's native map failed to appear in that client. This evidence justifies a stable export-first approach, not a claim of independently verified current dining operations or a universal ChatGPT renderer.

- **Owner responsibilities:** `city-attraction-research` exports sourced point GeoJSON and `attractions_mymaps.csv`; `local-food-and-dining-research` exports physical venue records, dish–venue match information and `dining_venues_mymaps.csv`. Both output explicit location-review reports. Neither needs mapping APIs or web traffic at script runtime.
- **Optional native visualization:** a host may display a map using its own supported geographic tools; no portable skill may assume the UI exists or falsely assert successful display.
- **Physical identity and precision:** `place_id` identifies a real-world place; source URLs, ISO observation dates, `coordinate_precision` and `location_status` control point eligibility independently of `research_status` and `menu_status`. Venue-only address geocoding is labeled provisional until visually checked.
- **Separate exports first:** two-layer Google My Maps import preserves precise coordinates for attractions and text-address geocoding for venues. Optional combined export merges only matching place IDs and is an address-geocoded convenience requiring another placement review; no name-only identity matching.
- **No default tiled HTML:** downloaded maps must not silently request volunteer-run public OpenStreetMap tiles. Native ChatGPT maps and Google My Maps are distinct presentation platforms, each dependent on availability and user permissions.
- **Reimport control:** `Place ID` provides a stable matching key; reimport/update matching in My Maps can delete unmatched old features, so backup and explicit manual review are required.
- **Travel stage unchanged:** `city-itinerary-builder` retains control of selected stops, sourced travel-time legs and printable materials; research-stage pins never imply a feasible route.

This is a portable skill + data-contract change only. No automatic account access, geocoding service, cloud synchronization, routing, Google My Maps creation, or live restaurant validation is introduced.

## Consequential decisions

1. **Three skills rather than one giant skill or one per output:** research remains useful alone; builder owns scheduling and materials.
2. **No required mapping API:** portable GeoJSON and link handoff work without proprietary accounts; richer maps require an external renderer/provider.
3. **No invented straight-line routes:** exporter emits an empty route layer if routing is unknown.
4. **No separate image rewrite of schedules:** deterministic HTML comes from the same canonical itinerary record.
5. **No hidden persistence:** files are portable, and external host state is unspecified.
6. **Unverified Samarkand example:** illustrative dates/times; no real-world coordinates, opening hours or route estimates are asserted.

## Expected acceptance examples (not live-model observations)

- Research only → all ranked candidates remain available, precise pins only for verified coordinates.
- Food only → no fake coordinate on a dish; venue identity links to a physical place.
- Late arrival → no 09:00 sightseeing on a 14:00 arrival day.
- Overlapping blocks or insufficient sourced transfer gap → validation fails.
- No routing provider → empty route GeoJSON; no invented numeric time.
- Revised appointment → regenerate all derived outputs from revised itinerary JSON.
- Unverified venue menu or booking → never show it as confirmed.

## Validation and review

Focused builder tests address overlapping schedules, verified/unverified coordinates, unsourced route data, source-backed geometry, booking status and render consistency. Metadata validation does not establish real-world accuracy or model quality. D2 diagrams are proposed review sources; the D2 CLI was unavailable in the authoring environment, so D2 format/render validation is not claimed.

Human reviewers should assess stage boundaries, the taxonomy migration, location-source provenance, privacy implications of navigation URLs and practical value of the printable outputs before merge.
