# Flight Sources — region-aware search guide

**Use when:** selecting where to research a flight, comparing search platforms, or choosing where to verify an offer. This guide selects **sources**, not tickets. For timing advice read [flight-purchase-strategy.md](flight-purchase-strategy.md). For actual itinerary evaluation follow [flight-research-selection.md](flight-research-selection.md).

## Starting search order (not a universal quality ranking)

These are **initial route-specific search priorities**, not measured price, trust, or customer-service rankings. Reorder or omit sources according to the origin, destination, language, payment method and observed inventory. A website link does not grant automated access, API access, or permission to scrape.

| Search order | China routes | Russia / CIS routes | Global routes |
|---|---|---|---|
| 1 | [Ctrip 中国国内机票](https://flights.ctrip.com/online/channel/domestic) — China domestic | [Aviasales](https://www.aviasales.ru/) — Russia/CIS discovery | [Google Flights](https://www.google.com/travel/flights) — dates and alternatives, where supported |
| 2 | [Qunar 去哪儿](https://www.qunar.com/) — compare domestic options; check app availability | [Tutu.ru](https://avia.tutu.ru/) — schedules, regional searches; calendar prices can be cached | [Skyscanner](https://www.skyscanner.net/) — compare sellers and dates |
| 3 | [Fliggy 飞猪](https://www.fliggy.com/) — domestic / mobile-app alternative | [Yandex Travel](https://travel.yandex.ru/avia/) — partner offers and alternate dates | [KAYAK](https://www.kayak.com/flights) — alternative search and filters |
| 4 | [Trip.com](https://www.trip.com/flights/) — international / multilingual alternative | [OneTwoTrip](https://www.onetwotrip.com/) — secondary seller comparison | [Trip.com](https://www.trip.com/flights/) — international OTA alternative |

**Always check the operating airline's official website** for the exact flight's schedule, baggage and fare rules, and compare its *current final price* with available seller checkout prices. Airline-direct is a verification step, not a global multicarrier search tool. For a China-origin international route, start with Ctrip + Trip.com and add relevant global sources. For Moscow–Samarkand, start with Aviasales + Tutu, cross-check Yandex Travel and the operating airline.

### Practical access caveats

- Ctrip's link above is **China domestic**, not an international route-search endpoint. Qunar and Fliggy may require an app/login or have limited desktop functionality. Verify what can actually be completed.
- Google Flights and other global services may lack coverage or availability in certain markets; mark inaccessible services as **unavailable**, and switch to another route-relevant source.
- Some platforms redirect to a distinct **ticket seller**. Record who will charge the traveler and whose support/refund terms apply; do not attribute the seller's terms to the search platform.
- Comparison calendars and public route pages may show **cached or advertised** fares. Only an observed final, equivalent checkout quote may be called checkout-verified.

## Lightweight MCDA to select sources per route

Score **accessible sources with actual observations**, 1–5 on each criterion; use `unknown` when a rating cannot be supported. Do not assign permanent website scores based on brand recognition.

| Criterion | Weight | What to measure |
|---|---:|---|
| Route/carrier coverage | 30% | Relevant flights found on the requested dates |
| Comparable fare information | 25% | Flight identity, exact fares, baggage, rules, source timestamps |
| Matched final-price competitiveness | 20% | Final amount for the **same itinerary and fare**, if observable |
| Payment/currency fit | 15% | Usable seller and payment method for this traveler |
| Servicing clarity | 10% | Identified seller, refund/change terms and support channel |

`SourceScore = sum(weight_percent * observed_rating_1_to_5) / 100` when all weighted ratings are known. If unknown, mark the source ranking **provisional** and report what could not be checked. Do not equate this source score with flight safety, MCDA itinerary quality, or the best ticket price.

**Minimum workflow:** inspect two complementary discovery sources where accessible, then verify the finalists with their **operating airlines** and actual sellers. Normalize date/time zones, flight numbers, airports, traveler count, fare family, baggage, currency, all mandatory fees, changes and refunds. Record source URL, observed time and evidence state; never invent a fare or silently merge incompatible offers. If provider access fails, use the remaining sources and disclose the gap.

**Scope:** read-only discovery and verification. Never reserve or pay. Follow the parent skill's hard-constraint and approval gates.

## Maintenance and relevant provider pages

Review routing links and capabilities periodically; static search order is a heuristic, not a benchmark.

- [Ctrip flights](https://flights.ctrip.com/online/channel/domestic), [Qunar](https://www.qunar.com/), [Fliggy](https://www.fliggy.com/), [Trip.com flights](https://www.trip.com/flights/)
- [Aviasales](https://www.aviasales.ru/), [Tutu](https://avia.tutu.ru/), [Yandex Travel](https://travel.yandex.ru/avia/), [OneTwoTrip](https://www.onetwotrip.com/)
- [Google Flights](https://www.google.com/travel/flights), [Skyscanner](https://www.skyscanner.net/), [KAYAK](https://www.kayak.com/flights)
