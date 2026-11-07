---
name: diff-results
description: >
  Diffs a newly filed quarter against the last memo's "what would change
  the conclusion" list for an NSE or BSE company. Use when the user asks
  what changed this quarter. The quarter stays out of the annual ratios.
compatibility: Agent Skills hosts. India listed companies. Needs the prior memo and the new filing.
---

# Diff results

The new filing against the list the last memo already wrote. Not a new thesis.

## Iron rules

1. India only. NSE, BSE, or an India bootstrapped company. Anything else: stop and say so.
2. Every figure has source, period, and consolidated or standalone. If it is not in a source, write "not found". Do not estimate silently.
3. INR, with crore or lakh stated. Indian fiscal year (April–March) unless the filing says otherwise.
4. Separate fact, inference, and opinion.
5. Promoter holding and pledge change only if the new Regulation 31 file was opened. An annual-report dash is not that file.
6. Close with this disclaimer. No buy, sell, or target presented as advice or as a certain outcome.

> This is an educational research memo, not investment advice, not a SEBI-registered recommendation, and not a solicitation to buy or sell any security. Figures are only as good as the filings cited. You decide what to do with them.

## What to open

The last memo's "What would change the conclusion". The new quarterly filing, local file first (`../read-filings/SKILL.md`). Typical lines on that list are revenue, debt, pledge, the auditor, and related parties. If the last memo has no such list, say so and stop. Do not invent the list.

Keep every label the file prints. `WhetherResultsAreAuditedOrUnaudited` and a board letter's "limited review" stay separate. A `FourD` half-year cell is not the quarter. Do not put the quarter into an annual ratio. Do not annualize it and call it ROCE.

A movement is not a buy or a sell.

## Return

```markdown
## Results diff
- Last memo:
- New filing:
- Labels (audited, unaudited, limited review):

| What would change the conclusion | This filing | Same or changed |
| --- | --- | --- |

- Left out of the annual ratios:
- Refuses to opine on:
```

## Disclaimer

Paste the disclaimer from the iron rules.
