# Sources

Use this order. A later source does not override an earlier one.

Before the list, read a file the user saved under `filings/<issuer>/`. The method is `../../read-filings/SKILL.md`. The list is what you open when that folder does not already hold the filing. A figure missing from the folder, whose exchange page was not opened, stays "not found".

1. The company's annual report, quarterly results, and investor presentation. Cite the document, the fiscal period, and the note or page.
2. BSE and NSE filings: financial results, corporate announcements, and the shareholding pattern (promoter holding and pledge live here, not in the P&L).
3. SEBI disclosures when the question is about insiders, pledges, or a takeover.
4. The sector regulator only when it changes the business (RBI, IRDAI, TRAI, and peers).
5. Screener, Trendlyne, Tijori, or Moneycontrol as a way to find the filing. Check any figure you keep against 1 or 2. If they disagree, show both and use the filing.

## Rules

- Prefer the PDF or the exchange page for this company. Do not build a bulk downloader.
- Label audited annual, unaudited quarterly, and limited-review figures differently.
- State consolidated or standalone on every figure. Do not mix them in one ratio.
- If the source does not contain the figure, write "not found". Do not fill the gap from memory.
- Private companies: MCA master data and the company's own published pages. Press numbers are unverified until the company or a filing states them.

## Freshness

Name the filing date or the period end you used. Do not describe a ratio as current without that date.

## Market-wide flows

FII, FPI, and DII cash flows are not a company filing. The method is in `../../analyze-flows/SKILL.md`. A portal figure does not override an NSE, BSE, NSDL, or CDSL page that was opened. Calendar nets, assets under custody, and a sector file stay in that skill. They are still not a holding in one company.

## Company disclosures that are not the statements

Block and bulk deals, SAST and insider rows, a scheme portfolio, a corporate action, and a credit-rating rationale are not the P&L. The methods are `../../analyze-deals/SKILL.md`, `../../analyze-funds/SKILL.md`, `../../analyze-actions/SKILL.md`, and `../../analyze-rating/SKILL.md`. Load one only when the question is that disclosure. A deal is not the promoter percent. A scheme holding is not the market-wide DII net. A bonus or an index change is not a better business. A news line is not the rating rationale.

## Your own files

The circle gate is `circle.md`. A decision note, a quarterly diff, and a cost note load only when asked: `../../review-decision/SKILL.md`, `../../diff-results/SKILL.md`, and `../../note-costs/SKILL.md`. A cost rate comes from the page opened for that year. The holdings list is `holdings/`, and it loads only when asked: `../../review-diversification/SKILL.md`.

## A server the user connected

An MCP server is not in the list above. It loads only when asked: `../../use-mcp/SKILL.md`. A broker quote does not replace a filing or an exchange page that was opened. If the server was not connected, the figure is not found. An order tool is not called.

## Screens from papers read locally

`../../screen-piotroski/SKILL.md` and `../../screen-altman/SKILL.md` load only when asked. The papers sit in `library/` on this machine. They are not a company filing. A score is not a filing figure. `library/SOURCES.md` says what was saved and what was not downloaded.
