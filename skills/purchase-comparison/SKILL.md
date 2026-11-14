---
name: purchase-comparison
description: Build a personalized purchase decision framework with suggested attribute weights and option suitability scores. Use for choosing a purchase category, deciding what attributes matter, exploring options, or comparing, shortlisting and ranking product models, including the Black Friday comparison sheet. Named products and spreadsheets are optional.
---

# Purchase comparison

Help the user decide what matters before comparing products. A useful, adjustable decision framework is a complete outcome without named models. Recommend both attribute weights and option scores with reasons tied to the user's context; suggestions are not adopted preferences until the user accepts them or asks to use your recommendations.

## Decision framework

1. **Category and context.** Reuse information already in the conversation or available memory. Identify the category, intended use, budget and constraints. Ask focused questions for material gaps; otherwise state assumptions and provide a useful starting framework. Do not require exact product models. In a Black Friday tracker (`tblItems`), `Item` is the category (Keyboard); `Model` holds an exact product name.
2. **Attributes and importance.** Read only the matching [category reference](#references), if available. Adapt it to the context, or propose a short list (usually 6–10 attributes). Recommend importance weights, normally 1–5, with reasons and assumptions. Weight means how much the attribute matters, not how good any option is.
3. **Options and suitability.** Define choices or numeric ranges for each attribute and recommend suitability scores, normally 0–5, with trade-offs and reasons. Score means how well an option suits this user. Check that options are mutually exclusive, numeric ranges cover realistic values without gaps or overlaps (including fractional values), and scores follow the same option order. Adapt reference ranges rather than copying them blindly.
4. **Personalize.** Invite the user to add or remove attributes, change weights or scores, and specify exclusions. Preserve all user-provided values, including values outside the suggested scales. Label each value as user-provided, suggested or adopted; never overwrite an existing value with a suggestion. Do not treat silence as adoption. A request to use your recommendations adopts the identified suggestions; unresolved assumptions remain visible. Finish with the framework unless comparison is requested.

Show two compact tables:

- `Attribute | Importance weight | Status | Reason and assumptions`
- `Attribute | Option | Suitability score | Status | Trade-offs and reason`

Include a clear opportunity to adjust the recommendations. These scales are presentation defaults, not restrictions on user values. If the user wants to leave values blank or declines numerical guidance, honor that choice. Suggestions depend on use: for example, shared-office typing and competitive gaming need different explanations and priorities, not a universal keyboard profile.

## Optional candidate comparison

When requested, use user-provided or adopted preferences. Do not silently use unaccepted suggestions as ranking inputs.

1. **Research candidates.** Record exact models, including version or size (for example `ZA12`, not `ZA`). Use official specifications where possible; record source and verification status for every spec. Mark memory or review-site facts `Verified = No`. Never invent specifications, prices or review numbers; leave unknown values blank.
2. **Score and reject.** Match each known value to an option. Flag unmatched values, missing option scores and missing weights. Unknown is not zero: do not present an incomplete total as a complete comparable result. A known matched `X` rejects the candidate even if other values are unknown. Keep raw facts separate from calculated scores.
3. **Explain results.** When inputs support ranking, give the top one to three, the decisive attributes, anything unverified and aspects needing hands-on testing (shape, click feel, texture). Otherwise explain what prevents ranking. Update the final score in `tblItems` only when that tracker is already in use, accessible and writable through available capabilities; report an update only after it succeeds.

## Sheet layout (always the same)

When a sheet is requested, use one sheet per item type. Columns: `Model | Row | <attribute 1> | <attribute 2> | ... | Total`, then optional `Source` and `Verified`. The `Row` column lets the user filter. Three header rows, then two rows per model:

| Model | Row | Layout | Weight (g) |
|---|---|---|---|
| Header | Weight | 3 | 2 |
| Header | Options | Full / TKL / 75% / 65% | <50 / 50–60 / >60–70 / >70 |
| Header | Option score | 1 / 5 / 5 / 3 | 2 / 5 / 4 / 0 |
| Model A | Value | TKL | 58 |
| Model A | Score | 5 | 5 |

Numbers above illustrate the format; they are not defaults. The interval `>60–70` means greater than 60 and at most 70.

- **Weight row:** user-provided or adopted importance weights. Negative weights remain allowed under the existing contract.
- **Options row:** mutually exclusive choices separated by ` / `; numeric ranges cover every realistic value.
- **Option score row:** user-provided or adopted scores in Options order, usually 0–5. `X` means reject when a model's value matches that option. Do not invent exclusions or preset Must/Prefer scores.
- **Value row:** raw facts, with unknowns blank and sources and verification status recorded.
- **Score row:** look up each Value using Options and Option score. `Total` appears only on Score rows: sum of weight × score, with the percentage relative to `5 × sum(weights)`. Any matched `X` makes Total show `Rejected`.

The existing percentage policy is unspecified for negative weights, scores outside 0–5 and a zero denominator. Preserve supplied values and the raw weighted-sum formula; flag normalization as unresolved in these cases instead of inventing a replacement or presenting a misleading percentage. Never divide by zero. Missing inputs must remain visibly incomplete, including in spreadsheet formulas.

## Building the file

Generate a spreadsheet only when requested and a suitable capability is available. If an xlsx skill is available, read it first. Otherwise use an available spreadsheet tool; if none is available, provide the tables without claiming a file was created.

Preserve the layout above: an Excel table with filterable `Row`, highlighted Option score cells, and Score lookups (for example `INDEX`/`MATCH` with `TEXTSPLIT` or helper ranges). Use helper ranges when splitting option text is unreliable. Use `SUMPRODUCT(weights, scores)` for numeric totals, with guards for rejection, missing inputs and unresolved normalization. Keep suggestion/adoption status explicit alongside the sheet without changing its core layout. Do not claim file creation or tracker updates that did not occur. This skill does not purchase products.

Keep replies short. After edits, show only what changed rather than repeating the entire sheet.

## References

- [Keyboard](references/keyboard.md), [mouse](references/mouse.md), [mousepad](references/mousepad.md): attribute and option starting points, not universal preference profiles. Read only the relevant file; adapt choices and suggest weights and scores from context.
- For other categories, build a contextual list in the same format and offer to save it as a new reference. Do not store personal scores as category defaults.
