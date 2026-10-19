# Flight Sources — where to search first

**Purpose:** choose a shortlist of **flight search websites** for a route. Prioritize **cheaper comparable fares and search quality**. This is a source-selection reference, **not** a ranking of tickets. For buying timing use [flight-purchase-strategy.md](flight-purchase-strategy.md); for selecting an actual itinerary use [flight-research-selection.md](flight-research-selection.md).

## Starting source rank, region, and score

Scores marked **H** are **provisional editorial search-priority estimates** on a 0–10 scale, **not measured price competitiveness or a claim that a source is consistently cheapest**. They are intended to help choose the first sites to check, not determine which seller to pay. There is no cross-platform fare benchmark yet; replace these estimates with measured scores when available.

| Recommended region | Rank | Source | Score / 10 | Why check it |
|---|---:|---|---:|---|
| **China** | 1 | [Ctrip 中国机票](https://flights.ctrip.com/online/channel/domestic) | 8.5 H | Strong China-domestic starting point; this link is **domestic only** |
| China | 2 | [Qunar 去哪儿](https://www.qunar.com/) | 8.2 H | Alternative China flight discovery; app/login may be needed |
| China | 3 | [Fliggy 飞猪](https://www.fliggy.com/) | 7.8 H | Compare China offers; app-centric access |
| China | 4 | [Trip.com](https://www.trip.com/flights/) | 7.7 H | Cross-border and multilingual search alternative |
| **Russia / CIS / Central Asia** | 1 | [Tutu.ru](https://avia.tutu.ru/) | 8.5 H | Regional flights and fares; **traveler reported a lower Moscow–Samarkand quote than Aviasales** (single case, unverified as a general trend) |
| Russia / CIS / Central Asia | 2 | [Aviasales](https://www.aviasales.ru/) | 8.3 H | Broad regional discovery and seller comparison |
| Russia / CIS / Central Asia | 3 | [Yandex Travel](https://travel.yandex.ru/avia/) | 7.9 H | Useful alternate search and seller offers |
| Russia / CIS / Central Asia | 4 | [OneTwoTrip](https://www.onetwotrip.com/) | 7.5 H | Secondary regional seller check |
| **Global** | 1 | [Google Flights](https://www.google.com/travel/flights) | 8.7 H | Explore dates and routes where supported |
| Global | 2 | [Skyscanner](https://www.skyscanner.net/) | 8.5 H | Compare multiple flight sellers |
| Global | 3 | [KAYAK](https://www.kayak.com/flights) | 8.1 H | Cross-check route and date alternatives |
| Global | 4 | [Trip.com](https://www.trip.com/flights/) | 7.9 H | Additional international offers |

**Airline-direct check (always):** After discovering candidates, check the **operating airline's official website** for flight schedule, airport, baggage and fare rules, and compare its *actual final payable fare*. Airline websites are not ranked alongside general metasearch sites because they have a different role.

**For Moscow–Samarkand:** Search **Tutu + Aviasales** first, then Yandex Travel and relevant operating airlines. Do **not** assume Tutu remains cheaper on every departure date or fare.

## How to replace heuristic scores with evidence (source MCDA)

Measure only accessible sources in the **relevant region**, using identical query conditions. Keep this separate from the traveler's flight-ticket MCDA:

| Source criterion | Weight | Evidence |
|---|---:|---|
| **Comparable final-price competitiveness** | **50%** | Same itinerary, date, fare family, baggage, taxes, seller fees and payment currency. Compare final payable prices. |
| **Relevant flight coverage** | **30%** | How many eligible airline/route options the site actually reveals |
| **Search and comparison quality** | **20%** | Visible flight numbers, airports, times, fare/baggage details, filters and price context |

`MeasuredSourceScore = 0.50 × PriceScore + 0.30 × CoverageScore + 0.20 × ComparisonScore`, with each input on 0–10. A **missing price observation remains unknown**, not zero or five; do not output a measured composite until the inputs are supported.

For price scoring, use a fixed rubric across sources, e.g. an equivalent observed offer matching the cheapest valid final quote scores 10; a quote 5% above that price scores 7.5; 10% above scores 5; 20% or more above scores 0. Aggregate over **at least five matched itineraries across multiple departure dates**, and record the sample size, dates and check timestamps. Fewer observations are **insufficient to promote a heuristic score to a measured rank**.

**Do not compare different fare products:** Matching airline and flight number is not enough. Check fare family, cabin, baggage, passenger count, cancellation/change terms, currency and mandatory charges. Record the **actual ticket seller**—some search engines redirect elsewhere. A cached fare or price calendar is not a final checkout offer. Booking service and refunds belong to the final ticket decision, not this search-source score.

## Operating rules

1. Choose **two complementary route-relevant search sites**; use the region list as a starting order, not an exclusive whitelist.
2. Search equivalent flights and capture final offers **only if checkout is accessible**. Otherwise label them advertised or unknown.
3. Compare the chosen candidate on the **operating airline website**, including the final price and rules.
4. Send matching, source-labeled evidence to [flight-research-selection.md](flight-research-selection.md) for hard-constraint checks and **ticket-level** MCDA.
5. If a site is blocked, missing inventory, or unsupported in a market, skip it and record the limitation; do not invent availability or scrape restricted sites.

A URL does not imply API or automated access. Update regional ordering when adequate real comparable-price samples justify it; review links and applicability periodically. **Read-only: no reservations or payments.**
