---
name: track-shareholding
description: >
  Tabulates the quarterly shareholding pattern of an NSE or BSE company
  across up to eight quarters: promoter, pledge, FPI, mutual funds, other
  DII, and public. Use when the user asks how shareholding, promoter
  stake, or institutional ownership changed over time. Not a deal list and
  not a named fund's holding.
compatibility: >
  Agent Skills hosts. India listed companies. Reads Regulation 31
  shareholding patterns from the exchange.
---

# Track shareholding

A series from the exchange filing. Not a reason to trade.

## Iron rules

1. India only. NSE or BSE. Anything else: stop and say so.
2. Every cell has the quarter-end date and the exchange page. A quarter not opened is "not found". Do not interpolate.
3. Percent of total shares as the filing prints it.
4. Separate fact, inference, and opinion.
5. Promoter holding and pledge are the core of this skill.
6. Close with this disclaimer. No buy, sell, or target presented as advice or as a certain outcome.

> This is an educational research memo, not investment advice, not a SEBI-registered recommendation, and not a solicitation to buy or sell any security. Figures are only as good as the filings cited. You decide what to do with them.

## Method

- Source: the Regulation 31 shareholding pattern on the NSE or BSE company page. Table I (summary) for categories, Table II for promoter pledge and encumbrance.
- Columns: promoter and promoter group, pledged or encumbered as percent of promoter shares, FPI (Category I and II together, say so), mutual funds, other DII (insurance, banks, AIF, pension), retail and HNI public, others.
- A change in share count (bonus, split, QIP, ESOP) moves percentages without a sale. Check `../analyze-actions/SKILL.md` rows for the quarter and say so when it applies.
- Who traded is `../analyze-deals/SKILL.md`. Which scheme holds it is `../analyze-funds/SKILL.md`. Do not restate them.

## Return

```markdown
## Shareholding
| Quarter end | Promoter % | Pledged % of promoter | FPI % | MF % | Other DII % | Public % | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |

- Change over the series: (fact)
- Share-count changes in the window:
- Reading: (opinion)
- Refuses to opine on: why anyone bought or sold, buy or sell
```

## Disclaimer

Paste the disclaimer from the iron rules.
