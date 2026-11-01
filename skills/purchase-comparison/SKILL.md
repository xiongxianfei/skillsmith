---
name: purchase-comparison
description: Build and fill a weighted comparison sheet to choose between products (keyboard, mouse, mousepad, suitcase, or any other item type), where the user sets the scores. Use whenever the user wants to compare, shortlist, rank, score or choose between candidate products or models, asks "which one should I buy", "what attributes should I look at", or mentions the Black Friday comparison sheet, even if they never say "comparison sheet". Covers listing attributes, defining the options for each attribute, letting the user assign option scores and weights, recording candidate models, calculating totals and recommending.
---

# Purchase comparison

Help the user choose a product by comparing candidates on a small set of attributes. The user decides what matters and how much; the skill supplies the structure, the options, the lookups and the arithmetic. **Never invent scores or weights for the user.** Suggestions are allowed only when the user asks for them, and are labelled as optional.

## Core idea

For each attribute: (1) list the **options** that exist, (2) the user gives each option a **score**, (3) the user gives the attribute a **weight**. Each candidate model's value is matched to an option, which gives its score. Total = weights x scores.

## Sheet layout (always the same)

One sheet per item type. Columns: `Model | Row | <attribute 1> | <attribute 2> | ... | Total`, then optional `Source` and `Verified`. The `Row` column lets the user filter. Three header rows, then two rows per model:

| Model | Row | Layout | Weight (g) |
|---|---|---|---|
| Header | Weight | 3 | 2 |
| Header | Options | Full / TKL / 75% / 65% | <50 / 50-60 / 61-70 / >70 |
| Header | Option score | 1 / 5 / 5 / 3 | 2 / 5 / 4 / 0 |
| Model A | Value | TKL | 58 |
| Model A | Score | 5 | 5 |

(Numbers above only show the format. They are not defaults.)

- **Weight row:** importance of each attribute, set by the user. A negative weight is allowed for an attribute the user wants to avoid.
- **Options row:** the possible choices for that attribute, separated by ` / `. Numeric attributes use non-overlapping ranges that cover every realistic value.
- **Option score row:** the user's score for each option, in the same order as the Options row, usually 0-5. The letter `X` means reject: the model is disqualified if its value falls in that option.
- **Value row:** the raw facts for a model, taken from official specs. Leave unknowns blank.
- **Score row:** looked up from the Value row via the Options and Option score rows. `Total` sits only on the Score row: the sum of weight x score, with the maximum (5 x sum of weights) shown beside it as a percentage. Any `X` makes the Total show "Rejected".

## Workflow

1. **Item type and context.** Ask what is being bought and what matters about the user (for example hand size and grip for a mouse, usage mix, budget). Check the conversation and memory first; do not ask for things already known. If the Black Friday tracker (`tblItems`) is in use, the `Item` there is the type name (Keyboard), while this sheet's `Model` column holds exact product names.
2. **Attributes.** Read `references/<item>.md` if one exists for the item type; otherwise propose a short list (6-10) and agree it with the user. Let them add or remove attributes.
3. **Options.** Define the options for every attribute (from the reference file, edited as needed). Check: options are mutually exclusive, ranges do not overlap or leave gaps, and the order is consistent.
4. **User scores.** Show the options and ask the user to fill in the Option score row and the Weight row. Offer to leave any blank for later. If the user asks for suggestions, give them as clearly optional, with a one-line reason each, and only for options the user has not scored.
5. **Candidates.** Record exact model names (including version or size, for example "ZA12", not "ZA"). Fill the Value row from official specs; where specs are from memory or a review site, mark `Verified = No` and say so. Never guess a missing value.
6. **Score and total.** Look up each Value in the Options row. Flag a Value that matches no option, an option with no score, or an attribute with no weight. Compute the Total.
7. **Recommend.** Give the top one to three with the reason (which attributes drove the score), anything unverified, and what needs hands-on testing (for example shape, click feel, texture). Write the final score back to `tblItems` if that tracker exists.

## Building the file

If the user wants a spreadsheet, read the xlsx skill first, then build it with the layout above: an Excel table with the `Row` column filterable, the Option score cells highlighted for the user to fill, and a lookup formula for the Score row (for example `INDEX` with `MATCH` on the Options list, using `TEXTSPLIT` or a helper range for the option lists). Put option lists in helper ranges if splitting text in one cell is unreliable. `Total =SUMPRODUCT(weights, scores)` on Score rows only.

## Rules

- Do not preset Must/Prefer scores. The user's weights and option scores are the only source of truth.
- Do not invent specifications, prices or review numbers. Blank means unknown.
- Keep the Value row factual and the Score row numeric.
- Record source and verified status for every spec.
- Keep replies short and show small tables. Do not repeat the whole sheet after each edit; show only what changed.

## References

- `references/keyboard.md`, `references/mouse.md`, `references/mousepad.md`: attribute lists with options only, no scores. Read the one that matches the item type. For other item types, build a new list in the same format and offer to save it as a new reference file.
