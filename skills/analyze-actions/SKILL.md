---
name: analyze-actions
description: >
  Reads dividends, splits, bonuses, buybacks, and index membership for
  an NSE or BSE company from the exchange. Use when the user asks about
  a corporate action or an index add or drop. An action is not a better
  business.
compatibility: Agent Skills hosts. India listed companies. No price target.
---

# Actions

What the exchange or the company filing records about the share itself. Not a change in the business.

## Iron rules

1. India only. NSE or BSE. Anything else: stop and say so.
2. Every figure has source, period, and the document it came from. If it is not in a source you opened, write "not found". Do not estimate silently.
3. INR, with crore or lakh stated, as the page prints. A per-share dividend stays per share.
4. Separate fact, inference, and opinion.
5. Promoter holding, pledge, related parties, and auditor notes are unchanged by a bonus unless a filing you opened shows a new percent.
6. Close with this disclaimer. No buy, sell, or target presented as advice or as a certain outcome.

> This is an educational research memo, not investment advice, not a SEBI-registered recommendation, and not a solicitation to buy or sell any security. Figures are only as good as the filings cited. You decide what to do with them.

## Where to open

- NSE corporate actions: <https://www.nseindia.com/companies-listing/corporate-filings-actions>. Record the purpose, face value, ex-date, and record date the row prints.
- The company's own exchange filing for a dividend, split, bonus, or buyback. If you only have the annual report's dividend line, say it is the company's reprint. The exchange ex-date is then not found until that page is opened.
- Index membership printed on a quote page is what that page prints on that date. An inclusion or an exclusion is the NSE Indices or BSE index announcement you opened. The quote-page label is not that announcement.

## What to keep straight

A bonus, a split, or an index change is not evidence of a better or worse business. Do not compare a close before the ex-date with a close after it unless you state the action. Do not adjust past profit, EPS, or a multiple unless the filing shows the restated figure. If you adjust, show the arithmetic and say it is yours.

A buyback size is the filing. A newspaper size is not the filing.

## Return

```markdown
## Actions
- Rows:

| Type | Ex-date or record date | Terms | Source |
| --- | --- | --- | --- |

- Index:
- Not a change in the business:
- Not opened:
- Refuses to opine on:
```

Worked pattern: a bonus issue is described as earnings power doubling. The profit figure was not restated. The sentence fails.

## Disclaimer

Paste the disclaimer from the iron rules.
