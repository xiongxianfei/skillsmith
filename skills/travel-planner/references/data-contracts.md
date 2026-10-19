# Data contracts and lifecycle states

Use structured records. Never invent missing values or use unverified facts as booking confirmations.

## TripBrief
`{trip_id, origin, destinations[], departure_date, return_date, travelers_count, time_zone, budget:{amount,currency,hard}, commitments:[{start,end,zone,buffer}], acceptable_airports[], baggage, recovery_windows[], priorities, assumptions[]}`

## Constraint
`{id, condition, hard:true, status:"pass"|"fail"|"pending", evidence_ref, assessed_at, notes}`. Missing is **pending**, not a pass.

## FlightOffer
`{offer_id, flight_numbers[], operating_carriers[], segments:[{departure_airport,arrival_airport,depart_local,arrive_local,zone,scheduled_aircraft}], traveler_count, cabin, hand_baggage, checked_baggage, price:{amount,currency,status}, fees, refund_terms, change_terms, provider, source_ref, observed_at}`

Price status must be `checkout_verified | advertised | derived | unknown`. Do not label a search-result fare verified unless the full comparable final checkout screen was actually observed.

## HotelOffer
`{hotel_id, property, location, room_nights, checkin, checkout, early_arrival_access, total_with_taxes, currency, cancellation_terms, source_ref, observed_at, availability_status}`

## Experience / POI
`{id,name,place_id,primary_category,secondary_tags[],location_status,address_or_coordinates,priority:"must"|"recommended"|"optional",opening_by_local_date,duration_minutes,price,reservation_requirements,source_ref,verified_at}`

Use a complete descriptive `primary_category` from the eight categories in the optional [City Attraction Research taxonomy](../../city-attraction-research/references/categories-and-scoring.md) when that sibling skill is installed; otherwise retain a full descriptive human-readable label. The previous four short codes (`historical`, `scenic`, `cuisine`, `cultural`) are no longer the canonical output contract. A related destination itinerary may be supplied by `city-itinerary-builder` with separate `places`, `days`, and sourced `legs` records; see its [input contract](../../city-itinerary-builder/references/input-contract.md) when available.

## GroundTransport
`{origin,destination,mode,journey_minutes_range,price_range,currency,payment_methods,available_hours,pickup_details,source_ref,fallback}`

## DayPlan
`{local_date,location,timezone,blocks:[{start,end,activity,transport_minutes,buffer_minutes,reservation_status,weather_backup}]}`

## BookingRecord / DecisionLog
Booking: `{item,travelers,approved_at,approved_price,currency,provider,terms_confirmed,submitted_at,provider_confirmation,booking_status}`. Decision: `{timestamp,stage,option,evidence,decision,owner,unresolved,downstream_impacts}`. Don't store account credentials or payment-card details.

## Lifecycle
```
draft -> feasibility_screen -> researching -> shortlisted -> approved_for_booking
                                                    \-> unbooked_plan
approved_for_booking -> purchase_attempted -> confirmed -> trip_ready
                     \-> action_failed | pending_confirmation
confirmed -> change_request -> reapproved -> reconfirmed
trip_ready -> in_trip -> completed -> reviewed
```

**Confirmed** requires an actual provider-issued ticket/reference or reservation confirmation, never merely a payment attempt or screenshot.

## Source metadata
Every critical price, immigration rule, closure, or transport claim should carry `source_url_or_ref`, `observed_at` (ISO with zone), `source_type`, and evidence quality. Preserve original currency plus exchange-rate source/date. Treat user-provided facts as user context; never frame them as independent provider confirmation.
