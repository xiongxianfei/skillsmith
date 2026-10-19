# Worked example: fictional Moscow–Samarkand weekend

> **Synthetic teaching example, not a real traveler, published timetable, live fare, or booking instruction.** Every date, flight ID, amount, work time and provider is invented solely to demonstrate the skill safely. No personal itineraries or actual user-provided screenshots are reproduced.

## Hypothetical trip brief

- Depart Moscow on Thursday **13 May 2027**, return Monday **17 May 2027** (fictional dates).
- Work ends at **17:00** Thursday; assume **90 minutes** to reach the departure airport.
- Be rested before Saturday **15 May** commitments; allow Friday recovery after overnight travel.
- Permitted Moscow airports: **SVO, VKO and DME**; exclude ZIA.
- One small backpack, subject to each fare's actual terms.
- Evaluation weights: schedule 25, cost 20, comfort 15, sleep 15, ground transport 10, reliability 15.
- Legal entry, aviation safety, baggage and checkout are all **PENDING**, not presumed to pass.

## Fictional round-trip comparison

| Criterion | Full-service outbound + regional return | Low-cost outbound + regional return |
| --- | --- | --- |
| Outbound | **AL101** (invented), SVO Thu 23:30 → SKD Fri 05:40 | **BL202** (invented), VKO Thu 22:45 → SKD Fri 04:55 |
| Return | **RL303** (invented), SKD Mon 20:00 → DME Mon 22:20 | Same fictional return |
| Outbound comfort | Conventional reclining economy assumed | Budget economy assumed |
| Example total price | **44,000 RUB**, synthetic derived amount | **41,000 RUB**, synthetic advertised amount |
| Ground access | 90 min to SVO, after protected work hours | 90 min to VKO, same assumption |
| Flight reliability | **Unknown**: no actual statistics | **Unknown** |
| Status | **Pending**: documents, safety, bag and fare | **Pending**: documents, safety, bag and fare |

Do **not** infer any real airline operations, flight numbers, aircraft assignments, prices, routes or safety status from these examples.

## Deterministic evaluator

Run from the skill folder:

```bash
python3 scripts/evaluate_itineraries.py --input examples/samarkand-input.json --output /tmp/samarkand-evaluation.json
```

The output has score bounds because reliability evidence is intentionally absent; it must **not** declare a winner while hard constraints are pending. Compare with [samarkand-evaluation.json](samarkand-evaluation.json).

## Itinerary planning implications

- **Friday:** allow a guaranteed early check-in or a rest location before sightseeing.
- **Saturday:** protect commitments, and offer evening activities only if availability is confirmed.
- **Sunday:** cluster historical/scenic/food visits (e.g., Registan and Siyob Bazaar) by grounded coordinates, with date-specific opening-hour checks.
- **Monday:** leave realistic airport and traffic buffer for the hypothetical return flight.
- **Connectivity:** check roaming/physical SIM compatibility, payment acceptance and offline backups.
- **Cross-platform comparison:** check official and independent sources when available; a screenshot or estimated price is not checkout verification.

## Pending gates

1. Actual traveler-specific documents and permission for both directions.
2. Official aviation-safety assessment against the traveler's criteria.
3. Verifiable bookable flights, aircraft, price, airport and fare conditions.
4. Baggage allowance, early lodging access and recovery feasibility.
5. Explicit purchase authorization and a permitted booking tool.

A proposed travel plan is not a booking; this example authorizes no external action.
