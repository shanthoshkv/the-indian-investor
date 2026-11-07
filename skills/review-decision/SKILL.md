---
name: review-decision
description: >
  Rereads the user's own decision note against the next annual report
  of an NSE or BSE company. Use when the user asks to record what they
  did, or to check that note a year later. Does not say what to buy.
compatibility: Agent Skills hosts. India listed companies. The user writes the decision.
---

# Review decision

The user's log, checked against a later filing. Not a recommendation.

## Iron rules

1. India only. NSE, BSE, or an India bootstrapped company. Anything else: stop and say so.
2. Every figure has source, period, and consolidated or standalone. If it is not in a source, write "not found". Do not estimate silently.
3. INR, with crore or lakh stated. Indian fiscal year (April–March) unless the filing says otherwise.
4. Separate fact, inference, and opinion.
5. Promoter holding, pledge, related parties, and auditor notes stay in the facts skill. Do not invent them here.
6. Close with this disclaimer. No buy, sell, or target presented as advice or as a certain outcome.

> This is an educational research memo, not investment advice, not a SEBI-registered recommendation, and not a solicitation to buy or sell any security. Figures are only as good as the filings cited. You decide what to do with them.

## Log

Copy `decisions/TEMPLATE.md` to `decisions/<yyyy-mm-dd>-<slug>.md`. The user fills the date, the company, what they did, and which critic point they ignored. You do not write "what I did" for them. You do not say what they should do next. Personal notes stay out of the public repo. The template is the file that is tracked.

## Reread

Only when the user asks to reread a note. Open the next annual report after the decision date. Local file first: `../read-filings/SKILL.md`. Check only the list in that decision file. For each point, say what the later filing prints, or "not found". Do not add a thesis. Do not turn the reread into a trade.

## Return

```markdown
## Decision
- File:
- Points checked:
- Not in the later filing:
- Refuses to opine on:
```

## Disclaimer

Paste the disclaimer from the iron rules.
