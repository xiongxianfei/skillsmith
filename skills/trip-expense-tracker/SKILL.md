---
name: trip-expense-tracker
description: Build or fix a multi-currency trip expense workbook (.xlsx) that separates cash from card, tracks ATM/exchange cash cost, flags reimbursable fees, splits totals by card, and reports everything in one configurable base currency. Use whenever the user mentions tracking trip or travel costs, a travel expense sheet or bill, exchanging or withdrawing cash abroad, ATM fees, effective exchange rate, reimbursable expenses, multiple currencies or multiple cards on a trip, or asks to design/repair such a spreadsheet, even if they don't say "skill" or "template".
---

# Trip Expense Tracker

Builds an Excel workbook that answers: what did the trip really cost, what will be paid back, and how much did fees on cash cost.

Read the xlsx skill (`/mnt/skills/public/xlsx/SKILL.md`) before creating the file.

## Step 1: Ask (only what is missing)

1. **Base currency**: the one all totals use (e.g. CNY, USD). Default: ask.
2. **Cash currency**: the destination currency obtained as cash (e.g. UZS).
3. **Other currencies** paid in (card currency, home currency, etc.).
4. **Cards** used (names or last four digits).
5. **Reimbursable categories** (e.g. visa fee only).
6. **Trip dates**.

Never hard-code a currency. Everything reads from Settings.

## Step 2: Workbook structure

Sheet order: `Summary`, `Expenses`, `Cash_in`, `Rates`, `Lists`. Sheet names have no spaces.

Each data range is an Excel Table with the `tbl` prefix: `tblExpenses`, `tblCashIn`, `tblRates`, and one single-column table per list (`tblCategories`, `tblCurrencies`, `tblMethods`, `tblCards`, `tblSources`, `tblYesNo`).

**Settings** (top of Rates, rows 1-2, tables start in row 4): named cells `Base_currency` and `Cash_currency`, each with a dropdown from `tblCurrencies`.

### tblExpenses (one row per payment)
`Date | Category | Description | Amount | Currency | Amount_base | Method | Card | Reimb | Note`
- Amount_base: `=[@Amount]/XLOOKUP([@[Currency]],tblRates[Currency],tblRates[Official_per_base])`
- Method is Card or Cash. Card is filled only when Method = Card.
- Reimb is Yes only for reimbursable items. Never subtract the reimbursement from the row.

### tblCashIn (one row per cash received)
`Date | Source | Description | Amount | Currency | Cost | Cost_currency | Method | Card | Cost_base | Rate_got`
- Source: ATM, Exchange, Person.
- Cost is what it cost the user to get the cash, in Cost_currency. Repayments and gifts: Cost = 0, Cost_currency = base currency.
- Cost_base: `=[@Cost]/XLOOKUP([@[Cost_currency]],tblRates[Currency],tblRates[Official_per_base])`. Always use Official_per_base here, never an effective rate (circular).
- Rate_got: `=IF([@[Cost_base]]=0,"",[@Amount]/[@[Cost_base]])`

### tblRates (units per 1 base currency)
`Currency | Official_rate | Official_per_base`
- Official_rate is typed, all in one common reference currency (the row whose rate is 1).
- Official_per_base: `=[@[Official_rate]]/INDEX([Official_rate],MATCH(Base_currency,[Currency],0))`

### Lists
One single-column table per dropdown. Data validation sources: `=INDIRECT("tblCategories[Category]")` etc.

Default categories: Lodging, Food, Local transport, Intercity transport, Tours, SIM, Visa fee, Fees, Shopping, Tips, Other.

## Step 3: Summary (formulas only; columns Item | Value | Note)

Stack blocks vertically with a blank row and a coloured title row between them:

1. **Headline (base currency)**: total cash cost `=SUM(tblCashIn[Cost_base])`, total card cost `=SUMIFS(tblExpenses[Amount_base],tblExpenses[Method],"Card")`, total trip cost (sum), reimbursable `=SUMIFS(tblExpenses[Amount_base],tblExpenses[Reimb],"Yes")`, personal cost (total - reimbursable).
2. **Cash exchange**: total exchanged cash currency, value at official rate, real cost, effective rate, fee rate. Exclude zero-cost rows with `tblCashIn[Cost_base],">0"`.
3. **By card**: per card, purchases, ATM/cash cost, total, reimbursable. Totals must match block 1.
4. **By category**: SUMIFS on Amount_base; add "Unspent cash (value)" so the total equals total trip cost.
5. **Cash balance** per cash currency: received minus spent with Method = Cash.
6. **Checks**: `IF(ABS(a-b)<0.01,"OK","Check")` for each cross-total, and base currency present in tblRates.

Headings that name the currency use formulas such as `="Total trip cost ("&Base_currency&")"`.

## Design rules

- Dates are real dates, displayed `yyyy-mm-dd`. Date is always column A.
- Same header style on every sheet; freeze row 1 of data sheets.
- Yellow fill = typed input, grey = formula.
- Number formats: `#,##0` for large-unit currencies, `#,##0.00` for others.
- Column names have no spaces or brackets. In formulas always use `[@[Column_name]]`.
- Headers must contain no trailing spaces.
- Do not count cash twice: spending cash is recorded in Expenses (Method = Cash) but only the cost of obtaining it (Cash_in) enters the trip total.

## Daily use (tell the user)

Log each payment and each cash receipt the same day, pick the Card, keep receipt photos for reimbursable items, then open Summary and confirm every check says OK.

## Known pitfalls

- `Base_currency` must be a workbook-scoped name pointing at the value cell. Do not quote it inside formulas.
- Table structured references need Excel; Google Sheets needs plain ranges instead.
- If a reimbursement is paid in another currency, keep the original amount and currency on that row.
