---
name: analyze-market-leader
description: >
  Identifies who leads a defined Indian market and what holds that lead.
  Use when the user asks for the market leader, number one, or leadership
  durability in an Indian industry. Does not repeat a full peer table.
compatibility: Agent Skills hosts. India only. Share claims need a cited source.
---

# Analyze market leader

A different question from competition: who is number one in the Indian market you defined, and what holds that place.

## Iron rules

1. India only. NSE, BSE, or an India bootstrapped company. Anything else: stop and say so.
2. Every figure has source, period, and consolidated or standalone. If it is not in a source, write "not found". Do not estimate silently.
3. INR, with crore or lakh stated. Indian fiscal year (April–March) unless the filing says otherwise.
4. Separate fact, inference, and opinion.
5. Promoter holding, pledge, related parties, and auditor notes are part of the analysis when you discuss the leader as an investment subject. If this run is only about who leads, say those items were not opened.
6. Close with this disclaimer. No buy, sell, or target presented as advice or as a certain outcome.

> This is an educational research memo, not investment advice, not a SEBI-registered recommendation, and not a solicitation to buy or sell any security. Figures are only as good as the filings cited. You decide what to do with them.

## Method

Use the market definition from `../analyze-market/SKILL.md` if it already ran. If it did not, write one sentence of definition (Indian customer, geography, price band) before naming a leader. A global category title is not a definition.

If `../analyze-competition/SKILL.md` already built a peer table, use it. Do not paste the table again.

If it did not, name up to five listed peers as names and symbols only. No second comparison table.

Answer:

- Who leads. Share, volume, revenue, or outlets, with a source and period. If none of those is sourced, the leader is an opinion and you must say the share is "not found".
- The mechanism that holds the lead: cost, distribution, regulation, habit, data, or owned assets. Tie it to a fact.
- Whether that sourced share is rising or falling across the periods you have. One period is "direction not found".
- What would dethrone them. Tag inference. Name a rival or a rule change, not "disruption".

## Return

```markdown
## Market leader
- Definition:
- Leader and the sourced measure:
- Mechanism:
- Direction of share:
- What would dethrone them:
- Peer names (only if no competition table exists):

## Disclaimer
```
