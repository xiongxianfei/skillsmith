# Flight Research & Selection — evidence-first module v1.0

**Purpose:** produce a source-grounded, **ranked shortlist of complete flight itineraries** for traveler approval. Scope ends **before reservations, purchases, holds, payments, ticket changes, or cancellations**. A request to shortlist is never booking authorization. The agent may offer links to known booking pages but must not invent links or claim live inventory not observed.

**Integration:** this is a focused extension of the existing Travel Planner `SKILL.md`, `references/scoring.md`, `references/data-contracts.md`, `references/research-and-tools.md`, `references/quality-gates.md`, and `scripts/evaluate_itineraries.py`. Read this reference when searching, comparing, ranking, or recommending flights. Reuse the existing weighted evaluator; do not establish a competing scoring implementation.

For route-specific provider discovery, follow [flight-sources.md](flight-sources.md); for purchase timing and price-monitoring advice, follow [flight-purchase-strategy.md](flight-purchase-strategy.md). Keep both guidance files independent of the existing scoring engine.

## 0. End state and modes

- `researching`: search ongoing; offers may be advertised, stale, or hypothetical.
- `provisional_shortlist`: candidates normalized but one or more prices/gates cannot be verified.
- `verified_shortlist`: **each listed recommended option** has matching itinerary/fare conditions, an observed, bookable all-in checkout quote within the applicable freshness target, complete feasibility checks, and supporting evidence. This is **not a reservation or price guarantee**.
- `blocked`: all options fail hard constraints or critical evidence cannot be checked; state reason and next required fact.
- `approval_requested`: present shortlist to traveler for selection; **selection is not authority to book**.

If checkout is inaccessible, return a `provisional_shortlist` and provide explicit checkout verification steps. Never silently promote a quote because multiple aggregators display it.

## 1. Intake: traveler and trip data

Ask only for missing *decision-critical* information. Reuse already supplied facts. Follow `assets/flight-search-brief.yaml`.

**Identity-independent:** origin/destination (city vs IATA airport), outbound/return local dates, ±day/date flexibility, number/ages of passengers if applicable, one-way/round-trip, cabin, baggage and size, mandatory work/event windows, travel time to/from airports, time-to-event or recovery margin, permitted airports, no-self-transfer/connection rules, max connections, maximum ticket cost if hard, currency/payment limitations, accessibility, willingness to fly overnight, refundable requirement, traveler risk/safety threshold, and relative weights.

**Travel permissions:** nationality and transit/re-entry eligibility only to the extent needed to check rules. Do not solicit passport numbers, scans, sensitive identity data, payment-card numbers, passwords, or OTPs. If personal document eligibility cannot be verified, mark `pending` and direct the traveler to official verification.

**Time:** every departure/arrival has local date, local time, IANA timezone and airport. Check day rollovers, overnight flights, DST on the *date of travel*, minimum airport arrival buffers, and workable arrival before a fixed event. No naive UTC offsets copied from today's date.

## 2. Discover a representative search space

Use tools **only if available and authorized**. Differentiate search/discovery from inventory verification. When possible:

1. Search airline-direct for operating schedules and fare families; check the **operating** as well as marketing carrier.
2. Search at least two independent booking/comparison channels for discovery and price comparison where geographically accessible. Record sources independently; some metasearch results reuse the same underlying inventory.
3. Compare nonstop options first when requested, then permitted one-stop itineraries. Search relevant acceptable airports, specified departure windows, and authorized flexible dates.
4. Search round trips and mixed-airline two one-way tickets where relevant. Treat separate tickets as independent contracts; document lost protected-connection, refund, and disruption protections.
5. Search equivalent baggage/cabin/number-of-travelers before sorting by price; capture cheapest fare *including necessities*. Include potential fees for payment, seat requirements, and compulsory services.
6. Build complete candidate **itineraries** instead of ranking outbound and return flights independently. Optionally combine feasible outbound and return one-way tickets, with correct total price and terms.
7. Deduplicate code-share and identical-flight listings by a segment fingerprint. Preserve sellers/fare offers as alternatives under the same itinerary, not fake distinct flights.
8. Search until a useful feasible Pareto-diverse set exists (normally 3–7 itineraries), or explain evidence/tool coverage limitations. Prefer diversity: low cost, low disruption, best balanced. No requirement to invent three choices if fewer exist.

### Entity keys and contracts

- `segment_key`: operating carrier + operating flight number + flight local departure date + departure IATA + arrival IATA (+ intermediate airports for multi-leg).
- `itinerary_key`: ordered outbound and inbound segment keys, including dates and separate-ticket structure.
- `fare_offer_key`: itinerary key + selling channel + fare family + passenger count + cabin + baggage allowances + cancellation/refund conditions.
- `quote_key`: fare offer + amount/currency + `observed_at` + payment option; multiple observed prices are a history, not duplicate candidates.

A **source** record has: `url_or_ref`, source type, provider, capture timestamp (ISO 8601 with offset), fields substantiated, and limitations. Do not treat a calendar price as proof of current booking availability. Screenshots provided by a traveler count as observed evidence at the stated capture time, not verified issuance.

## 3. Field-level research contract

### A. Route and schedule

- IATA airports **and** full names, flight number, marketing and operating airlines, local departure/arrival dates/times/timezones, elapsed air time, stops, layover duration, terminals where available, flight operating days.
- If a connection: airport change, immigration, checked-bag collection/recheck, minimum connection time, protected vs unprotected transfer, transit visa, layover safety margin.
- Door-to-door: workplace/home/hotel to airport, airport arrival required by check-in/security/immigration, airport to destination lodging/event, ground service operating hours at scheduled and delayed arrival times.

### B. Fare and booking conditions

- Quoted *entire itinerary* for exact travelers, total payable, taxes, provider/agency fees, currency of charge, payment-method fees and currency conversion caveats, baggage including personal item/carry-on/checked, optional seat/meals only if traveler needs them.
- Fare brand/class, change/cancellation/no-show rules, penalties, whether fare difference applies, agency service fees, refund method/timing if known, passenger naming restrictions, linked vs separate ticket numbers.
- Deep link only if it was actually returned or verified. Price status = `checkout_verified | advertised | derived | unknown`. `derived` is never a buyable quote.

### C. Experience and risk

- Aircraft family/model (scheduled, not guaranteed), seat pitch/recline where independently sourced, meals and service, accessibility, overnight cabin sleep suitability.
- Official aviation safety/regulatory status and documented audits; explain limitations, never infer an accident probability from customer-review score.
- Comparable route/flight on-time and cancellation statistics with sample size, lookback dates, definition of on-time, source and operating-carrier match; **no invented reliability score**.
- Likelihood of missing commitments is modeled by schedule margin and delay scenarios; avoid double counting the same delay as both published schedule and reliability.

## 4. Hard-constraint screening (G1)

For each **complete itinerary**, record `pass | fail | pending`, rationale and provenance. Missing evidence is `pending`, never `pass`.

| Gate | Example rule | Failure/pending treatment |
|---|---|---|
| `travel_documents` | Destination entry, transit, and return entry eligibility | Without confirmed applicability, pending; seek official verification |
| `safety` | Traveler-defined acceptance based on appropriate regulators/operating carriers | Never replace regulatory evidence with review stars; user must specify threshold when consequential |
| `work_time` | Departure for airport is after protected work end; realistic travel + check-in buffer | Reject itinerary violating actual user schedule |
| `event_ready` | Arrival + transfer + recovery satisfy critical event start time | Fail if mandatory readiness window impossible |
| `airports` | Only permitted origin/return airports and no disallowed connections | Reject disallowed IATA codes |
| `baggage` | Mandatory bags allowed under exact fare | Fail or make fare change to compliant fare |
| `connection` | Maximum stops, sufficient protected transfer time, correct transit docs | Fail or mark pending until verified |
| `budget_hard` (optional) | Verified all-in cash outlay ≤ strict cap | Do not reject purely on outdated/derived quote; pending if cost unknown |
| `fare_checkout` | Current final quote observed for exact offer | Pending unless `price.status=checkout_verified`; this controls verified shortlist level |

Where an actual airline inventory tool is unavailable, the agent can still produce a conditional comparison but cannot assert real-time seats or checkout bookability.

## 5. Six mutually constrained soft criteria (G2)

Reuse `references/scoring.md` and `scripts/evaluate_itineraries.py`. Every scored indicator has fixed anchors agreed **before comparing specific offers**; document the measurement and source.

| Criterion | Default | Measurable indicators | Exclude to avoid double count |
|---|---:|---|---|
| `schedule` | 25 | Planned work/event time margin; usable destination hours; schedule flexibility | Delay likelihood, sleep quality, transfer fare |
| `sleep` | 15 | Normal sleep opportunity lost; recoverable hours before event; forced early hotel access | Seat pitch, onboard service |
| `reliability` | 20 | On-time arrival % at stated threshold, cancellation %, delay tail when enough comparable observations | Scheduled departure time |
| `comfort` | 10 | Seat space/recline, cabin density, meals/service, accessibility | Reliability, airline brand alone |
| `ground` | 10 | Door-to-door transfer minutes, number of transfers, pickup complexity, ground-arrival hour | Ground fares and lodging expense |
| `cost` | 20 | Fare + taxes + compulsory ancillaries + necessary incremental hotel/transfer costs | Monetized lost time already in schedule |

Default weights total 100; user weights override (any positive relative values; normalize internally). Optional flexibility criterion: allocate 5–10% by *reallocating*, not simply adding unbalanced points.

### Numeric normalization

Define fixed anchors `L` (good minimum) and `U` (poor maximum), score 0–10:

- Benefit indicator: `10 * clip((x-L)/(U-L), 0, 1)` if `U` is best and `L` worst.
- Cost indicator: `10 * clip((U-x)/(U-L), 0, 1)` if `L` is best and `U` worst.
- Composite qualitative dimension: documented rubric, not a brand-based score.
- Final: `S_i = sum(w_j * s_ij) / sum(w_j)` **only for feasible options**, with complete scores.

If a score lacks sound data, keep `null`; do not assign 5. Compute bounds `known_weighted_sum / total_weight` and `(known_weighted_sum+10*unknown_weight)/total_weight`. These represent ignorance bounds, not statistical confidence limits. Existing evaluator may rank only complete, eligible contenders; otherwise display partial ordering, score ranges, blockers and a provisional shortlist.

### Sensitivity / robustness

Stress test +10–15% fare, 30–60 min ground delay, +2 h/+6 h/+12 h flight arrival delays, paid early hotel room, and ±10–20% perturbation of leading priorities. Mark robust, sensitive, or inconclusive. Do not estimate delay probability from isolated anecdotes. If score intervals overlap, do not imply precise superiority.

## 6. Multi-platform matching & verification protocol

**Two distinct checks:**

1. **Identity and independent comparison:** match exact date, operating segments/airport codes and fare terms across airline direct and 1–2 independent search/seller channels when accessible. Two apparent sellers might use identical wholesalers; record actual source and seller separately. If identical fares differ, investigate included bags, fare family, ticketing agency fees, checkout currency, payment options, inventory and refund authority. Do not average prices.
2. **Checkout-level verification:** for each recommended candidate, observe the final payable offer **before payment** with correct traveler count, flight numbers, dates, airports, fare family, bags, fees, currency, and terms. Record exact time. A public flight calendar or cached metasearch price cannot satisfy this check. When access is blocked, request a traveler checkout screenshot and label observation method; otherwise use `advertised` and mark provisional.

Prefer an airline-direct checkout as authoritative for that airline's own inventory. Agencies can offer legitimate different fares; a lower agency quote is not disproved by the direct fare. Neither source guarantees the amount at later purchase. Resolve conflicting scheduled airports/flight times at operating carrier; if unresolved mark schedule `pending`.

### Freshness policy (heuristic targets, configurable)

| Evidence | Target freshness before releasing shortlist | Mandatory response if stale |
|---|---|---|
| Checkout final price and bookability | ≤15 minutes (recheck at any subsequent booking) | Downgrade to advertised/provisional |
| Search-result fares and alternative discovery | ≤6 hours for near-term departures; otherwise same-day | Refresh; mark stale if unavailable |
| Airline schedule/airport/terminal | ≤24 hours when departing within 14 days | Re-verify against operator |
| Baggage and refund/change terms | Date of comparison; exact fare terms checked at checkout | Mark condition pending until confirmed |
| Visa/transit/entry/safety restrictions | Latest effective official notice, checked for travel date | Pending if applicability unclear; do not impose arbitrary document publication-date limit |
| Reliability history | Documented observation period, preferably recent 60–90 days and adequate sample (30+ comparable operations suggested, not required) | Unknown if sample not comparable or sufficient |
| Exchange-rate conversion | Same day as comparison | Recalculate and retain original charge currency |

These targets are quality-control heuristics, **not promises that inventory or terms remain valid**. Log time with zone. Missing `observed_at` means freshness unverified.

## 7. Ranking and shortlist presentation

Do not give a mathematically final winner when any active contender has pending mandatory checks or missing scored evidence. Exclude hard fails, mark pending options separately. Prefer the **best 3 distinct complete itineraries**: balanced, lower-cost and most schedule-friendly if differences are meaningful. Multiple sellers of the same flights should be nested under a single itinerary.

Each displayed option must show:
- rank or conditional position; `eligible` / `pending` / `rejected` and `verified` / `provisional` quote tier;
- outward/return airlines, operating numbers, departure/arrival local dates, times, and IATA airports; connections/self-transfers; planned aircraft marked `scheduled`;
- complete airfare + necessary ancillary breakdown and total journey cost, charge currency, source/provider, quote timestamp, booking terms;
- gate results, 0–10 score or interval, strongest advantage/trade-off, confidence/limitations and next required confirmation;
- exact observed booking link if known, otherwise where/how to check (without a fabricated deep link).

Use `assets/flight-ranked-shortlist.md` and `assets/flight-evidence-ledger.csv`. Keep a `next_action` that stops at **traveler review and approval of the shortlist**; never hand off to a payment action implicitly. For an absent buyable quote, change header to `Provisional shortlist — checkout required`.

## 8. Mandatory QA (G2 release gate)

- [ ] Trip details/commitments/permissions identified; unverifiable legal/safety inputs pending.
- [ ] At least airline direct + independent platform searched if accessible; limitations otherwise stated.
- [ ] Options are **complete round trips**; deduplicated codeshares; no mixed-ticket protection assumptions.
- [ ] Local dates, IANA zones, DST, midnight rollover, airport and terminal crosschecked.
- [ ] Actual operating carriers and aircraft qualifier (scheduled) recorded; safety assessed from official evidence.
- [ ] Quote status honestly classified; final all-in amount/currency and **fare rules** equivalent across compared sellers.
- [ ] Provenance with source, timestamp, and screenshot type retained; every dynamic quote freshness evaluated.
- [ ] Ground and hotel consequences included but not double-counted; no missing cash fees hidden.
- [ ] Reliability stats include comparable sample and definition or remain unknown.
- [ ] Scores are grounded, missing values retained as `null` and ranges shown; no score for failed hard gate.
- [ ] Sensitivity analysis completed; option-specific downside and contingency recorded.
- [ ] Output states `verified` vs `provisional` and `not booked`; no payment or booking attempted.
- [ ] Sanitized examples and evidence logs contain no traveler identifying or payment data.

## 9. Failure behavior & acceptance tests

1. **Forbidden airport:** reject even when cheapest.
2. **Airport-transfer impossibility:** if the traveler finishes work too late to reach departure/check-in, reject or mark pending if travel-time evidence is missing.
3. **Calendar fare only:** keep `advertised`, downgrade shortlist to provisional.
4. **Baggage mismatch:** price compliant fare, not misleading bare base fare.
5. **Unknown delay statistics:** score `null`, report interval; no invented punctuality number.
6. **Contradictory provider airport/time:** stop final verification for affected segment until operating carrier confirms.
7. **Mixed two one-way tickets:** show total but warn that conditions and disruption protections are separate.
8. **Disallowed travel documents/safety:** reject or pending, never weighted away.
9. **Checkout fare changes:** refresh total and re-run eligibility and rankings.
10. **User selects a flight:** stop at selection; request explicit authorization in the separate booking workflow if ever initiated.

## 10. Example application

See `examples/flight-selection-synthetic.md`. Every price, time and airline code in that example is invented; no live inventory, travel-document clearance or actual traveler schedule is represented.