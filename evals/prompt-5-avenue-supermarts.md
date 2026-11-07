# Avenue Supermarts — every investor lens, then the critic

Eval prompt 5, answered in this session. The company is Avenue Supermarts Limited, NSE: DMART. This is not a second, fresh agent. The annual figures are the ones already in [phase-2-avenue-supermarts.md](phase-2-avenue-supermarts.md). The close is the one in [dmart-price-pledge.md](dmart-price-pledge.md). The quarter in [dmart-quarter-fy27.md](dmart-quarter-fy27.md) is not an input to any ratio below.

## Scope

Listed. Avenue Supermarts Limited, NSE: DMART, BSE: 540376, CIN L51900MH2000PLC126473, ISIN INE192R01011. India.

Periods for the ratios: audited consolidated years ended 31 March 2026 and 31 March 2025, from the FY26 annual report. The close is the BSE search extract for 23 October 2026. No FY24 annual report was opened as its own document.

Skills used: `analyze-financials` (already run in the phase-2 memo), then every `skills/lens-*` because the prompt asked for every investor lens: Damani, Buffett, Munger, Jhunjhunwala, Kedia, Agrawal, Prasad, Bakshi, Andrade. Then `critique-thesis`.

Not loaded: `screen-coffee-can`. The prompt did not ask for that screen. `analyze-market`, `analyze-competition`, `analyze-market-leader`, and `analyze-swot` were not loaded again. Where a lens needs a share or an India market size, this memo cites the phase-3 result that those were not found, and it does not write a new industry essay. `analyze-deals`, `analyze-funds`, `analyze-actions`, and `analyze-rating` were not loaded. Their dry runs are separate files. A deal, a bonus, and a rating symbol are not used as lens evidence.

## Business

Indian supermarket retail under D-Mart. Goods are sold at a point in time. Note 54 says revenue from customers is entirely in India. The directors' report, other information, says 85 stores were added in the year ended 31 March 2026 and 500 stores were open on that date. Avenue E-Commerce runs DMart Ready. Detail and the evidence table are in the phase-2 memo.

## Evidence used here

Consolidated, ₹ crore, unless a row says otherwise. Source for the annual rows: the phase-2 memo, which cites the FY26 annual report filed on BSE.

| Metric | Value | Period | Statement | Source |
| --- | --- | --- | --- | --- |
| Revenue from operations | 68,820.74 (prior 59,358.05) | Years ended 31 Mar 2026 and 2025 | Consolidated | Phase-2 memo, profit and loss |
| Profit attributable to owners | 2,970.49 (prior 2,708.02) | Same | Consolidated | Same |
| Profit for the year | 2,969.86 | Year ended 31 Mar 2026 | Consolidated | Same. Not silently swapped for the attributable figure |
| Basic EPS | 45.65 | Same | Consolidated | Same. Face value ₹10 |
| ROE | 12.9% (prior 13.5%) | FY26 and FY25 | Consolidated, computed in phase 2 | Phase-2 arithmetic on owners' profit and average owners' equity |
| ROCE | 18.3% (prior 19.0%) | Same | Consolidated, computed in phase 2 | EBIT over average of equity plus borrowings minus cash. Leases left out |
| Net debt | 681.56 | 31 Mar 2026 | Consolidated, computed | Borrowings 965.27 minus cash 283.71. Other bank balances not subtracted. FY25 borrowings are a printed dash, read as nil |
| Lease liabilities | 1,459.72 (prior 819.62) | 31 Mar 2026 and 2025 | Consolidated | Not inside net debt |
| Cash after the PPE line | (646.61) (prior (960.07)) | Years ended 31 Mar 2026 and 2025 | Consolidated | Cash from operations minus the whole PPE cash line. Not maintenance |
| Inventory plus receivables, versus payables | 6,049.98 versus 1,338.23 | 31 Mar 2026 | Consolidated | Phase-2 working-capital line |
| Promoter, Radhakishan Damani | 22.98% | 31 Mar 2026 | Note 53 | Pledge not found. Regulation 31 was not opened |
| Promoter group | 74.51%, computed | 31 Mar 2026 | Note 53 | Not the 2020–2022 SAST figure of 74.99% |
| BSE close | 3,166.00 | 23 Oct 2026 | Not a statement | Search extract. Direct fetch not completed. NSE not opened |
| Mcap Full, as the page prints it | 2,06,521.19 crore | 23 Oct 2026 | The page's cell | Not replaced by shares times the close. See the price memo |
| Page P/E, standalone / consolidated | 60.97 / 66.28 | 23 Oct 2026 | The page's cell | Not an exchange market cap. Not FY26 basic EPS |

One growth step, computed, not a new filing fact: (68,820.74 − 59,358.05) / 59,358.05 is 15.9%. (2,970.49 − 2,708.02) / 2,708.02 is 9.7%. The filing figures are the fact. The percents are that division. Two years are one step. They are not a three-year window.

The September 2026 unaudited quarter is excluded from this table on purpose.

## Lens: Buffett

- Understandable: Pass, as far as the phase-2 test went. Indian supermarket retail under D-Mart, goods sold at a point in time, revenue in India.
- Moat: Not found. Owned stores and 500 outlets are an asset-base fact. Share against a named rival was not opened. Phase 3 did not conclude who leads. A slogan is not a moat.
- Management: Not a pass. Note 53 has the holding. Pledge is not found, and not found is not a pass. Related-party PPE of 25.81 and Palya purchases of 39.73 are facts, not a failed character test by themselves. The audit opinion is unmodified. No dividend was paid. Cash after the PPE line is negative.
- Reinvestment return: Not a pass. Two years only. ROE 12.9% and 13.5%. ROCE 18.3% and 19.0%. FY24 as its own annual report was not opened.
- Price versus owner earnings: Not found. The close is now sourced. Owner earnings are not. Maintenance is not split from new stores. Facts left on the table: profit for the year 2,969.86, depreciation 1,037.02, PPE cash line 4,113.35. The page's consolidated P/E of 66.28 is a fact from that page. It is not this test, and it is not a target. 3,166 divided by 45.65 is not used.
- India caveat: Ind AS. Promoter control is the normal structure. Honesty is the filing record.
- Refuses to opine on: owner earnings as one number, and whether 3,166.00 is cheap.

## Lens: Munger

- Paths to failure: The same three inferences as phase 2, each tied to a filing fact. Store building can keep absorbing cash (cash from operations 3,466.74, PPE line 4,113.35, commitments 5,294.10, 85 stores added). DMart Ready can keep losing money (Avenue E-Commerce revenue 4,093.61, loss 306.53, both wider than the prior year, directors' report). The lease and borrowing stack can keep rising (leases 1,459.72, borrowings 965.27, finance cost 142.05 of which 120.76 is lease interest). Interest cover of 29.7 times means the third path is not a claim that cover has already failed.
- Bias in the bull case: No bull case is written. The test is skipped. A bull case is not invented in order to name a bias.
- Several forces or one ratio: Several facts. Cash after capex, the lease stack, the subsidiary loss, and working capital that payables do not fund. The memo does not rest on the page P/E.
- Quality at a fair price: Not scored as a pass. The page now prints a multiple. The moat test is not finished, so "a high multiple on a strong business" is not established. The printed P/E is not an automatic fail.
- India caveat: The paths use the Indian filing: store capex, a grocery e-commerce subsidiary, and Ind AS 116 leases.
- Refuses to opine on: a price target. The kill does not fire. Nothing here is a forecast of next year's multiple and nothing else.

## Lens: Damani

- Build it: Not a fail. The product on the filing is simple: Indian supermarkets, goods at a point in time, all of the revenue in India. Repeat demand is an inference from that format. The filing has no cohort.
- Multiple versus price: Not found. This lens does not assign a multiple. The page's P/E is not that assignment. Cash after the PPE line is negative in both years, and maintenance is not split. No peer median is copied. The close exists and is still not compared, because the multiple this lens would assign is not found.
- Lend to the promoter: Not found. The pledge file was not opened. The SAST rows are not that file. An unmodified audit is not a pass.
- Debt and working capital: Fail on working capital. Inventory plus receivables, 6,049.98, exceed payables, 1,338.23. A grocery format is not evidence the other way. Net debt 681.56. Leases 1,459.72 are larger than borrowings and are outside that net debt. Interest cover 29.7 times. "Little or no debt" is unavailable once the lease liability is on the page. "High debt" is not the finding.
- Cash flow and capex: Fail for these two years. Cash after the PPE line is (646.61) and (960.07). New stores are not maintenance.
- Government discretion: Not what protects the profit on the pages opened. No tariff or tender is cited as the source of profit.
- Core versus trading (only if asked): Not asked.
- India caveat: Ind AS, April–March, consolidated rupee crore.
- Refuses to opine on: any multiple he would assign, and whether the promoter can be lent to.

## Lens: Jhunjhunwala

- India or company edge: Both are only partly on the page. The directors describe an everyday-low-price supermarket chain in India, which is a company format, and the revenue is in India. A sourced cost gap versus a named rival is not found. Phase 3 did not find a market size. This is not a bare "India story" with no numbers, and it is also not a finished edge.
- Unit economics: They exist for the years opened. Consolidated ROCE 18.3% and 19.0%. Profit attributable to owners 2,970.49 on revenue 68,820.74. Not found is not the result. The September quarter is not added.
- What proves it wrong: Cash after the PPE line stays negative while stores are added, or a sourced share shows the chain is not the operator the store count suggests. Those are observable. A mood is not used.
- Multiple versus growth: The page prints a consolidated P/E of 66.28 and a standalone P/E of 60.97 on 23 October 2026. The filing step from FY25 to FY26 is 15.9% on revenue and 9.7% on profit attributable to owners, computed as above. Setting that page multiple beside that one step is an opinion. It is not a target, and it is not a forecast of the next year.
- Conviction shape: Not called that kind of name. Unit economics exist, and the moat, the pledge, and a third year do not. No portfolio size is stated.
- Disagreement with Damani (only if that lens ran): Damani does not assign a multiple, so he does not compare 3,166.00 with one. This lens will put the page's printed P/E next to the filed step and still refuse a target. The two results stay apart. Damani also fails working capital and cash after capex. This lens does not average those fails away.
- Refuses to opine on: a portfolio weight and a price target.

## Lens: Kedia

- Fit (smaller listed company): Listed, so the screen can be attempted. Phase 3 did not conclude that this company leads its market, so S is not failed for being the leader. No rupee cutoff is invented. The BSE 100 label is a quote-page field, not this test.
- Small (S): Not found. The page prints Mcap Full of 2,06,521.19 crore on 23 October 2026. A sourced share was not opened, and the sector leader's sourced size was not opened. A market cap without that pair does not pass S.
- Medium experience (MI): Not found. Note 53 names Radhakishan Damani and the holding. The years he has run the business were not extracted. The CIN year is incorporation, not that tenure. Pledge not found is not a clean-record pass.
- Large aspiration (L): Evidenced by the filing's own capex commitment. Note 39, capital commitments for sites under construction, 5,294.10 at 31 March 2026, net of advances. The 85 stores are stores already added, not a fresh target. The market skill was not loaded. This letter does not need it.
- Extra-large Indian market (E): Does not pass. Phase 3 recorded India grocery market size as not found. Size not found does not pass. A global TAM is not substituted.
- Sit tight (only if all four evidenced): Not added. S is not found, MI is not found, and E does not pass.
- Refuses to opine on: a buy, and any market-cap cutoff in rupees.

## Lens: Agrawal (QGLP)

- Quality: Does not pass. ROE and ROCE were built from the filing for two years, FY26 and FY25. Three years is the minimum when the filings exist, and the FY24 annual report was not opened as its own document. The competitive fact is not found: phase 3 did not find a share and did not conclude who leads. Adjectives are not used. This is not a Coffee Can pass. That screen was not loaded.
- Growth: One step, reported, not passed off as a longer window. Revenue 68,820.74 from 59,358.05, which is 15.9% computed. Profit attributable to owners 2,970.49 from 2,708.02, which is 9.7% computed. Both consolidated. One missing earlier year means the window is shorter.
- Longevity: Not passed. An Indian runway was not sourced. Phase 3's market size is not found. A TAM slide is not here, and it would not pass if it were. Inference would need a sourced runway. There isn't one.
- Price versus growth: The page's consolidated P/E is 66.28 beside the 15.9% revenue step and the 9.7% profit step. Whether that price is reasonable versus that growth is not decided. No target. This multiple does not replace Buffett's owner-earnings bridge. That bridge is not found, so the two price tests disagree by construction: this one has a printed multiple, and Buffett's does not have owner earnings.
- Refuses to opine on: a reasonable-price verdict, and any decade label.

## Lens: Prasad

- Turnaround: Not this thesis. The business is not written up as a failing company being rescued. ROCE moved from 19.0% to 18.3%. The Nalanda page allows a temporary decline and prints no percent. This memo does not call the dip a turnaround, and it does not call it a pass of the return screen.
- Return series: Not passed. Two years were opened. One year is not the series, and two years are not "consistently high" stretched over a longer record. No 15% cutoff is inserted. The page prints none.
- Promoter: Not a pass. Holding is in note 53. Pledge was not opened. Related-party amounts are in the phase-2 memo. Silence is not "clean". SEBI orders were not searched.
- Debt and acquisitions: Net debt 681.56. Lease liabilities 1,459.72, not inside that net debt. A string of acquisitions was not what the pages described. The preference against debt is his, and it sits next to these figures. It is not a zero-debt kill.
- Fair price: The close, 3,166.00 on 23 October 2026, and the page's consolidated P/E, 66.28, are sourced. This memo does not call that price fair. No next-year earnings are forecast to justify it. Model not built. The Nalanda page says the fourth screen uses financial modeling, and accounts of the book say he does not forecast and does not build a DCF. Both are on the record. An unbuilt model is not a fail of the business.
- Disagreement with Jhunjhunwala (only if that lens ran): Jhunjhunwala will set the printed multiple beside the filed growth step as an opinion. This lens will not forecast the next year to make the same price look fair, and it will not underwrite a rebound story. Neither assigns a target.
- Refuses to opine on: a DCF, a holding instruction, and "be very lazy" as an instruction to the reader. That phrase is his description of holding a name that passed. This name has not passed.

## Lens: Bakshi

- Float: Not found. Trade payables of 1,338.23 are supplier payables. They are not customer cash paid before delivery. No advances-from-customers line was extracted. Not found is not zero.
- Expensed moat spend: Not found as a named line. New stores sit in the PPE cash line, which is capitalised, not an expense this lens adds back. No advertising line was extracted. Adjusted earnings are not computed.
- Multiple: The page prints standalone 60.97 and consolidated 66.28 on 23 October 2026. A sentence that the shares fail because that multiple is above a round number is not used. No ceiling is installed. The test does not fail.
- Permanent loss: Not found, not a pass. A moat fact with a sourced mechanism was not finished. The promoter pledge was not opened. Either missing is enough.
- Disagreement with Buffett (only if that lens ran): This is not his owner-earnings figure. Owner earnings stay not found in that lens. This lens does not rebuild them, and it does not fail the name solely because the reported P/E is high.
- Refuses to opine on: an adjusted profit, and a round-number ceiling.

## Lens: Andrade

- Dominance and capital: Does not pass. Share is not found, and phase 3 did not conclude who leads. Capital for the FY26 ROCE denominator is on the page: equity plus borrowings minus cash, 25,145.60, which is the year-end figure phase 2 averaged. Higher sales and lower capital employed versus a named rival were not shown. A large revenue without the share does not pass.
- Forecast refused: No next-year profit is predicted. ROCE is the statements definition, which already subtracts cash: 18.3% and 19.0%. The memo's reason is not a growth forecast.
- Supply: Not found for the industry. This company's own additions are a fact: 85 stores, and commitments of 5,294.10. Competitor capex was not opened. A demand sentence is not a supply check.
- Cycle: Not a pass, and not a sell instruction. Two years of ROE, 12.9% and 13.5%, are not the low-ROE side of his cycle, and they are not a reason to accept any multiple because the business is called high quality. "Exit" in his cycle sentence is his description. It is not used here.
- Price: The close and the page P/E are sourced, as above. They are not a verdict.
- Disagreement with Buffett (only if that lens ran): Buffett's price test stays not found because owner earnings are not found. This lens does not treat the unfinished moat as quality worth any price. Neither one passes the name.
- Refuses to opine on: next year's growth, and a target return such as double a risk-free rate.

## Where the lenses disagree

Damani does not assign a multiple. The page P/E is not his. He fails working capital and cash after capex on the filed figures. Jhunjhunwala reports unit economics that exist and sets the page P/E beside the one-step growth as an opinion, without a target and without erasing Damani's fails.

Buffett's price test is not found, because owner earnings are not found, even though the close is now sourced. Bakshi does not fail the shares for that printed P/E, and he does not rebuild owner earnings. Andrade does not accept quality at any price, and he does not pass dominance while the share is not found.

Agrawal does not pass quality on two years. Prasad does not pass a return series on two years, does not forecast, and leaves the model unbuilt. Kedia does not pass. A sourced market cap without the leader's size is not S, and market size not found does not pass E.

These are left as nine results. They are not averaged.

## Critic

- Breaks the thesis: There is no positive thesis. One that said the lenses pass because a close was found, because the page P/E is 66.28, because the promoter is Radhakishan Damani, or because the company runs grocery stores, would break. Owner earnings are not found. Pledge is not found. Damani's working-capital and cash-after-capex tests fail on the filed figures. The printed Mcap Full is the page's number. Shares times 3,166.00 were not allowed to replace it.
- Weakens it: The close is a search extract. A direct fetch was not completed, and the NSE close was not opened. Regulation 31 was not opened. Only two annual years were used. The moat and the market size were already not found in phase 3, and those skills were not reopened. The SAST 74.99% is a different date and was not used as the FY26 holding.
- Nit: The September 2026 quarter exists in another file and is excluded here. That exclusion is the rule, not a hidden gap in the annual ratios.

Checks that do not fail: consolidated and standalone are not mixed in one ratio. The page P/E is not used as the market cap. An annual-report dash is not used as the Regulation 31 pledge. Coffee Can was not loaded, so it was not passed on unopened years. QGLP was not passed on two years. NSE-only and combined flows are not in this memo. No deal is used as the promoter percent. No fund holding is invented. No bonus or index label is used as a better business. No news line is used as a rating rationale.

## Revised conclusion

Do not conclude. The business can be described as an Indian supermarket chain. The close on one BSE extract is 3,166.00 on 23 October 2026, and the page prints its own market cap and its own P/E. Owner earnings cannot be built until maintenance is split from new stores. Promoter pledge was not opened. Two years of ratios are not a three-year quality test and not a Coffee Can screen. The lenses that will talk about the printed multiple will not agree with the lens that refuses to assign one. None of that is a target.

## What would change the conclusion

An exchange Regulation 31 file. A capex note that splits maintenance from new stores. A third annual year opened as its own filing. A sourced share against a named rival. A direct fetch of the NSE or BSE close, if it differs from this extract. None of those is filled by the September quarter, by a SAST row from 2020 or 2022, or by the page's P/E.

## Unknowns

Pledge. Owner earnings. NSE close. Whether the search extract matches a completed page fetch. Sector share. India grocery market size. Promoter tenure in years. Customer float. A named advertising line. Competitor capex. The rationale behind the rating symbols. Any scheme's holding. The exchange ex-date of a dividend. FY24 as its own annual report.

## Disclaimer

This is an educational research memo, not investment advice, not a SEBI-registered recommendation, and not a solicitation to buy or sell any security. Figures are only as good as the filings cited. You decide what to do with them.
