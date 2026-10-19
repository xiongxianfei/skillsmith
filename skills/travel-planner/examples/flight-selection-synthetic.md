# Synthetic flight-selection exercise

**All dates, operating flight codes, amounts and airport/access inputs below are fictional.** This example demonstrates methodology and must never be interpreted as real flight inventory, airline operations, prices, travel authorization or safety assurance.

## Fictional inputs

- A generic traveler wants a return journey between City A and City B, departing Thursday 13 May and returning Monday 17 May 2027.
- Thursday work ends at 17:00. Two hypothetical departures leave approved airports at 22:45 and 23:30. Both arrive in City B Friday morning.
- Work/ground-transfer buffer is **to be verified**, not implicitly passed. Saturday readiness matters; Friday early hotel access has not been confirmed.
- Traveler has not provided travel document eligibility or a safety acceptance rule.
- Hypothetical ticket offers are 41,000 and 44,000 units of a fictional currency, both **advertised only**. These are not observed fares and have no booking links.
- Route reliability is unknown. Both were described as comfortable/budget in qualitative source-independent assumptions, not empirical airline ratings.

## Correct model behavior

1. Assemble complete return itineraries, not two independent flight rankings.
2. Mark `travel_documents`, `safety`, `fare_checkout`, `work_time` and `event_ready` as **pending** until evidence exists.
3. Classify price as `advertised` (not `checkout_verified`); price may be part of a *scenario* but is not confirmed purchasable.
4. Mark unmeasured `reliability` score `null`; present a score interval rather than an invented 5/10.
5. Publish only a **provisional shortlist**, with specific next checks (documents, operating carrier safety status, airport transfer, early hotel check-in, final checkout prices).
6. Do **not** choose an unconditional winner or initiate booking.

The companion `examples/flight-selection-input.json` is compatible with `scripts/evaluate_itineraries.py` in the parent Travel Planner skill and demonstrates unresolved gating.