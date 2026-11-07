---
name: screen-piotroski
description: >
  Scores nine annual fundamental signals for an NSE or BSE company
  from filings that were opened. Use when the user asks for a
  Piotroski or F-score screen. Not a lens and not a buy list. A
  missing input leaves the total not found.
compatibility: Agent Skills hosts. India listed companies. No data-website scores.
---

# Piotroski screen

A screen, not a lens. It does not replace a temperament lens or `screen-coffee-can`.

The nine tests are the annual signals in Piotroski (2000), as restated in appendix A.4.21 of Hou, Xue, and Zhang, NBER working paper 23394. That restatement was read from `library/nber-w23394.pdf` on this machine. The Journal of Accounting Research PDF was not opened. The sample in the restatement is US Compustat firms. An Indian filing is not that sample. Say so.

The paper then sorts portfolios and computes US stock returns. Those returns stay in the paper. This screen does not quote them and does not treat a high score as a buy. Appendix A.4.22 is a quarterly score. Do not use it. Appendix A.4.23 is a failure probability that needs market returns and an index. Do not use it.

## Iron rules

1. India only. NSE or BSE. Anything else: stop and say so. A private company is in scope only when the user saved the accounts and those pages were opened.
2. Every figure has source, period, and consolidated or standalone. If it is not in a source, write "not found". Do not estimate silently.
3. INR, with crore or lakh stated. Indian fiscal year (April–March) unless the filing says otherwise.
4. Separate fact, inference, and opinion.
5. Promoter holding, pledge, related parties, and auditor notes stay in the memo when this screen is part of a full memo. The screen itself does not pass on a clean promoter.
6. Close with this disclaimer. No buy, sell, or target presented as advice or as a certain outcome.

> This is an educational research memo, not investment advice, not a SEBI-registered recommendation, and not a solicitation to buy or sell any security. Figures are only as good as the filings cited. You decide what to do with them.

Take each year from `../analyze-financials/SKILL.md`. Local file first: `../read-filings/SKILL.md`. A bank or an RBI-regulated NBFC is outside this screen. Stop. The lender statements live in `../analyze-financials/references/lenders.md`. Do not put ROE or ROCE in place of these ratios. Those ratios use another denominator and live in `statements.md`.

## Tests

Score a test 1 or 0 only when every input for that test was opened. If an input is not found, that test is not found. Do not score a missing input as zero. F is the sum of the nine, and only when all nine are 1 or 0. Otherwise F is not found. Do not print a partial total.

Use one statement type, consolidated or standalone, for every input. A change test needs the prior annual filing. A ratio that lags assets by a year also needs the year before that. A quarter does not fill a year.

Profitability uses one-year-lagged total assets: the prior year-end total assets. Not the average. Not capital employed.

1. Roa. Profit for the year divided by prior year-end total assets. Above zero scores 1. Zero scores 0. The Compustat line is income before extraordinary items. If the filing prints an extraordinary line, use profit before that line and say so. If it does not, use profit for the year and say there was no extraordinary line. Do not strip exceptional items unless the filing calls them extraordinary. If profit attributable to owners differs, state it and still use profit for the year. The assets are the whole entity.
2. Cash flow. Net cash from operating activities divided by the same prior year-end total assets. Above zero scores 1. Use the cash-flow statement total. Reconstruct it from funds from operations minus the change in working capital only when both of those lines were opened and the operating total was not printed. A missing cash-flow statement is not found.
3. Change in Roa. This year's Roa minus the prior year's Roa. The prior year's Roa divides that year's profit by total assets from the year before that. An increase scores 1. No change scores 0. If the year before the prior year was not opened, this test is not found.
4. Accrual. Scores 1 when cash flow over lagged assets is greater than Roa, both for the year being scored. Equal scores 0.
5. Long-term debt. The ratio is non-current borrowings divided by the average of this year-end total assets and prior year-end total assets. Say which line. Do not fold in current borrowings or lease liabilities unless that long-term line already includes them, and then say so. The change is this year's ratio minus the prior year's ratio. The prior year's ratio averages the prior year-end assets and the year before that. A fall, meaning the change is below zero, scores 1. A printed dash is nil. Nil in both years is a change of zero, which scores 0. A blank line is not found.
6. Current ratio. Current assets divided by current liabilities, at year-end. This year minus the prior year. An increase scores 1. No change scores 0.
7. Equity issued. Scores 1 only when the opened filing shows the company did not issue equity shares in the year. Issuance is the cash-flow proceeds from the issue of shares, or the directors' allotment sentence. Subtract an increase in preference share capital only when that increase was opened. A buyback does not cancel an issue. Shares allotted under an employee scheme are an issue. A buy-back that appears only inside a committee's terms of reference is not an issue and is not a buyback that was carried out. If neither the cash-flow line nor the allotment sentence was opened, this test is not found. Silence is not "no issue".
8. Gross margin. Revenue from operations minus the goods-cost line the filing uses, divided by revenue from operations. This year minus the prior year. An increase scores 1. If the filing prints the goods-cost lines separately and no total, add them only as a sum labeled computed, and name the lines. If you cannot tell which lines are the goods cost, the test is not found. Do not use EBITDA margin, employee cost, or total expenses as the goods cost.
9. Asset turnover. Revenue from operations divided by prior year-end total assets, minus the same ratio for the prior year. The prior year's ratio needs total assets from the year before that. An increase scores 1.

## Kill

Do not report a total when any of the nine is not found. Do not call 8 or 9 a buy. The restatement combines 8 and 9 only as its high portfolio for a US return test. That sort is not a rule for this company.

## Return

```markdown
## Screen: Piotroski
- Source of the tests:
- Years opened:
- Statement type:
- Roa:
- Cash flow / assets:
- Change in Roa:
- Accrual:
- Change in long-term debt ratio:
- Change in current ratio:
- Equity issued:
- Change in gross margin:
- Change in asset turnover:
- F:
- Result:
- Refuses to opine on:
```

Worked pattern: a website prints an F of 8 and the annual reports were not opened. F is not found. A September quarter used as one of the nine is not the annual score.

## Disclaimer

Paste the disclaimer from the iron rules.
