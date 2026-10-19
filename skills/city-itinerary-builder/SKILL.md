---
name: city-itinerary-builder
description: >
  Build practical city sightseeing and food itineraries from researched attraction and food
  shortlists, arrival/departure arrangements, reservations, and traveler preferences.
  Use for selecting stops, scheduling feasible city days, mapping sourced locations and
  routes, and producing timelines, printable guides, infographic-style plans, navigation
  links and practical checklists. Works with or without separately installed research skills.
compatibility: Agent Skills-compatible host. Python 3.9+ standard library for optional itinerary validation and HTML/GeoJSON/CSV generation; real route times and live venue access require external providers.
metadata:
  version: "1.0.0"
  category: "travel"
---

# City Itinerary Builder

## Purpose and boundaries

Turn **already-researched options** and **actual travel arrangements** into a realistic, editable city itinerary. The skill operates independently: accept pasted checklists or machine-readable exports when the research skills are unavailable. The itinerary is the single source of truth for maps, timelines, infographic-style layouts, printable guides and navigation links. **Never fabricate** a road route, travel duration, hotel booking, admission ticket, venue menu or opening hours.

This skill owns city **selection, scheduling, route feasibility and itinerary materials**. It does not redo full city attraction research (`city-attraction-research`), independently rank dishes or venue matches (`local-food-and-dining-research`), or take over broader flight, hotel, payment and trip-wide booking work (`travel-planner`). When research is absent, create a **provisional** candidate plan with explicit missing evidence, not a fabricated researched ranking.

## Inputs

Collect what is known: city/country, local time zone, dates, exact arrival/departure times and terminals/locations, hotel location and check-in/out, prior tickets/reservations and fixed commitments, number of travelers, desired pace and interests, dietary/accessibility constraints, transport preferences, ranked attraction checklist, ranked food checklist and venue matches. Do not request sensitive documents or payment credentials. When unknown details are non-blocking, make the draft provisional and mark them for verification. Read [references/input-contract.md](references/input-contract.md) when converting checklists or bookings into structured records.

## Workflow

1. **Protect commitments first:** Put flights/arrival transfers, hotel access, fixed bookings, required rest, and departure buffers into time constraints. Label confirmed, pending and unverified arrangements distinctly.
2. **Choose, do not exhaust:** Select a manageable subset from attraction and food lists using personal interest, independent research scores, diversity, available meal slots, costs, geographic convenience and diminishing returns. Store skipped alternatives without changing their research ranking.
3. **Validate geography:** Reuse one stable `place_id` for a market appearing in both research sources. Include verified coordinates with provenance only; never guess unknown coordinates or conflate a neighborhood with a building entrance. Use [references/routing-and-maps.md](references/routing-and-maps.md) when mapping.
4. **Build a local-time itinerary:** For each day, include chronological blocks, durations, necessary transfers and rest. Verify site opening on the exact local date and meal service. Use actual routing-tool distances and times when available; if unavailable, leave metric fields null and flag the transfer as needing verification. Do not let a schedule with unsupported tight transfers appear confirmed. Read [references/selection-and-scheduling.md](references/selection-and-scheduling.md) when selecting and scheduling.
5. **Check feasibility:** Reject overlapping blocks, impossible sourced transfers, wrong time zones, incompatible opening/booking windows, and missing hard-constraint handling. Never label an itinerary `booked` simply because it is planned.
6. **Build a canonical itinerary:** Use [assets/samarkand_itinerary_example.json](assets/samarkand_itinerary_example.json) for the **shape only**, not factual location or opening-hour evidence. Preserve dates, place IDs, source references and current arrangement state. Read [references/output-contract.md](references/output-contract.md) when generating deliverables.
7. **Render requested outputs from that record:** With Python/file access, run `python scripts/build_trip_materials.py itinerary.json output_dir`. This validates and generates printable HTML travel guide, timeline HTML, infographic-style HTML, practical checklist CSV, source-backed GeoJSON point/route layers, unlocated-place report, and navigation links. The script does not geocode, route, print PDF, or make bookings. Without executable tools, produce a consistent textual itinerary and structured JSON, stating which artifacts are not available.
8. **Revise safely:** A change to timing, location, booking, or selection updates the canonical record first, then all derived outputs. Treat itinerary revisions and new research evidence as different processes.

## Output levels

- **Quick draft:** feasible-looking, clearly provisional schedule plus blockers/uncertainties and selected alternatives.
- **Validated itinerary:** structured blocks and sourced practical constraints; still distinguish booking from planning.
- **Travel materials:** only the requested outputs—checklist, navigation links, timeline, infographic-style HTML and printable guide. Map pins only for verified locations; route geometry only with a sourced routing response. Static HTML is not turn-by-turn navigation.

## Verification and safety

- Do not treat a location name, general web search result, or illustrative example as a verified coordinate. Real-time hours, menus, road closures, and service disruptions must be checked when pertinent and possible.
- Keep all dates local with IANA time zone and explicit cross-day transitions. The script intentionally rejects an activity that crosses midnight; split it into separate day blocks.
- If a route provider or geocoder is unavailable, show the itinerary with an **unlocated** report and empty route layer rather than draw straight-line road connections.
- Navigation links open a separate map application at sourced coordinates; they do not guarantee a viable route, provider availability, or mode-specific navigation.
- Treat maps, itineraries, guides and images as separate *views of the same factual plan*. Avoid image-based generation of critical schedule text that may silently alter times or spellings.
- Review privacy before exporting home/hotel addresses, private booking notes, or sharing itineraries publicly.

## References and validation

- [Input contract](references/input-contract.md): accepted research records, fixed arrangements, and canonical example schema.
- [Selection and scheduling](references/selection-and-scheduling.md): independent ranking versus marginal itinerary value; capacity and feasibility.
- [Routing and maps](references/routing-and-maps.md): GeoJSON, provenance, pin map versus route, navigation and fallback.
- [Output contract](references/output-contract.md): generated files, validation, extension points, and QA.
- Example: [Samarkand itinerary JSON](assets/samarkand_itinerary_example.json), an **unverified illustrative draft** with no fabricated coordinates or route metrics.
- Optional renderer: `python scripts/build_trip_materials.py <itinerary.json> [output_dir]`; standard library only.
- Focused tests: `python -m unittest discover -s tests -v` from this skill directory. Tests cover example and failure cases; they do not prove live routing or historical research accuracy.
