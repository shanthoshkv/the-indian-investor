---
name: analyze-bootstrapped
description: >
  Assesses an India-headquartered bootstrapped private company and stops
  when the company is mainly VC- or PE-funded. Use when the user asks
  about an unlisted Indian startup, a founder-funded business, or a
  bootstrapped company. Unpublished revenue stays not found.
compatibility: >
  Agent Skills hosts. Public pages and MCA only. No invented ARR.
---

# Analyze bootstrapped

Private companies headquartered in India. A long list of unknowns is a successful run. A precise ARR you did not read is a failed run.

## Iron rules

1. India only. NSE, BSE, or an India bootstrapped company. Anything else: stop and say so. If the company is listed, use `../analyze-financials/SKILL.md` instead.
2. Every figure has source, period, and consolidated or standalone. If it is not in a source, write "not found". Do not estimate silently.
3. INR, with crore or lakh stated. Indian fiscal year (April–March) unless the filing says otherwise.
4. Separate fact, inference, and opinion.
5. Promoter holding, pledge, related parties, and auditor notes are part of the analysis when a filing or MCA charge exists. If they were not published, write "not found". Do not treat silence as a clean promoter.
6. Close with this disclaimer. No buy, sell, or target presented as advice or as a certain outcome.

> This is an educational research memo, not investment advice, not a SEBI-registered recommendation, and not a solicitation to buy or sell any security. Figures are only as good as the filings cited. You decide what to do with them.

## Funding gate

From pages you opened (company site, MCA, press), classify:

- Bootstrapped: founder-controlled, no evidence of a venture or private-equity round as the main capital.
- Not bootstrapped: a VC or PE round is the funding story.

If it is not bootstrapped, say so and stop, unless the user explicitly asked to include VC-backed companies. Do not continue into unit economics after the stop.

If the pages do not say, write "funding not found" and continue only with items you can source. Do not guess bootstrapped from a modest website.

## What to collect

Only from a page or filing you opened.

- India headquarters or majority of operations in India. If you cannot show that, stop.
- Founder and whether founder control is published. Else "not found".
- Lend-to-founder, the Damani question, on public behavior only (disputes, defaults, charges). No record is "not found", not a pass.
- Repeat demand. Evidence or hypothesis.
- Unit economics, revenue, margin, retention: only if the company or a filing published the number. Press articles stay unverified and do not become the figure.
- Customer concentration. "Not found" unless disclosed.
- MCA: date of incorporation and charges on assets, if you opened the master data. If you did not open it, "MCA not opened", which is not the same as "no charges".

A listed peer's multiple may appear as a labeled analogy. It is not a valuation of this company.

## Return

```markdown
## Scope
Private. India. Bootstrapped, not bootstrapped, or funding not found.

## Evidence
| Item | Value | Period | Source |

## Unknowns
Every material not-found. This section should usually be longer than the evidence table.

## Disclaimer
```

## Disclaimer

Paste the disclaimer from the iron rules.
