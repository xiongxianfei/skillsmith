# City Itinerary Builder — input and canonical record

## Independent inputs

The skill accepts (a) user-supplied arrival/departure/hotel/commitment details and (b) attraction and food inventories from any credible source. Structured files are optional; a pasted checklist can be normalized into the canonical JSON model. Do not require sibling skill installation.

Research records should provide **stable IDs, a full descriptive primary category, priority/score, place identity, source evidence, estimated visit duration**, and verification status. Food-to-venue records should additionally provide the food ID, venue ID and **pair-level** suitability evidence. A dish has no single coordinate; choose a mapped venue first. **Research score and trip-specific selection status remain separate.**

## Canonical JSON (version 1.0)

See `../assets/samarkand_itinerary_example.json`. Fields:

- `version`: `"1.0"`.
- `trip`: `id`, `city`, `country`, `timezone` (IANA), `start_date`, `end_date` (`YYYY-MM-DD`), and `status` (`draft`, `reviewed`, or `final_plan`; does not equal *booked*).
- `places[]`: `place_id`, `name`, `primary_category` (full name), optional `address`, `latitude`, `longitude`, `location_status` (`verified`, `provisional`, `unlocated`), `location_source_url`, `location_verified_at`. Both coordinates or neither. Verified coordinates require a source and date.
- `days[]`: `date` and chronological `blocks[]` with unique `block_id`, `start` and `end` in local `HH:MM`, `kind` (`arrival`, `departure`, `attraction`, `food`, `rest`, `transfer`, `appointment`, `lodging`, `other`), `title`, optional `place_id`, optional `research_id`, `state` (`planned`, `selected`, `completed`, `skipped`), `booking_status` (`confirmed`, `pending`, `unverified`, `not_required`), and optional `notes`.
- `legs[]`: `from_block_id`, `to_block_id`, `mode` (`walking`, `driving`, `cycling`, `transit`, `other`), optional `duration_minutes`, `distance_meters`, `route_geometry` (GeoJSON `LineString`), `source_url`, `verified_at`. Duration/distance/geometry may be non-null **only when supported by source and verification date**.

Trip-specific constraints should be represented as real itinerary blocks (for example, a confirmed restaurant reservation with `booking_status="confirmed"`). Retain separate sensitive booking details privately; do not leak them into shared infographic outputs.

## Coherence requirements

`place_id` denotes the **physical place**, not the food or an appointment. When Siyob Bazaar is linked to both attraction and dining records, use one place record. Keep stable research IDs in `research_id` on blocks so itinerary decisions remain traceable. Locations may be `unlocated` yet still schedulable as provisional—do not silently plot them.

Use whole-hour or minute-local time blocks; split cross-midnight events across days. For multi-time-zone trips, create a city-specific plan per zone or explicitly resolve each leg before localizing; do not assume one zone for flights elsewhere.
