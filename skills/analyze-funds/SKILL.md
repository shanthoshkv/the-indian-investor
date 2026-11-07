---
name: analyze-funds
description: >
  Reads a mutual fund scheme's month-end portfolio from AMFI or the
  fund's own disclosure. Use when the user asks which scheme holds an
  NSE or BSE stock, or asks to split DII into named funds. A market-wide
  DII net is not a scheme holding.
compatibility: Agent Skills hosts. India only. No buy list of funds.
---

# Funds

One scheme's disclosed portfolio. Not the market-wide DII net in `../analyze-flows/SKILL.md`.

## Iron rules

1. India only. An Indian mutual fund scheme and an NSE or BSE security. Anything else: stop and say so.
2. Every figure has source, period, and the line it came from. If it is not in a source you opened, write "not found". Do not estimate silently.
3. INR, with crore or lakh stated, as the page prints. Quantity is as the page prints.
4. Separate fact, inference, and opinion.
5. Promoter holding is not a fund's holding. Do not move a scheme into the promoter group unless the shareholding pattern says so.
6. Close with this disclaimer. No buy, sell, or target presented as advice or as a certain outcome.

> This is an educational research memo, not investment advice, not a SEBI-registered recommendation, and not a solicitation to buy or sell any security. Figures are only as good as the filings cited. You decide what to do with them.

## Where to open

The month-end portfolio, with ISIN, on AMFI (<https://www.amfiindia.com/online-center/portfolio-disclosure>) or on the AMC's own portfolio page. Open the scheme and the month the user asked for. If the index page lists no scheme, the holding is not found. Do not download every scheme.

Report the security name, ISIN, quantity, market value, and percent of the scheme if that column is printed, plus the portfolio date.

A factsheet's top holdings are not the full portfolio. Say which one you opened. Monthly average AUM is not a holding of this stock. A change versus last month is not found unless you opened both months.

Do not infer the scheme from a day's DII buy. Do not add several schemes and call the sum "DII owns this percent" unless each scheme was opened and you show the arithmetic. That sum is still not the shareholding pattern's mutual-fund line.

## Return

```markdown
## Funds
- Scheme and date:
- Holding:

| Scheme | Date | Security | ISIN | Quantity | Value | Percent of scheme | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |

- Not opened:
- Not a market-wide DII figure:
- Refuses to opine on:
```

Worked pattern: the day's DII net is negative, so a named scheme is said to have sold this stock. The scheme's portfolio was not opened. The holding is not found. The sentence fails.

## Disclaimer

Paste the disclaimer from the iron rules.
