---
name: note-costs
description: >
  Notes brokerage, securities transaction tax, and holding-period tax
  for one year from the page that was opened. Use when the user asks
  what a delivery trade in an Indian listed share costs. A rate that
  was not on the page is not found.
compatibility: >
  Agent Skills hosts. India cash equities. Not an F&O tip. No invented rate.
---

# Note costs

Charges for a year, from pages opened that year. Not a view on a share. Not part of the default memo.

## Iron rules

1. India only. A delivery trade in an NSE or BSE equity share. Anything else: stop and say so. Do not turn a derivatives row into an F&O tip.
2. Every rate has the page and the column date. If the page was not opened, write "not found". Do not estimate silently.
3. INR. State percent as the page prints it.
4. Separate fact, inference, and opinion.
5. A cost is not promoter holding, pledge, or a reason to trade.
6. Close with this disclaimer. No buy, sell, or target presented as advice or as a certain outcome.

> This is an educational research memo, not investment advice, not a SEBI-registered recommendation, and not a solicitation to buy or sell any security. Figures are only as good as the filings cited. You decide what to do with them.

## Where to read

- Brokerage is the user's broker contract, if they saved it or you opened it. Otherwise brokerage is not found. Do not invent a brokerage rate.
- STT, and GST on stock-broker services, come from the NSE charge sheet you opened. The sheet's heading on the page already saved is "SEBI Turnover Fees, STT and Other levies". Quote the row for purchase or sale of an equity share settled by delivery, and the GST row for stock brokers services. Name which rate column the year falls in. If a later page you open prints a different rate, use that page and say so.
- Holding-period tax comes from the Income Tax Department page you opened. If that page was not opened, the rate is not found. A holding-period sentence is not the tax rate unless that same page prints the rate. Do not supply a rate from memory.

Quote the delivery rows only. Leave the option and futures rows unread in the memo.

## Return

```markdown
## Costs
- Year:
- Brokerage:
- STT, delivery purchase:
- STT, delivery sale:
- GST on broker services:
- Holding-period tax:
- Page not opened:
- Refuses to opine on:
```

Worked pattern: the charge sheet was opened and the income-tax rate page was not. Brokerage is not found. The tax rate is not found. The STT cells are whatever that sheet printed. That is not a view on the share.

## Disclaimer

Paste the disclaimer from the iron rules.
