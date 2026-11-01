---
name: purchase-comparison
description: Compare products with a Must/Prefer weighted-scoring method and build the Excel comparison sheet. Use this skill whenever the user is deciding what to buy (suitcase, keyboard, mouse, gadgets, Black Friday purchases), wants to list selection factors, rank candidates, set attribute weights, calculate a score out of 100, or design a purchase tracker or comparison table in Excel, even if they don't say "scoring" or "comparison".
---

# Purchase comparison

Help the user pick a product by filtering with Musts, then scoring the rest with weights. Keep raw facts visible next to the scores.

## Method

1. **Define the use.** Who uses it, how often, budget, constraints (e.g. airline size limit, hand size and grip, wired or wireless).
2. **List all candidate attributes first** and let the user pick the ones they care about. Do not decide for them.
3. **Tag each chosen attribute:**
   - **Must**: pass/fail. Failing one removes the model. Keep to 2-4.
   - **Prefer**: scored 0-5 and given a weight 1-5. Avoid giving many attributes the same top weight; the weights should separate what matters most.
   - **Nice**: tie-breaker only, not in the total.
   - **Avoid**: reject the model if present.
4. **Shortlist 3-5 models** that pass every Must. Record raw values, then score each Prefer attribute 0-5.
5. **Scoring rules.**
   - Numeric attributes (weight, price, warranty years): use a rule table that maps ranges to scores.
   - Text attributes (wheel type, shell): use a dropdown mapped to scores.
   - Subjective attributes (zipper quality, click feel): score by hand and explain in Notes.
   - Range-fit attributes (capacity, size): score closeness to the target, not bigger-is-better.
   - Missing data: leave blank and mark the model incomplete. Do not guess.
6. **Check the 1-3 star reviews** of the top two models for recurring problems.
7. **Fit items** (grip, hand size, shoe size) need a real measurement and an easy return policy, since specs cannot confirm comfort.
8. **Timing.** For sales events, check price history (CamelCamelCamel, Keepa) to see whether a deal is real.

## Excel layout

**Main tracker** (one row per purchase)
- Item = the type name (e.g. Suitcase), not the exact model. Put the model in Spec or Notes, or add a Model column.
- Typical columns: Item, Category, Priority, Status, Store, Quantity, target price, current price, Score, Purpose, Spec, Link, Notes.
- When a winner is chosen, copy its price and score into the main row.

**Comparison sheet** (one per compared item; sheet `Suitcase`, table `tblSuitcase`)
- Row 1: attribute weights, above the matching columns. A blank weight means Must. These cells are outside the table.
- Row 2: the table header: `Model | Row | attribute columns... | Total`.
- Freeze panes below the header (cell A3).
- Each model has two rows: a **Value** row (raw facts) and a **Score** row (Pass/Fail for Musts, 0-5 for Prefer). Fill the Model name on both rows.
- Filter Row = Value to see the facts, Row = Score to compare.
- Store numbers as plain numbers and put units in the header, e.g. `Weight (kg)`.

**Total score out of 100** (calculated column, results only on Score rows):

```
=IF([@Row]<>"Score","",SUMPRODUCT($E$1:$K$1,[@[FirstAttr]:[LastAttr]])/(5*SUM($E$1:$K$1))*100)
```

- The weight range and the attribute range must cover the same columns in the same order.
- The denominator is the maximum possible score (5 x sum of weights), not a per-model value.
- Add conditional formatting to turn a Score row red when any Must cell is "Fail".

## Files and folders

- One Excel file per year (e.g. `BlackFriday2026.xlsx`), copied from a clean template with headers, formulas, weights, and lookup sheet but no data.
- Suggested folders: `Shopping/Template`, `Shopping/2026`, `Shopping/Archive`. Keep receipts and warranty PDFs in the year's folder.
- Name sheets and tables the same way, without spaces: `Main` / `tblMain`, `Suitcase` / `tblSuitcase`, `Lists` for lookup tables.

## Pitfalls

- Do not apply a plain AutoFilter to the whole sheet; use the table's filter, or the weight row will be filtered.
- Do not make the weight row part of the table.
- Adding an attribute means inserting a table column and filling its weight in row 1, then extending the Total formula ranges.
- Keep column names distinct from the Row labels (use `Weight (kg)`, not `Weight`).
- Do not use Nice items in the total.

## Worked example (gaming mouse)

Profile: FPS, claw grip, medium hand (18.4 cm x 7.9 cm), wireless, budget $80.
- Musts: Price (at most 80), Fits grip and size (about 110-120 mm long, 60-66 mm wide, hump toward the back).
- Prefer weights: Sensor 5, Weight (g) 4, Click feel 4, Battery 3, Software 2.
- Model A scores 5, 5, 4, 4, 4: 25 + 20 + 16 + 12 + 8 = 81 out of a maximum 90, which is 90/100.
- A model that fails the price Must is out, whatever its score.
