---
name: city-view-model
description: Build a structured, multi-view profile of a city or travel destination using the 5+1 City View Model (Place, Taste, Culture, Space, Time, plus Scenarios). Produces linked tables in one Excel workbook, 1-5 priority scores, checklists, map/chart/diagram suggestions and a one-page layout. Make sure to use this skill whenever the user wants to summarize, organize, record, score or present a city or destination - attractions, food, culture, weather, maps, trip scenarios, checklists, or "how should we record data about a city" - even if they do not mention views or Excel.
---

# 5+1 City View Model

Describe a city through six views, each answering one question, all built from a small set of linked tables. The method borrows the idea of 4+1 architecture views: choose views by what people need to know, then use scenarios to test them.

## Views

| View | Question | Table |
|---|---|---|
| Place | What is there? | Places |
| Taste | What do I eat and drink? | Food |
| Culture | Why does it matter? | Culture |
| Space | Where is it? | Places (Area, Latitude, Longitude) |
| Time | When should I go? | Weather, plus Season and Best time columns |
| Scenarios (+1) | How do I use it all? | Scenarios |

Details: `references/views.md`. Do not add views unless a scenario cannot be answered with these. Optional later views: Practical (money, language, transport, etiquette) and Costs.

## Workflow

1. **Scope.** Ask which city and what the purpose is (trip length, interests). Ask at most one or two questions, then proceed.
2. **Collect items.** List places and food, then check for gaps with the user (for example drinks, sweets, workshops, markets).
3. **Build tables.** Use the sheets and columns in `references/tables.md`. One row per item, unique IDs, tables linked by ID, never by retyped names.
4. **Score.** Give each Place and Food item one score from 1 to 5 (5 = can't miss). Priority is a formula: 4-5 Must, 3 Nice, 1-2 Optional. Scores are the user's to adjust.
5. **Pick pictures.** Choose one picture type per view, generated from the tables (see `references/pictures.md`).
6. **Assemble.** Arrange the one-page layout: header, Place and Taste checklists, map, Time and Culture, Scenario at the bottom.
7. **Test with scenarios.** Write 2-3 example trips (for example "4-day first visit", "Food lover day"). If a stop cannot be linked to an ID, an item is missing from the tables.

## Output defaults

- One Excel workbook named `City_City_Views.xlsx` (for example `Samarkand_City_Views.xlsx`), one sheet per table, plus an optional "Read me" sheet first. Use the xlsx skill to build it if available.
- Underscores in all file and folder names (a double-click selects the whole name on any device).
- Folder: keep the master workbook and working files together, and add one `00_Published` folder for final files only. Never edit files inside it; edit the original and copy over again.
- If the user asks for the one-page picture, build it from the tables and keep colors consistent: Must red, Nice amber, Optional gray.

## Rules

- Keep it simple: at most six sheets, one score per item, remove any column that is never used.
- If a file, sheet or column cannot be explained in one sentence, remove or merge it.
- Prices, hours, seasons and other changing facts should be checked with current sources, and the check date recorded.
- Put unknown values as "(fill in)" rather than inventing them.
