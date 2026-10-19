# Food taxonomy, provenance and scores

## Approved food primary categories (full labels only)

1. **Rice, Grains, and Substantial Staples** — rice- and grain-centered dishes, significant porridge- or legume-based staple meals.
2. **Breads and Baked Pastries** — flatbreads, filled pastries, tandoor-baked savory goods, bread-centered specialties.
3. **Dumplings and Noodles** — stuffed dough, noodle dishes, steamed dumplings, regional forms of pasta.
4. **Grilled and Meat Specialties** — grilled, roasted, fried, or otherwise protein-centered specialty dishes typical of the cuisine.
5. **Soups and Stews** — soups, broths, slowly cooked spoonable meat/legume preparations, substantial stews.
6. **Produce, Salads, and Accompaniments** — fruits, vegetable specialties, preserved produce, side salads, condiments, and dairy sides.
7. **Sweets and Desserts** — confections, sweets, baked desserts, festive sweet preparations.
8. **Traditional Drinks** — teas, fruit drinks, nonalcoholic specialties, and other locally relevant traditional beverages.

These eight are the Samarkand-compatible baseline taxonomy, not a reason to force nonmatching dishes into the wrong category in another city. If researching a city where an entire major food group is not well covered (e.g. seafood-centered raw specialties), document and propose a **new full descriptive category**, maintain a taxonomy version, and classify consistently. Never use `Other`, category initials, or opaque codes to avoid this decision.

## Geographic identity field

- `city_specific_style`: strong evidence of a distinctive local preparation, NOT necessarily exclusive invention there.
- `regional`: tied to the wider geographic region.
- `national`: established nationally without strong city-exclusive evidence.
- `shared_cross_border`: common across multiple culinary traditions.
- Store sources for the attribution; if evidence is poor, label `needs_verification` in research status.

## Food score: five ratings, 0–5 integers

| Field | Dimension | Weight |
|---|---|---:|
| `local_distinctiveness` | Local distinctiveness | 30% |
| `cultural_significance` | Cultural significance | 25% |
| `culinary_distinctiveness` | Culinary distinctiveness / preparation | 20% |
| `general_traveler_relevance` | General traveler relevance | 15% |
| `availability` | Availability | 10% |

`food_score = (30*local_distinctiveness + 25*cultural_significance + 20*culinary_distinctiveness + 15*general_traveler_relevance + 10*availability) / 5`

Tier labels: `Must-Try Candidate` >=80; `Highly Recommended` >=60; `Optional or Specialist Interest` <60.

## Venue suitability for a particular food

**IMPORTANT:** this is a pair-level score recorded in `food_venue_matches`, not a one-size-fits-all restaurant score. Pair every `food_id` with a `venue_id` and evaluate:

| Field | Dimension | Weight |
|---|---|---:|
| `signature_food_match` | Suitability for this exact food / variant | 35% |
| `preparation_experience` | Preparation or service evidence | 25% |
| `cultural_character` | Relevant cultural setting/experience | 15% |
| `practicality` | Location, accessibility, timing, cost relative to goal | 15% |
| `evidence_confidence` | Strength and currency of verification | 10% |

`venue_suitability_score = (35*signature_food_match + 25*preparation_experience + 15*cultural_character + 15*practicality + 10*evidence_confidence) / 5`

Store independent published venue ratings separately if available; **never** treat them as this specialized suitability score. Do not score a food–venue pair unless a dish-specific match is supported. Record menu status: `verified`, `plausible_needs_confirmation`, or `not_yet_researched`.
