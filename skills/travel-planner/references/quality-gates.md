# Quality gates, approvals, dependencies and failure modes

| Gate | Required evidence | On fail/pending |
|---|---|---|
| G0 — Trip brief | Dates, purposes, commitments, constraints, preferences | Ask one consequential question; state assumptions |
| G1 — Feasibility | Valid travel documents, safety rule, airport/time fit, bag, viable plans | Exclude failed; pending remains provisional |
| G2 — Shortlist | Matched sourced fares, full travel cost, provider timestamps, hotel access | Re-research missing or incomparable offer |
| G3 — Transaction | Explicit user authorization of exact vendor, itinerary, passengers, price/currency, refund/baggage terms | STOP: no purchase, charge, booking changes |
| G4 — Confirmation | Actual provider booking reference/PNR or ticket and segment details | `purchase_attempted` or `pending_confirmation`, never `confirmed` |
| G5 — Trip ready | Entry docs, confirmed tickets, hotel/transfer access, payments, connectivity, weather and backups | Flag item; withhold trip-ready label |
| G6 — Replanning | Analyze impact on hotels, transfers, commitments, payments and daily blocks | Reconfirm material decisions and seek renewed approval |

## Early booking gate
Flight inventory may be time-sensitive. Booking can be authorized after G1/G2 **and** enough lodging/arrival feasibility checking, without requiring a finished restaurant or sightseeing plan. This is a deliberate dependency shortcut, not a bypass of legal, safety or approval screening.

## Authorization boundaries
The traveler approving a shortlist or preferred airline is **not** permission to reserve, pay, cancel or reschedule. Each consequential transaction must show the exact booked item, dates/local times/time zones, price/currency, traveler count, accepted fees and refund conditions. If a site changes price or airports, return to approval rather than accept silently.

## Change-impact graph
- Flight or arrival airport changes → recheck visa/transit, hotel night/access, pickup, baggage, event buffers and sightseeing day.
- Hotel change → recheck transfer, check-in recovery, walking/geographic clusters, fees and refund deadlines.
- Fixed work/event changes → recheck flights, recovery, mandatory feasibility and the daily itinerary.
- Attraction closure → replace with geographically nearby alternative; do not touch paid reservations without approval.
- Connectivity outage → switch to saved offline map, local cash and licensed taxi backup.

## QA before handoff
- [ ] Every hard constraint marked pass/fail/pending with evidence.
- [ ] Date boundary/time zone/overnight segments correct.
- [ ] Side-by-side comparisons match passenger, fare and baggage conditions.
- [ ] Prices marked checkout-verified, advertised, derived or unknown.
- [ ] Missing performance data displayed as unknown/bounds, not invented score.
- [ ] Approved/attempted/confirmed are distinct states.
- [ ] No private identifiers, bank numbers or account secrets in public assets.
- [ ] Route geography and hours sourced, no AI-invented navigation data.
- [ ] Booking links/dependencies/cancellation conditions verified as far as tools allow.
- [ ] Remaining blockers clearly identified; evidence/timestamps retained.

Escalate official immigration or aviation-safety interpretation to authoritative sources and the traveler; do not provide absolute guarantees. For disputes, payment risk or major changes, stop before action and ask authorization.
