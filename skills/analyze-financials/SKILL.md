---
name: analyze-financials
description: >
  Reads Indian listed financial statements: consolidated and standalone
  P&L, balance sheet, cash flow, pledge, related parties, and auditor
  notes. Use when the user asks for fundamental analysis, an annual
  report, results, ratios, or financials of an NSE or BSE company.
  Banks and NBFCs use the lenders reference.
compatibility: >
  Agent Skills hosts. Needs access to the company's filing or a PDF
  the user supplied. Does not scrape exchanges in bulk.
---

# Analyze financials

Listed NSE or BSE companies. Read `references/statements.md` and follow it. If the issuer is a bank or an RBI-regulated NBFC, read `references/lenders.md` instead of the non-financial ratio section. Price, the Regulation 31 pledge file, and the governance series are defined in `references/statements.md`. Jewellery, retail stores, IT services, pharmaceuticals, and insurers also use `references/sectors.md`.

## Iron rules

1. India only. NSE, BSE, or an India bootstrapped company. Anything else: stop and say so. This skill is for listed companies. A private company goes to `../analyze-bootstrapped/SKILL.md`.
2. Every figure has source, period, and consolidated or standalone. If it is not in a source, write "not found". Do not estimate silently.
3. INR, with crore or lakh stated. Indian fiscal year (April–March) unless the filing says otherwise.
4. Separate fact, inference, and opinion.
5. Promoter holding, pledge, related parties, and auditor notes are part of the analysis.
6. Close with this disclaimer. No buy, sell, or target presented as advice or as a certain outcome.

> This is an educational research memo, not investment advice, not a SEBI-registered recommendation, and not a solicitation to buy or sell any security. Figures are only as good as the filings cited. You decide what to do with them.

## Source order

Follow `../indian-investor/references/sources.md`. Annual report and exchange filing before any data website. If two sources disagree, show both and use the filing.

Open the PDF or the filing page. Cite the note or the page. Do not build a downloader.

## Return

```markdown
## Evidence
| Metric | Value | Period | Consolidated or standalone | Source |

## Statements
Short notes on P&L, balance sheet, and cash flow. Call out CFO versus PAT and other income versus profit.

## Price
Close, date, and source, or "not found". A printed P/E stays a printed P/E.

## Promoter, pledge, related parties, auditor
One subsection each. Pledge is the Regulation 31 figure. "Not found" if that file was not opened. A dash in the annual report is not zero.

## Flags
Only items the references tell you to flag. No recommendation.

## Disclaimer
```

Use at least three years when the filings are available. One year is allowed only if you say the earlier years were not opened.

Quarterly figures stay labeled unaudited or limited review. Do not mix a quarterly run-rate into an annual ratio without saying so.
