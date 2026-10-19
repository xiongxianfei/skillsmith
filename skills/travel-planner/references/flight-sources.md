# Flight Sources — global search-source ranking

**Purpose:** decide **where to search first** for flight offers. This is **source selection**, not the user's **ticket ranking**. For actual itinerary evaluation read [flight-research-selection.md](flight-research-selection.md); for buying timing read [flight-purchase-strategy.md](flight-purchase-strategy.md).

## Global MCDA source table

**P = provisional editorial estimate** for **all** scores below, including the three sub-criteria. These are transparent starting assumptions—not measured worldwide price competitiveness or evidence that one website is always cheaper. Every platform uses the **same global expectations**, so region-specialized sites can score lower on worldwide coverage. One decimal shows weighted arithmetic, **not empirical precision**.

| Rank | Source | Score / 10 | Price Competitiveness | Flight Coverage | Comparison Quality | Why This Score? | Recommended Region |
|---:|---|---:|---:|---:|---:|---|---|
| 1 | [Google Flights](https://www.google.com/travel/flights) | 8.7 P | 8 | 9 | 10 | Strong date and airport comparisons; geographic coverage varies. | Global (where available) |
| 2 | [Skyscanner](https://www.skyscanner.net/) | 8.5 P | 8 | 9 | 9 | Broad multi-seller international search. | Global |
| 3 | [Trip.com](https://www.trip.com/flights/) | 8.3 P | 8 | 9 | 8 | Wide international flight search and multilingual interface. | Global; Asia |
| 4 | [KAYAK](https://www.kayak.com/flights) | 8.2 P | 8 | 8 | 9 | Global metasearch with useful itinerary filters. | Global |
| 5 | [Ctrip 中国机票](https://flights.ctrip.com/online/channel/domestic) | 7.6 P | 8 | 6 | 9 | Strong China domestic search; linked page is domestic-only. | China |
| 6 | [Aviasales](https://www.aviasales.ru/) | 7.4 P | 8 | 6 | 8 | Useful Russia/CIS comparison; less consistent worldwide coverage. | Russia/CIS |
| 7 | [Tutu.ru](https://avia.tutu.ru/) | 7.2 P | 8 | 6 | 7 | Regional fares and schedules; calendar prices can be cached. | Russia/CIS; Central Asia |
| 8 | [Qunar 去哪儿](https://www.qunar.com/) | 7.1 P | 8 | 5 | 8 | China-focused comparisons; app/login can be required. | China |
| 9 | [Yandex Travel](https://travel.yandex.ru/avia/) | 6.9 P | 7 | 6 | 8 | Russian-market alternatives with varying ticket sellers. | Russia/CIS |
| 10 | [Fliggy 飞猪](https://www.fliggy.com/) | 6.4 P | 7 | 5 | 7 | China-focused, app-centric experience. | China |
| 11 | [OneTwoTrip](https://www.onetwotrip.com/) | 6.2 P | 7 | 5 | 6 | Useful secondary regional seller check. | Russia/CIS |

**Summary interpretation:** The rationale column explains the intended comparison role and most relevant limitation without listing each supporting observation. A traveler reported that Tutu offered a lower Moscow–Samarkand fare than Aviasales on one occasion: useful **route-specific search guidance**, but insufficient to infer globally lower prices. For that particular route, check both sites early regardless of their global ranks.

## Source MCDA: how the scores are obtained

| Criterion | Weight | Interpretation |
|---|---:|---|
| **Price competitiveness** | **50%** | Lower **final payable** quote for the *same* flights, fare conditions and currency |
| **Flight coverage** | **30%** | Relevant carriers and itineraries available **worldwide** |
| **Comparison quality** | **20%** | Search filters, dates, schedules, airports, baggage and fare clarity |

`Score / 10 = 0.50 × Price + 0.30 × Coverage + 0.20 × Comparison`; sub-scores each range from 0–10. For now, all inputs are **P (expert working judgments)**; the total is calculated from those inputs, not from a global fare dataset.

**Measured status (M) requires a representative cross-market comparison**, not anecdotes: sample matched final fares across China, Russia/CIS and other international routes, across multiple dates and booking windows, with the same flights, travelers, fare family, baggage, taxes, payment currency and mandatory fees. Retain source links, check times, sample counts and detailed evidence in a separate benchmark record. This summary need not reproduce the raw evidence. If a criterion lacks measured data, display **unknown**, not a fabricated measured sub-score or overall score; retain P or leave the measured ranking pending.

## Practical source selection

1. **Filter by region and accessibility** before choosing the top **two or three applicable** providers. A global rank is a starting index, not a mandatory search sequence. Moscow–Samarkand: Tutu + Aviasales, then Yandex Travel. China domestic: Ctrip + Qunar, then Fliggy where accessible.
2. Compare the **same itinerary and fare** with identical dates, cabin, baggage, refund conditions, passenger count, currency and fees. Price calendars can be stale and seller checkout may differ.
3. **Always verify shortlisted flights with the operating airline's official website**, including schedule, airports, baggage, fare rules and direct checkout price. Airline-direct is a separate verification role, not a global multicarrier search site.
4. Feed source-labelled actual offers to [flight-research-selection.md](flight-research-selection.md) for **hard constraints and ticket-level MCDA**. Identify the actual ticket seller (it may differ from the comparison platform).
5. Record blocked or unsupported websites as unavailable; do not assume a listed URL grants an API, browser automation, or scraping permission.

**Scope:** read-only research. No reservations or payments. Maintain [flight-purchase-strategy.md](flight-purchase-strategy.md) separately.
