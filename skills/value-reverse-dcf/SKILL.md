---
name: value-reverse-dcf
description: >
  Solves for the growth that the current market cap of an NSE or BSE
  company already implies, from a sourced price and sourced cash flow.
  Use when the user asks for a reverse DCF, implied growth, or what the
  price assumes. Not a target price and not a fair value.
compatibility: >
  Agent Skills hosts. India listed companies. The discount rate is the
  user's or is stated as an assumption. No invented price.
---

# Reverse DCF

Ask what the price already assumes. Do not say what the price should be.

## Iron rules

1. India only. NSE or BSE. Anything else: stop and say so. Not for a bank, NBFC, or insurer; free cash flow is not their earnings. Say so and stop.
2. Every figure has source, period, and consolidated or standalone. If it is not in a source, write "not found". Do not estimate silently.
3. INR, with crore or lakh stated. Indian fiscal year (April–March) unless the filing says otherwise.
4. Separate fact, inference, and opinion. Inputs are facts. Discount rate, years, and terminal growth are assumptions. The implied growth is inference.
5. Promoter holding, pledge, related parties, and auditor notes are part of the analysis.
6. Close with this disclaimer. No buy, sell, or target presented as advice or as a certain outcome.

> This is an educational research memo, not investment advice, not a SEBI-registered recommendation, and not a solicitation to buy or sell any security. Figures are only as good as the filings cited. You decide what to do with them.

If `analyze-financials` has not already produced the evidence table, read `../analyze-financials/SKILL.md` and do that first.

## Inputs

- Market cap: exchange close times shares outstanding, with the date and exchange. Use the price section in `../analyze-financials/references/statements.md`. A company-printed P/E is not a market cap. A broker quote is not the close.
- Net debt: borrowings minus cash and current investments, same balance-sheet date. Lease liabilities stay out unless the user asks; say which.
- Base free cash flow: cash from operations minus capex (purchase of property, plant, and equipment plus intangibles), consolidated, latest audited year. If it is negative or swings sign across the years opened, stop: the method does not fit. Say "reverse DCF not applicable" and why.
- Discount rate: the user's number. If they gave none, show the result at three rates and label each an assumption. Do not call any rate the cost of equity of this company.
- Explicit years: 10 unless the user says otherwise. Terminal growth: the user's, or show it as an assumption at or below the discount rate minus 4 points. Never above the discount rate.

## Method

Enterprise value = market cap + net debt.

Find g such that the sum over t = 1..N of FCF0 × (1+g)^t / (1+r)^t, plus the terminal value FCF0 × (1+g)^N × (1+gT) / (r − gT) discounted by (1+r)^N, equals enterprise value. Solve by bisection on g between −20% and 60%. If no g in that band fits, write "outside the band" and stop. When a shell is available, run `python scripts/reverse_dcf.py EV FCF0 R N GT` from the repo root rather than solving by hand.

Show the arithmetic once, in a table. Then compare g only with the company's own filed history: revenue and FCF CAGR over the years opened. Do not compare with a sector "normal".

## Return

```markdown
## Reverse DCF
- Market cap: [value, date, exchange, source]
- Net debt: [value, date, statement]
- Base FCF: [CFO, capex, FCF, year, consolidated]
- Assumptions: r = , N = , gT =
- Implied FCF growth: [g at each r] (inference)
- Filed history: [revenue CAGR, FCF CAGR, years] (fact)
- Reading: what the price assumes versus what the filings show (opinion)
- Refuses to opine on: fair value, target, buy or sell
```

## Disclaimer

Paste the disclaimer from the iron rules.
