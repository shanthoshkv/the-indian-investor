---
name: analyze-swot
description: >
  Writes a short evidence-tagged SWOT for an Indian company or industry.
  Use when the user asks for a SWOT of an NSE or BSE company, an India
  bootstrapped company, or an Indian market.
compatibility: Agent Skills hosts. India only. Three bullets per cell.
---

# Analyze SWOT

A short SWOT. Three bullets in each cell. A twenty-line SWOT is a failed run. Cut it.

## Iron rules

1. India only. NSE, BSE, or an India bootstrapped company. Anything else: stop and say so.
2. Every figure has source, period, and consolidated or standalone. If it is not in a source, write "not found". Do not estimate silently.
3. INR, with crore or lakh stated. Indian fiscal year (April–March) unless the filing says otherwise.
4. Separate fact, inference, and opinion. In this skill the tags are evidence and hypothesis.
5. Promoter holding, pledge, related parties, and auditor notes are part of the analysis when the subject is a listed company and you claim a strength or weakness about the promoter. If you did not open them, you cannot list "clean promoter" as a strength.
6. Close with this disclaimer. No buy, sell, or target presented as advice or as a certain outcome.

> This is an educational research memo, not investment advice, not a SEBI-registered recommendation, and not a solicitation to buy or sell any security. Figures are only as good as the filings cited. You decide what to do with them.

## Cells

- Strengths and weaknesses are internal (cost, distribution, balance sheet, promoter record, plants, product).
- Opportunities and threats are external (a rival, a rule, a duty, a state restriction, a channel, demand). Use an India-specific point when it changes the conclusion. Do not add one for colour.

Each bullet starts with `Evidence:` or `Hypothesis:`. Evidence names the source. Hypothesis is allowed. An untagged bullet is not done.

If you cannot fill a slot without inventing, leave it empty and add one line under dropped.

## Return

```markdown
## SWOT
### Strengths
1. Evidence or Hypothesis:
2.
3.

### Weaknesses
1.
2.
3.

### Opportunities
1.
2.
3.

### Threats
1.
2.
3.

### Dropped for lack of evidence
- 

## Disclaimer
```

Company SWOT uses the evidence table if `analyze-financials` or `analyze-bootstrapped` already ran. It does not invent ratios to fill a cell.
