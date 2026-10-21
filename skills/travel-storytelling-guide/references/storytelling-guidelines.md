# Evidence, narrative and saved-output guidance

## Research once; adapt the delivery

Choose a small supported fact set before drafting either mode. The pre-trip story
creates curiosity; the on-location script directs attention. They need not use every
claim or repeat the same sentences. Preserve the same dates, names, qualifications
and sense of place. A rhetorical question or declared metaphor is not historical
proof; do not disguise invented action as an evocative reconstruction.

Use factual detail selectively: one contrast is stronger than a list of rulers.
Explain an unfamiliar term on first use. Food commentary should distinguish a
regional preparation from a wider tradition and a documented recipe from a particular
restaurant's unverified plate. Invite comparison without declaring a single authentic
version or exoticizing communities.

## Evidence rules

| Kind | Treatment |
| --- | --- |
| Documented fact | Link the specific assertion to a credible source and relevant passage. |
| Interpretation | Label as a way to understand the evidence, not a proven historical intention. |
| Legend / oral tradition | Identify who records it and explicitly say it is a tradition, not an established event. |
| Disputed claim | State the disagreement or use the less precise supported claim. |
| Unsupported claim | Omit from narration; record as a gap if material. |

Prefer original heritage descriptions, museum records, scholarship and practitioner
accounts. A tourism authority is useful, but is not sufficient proof of every anecdote
or symbolic interpretation it publishes. Cross-check consequential, contested or
surprisingly precise claims when possible. Repeated travel-blog wording is not
independent corroboration. Do not cite an unopened page as read: record an indexed
excerpt, supplied extract, inaccessible page or user account accurately. If browsing
is unavailable, use supplied evidence with its limits and write less; do not fabricate
fresh verification. Record publication dates when known and a separate checked date.

Paraphrase sources, quote sparingly and accurately, and avoid invented speech or
unlicensed copied illustrations. Claims about restoration, contested chronology or
origins must not vanish when a reading version is shortened into a spoken version.
When no legend is needed, do not add one merely for drama.

## On-location delivery

Begin with a safe, optional orientation: “From a permitted place where the facade is
visible…” or “Once you are comfortably seated…”. Use conditionals for visibility,
access, service and sensory details. Do not assume a particular viewpoint or claim
live awareness. A named feature is safer than an unexplained “on your left.” Stage
cues such as `[Pause]` are not spoken. Give a nonvisual or non-tasting alternative
where practical. State that timing is estimated (use 130 spoken words/minute for
English demos); actual pacing and pauses vary. If a requested shorter duration is
unrealistic, shorten the story rather than accelerating factual overload.

Keep precautionary context separate from the main story where possible. Do not turn
cultural commentary into clinical dietary advice, a kitchen inspection, directions
through closed areas or a claim of access. Sensory invitations are optional, not
universal truths about the visitor's experience.

## Two-file contract (only for saved commentary)

`stories.json` has `schema_version`, `language`, `created_date`, `sources[]` and
`stories[]`. A source has `source_id`, `title`, `publisher`, `url`, `checked_at`,
`access` and `supports`; distinguish `page_read`, `indexed_excerpt` and `user_supplied`.
Use an appropriate supplied-source label rather than inventing a URL.

A story has:

- `story_id`, `subject_type` (`attraction` or `food`), `subject_id` (upstream ID or
  null), `title`, optional `place_id` / `venue_id`, and `research_input` provenance.
- `claims[]`: `claim_id`, `text`, `kind` (`documented`, `interpretation`, `tradition`
  or `disputed`), `source_ids[]` and optional `note`. Unsupported content belongs in
  `limitations[]`, not a falsely sourced claim.
- `pre_trip` and/or `on_location`: `text`, `claim_ids[]`, `word_count`; on-location
  may also have `estimated_minutes` and `assumed_words_per_minute`.
- `limitations[]`: current access, source gaps, variant differences and any content
  deliberately excluded. Never imply that a working restaurant or entrance was checked
  merely because historical sources were read.

Use UTF-8, unique IDs and valid references. Subject IDs are not ranks. When reconciling
an existing story, retain its ID; multiple stories can discuss the same physical place.
The readable `guided_commentary.md` contains identical narrative text, mode headings,
orientation/pacing notes and a claim/source key outside the spoken script. Keep
commentary order independent of itinerary order. Unknown facts stay unknown.

## Review cases

- **Both modes:** same claim set; no contradictory dates or regional attribution.
- **“Invent what the ruler said”:** no invented quotation presented as history.
- **Legend requested:** recorded tradition explicitly labeled in both narrative and ledger.
- **No research/browsing:** brief qualified account from available evidence; missing
  claims disclosed, never filled with an imagined scene.
- **Unknown position or plate:** conditional cues, no ungrounded directions or ingredients.
- **Audio requested without tools:** a speech-ready script, explicitly no audio file.
- **Research imports:** actual subject IDs retained; scores and planning data untouched.
- **Saved pair:** every claim/source ID resolves, both files have the same prose,
  and source-access notes distinguish full pages from indexed excerpts.

These are expected behaviors for review, not proof of model performance. Structural
tests establish file consistency only. Review actual prose for accuracy, engagement,
respect, pronunciation burden and natural spoken flow before calling it ready.
