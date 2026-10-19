# Flight Purchase Strategy — monitor versus buy

**Use when:** advising when to search, set alerts, wait or purchase a ticket. This is **decision guidance**, not a reservation instruction, fare forecast, or promise of the lowest price. Find search providers in [flight-sources.md](flight-sources.md); normalize and evaluate itineraries under [flight-research-selection.md](flight-research-selection.md).

## Three rules

1. **Do not wait for a special purchase weekday.** Google's October 2026 US-origin analysis found about **1.4%** difference between Wednesday (cheapest) and Sunday (most expensive) purchase days. Expedia's 2026 UK analysis instead identifies Sunday, with only ~2% advantage over Tuesday in its sample. Results differ by market. Departure dates, fare class, inventory, flexibility and overall timing matter more.
2. **No universal “book exactly N days ahead” rule.** As *illustrations, not rules*: Google Flights' 2026 US-origin analysis found a domestic low-price range **22–57 days** out and international **50–133 days**; Expedia's UK-origin 2026 dataset reported a different international window, **15–30 days**. Do not transfer those averages automatically to China or Russia/CIS routes.
3. **Buy for a good verified itinerary, not a predicted bottom.** If commitments are fixed and a fare meets constraints and the traveler's acceptable total cost, favor securing it over waiting for an uncertain price drop.

## Lightweight planning and monitoring defaults

| Time until departure | Practical approach |
|---|---|
| 3+ months | For international, high-demand or inflexible trips: begin comparing routes and set a target all-in price. Monitor weekly or use a supported alert. |
| 1–3 months | Actively compare alternatives. Monitor around 2–3 times/week if not yet ready to buy. Domestic trips often enter their relevant shopping period; this is not a guarantee. |
| 15–30 days | With fixed dates, shortlist and verify promptly; monitor daily only if the traveler deliberately chooses to wait. |
| 0–14 days | Treat feasible, acceptable checkout prices as time-sensitive. Avoid speculative waiting for a weekday or predicted dip. |

These intervals govern **effort and risk**, not expected minimum fares. For popular events or limited nonstop capacity, start and decide earlier. If dates are flexible, compare different **days of travel** and nearby airports (only if the traveler permits them).

## Decision gate

- **RECOMMEND BUY NOW:** Legal/safety/schedule/airport/baggage hard checks pass; a matching itinerary and final all-in checkout price have been observed; the price is within the traveler's acceptable limit; fare restrictions and seller/payment method are understood. **Stop for user decision; do not transact.**
- **MONITOR:** Enough time and date flexibility remain, and the current total is materially above a traveler-defined target or reliable comparable route observations. Record the next recheck date and any price alert actually enabled.
- **REJECT:** A hard constraint fails, regardless of price.
- **PENDING:** Entry rules, airline, fare family, payment, actual checkout or other critical evidence remains unresolved. Return a provisional shortlist with explicit missing checks, never “buy now.”

## Minimal price log

Track `observed_at`, source and **actual seller**, exact flights/dates/airports, fare class, passenger/baggage conditions, base currency, **all-in payable amount**, payment fees, change/refund conditions and price evidence (`checkout_verified | advertised | derived | unknown`). Comparisons must hold the fare conditions constant.

Price history or an algorithmic trend is a **signal**, not proof the price will fall. If no comparable dated history exists, state that no trend can be determined. Do not create scheduled checks or claim alerts are active unless the traveler requests them and an authorized alert/scheduler is actually used.

## Evidence used for these rules

- [Google Flights, Trends and tips for 2026 holiday travel, 5 October 2026](https://blog.google/products-and-platforms/products/search/holiday-travel-trends-2026/) — five years of aggregate **US-origin** flight data; day-of-purchase spread and booking windows.
- [Expedia UK, Air Hacks 2026](https://www.expedia.co.uk/newsroom/expedia-2026-air-hacks-2/) — UK-platform samples, different lowest-price window and small purchase-weekday spread.
- [Trip.com flight search](https://www.trip.com/flights/) — an example provider of price trend/alert capabilities; verify actual feature access by market.

**Output:** one sentence describing whether to buy/monitor/reject/pending, the evidence timestamp and target price comparison, plus 2–3 eligible flight options where supported. The parent skill owns final itinerary ranking, approval and any later booking workflow.
