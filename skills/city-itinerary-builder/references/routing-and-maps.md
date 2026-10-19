# Routing, pin maps and navigation

## Four distinct geographic outputs

- **Research pin map:** All sourced research candidates, including unselected alternatives; owned by the research skills. It does not imply visit order.
- **Selected itinerary pin layer:** A GeoJSON `FeatureCollection` containing one point per selected **verified** physical place (deduplicated on `place_id`). The builder writes `selected_places.geojson`.
- **Geographical route map:** Sourced road/walking/transit path geometries for chosen adjacent itinerary stops. The builder writes `verified_routes.geojson` only for legs with actual `LineString` geometry and evidence; a blank layer is a meaningful result. A pin sequence, straight line, or arrows on a timeline are not geographic routes.
- **Navigation link:** An external map-app destination URL for a verified coordinate. It is a handoff, not turn-by-turn directions supplied by the skill.

## Portable data contract

GeoJSON follows RFC 7946; point `[longitude, latitude]` order, WGS84. The input JSON uses separate `latitude` and `longitude` fields for readability. Require coordinates to be numeric/in range, and a source URL plus verification date for a `verified` position. Retain provisional and unlocated places in the main inventory and `unlocated_places.csv`, but withhold them from precise pins/navigation links.

For route legs, store `from_block_id`, `to_block_id`, mode, optionally provider-supplied duration/distance/geometry, source URL, and verified date. Never calculate street travel time from raw coordinate difference. Do not infer a road geometry by connecting point coordinates. If a route is unknown, route fields remain `null`.

Optional renderers may display these GeoJSON layers via a mapping host, a Leaflet or MapLibre application using a licensed/configured map-tile source, or GIS tools. Neither a tile provider nor a routing API is bundled into this skill. Do not assume public OpenStreetMap services can be used for unrestricted geocoding, tiles or routing. Do not promise offline use unless the chosen renderer has stored data and licensed tiles.

## Travel links and privacy

With verified coordinates, the script creates Google Maps `https://www.google.com/maps/dir/?api=1&destination=LAT%2CLON` links. Users may open them in an installed mapping application. Route choices and real-time travel times remain the application's responsibility. Avoid exporting nonpublic addresses/booking IDs into shareable maps without authorization.
