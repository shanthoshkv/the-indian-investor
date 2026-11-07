---
name: analyze-flows
description: >
  Reads market-wide FII, FPI, and DII cash flows from the NSE report,
  the BSE category-wise turnover page, and NSDL or CDSL FPI reports,
  including calendar nets, assets under custody, and a sector file
  when those were opened. Use when the user asks about FII, FPI, DII,
  or institutional buying and selling in the Indian cash market. Not a
  company fact, not an F&O tip, and not part of the default memo.
compatibility: Agent Skills hosts. India cash market. No market-data API. No F&O tips.
---

# Flows

Market-wide cash buying and selling. A row here is not a fact about one issuer. A day's net is not a reason to buy or sell a stock. Stock-level FPI or DII holding stays in the shareholding pattern, in `../analyze-financials/SKILL.md`.

SEBI folded the old FII category into foreign portfolio investors. Reports still print FII/FPI. Use the label the page prints. Do not rename a row.

## Iron rules

1. India only. Cash activity on NSE, BSE, or MSEI, or an FPI report from NSDL or CDSL about India. Anything else: stop and say so.
2. Every figure has source, period, and the series it belongs to. If it is not in a source you opened, write "not found". Do not estimate silently. Consolidated or standalone does not apply to a market-wide flow. Say so.
3. INR, with crore or lakh stated, as the page prints. If the page is in USD, say USD. Do not convert unless that same page prints the INR figure.
4. Separate fact, inference, and opinion.
5. Promoter holding, pledge, related parties, and auditor notes are not this report. Do not invent them from a flow.
6. Close with this disclaimer. No buy, sell, or target presented as advice or as a certain outcome.

> This is an educational research memo, not investment advice, not a SEBI-registered recommendation, and not a solicitation to buy or sell any security. Figures are only as good as the filings cited. You decide what to do with them.

## Where to open

Open the dates the user asked for. If they ask for a year and the page shows a shorter window, say what was not opened. Do not save a history into a database.

Keep these series apart. If two were opened and they differ, show both. Do not average them. Do not subtract one from another and call the difference a venue you did not open.

1. NSE, one page, two cash tables: <https://www.nseindia.com/reports/fii-dii>
   - The first table is NSE-only capital-market activity (NSE exclusive).
   - The second is FII/FPI and DII trading activity on NSE, BSE, and MSEI in the capital market segment.
   - Both are provisional. The page's own note: the figures can change on custodial confirmation; FII/FPI is compiled from PANs provided by NSDL; expiry-day physical-settlement obligations are included; DII uses trading codes and the client-category classification members upload.
   - That note sends final FII/FPI to NSDL or CDSL. A provisional net is not the confirmed net.

2. BSE category-wise turnover: <https://www.bseindia.com/markets/equity/EQReports/categorywise_turnover.aspx?expandable=3>
   - Blocks headed as FII/FPI or DII activity on BSE, NSE, and MSEI are the combined series, the same family as NSE's second table. Label them combined. Do not call them BSE-only.
   - Clients, NRI, and proprietary turnover on that page is a different report. Do not add those columns into FII or DII.
   - If a file you opened is actually BSE-only institutional cash, label it BSE. If the fetch is denied or the cells are empty, the amount is not found.

3. NSDL confirmed FPI: <https://www.fpi.nsdl.co.in/web/Reports/Latest.aspx>
   - Keep the asset classes the page prints apart: equity (including a primary-market line if that is the heading), debt general limit, debt VRR, debt FAR, hybrid, mutual fund schemes, AIFs, and the total. Do not drop debt or hybrid into the equity net. Do not add rows the page already totaled and call that the page's total.
   - Exchanges compile provisional FII/FPI from members on the trade day. Confirmed figures are custodian reports to the depositories and are trades up to the previous trading day. Say which of those the page is.
   - A section on FPI derivative trades is not this skill. If the user asks for FII futures, options, or open interest, say this pack does not give an F&O tip. Report cash only when cash was opened.
   - Foreign investment limit monitoring is a different report. Do not use it as the daily flow.
   - If the numeric cells do not come through, the amounts are not found. Do not fill them from a portal.

4. CDSL: <https://www.cdslindia.com/Publications/ForeignPortInvestor.html>
   - Open it when NSDL was not opened, or when the user asked. If both were opened and they differ, show both.

A portal, newspaper, or social post is a way to find the date. If an exchange or depository page was opened, the portal does not override it. If only the portal was seen, the figure is not found.

SEBI's FPI statistics, only after you have opened that page. Do not invent the path. A registration count is not a day's cash flow. An NSE Market Pulse share of turnover is not this buy/sell report. Do not mix them.

## What to report

For each row: date, category as printed, gross buy, gross sell, net, segment, provisional or final, venues, and the URL.

Net is buy minus sell, as the page prints. A small net on a large gross is not a quiet day. Report all three.

Do not sum a window the page did not print and call it the source's total. If you add days you opened, show the days and say the sum is yours.

Do not split DII into mutual funds, insurers, and banks unless the page you opened prints that split. A named scheme's holding of one company is `../analyze-funds/SKILL.md`. The market-wide net is not that holding.

## Stock, not a day's trade

These are still this skill. They are not the provisional cash tables above. If a total here differs from a day's NSE net, show both. Do not average them.

- NSDL calendar-year nets: <https://www.fpi.nsdl.co.in/Reports/Yearwise.aspx?RptType=6>. Monthly equity, debt general limit, debt VRR, debt FAR, hybrid, mutual-fund rows, and AIFs stay apart. The page's note says the figures are custodian reports and trades up to the previous trading day. A stub that says "up to" a date is not a full month.
- NSDL quarterly nets: <https://www.fpi.nsdl.co.in/web/Reports/QuarterlyWise.aspx>. A different aggregation. If its total differs from the monthly page, show both.
- Assets under custody: the category-wise AUC report you opened from <https://www.fpi.nsdl.co.in/web/Reports/ReportsListing.aspx>. AUC is a stock of assets. It is not a buy. Use it only with the year or the as-on date that page prints. A report that opens on an old default year is that year.
- Fortnightly sector file: the NSDL file titled as sector-wise FII or FPI investment. Keep each sector's equity AUC apart from that fortnight's net investment, and apart from debt. A sector total is not a holding in one company. If the file you opened is on a pilot host, say so. Do not treat it as confirmed against www.fpi.nsdl.co.in unless you opened that file too.
- NSDL's DII report, if you opened it, may split banks and other institutions. That split is still market-wide. It is not a scheme's portfolio.

The foreign-investment breach list is not a day's flow and not a fund's holding.

## Return

```markdown
## Flows
- Dates asked:
- Series opened:
- Rows:

| Date | Category | Buy | Sell | Net | Segment | Provisional or final | Venues | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

- Not opened:
- Not the same series:
- Stock versus a day's trade:
- Refuses to opine on:
```

Worked pattern: a portal prints one FII net and says a named stock will rise. The exchange page for that date has an NSE-only net and a combined NSE+BSE+MSEI net, and they are not the same number. Reporting the portal net as the NSE-only net fails. Using either net as a reason to buy the stock fails. One day has no company link.

## Disclaimer

Paste the disclaimer from the iron rules.
