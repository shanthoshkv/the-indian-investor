---
name: read-concall
description: >
  Reads earnings-call transcripts or investor presentations of an NSE or
  BSE company filed on the exchange and checks what management said
  against what the next filings showed. Use when the user asks about a
  concall, management guidance, commentary, or whether management
  delivered. Guidance is not a fact about the future.
compatibility: >
  Agent Skills hosts. India listed companies. Reads Regulation 30
  transcript and presentation filings.
---

# Read concall

Say-versus-do. Not a forecast.

## Iron rules

1. India only. NSE or BSE. Anything else: stop and say so.
2. Every quote has the call date, the speaker's role, and the filing link. Every check-back figure has source, period, and consolidated or standalone. If not opened, "not found".
3. INR, with crore or lakh stated. Indian fiscal year (April–March) unless the filing says otherwise.
4. Separate fact, inference, and opinion. What management said is a fact that it was said. Whether it happens is not a fact.
5. Promoter holding, pledge, related parties, and auditor notes are part of the analysis.
6. Close with this disclaimer. No buy, sell, or target presented as advice or as a certain outcome.

> This is an educational research memo, not investment advice, not a SEBI-registered recommendation, and not a solicitation to buy or sell any security. Figures are only as good as the filings cited. You decide what to do with them.

## Where to read

Transcripts are filed with the exchange under Regulation 30, usually within days of the call. Use the exchange filing or the company's investor page. A media summary or a broker note is not the transcript.

## Method

1. Pick the calls the user named, or the last four filed.
2. Extract only quantified or dated statements: a margin band, a capex amount, a store or plant count, a launch date, a debt target. Skip adjectives.
3. For each, find the later filing that settles it. If the date has not passed, mark "open". If no filing settles it, "not found".
4. Mark each: delivered, missed, moved (the date or number was changed on a later call; quote both), or open.

## Return

```markdown
## Concall
| Call date | Speaker | Statement (quoted) | Settled by | Result |
| --- | --- | --- | --- | --- |

- Delivered / missed / moved / open: counts
- Reading: (opinion)
- Refuses to opine on: next quarter, price, buy or sell
```

## Disclaimer

Paste the disclaimer from the iron rules.
