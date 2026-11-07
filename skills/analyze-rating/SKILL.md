---
name: analyze-rating
description: >
  Reads a credit-rating symbol and, when the file was opened, its
  rationale for an NSE or BSE company from the exchange filing. Use when
  the user asks for a rating, outlook, or downgrade. A news line is not
  the rationale.
compatibility: Agent Skills hosts. India listed companies. No safe-rating scale.
---

# Rating

The rating the company or the agency filed. Not a view on the share.

## Iron rules

1. India only. NSE or BSE, or the rating of an instrument of that issuer. Anything else: stop and say so.
2. Every figure has source, period, and the instrument. If it is not in a source you opened, write "not found". Do not estimate silently.
3. INR, with crore or lakh stated, only if the page prints the unit. If the amount cell has no unit, do not invent one.
4. Separate fact, inference, and opinion.
5. Promoter holding and pledge are not a rating. Do not infer them from a symbol.
6. Close with this disclaimer. No buy, sell, or target presented as advice or as a certain outcome.

> This is an educational research memo, not investment advice, not a SEBI-registered recommendation, and not a solicitation to buy or sell any security. Figures are only as good as the filings cited. You decide what to do with them.

## Where to open

The credit-rating announcement on NSE or BSE, or the CRA submission table on the company's exchange page. Report the agency, the instrument, the symbol, the outlook if the cell has one, the date, the amount as printed, and the action (new, reaffirmed, or whatever that row prints).

The reason is the rationale PDF that row links, and only after you opened it. A symbol with an unopened link means the reason is not found. The annual report's sentence about a rating is the company's reprint. Say so. It does not replace the rationale.

A newspaper line is not the rationale. Do not invent a notch ladder or call a symbol safe. A rating is not a conclusion about the equity.

## Return

```markdown
## Rating
- Rows:

| Date | Agency | Instrument | Symbol | Outlook | Amount | Action | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |

- Reason, from the rationale file:
- Not opened:
- Refuses to opine on:
```

Worked pattern: a news headline says the rating was cut. The exchange row was not opened. The symbol and the reason are not found. The headline fails.

## Disclaimer

Paste the disclaimer from the iron rules.
