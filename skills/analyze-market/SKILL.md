---
name: analyze-market
description: >
  Defines an Indian market by customer, geography, and price band, with
  a cited size or an explicit not-found. Use when the user asks for
  market analysis, industry size, TAM, or growth drivers in India.
compatibility: Agent Skills hosts. India only. No global TAM as evidence.
---

# Analyze market

Define the market in India. Do not paste a global TAM and call it the market.

## Iron rules

1. India only. NSE, BSE, or an India bootstrapped company. Anything else: stop and say so. A sector question must be about customers, plants, revenue, or regulation in India.
2. Every figure has source, period, and consolidated or standalone. If it is not in a source, write "not found". Do not estimate silently. Market size that is not in a source is "not found", including a size you could back into.
3. INR, with crore or lakh stated. Indian fiscal year (April–March) unless the filing says otherwise.
4. Separate fact, inference, and opinion.
5. Promoter holding, pledge, related parties, and auditor notes are part of the analysis when the subject is a company. For a sector with no company, say those items are not applicable.
6. Close with this disclaimer. No buy, sell, or target presented as advice or as a certain outcome.

> This is an educational research memo, not investment advice, not a SEBI-registered recommendation, and not a solicitation to buy or sell any security. Figures are only as good as the filings cited. You decide what to do with them.

## Method

Write one definition before any number: who the Indian customer is, which geography (India, or a state if the business is local), and the price band or product boundary. If the boundary is fuzzy, say what you excluded.

Then:

- Size, only from a cited source (company presentation, regulator, industry filing). Else "not found".
- Growth labeled structural or cyclical. Name the cycle only when it moves this industry (monsoon, capex, rates, a policy such as PLI). A policy mention with no link to this revenue is noise. Drop it.
- The regulator, named, when one licenses, prices, or bans the product. Otherwise "no sector regulator identified".
- What would shrink the market in India. Tag inference.

## Return

```markdown
## Market
- Definition:
- Size:
- Drivers (structural or cyclical):
- Regulator:
- What would shrink it:
- Not found:

## Disclaimer
```

Do not name a market leader here. That is `../analyze-market-leader/SKILL.md`. Do not build the peer table. That is `../analyze-competition/SKILL.md`.
