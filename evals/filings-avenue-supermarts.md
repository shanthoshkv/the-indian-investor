# Avenue Supermarts — filings that were opened

## Scope

Listed. NSE: DMART. BSE: 540376. ISIN INE192R01011, as the annual report's shareholder-information page prints it.

Periods in the files that opened: consolidated and standalone year ended 31 March 2026; consolidated quarter 1 July 2026 to 30 September 2026 and half year 1 April 2026 to 30 September 2026 in the inline XBRL. Skills used: `read-filings`, the capital and cash sections of `analyze-financials`, `note-costs` for the NSE charge sheet. Lenses were not loaded. `analyze-rating` was not run as its own pass. The January 2026 rationale PDF was read because it was on disk.

Circle: `skills/indian-investor/references/circle.md` still says "(none yet)". The gate stayed open. The circle is not filled.

How the files got here: Chrome on this laptop, via a Chrome user-agent request, saved the annual report, the board PDF, the XBRL HTML, and the NSE charge sheet. Headless Chrome on the NSE shareholding URL timed out and wrote an empty document. The NSE RSS feed that did open contained Kiri Industries, not DMART. The BSE rating URL returned the BSE homepage shell. No Regulation 31 row was downloaded.

## Business

The annual report describes a retail business. This note does not add a moat or a trade.

## Evidence

₹ crore unless the row says otherwise. The annual-report rupee sign was extracted as text. The figures below are the digits on those pages.

| Metric | Value | Period | Consolidated or standalone | Source |
| --- | --- | --- | --- | --- |
| Profit for the year | 2,969.86 (prior 2,707.45) | Year ended 31 March 2026 | Consolidated | Annual report, statement of profit and loss, page 198 of the saved PDF |
| Profit attributable to equity holders | 2,970.49 (prior 2,708.02) | Year ended 31 March 2026 | Consolidated | Same page. Non-controlling interests (0.63) |
| Purchase of property, plant and equipment and related capital items (net) | (4,113.35) (prior (3,423.04)) | Year ended 31 March 2026 | Consolidated | Cash flow, page 199 |
| Proceeds from exercise of share options | 36.65 (prior year cell is a dash) | Year ended 31 March 2026 | Consolidated | Cash flow, page 199 |
| Proceeds from share application money pending allotment | 0.72 (prior dash) | Year ended 31 March 2026 | Consolidated | Cash flow, page 199 |
| Proceeds from short-term borrowings | 987.61 (prior dash) | Year ended 31 March 2026 | Consolidated | Cash flow, page 199 |
| Proceeds from commercial papers | 600.00 (prior dash) | Year ended 31 March 2026 | Consolidated | Cash flow, page 199 |
| Repayment of short-term borrowings | (402.61) (prior dash) | Year ended 31 March 2026 | Consolidated | Cash flow, page 200 |
| Repayment of commercial papers | (600.00) (prior dash) | Year ended 31 March 2026 | Consolidated | Cash flow, page 200 |
| Payment of lease liabilities | (193.51) (prior (189.85)) | Year ended 31 March 2026 | Consolidated | Cash flow, page 200. This is cash paid, not the change in the lease liability |
| Capital commitments, sites under construction, net of advances | 5,294.10 (prior 4,298.58) | As at 31 March 2026 | Consolidated | Commitments note, page 234 |
| Capital commitments, same description | 5,238.65 (prior 4,274.09) | As at 31 March 2026 | Standalone | Page 174. Not added to the consolidated figure |
| Shares allotted on option exercise | 12,26,055 shares of ₹10 at ₹299 | 27 March 2026 | Company (directors' report) | Page 45. Paid-up after allotment 651,959,123 shares of ₹10 |
| Promoters | 485,796,256 shares, 74.51% | As on 31 March 2026 | Company reprint | Corporate governance shareholding table, page 79. No pledge column |
| Current assets pledged as security for borrowings | Receivables 356.97, inventories 2,789.89, total 3,146.86 (prior total 2,686.23) | As at 31 March 2026 | Standalone | "Assets pledged as security", page 172. Not promoter pledge |
| Whether results are audited or unaudited | Unaudited | Context OneD | Consolidated, as the filing's identifier is scrip 540376 | Inline XBRL field `WhetherResultsAreAuditedOrUnaudited` |
| Dividends paid, financing | 0.00 | Context FourD, 1 April 2026 to 30 September 2026 | Consolidated XBRL | `DividendsPaidClassifiedAsFinancingActivities`, scale 7. Not the FY26 figure |
| Payments of lease liabilities | 122.89 | Context FourD | Consolidated XBRL | scale 7. Not the FY26 cash-flow line of 193.51 |

A dash in the cash-flow prior-year cells above is nil, because that statement uses a dash for no amount.

`scale='7'` with unit INR is why the XBRL cells are already in crore. They were not multiplied again.

## Capital and profit

Consolidated, year ended 31 March 2026. Method: `statements.md`. No hurdle. Nothing here is a pass or a fail.

Profit out is profit for the year, ₹2,969.86 crore. Attributable profit is ₹2,970.49 crore. They are not the same number.

PPE cash outflow is ₹4,113.35 crore. That sits beside ROCE. ROCE was not recomputed in this note. The two capital-and-profit figures are the PPE line and profit for the year.

Commitments of ₹5,294.10 crore are not cash spent. They are not added to ₹4,113.35 crore.

Borrowings cash, computed from the four financing lines and labeled computed: proceeds 987.61 + 600.00 = 1,587.61. Repayments 402.61 + 600.00 = 1,002.61. Net 585.00. The balance-sheet borrowings line was not re-read for this note, so the stock of debt is not found here.

Lease cash paid is ₹193.51 crore. The change in the lease-liability balance was not re-read, so that change is not found. Lease cash is not folded into net debt.

## Where the cash went

Year ended 31 March 2026 unless a row says otherwise. Consolidated unless noted.

- Dividend. The auditor's report says no dividend has been declared or paid during the year by the holding company and its Indian subsidiaries (page 194). The directors say they have not recommended any dividend (page 46). The shareholder page prints dividend payment date NA (page 79). The XBRL dividends-paid cell of 0.00 is the half year to 30 September 2026, not this year.
- Buyback. The pages opened quote the buy-back regulations and a committee procedure. They do not say the company bought back shares this year. A buyback carried out is not found.
- Dilution. 12,26,055 shares allotted on 27 March 2026 at ₹299, face ₹10. Computed, 12,26,055 × 299 = ₹36.659 crore. The cash-flow line is ₹36.65 crore. They are not the same figure. Share-application money of ₹0.72 crore is a separate line. The difference is not bridged.
- ESOP. The consolidated cash-flow add-back is ₹33.87 crore (prior ₹30.72 crore). The consolidated profit-and-loss line on page 228 is ₹33.91 crore (prior ₹30.72 crore). Both are cited. They are not reconciled. The expense is not added back to profit.
- Capex. The PPE cash line above, ₹4,113.35 crore. Not a second analysis.

The board PDF of 10 October 2026 says the limited review under LODR Regulations 33 and 52 was completed, and the board took the standalone results on record that day. One commercial-paper row on that note: 10,000 papers of ₹5 lakh each, ICRA A1+, issued 10 April 2026, maturity 29 June 2026, ₹500 crore, discount 6.60% a year. That row is the half-year note. It is not added to the FY26 cash flow. Later rows on the same page were not summed.

## Rating

The ICRA PDF that opened is dated 5 January 2026. Instrument: Commercial Paper Programme. Previous rated amount 300.0, current 500.0, unit Rs. crore. Action: [ICRA]A1+ reaffirmed and assigned for enhanced limits. The annual report, page 45, prints the same enhancement from ₹300 crore to ₹500 crore in FY 2025-26, and its heading on that CP line says "Long-Term Rating". That heading is quoted. It is not relabeled. The same page says CRISIL reaffirmed bank-loan facilities of ₹500 crore at CRISIL AAA/Stable.

The narrative of the ICRA PDF uses the agency's own "expected" language. This note does not adopt that language as a forecast.

The 9 October 2026 exchange rationale link was not in the files opened. That reason is not found. The January PDF is not that reason.

## Costs

Year: the NSE sheet's two columns, "rates w.e.f. April 1, 2026" and "rates up to March 31, 2026". Page saved from `https://www.nseindia.com/static/invest/first-time-investor-sebi-turnover-fees-stt-other-levies`.

- Brokerage: not found. No broker contract was opened.
- STT, purchase of an equity share settled by delivery: 0.100 per cent in both columns. Purchaser, on volume-weighted average price.
- STT, sale of an equity share settled by delivery: 0.100 per cent in both columns. Seller, on volume-weighted average price.
- GST on stock brokers services: 18.00%, brokers and collected from their clients.
- Holding-period tax: not found. The Income Tax Department page was not opened.
- Option and futures rows on the same sheet were not used.

## Critic

- Breaks the thesis: a conclusion that needs the Regulation 31 pledge. Column XIV is in the NSE page shell. The company row was not. Pledge is not found, not zero. The governance table's 74.51% has no pledge column. The assets-pledged note is the company's receivables and inventory.
- Weakens it: the October 2026 rating reason is not found. The share-option cash line does not equal shares times ₹299. The income-tax rate is not found.
- Nit: none.

No hurdle was applied to capital versus profit. The quarter and the half year were not put into the FY26 ratios. No brokerage or tax rate was filled in.

## Revised conclusion

Do not conclude. The opened filings show profit, capex, a share allotment, a company-asset charge, and a January 2026 commercial-paper rating. They do not show the exchange pledge, the October rationale, or a tax rate.

## What would change the conclusion

The exchange Regulation 31 file for 30 September 2026 or 31 March 2026, with Column XIV read. The rationale PDF linked from the 9 October 2026 exchange row. An Income Tax Department page that prints the holding-period rate, if a cost note is asked again.

## Unknowns

Exchange pledge. October 2026 rating reason. NSE close. Brokerage. Holding-period tax rate. Change in lease liabilities. Balance-sheet borrowings. Why ₹36.65 crore differs from ₹36.659 crore. Why the ESOP cash-flow add-back differs from the P&L line by ₹0.04 crore. Circle not filled.

## Disclaimer

This is an educational research memo, not investment advice, not a SEBI-registered recommendation, and not a solicitation to buy or sell any security. Figures are only as good as the filings cited. You decide what to do with them.
