---
name: analyze-competition
description: >
  Builds an Indian competitor set from NSE and BSE peers first, then
  unverified unlisted rivals. Use when the user asks for competition,
  peers, rivals, or competitive analysis of an Indian company or market.
compatibility: Agent Skills hosts. India only. Listed peers before unlisted names.
---

# Analyze competition

Who else sells this in India, and on what terms. Do not declare a winner from brand recall.

## Iron rules

1. India only. NSE, BSE, or an India bootstrapped company. Anything else: stop and say so.
2. Every figure has source, period, and consolidated or standalone. If it is not in a source, write "not found". Do not estimate silently.
3. INR, with crore or lakh stated. Indian fiscal year (April–March) unless the filing says otherwise.
4. Separate fact, inference, and opinion.
5. Promoter holding, pledge, related parties, and auditor notes are part of the analysis for any listed peer whose numbers you use. If you did not open that peer's filing, do not imply those items are clean.
6. Close with this disclaimer. No buy, sell, or target presented as advice or as a certain outcome.

> This is an educational research memo, not investment advice, not a SEBI-registered recommendation, and not a solicitation to buy or sell any security. Figures are only as good as the filings cited. You decide what to do with them.

## Method

Listed NSE or BSE names first. Cap the table at five peers plus the subject. Same fiscal year and the same consolidated or standalone choice on every row. If a peer's filing is standalone-only, mark that cell. Do not mix.

Columns: company, symbol, revenue, operating margin, one returns ratio you actually calculated or cited, and the source. A cell you did not open is "not found".

Unlisted rivals go in a second list. Any number next to them is unverified, or "not found".

Compare, in prose, only what the table supports: price position, cost position, switching costs, capacity, and distribution in India. A gap you cannot support is an inference and must say so.

## Return

```markdown
## Competition
### Listed peers
| Company | Symbol | Revenue | Operating margin | ROCE | ROE | Debt/equity | CFO/PAT | Working-capital days | Period | Statement | Source |

Same period and same statement type across rows. A cell the filing does not support is "not found". The ratio methods are in `../analyze-financials/references/statements.md`. For a lender, swap the ratio columns for the ones in `../analyze-financials/references/lenders.md`.

### Unlisted rivals
Names, and unverified or not found on figures.

### Position
Price, cost, switching costs, capacity, distribution. Fact or inference on each.

## Disclaimer
```

Do not write the leader's durability essay here. Point the reader at `../analyze-market-leader/SKILL.md` if they asked who leads and why the lead holds.
