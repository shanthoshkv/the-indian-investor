---
name: analyze-deals
description: >
  Reads block deals, bulk deals, and SAST or insider disclosures for
  one NSE or BSE company from the exchange page. Use when the user asks
  who bought or sold in bulk, a block, a pledge event, or an insider
  filing. A deal is not the promoter holding percent.
compatibility: Agent Skills hosts. India listed companies. No F&O tips.
---

# Deals

One company's exchange disclosures of large trades and of acquisitions, sales, and encumbrances. Not the market-wide flow in `../analyze-flows/SKILL.md`. Not a reason to buy or sell.

## Iron rules

1. India only. NSE or BSE. Anything else: stop and say so.
2. Every figure has source, period, and the series it belongs to. If it is not in a source you opened, write "not found". Do not estimate silently. Consolidated or standalone does not apply to a trade row. Say so.
3. INR, with crore or lakh stated, as the page prints. Quantity is in shares as the page prints.
4. Separate fact, inference, and opinion.
5. Promoter holding and pledge stay the shareholding pattern and the Regulation 31 file in `../analyze-financials/SKILL.md`. A deal row does not replace them.
6. Close with this disclaimer. No buy, sell, or target presented as advice or as a certain outcome.

> This is an educational research memo, not investment advice, not a SEBI-registered recommendation, and not a solicitation to buy or sell any security. Figures are only as good as the filings cited. You decide what to do with them.

## Where to open

Open the dates the user asked for. If the page caps the rows, say the cap and that the rest was not opened. Do not build a history database.

- NSE bulk, block, and the short-selling tab live on one report: <https://www.nseindia.com/report-detail/display-bulk-and-block-deals>. Use the tab you opened. The short-selling tab is not a bulk deal and not an F&O tip. The page says the rows can change when a member asks, and that the screen may not show every row.
- BSE bulk: <https://www.bseindia.com/markets/equity/EQReports/bulk_deals.aspx>. BSE block: <https://www.bseindia.com/markets/equity/EQReports/Block_Deals.aspx>. The combined selector is <https://www.bseindia.com/markets/equity/EQReports/BulknBlockDeals.aspx>. B and S mean what that page's note says.
- SAST and insider rows: the company's own exchange disclosure (the SAST tab or the announcement PDF), not a newspaper. Report the regulation number the row prints. Do not invent one. An inter-se transfer, an offer for sale, and a market purchase are different modes. Keep the mode the page prints.
- A person or fund on a bulk row is that name. It is not "the promoter" unless the row, or the shareholding pattern you opened, says so.

If the same trade might be on NSE and on BSE and you cannot see that it is one trade, show both rows and do not add the quantities.

## What a row is not

The promoter percent is the shareholding pattern. A deal's "holding after transaction" is that disclosure's figure on that date. It does not replace a later pattern. A pledge event under the regulation the row prints is not the Regulation 31 percent until that file is opened.

## Return

```markdown
## Deals
- Dates asked:
- Rows:

| Date | Venue | Name | Buy or sell | Quantity | Price | Mode or regulation | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |

- Not the promoter percent:
- Not opened:
- Refuses to opine on:
```

Worked pattern: an old inter-se row is copied in as this year's promoter percent. The dates differ. The row fails as a holding figure.

## Disclaimer

Paste the disclaimer from the iron rules.
