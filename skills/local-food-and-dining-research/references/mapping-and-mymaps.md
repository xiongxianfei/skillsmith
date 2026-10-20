# Dining venue maps — ChatGPT and Google My Maps

Read this file when the user asks to map food venues, restaurants, bakeries, street-food vendors or dining recommendations.

## Map objects and scores

A **dish is never a geographic pin**. Map researched physical venues, linked to food-to-venue match records and their *pair-specific* scores; do not present a dish's cultural score as a restaurant rating. Preserve `menu_status` (`verified`, `plausible_needs_confirmation`, `not_yet_researched`) and do not infer current serving from a historic menu.

`venue_id` identifies a business/venue record. `place_id` identifies a physical place, potentially also in the attraction inventory (e.g. a bazaar). Multiple dish matches attach to the same venue pin. Different branches require separate venue identities.

## Location evidence and eligibility

- For exact coordinates, `location_status=verified` requires a finite numeric latitude/longitude pair, non-null source URL and ISO verification date. Do not derive coordinates from address text or guess an entrance.
- For Google My Maps, address-based pins can be **provisional**: only export a credible unambiguous full address, with location source and date. Prefer a manually curated `map_address` field that removes reporter commentary from `address` and identifies the correct branch. The converter rejects annotated/incomplete addresses unless an explicit clean `map_address` is given.
- Address matching occurs **inside Google My Maps**, not within Skillsmith. An address-based venue must display `address_geocoded_by_google_needs_visual_review` until the user checks the actual pin. A successful import does not verify the menu, hours or operation.
- If a venue has verified coordinates but no suitable street address, the exporter may output the sourced place name as `Map Address`, tagged `provider_name_lookup_needs_review`; this is not proof of Google geocoding accuracy.
- If geographic identity is uncertain, keep the venue in the research inventory and list it in `dining_needs_location_review.csv`. No arbitrary approximate pin.

## Command and outputs

```sh
python scripts/export_venues_mymaps.py dining_venues.csv foods_scored.csv food_venue_matches.csv output/
```

Generates `dining_venues_mymaps.csv`, `dining_needs_location_review.csv`, and `dining_venues.geojson` (the GeoJSON includes **only** verified coordinate points). The script uses Python standard library only, has no network access or API keys, and never checks actual current menus.

On desktop open https://www.google.com/maps/d/, create a `Dining Venues` layer and import the CSV selecting `Map Address` for position and `Name` for marker title. **Do not select Latitude/Longitude for a mixed address-based dining file with blank coordinate cells.** Visually check each venue branch after import.

Google's official instructions are at https://support.google.com/mymaps/answer/3024836?hl=en. They specify supported CSV imports, up to 2,000 rows per import, and matching-item reimports. When updating an existing map, back up first and match by stable `Place ID`; unmatched old items may be deleted.

If the AI host offers native ChatGPT maps, it can show the verified venue points and supported provider business references as an optional convenience. The portable skill **cannot guarantee that UI is enabled or that it rendered**. Always supply My Maps CSV when requested, or when the native map is not visible. Do not generate HTML with public OpenStreetMap tile URLs by default.

A combined city map can be requested later using the attraction skill's optional `combine_mymaps.py`. This food skill remains independently usable without that sibling. Detailed itinerary routes belong to `city-itinerary-builder`, not research-stage venue mapping.
