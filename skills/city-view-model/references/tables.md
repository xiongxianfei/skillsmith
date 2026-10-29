# Tables (one Excel sheet each)

| Sheet | One row is | Columns | Feeds |
|---|---|---|---|
| Places | One place (sight, market, workshop, winery) | Place ID, Name, Category, Description, Area, Latitude, Longitude, Best time, Time needed, Cost, Culture ID, Score, Priority, Visited?, Notes | Place, Space |
| Food | One food or drink item | Food ID, Name, Type, Description, Where to try, Season, Price, Related place ID, Score, Priority, Tried?, Notes | Taste |
| Culture | One theme | Culture ID, Theme, Description, Era | Culture |
| Weather | One month | Month, Avg high, Avg low, Rain, Rating (Best/Hot/Cold), Notes | Time |
| Scenarios | One stop in a trip | Scenario, Day, Order, Time, Item type (Place/Food), Item ID, Notes | Scenarios |
| Costs (optional) | One price | Cost ID, Item type, Item ID, Name, Unit, Price, Currency, Price level, Date checked, Notes | Practical |

## Links
- Places -> Culture through Culture ID
- Food -> Places through Related place ID
- Scenarios -> Places or Food through Item type and Item ID
- Costs -> Places or Food through Item type and Item ID
- Weather stands alone

## Conventions
- Sheet names: one capitalized word, no spaces (Places, Food, Culture, Weather, Scenarios, Costs).
- Fix category and type lists first so filters work.
- Priority formula (score in column D, adjust the reference): `=IF(D2>=4,"Must",IF(D2=3,"Nice","Optional"))`
- Use a lookup such as XLOOKUP to show names next to IDs in Scenarios.

## Example Culture themes
Silk Road trade; Timurid empire; Science and learning; Islamic architecture; Traditional crafts; Food traditions. Keep 5-8 themes. A place has one main Culture ID; for several themes use a small link table (Place ID, Culture ID).

## Example Scenario rows
| Scenario | Day | Order | Time | Item type | Item ID | Notes |
|---|---|---|---|---|---|---|
| 4-day first visit | 1 | 1 | Morning | Place | P1 | Buy bread and fruit |
| 4-day first visit | 1 | 2 | Lunch | Food | F1 | Eat before it sells out |
