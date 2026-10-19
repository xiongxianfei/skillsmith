# Attraction taxonomy and scoring reference

## Approved primary category values (use exact full labels)

1. **Historical Sites and Architectural Landmarks** — monuments, historic buildings, archaeological sites, architectural ensembles, heritage streets where built heritage is the primary purpose.
2. **Museums, Science, and Learning** — collections, educational displays, science facilities, museum-houses, observatories where learning/interpretation is the main experience.
3. **Scenic Views and Nature** — viewpoints, landscapes, gardens, parks, waterfronts, trails, natural features where setting or scenery is primary.
4. **Local Cuisine and Food Markets** — food markets, culinary walks, cooking demonstrations, characteristic dining locations when evaluated as visitor experiences; individual dishes belong to the food skill.
5. **Arts, Crafts, and Cultural Activities** — workshops, galleries, concerts, performances, traditional crafts, cultural participation.
6. **Neighborhoods and Local Life** — district explorations, lived-in streets, local routines, and residential/urban atmosphere.
7. **Sacred Sites and Spirituality** — active shrines, spiritual practices, pilgrimage destinations where devotion is the principal visitor purpose.
8. **Entertainment, Recreation, and Modern Attractions** — theme parks, modern leisure complexes, sport venues, family recreation, entertainment precincts.

Do not abbreviate these primary category names in deliverables or data.

## Tie-break rules

- A museum inside an old building is **Museums, Science, and Learning** when exhibits are the main reason to go; the building's architecture is a tag.
- A monumental mosque chiefly visited for historic architecture is **Historical Sites and Architectural Landmarks**; a shrine primarily visited for pilgrimage is **Sacred Sites and Spirituality**.
- A *view from* a historic building can be a separate **Scenic Views and Nature** experience only if it adds a genuinely distinct visit; otherwise tag `viewpoint` on the heritage record.
- A working craft demonstration is **Arts, Crafts, and Cultural Activities**; a curated craft museum is **Museums, Science, and Learning**.
- A food bazaar visited chiefly to taste and discover cuisine is **Local Cuisine and Food Markets**; a district walking experience centered on ordinary street life is **Neighborhoods and Local Life**.
- A recently constructed historical-themed entertainment complex is **Entertainment, Recreation, and Modern Attractions**, even if it depicts an old city.

## Secondary tags

Provide two to four highly discriminating tags from themes, context, and experience format. Examples: `Timurid architecture`, `Sogdian archaeology`, `Islamic scholarship`, `Jewish heritage`, `tilework`, `food market`, `traditional papermaking`, `neighborhood walk`, `panorama`, `hands-on workshop`, `Silk Road`. Do not tag everything as `culture`, `beautiful`, or `famous`.

## Rating criteria and weights

| Field name | Dimension | Weight | Meaning |
|---|---|---:|---|
| `city_distinctiveness` | City distinctiveness | 30% | How specifically and strongly it embodies the place's identity |
| `traveler_relevance` | Traveler relevance | 25% | Fit with the stated interests, or an explicit balanced first-time baseline |
| `experience_quality` | Experience quality | 20% | Expected quality, grounded in specific evidence where possible |
| `historical_cultural_value` | Historical or cultural value | 15% | Interpretive, historical, scholarly or cultural importance |
| `practical_value` | Practical value | 10% | Value relative to time, effort, accessibility, and cost |

Each score is an integer from 0 (very weak) to 5 (exceptional).

`weighted_score = (30*city_distinctiveness + 25*traveler_relevance + 20*experience_quality + 15*historical_cultural_value + 10*practical_value) / 5`

Tiers: `Must-Visit Candidate` >=80; `Highly Recommended` >=60 and <80; `Optional or Specialist Interest` <60. Scores are editorial judgments; all ratings must be present before calculation. Never give an unrated candidate a zero score.
