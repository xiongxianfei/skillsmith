# Constrained MCDA and Weighted Sum Model (WSM)

## 1. Filter hard constraints before scoring

A candidate's hard checks are `pass | fail | pending`. At least one `fail` makes it ineligible; any `pending` prevents a booking-ready winner. Common gates: travel documents and re-entry, regulatory safety threshold, commitments, airports, necessary baggage, flight operation/availability and verified checkout terms.

## 2. Nonoverlapping soft criteria

| Criterion | Include | Exclude to avoid counting twice |
|---|---|---|
| Schedule fit | Planned work/event margins; usable sightseeing hours | Delay likelihood and fatigue |
| Sleep & recovery | Missed normal sleep and recovery time | Seat specifications |
| Reliability | Comparable delay/cancellation statistics | Published block time |
| Cabin comfort | Seat pitch/recline, space, amenities, onboard service | Airline brand alone, airport location |
| Ground logistics | Door-to-door minutes, transfers, route complexity | Ground fares |
| Total trip cost | Fare, taxes, baggage, ground fares, necessary extra hotel nights | Lost hours already scored in schedule |
| Optional fare flexibility | Change/refund rules and penalties | Duplicate fees counted in all-in cash cost |

Default weights (%): schedule 25, sleep 15, reliability 20, comfort 10, ground logistics 10, total trip cost 20. Users may override. The worked example intentionally uses independent hypothetical weights.

## 3. Operationalize 0–10 scores

Choose fixed, meaningful anchors before inspecting candidates. When bigger is better:
`s(x)=10*clip((x-L)/(U-L),0,1)`.
When smaller is better and `L` is the desirable minimum while `U` is the poor upper anchor:
`s(x)=10*clip((U-x)/(U-L),0,1)`.
Use documented rubrics for partly subjective comfort. Never award 10 merely because a ticket happens to be the cheapest among two results.

For an entirely scored and feasible itinerary:
`S_i=sum(w_j*s_ij)/sum(w_j)`.

Unknown inputs are **not** 0 and **not** assumed 5. If a criterion is unknown, report:
- `lower_bound=known_weighted_sum / total_weight`
- `upper_bound=(known_weighted_sum+10*missing_weight) / total_weight`

These are bounds, not probabilities or confidence intervals. Unknown reliability makes the score interval wider; pending safety or legal checks block a winner regardless of score. The bundled evaluator enforces this for well-formed input but cannot substantiate external evidence.

## 4. Comparable cross-platform pricing

Match the complete itinerary: exact dates/time zones, airport codes, operating flights, passenger count, cabin, carry-on and checked baggage, agency fee, refundable/change terms, currency and final payment amount.

Classify price evidence:
- `checkout_verified`: user/provider actually observed final bookable checkout at recorded timestamp.
- `advertised`: search result or calendar price, may change at checkout.
- `derived`: arithmetic estimate, never an actual offer.
- `unknown`: no trustworthy quoted price.

Combine necessary lodging and transport costs in total-trip-cost, but keep flight fare quoted separately. Do not infer live inventory from historical examples.

## 5. Uncertainty and sensitivity

Try fare +10–15%, ground transfer +30–60 minutes, flight delays +2h/+6h/+12h, shift two highest weights by 10–20%, and alternate availability/rest assumptions. Say whether one option dominates, whether score intervals overlap and which missing observations would make the decision more robust. Never collapse a hard constraint into an adjustable weight.

## 6. CLI

`scripts/evaluate_itineraries.py --input examples/samarkand-input.json --output output.json` produces auditable status, weighted score bounds and an optional winner only when every hard check passes and soft criteria have data. It does not browse the web, verify prices, or book.
