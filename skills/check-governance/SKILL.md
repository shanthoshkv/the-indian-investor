---
name: check-governance
description: >
  Lists governance red flags for an NSE or BSE company from filings and
  regulator pages opened: auditor resignation, KMP churn, SEBI or SAT
  orders, loans and guarantees to group entities, contingent liabilities,
  and promoter pledge trend. Use when the user asks for governance, red
  flags, promoter integrity, or forensic checks. A flag is not a fraud finding.
compatibility: >
  Agent Skills hosts. India listed companies. Reads exchange
  announcements, the annual report, and SEBI orders when opened.
---

# Check governance

A list of what the public record shows. Not an accusation.

## Iron rules

1. India only. NSE or BSE. Anything else: stop and say so.
2. Every flag has source, date, and the sentence it rests on. If a page was not opened, the row is "not found", not "clean".
3. INR, with crore or lakh stated. Indian fiscal year (April–March) unless the filing says otherwise.
4. Separate fact, inference, and opinion. Do not call anything fraud, diversion, or manipulation unless a regulator's order says it.
5. Promoter holding, pledge, related parties, and auditor notes are part of the analysis.
6. Close with this disclaimer. No buy, sell, or target presented as advice or as a certain outcome.

> This is an educational research memo, not investment advice, not a SEBI-registered recommendation, and not a solicitation to buy or sell any security. Figures are only as good as the filings cited. You decide what to do with them.

Auditor opinion, related-party note, contingent liabilities, and the three-year governance series are already in `../analyze-financials/references/statements.md`. Reuse those rows. Do not restate the method.

## Checks

Each is flag, no flag, or not found.

1. Auditor resignation or a change before the term ended. Source: the Regulation 30 announcement and the outgoing auditor's letter, if filed. Quote the stated reason.
2. KMP churn. CFO, company secretary, or MD/CEO leaving within the last three years, from Regulation 30 announcements. Two or more exits of the same role is a flag.
3. Regulator action. SEBI orders, SAT appeals, or exchange penalties naming the company or a promoter, from the SEBI orders page searched by name. Unopened is not found.
4. Money to the group. Loans, inter-corporate deposits, guarantees, or investments to promoter-group entities in the related-party note and the Section 186 disclosure. Flag when the total is large versus net worth and say the ratio.
5. Contingent liabilities versus net worth, same balance-sheet date.
6. Pledge trend. Regulation 31 pledge percent across the quarters opened. A rise is a flag. One quarter is not a trend.
7. Cash quality. CFO versus PAT over the years opened; a gap that persists three years is a flag. Other income share of PBT.
8. Promoter remuneration versus PAT, from the annual report. Flag when it rises while PAT falls.
9. Qualified or adverse secretarial audit report (MR-3), when opened.

## Return

```markdown
## Governance
| Check | Result | Date | Source | Quoted line |
| --- | --- | --- | --- | --- |

- Flags: count of flag, no flag, not found
- Reading: (opinion)
- Refuses to opine on: fraud, intent, buy or sell
```

## Disclaimer

Paste the disclaimer from the iron rules.
