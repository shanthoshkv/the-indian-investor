---
name: read-filings
description: >
  Reads an NSE or BSE filing the user saved under filings/ before any
  exchange page. Use when a company memo needs an annual report, a
  quarterly XBRL, a Regulation 31 file, or a rating PDF. A missing file
  stays not found.
compatibility: >
  Agent Skills hosts. Local files only. No bulk downloader and no
  market-data API.
---

# Read filings

Local files first. This skill adds no memo heading. The facts skill cites the path and the page or the XBRL field.

## Iron rules

1. India only. NSE, BSE, or an India bootstrapped company. Anything else: stop and say so.
2. Every figure has source, period, and consolidated or standalone. If it is not in a source, write "not found". Do not estimate silently.
3. INR, with crore or lakh stated. Indian fiscal year (April–March) unless the filing says otherwise.
4. Separate fact, inference, and opinion.
5. Promoter holding, pledge, related parties, and auditor notes are part of the analysis.
6. Close with the disclaimer the calling skill already uses. No buy, sell, or target presented as advice or as a certain outcome.

## Folder

Look in `filings/<issuer>/` at the repo root, or in a path the user names. The slug is the NSE symbol in lower case when the company has one.

The pack does not commit the PDFs, the HTML, or a browser profile. If the folder is missing, or the file you need is missing, that figure is not found until the exchange page is opened. A page that fails to load stays not found. Do not invent the file. Do not build a downloader.

## Shapes

These shapes were taken from Avenue Supermarts files that were opened. They are how to read the next file. They are not a second set of figures.

### Annual report

- A sentence that employees "take a pledge" is not promoter pledge.
- "Assets pledged as security" (receivables, inventory, or another asset of the company) is security for borrowings. It is not the Regulation 31 promoter pledge.
- "No property, plant and equipment are pledged" is that PPE note. It is not the promoter pledge.
- A CARO clause that the company has not raised loans on the pledge of securities held in its subsidiaries is that clause. It is not the promoter pledge.
- The shareholding table in the corporate governance report is the company's reprint, with the as-on date that table prints. It is not the exchange Regulation 31 file. If that file was not opened, pledge is not found.
- A bonus or a buy-back inside a committee's terms of reference is not an action the company carried out. The exchange action, when asked, is `../analyze-actions/SKILL.md`.

### Inline XBRL

An integrated-filing HTML page is XBRL, not a news article.

- `WhetherResultsAreAuditedOrUnaudited` is its own fact. A board letter that says "limited review" is a second label. Keep both. Do not collapse them.
- Context `OneD` is the quarter whose start and end that context prints. `FourD` is the year-to-date period that context prints. `OneI` is an instant. Do not put a `FourD` number in a `OneD` column.
- `scale='7'` with `unitRef='INR'` means the number in the cell is already in crore. Do not multiply by 10^7 again. `decimals` is precision, not a second scale.
- A cash-flow line, including one with a sign attribute, is that cash-flow line. It is not the balance-sheet cash line.
- An audit-qualification table that prints "No records available" is that cell. It is not a qualification you write, and it is not a clean opinion you write.
- The scrip code is the identifier under `http://www.sebi.gov.in/in-capmkt/ScripCode`.

Do not mix the quarter into an annual ratio. Do not annualize one quarter and call it ROCE.

### Shareholding pattern

- The NSE shareholding-pattern page can arrive as column headers and no company rows. Headers are not the company's numbers.
- Promoter pledge is "Number of Shares pledged" (Column XIV), then Non-Disposal Undertaking (Column XV) and Other encumbrances (Column XVI). The page note calculates each as a percent of shares held. A promoter percent in the category column is not Column XIV.
- The nav item "Pledged Data" is a different NSE page.
- An RSS item's `PR_AND_PRGRP` and `PUBLIC_VAL` are category percents. They are not Column XIV. If the feed's item is another company, this company's file was not in that feed.

Worked failure: the DMART shareholding HTML contained Column XIV and no company row. Headless Chrome returned an empty document. Pledge stays not found.

### Rating PDF

A rationale PDF is the reason only for the instrument and the date that PDF prints. A later exchange row whose link was not opened stays reason not found. Do not use the earlier PDF as that later reason. Words such as "expected" in the rationale are the agency's words. They are not this pack's forecast. The symbol method, when asked, is `../analyze-rating/SKILL.md`.
