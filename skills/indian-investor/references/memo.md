# Memo

Use this order for a full company memo. Drop an industry section when that skill did not run. Do not drop scope, evidence, unknowns, or the disclaimer.

```markdown
# [Company] — research memo

## Scope
Listed or bootstrapped. Exchange and symbol, or private. Periods covered. Skills used. Circle filled or not filled, from `circle.md`.

## Business
One paragraph. What it sells, to whom, in India.

## Evidence
| Metric | Value | Period | Consolidated or standalone | Source |
| --- | --- | --- | --- | --- |

## Capital and profit
When the statements were opened. The method is in `../../analyze-financials/references/statements.md`. Computed. No hurdle.

## Where the cash went
When the statements were opened. Dividend, buyback, dilution, ESOP, and capex from filings opened. Same reference. The exchange action, if asked, is `../../analyze-actions/SKILL.md`.

## Compare
Only if the user asked to compare Indian issuers. One evidence table per issuer. Same period and the same statement type in any ratio that uses two issuers. Do not divide one revenue by another and call the result a market share. Do not average a lens across issuers.

## Flows
Only if analyze-flows ran. Market-wide cash. Not a fact about this issuer. The method is in `../../analyze-flows/SKILL.md`.

## Deals
Only if analyze-deals ran. Exchange rows for this issuer. Not the promoter percent. The method is in `../../analyze-deals/SKILL.md`.

## Funds
Only if analyze-funds ran. One scheme's month-end portfolio. Not the market-wide DII net. The method is in `../../analyze-funds/SKILL.md`.

## Actions
Only if analyze-actions ran. Dividend, split, bonus, buyback, or index membership. Not a change in the business. The method is in `../../analyze-actions/SKILL.md`.

## Rating
Only if analyze-rating ran. The symbol the exchange row prints. The reason only if the rationale file was opened. The method is in `../../analyze-rating/SKILL.md`.

## Decision
Only if review-decision ran. The user's note, or the reread of that note. The method is in `../../review-decision/SKILL.md`.

## Results diff
Only if diff-results ran. The new quarter against the last memo's change list. Not an annual ratio. The method is in `../../diff-results/SKILL.md`.

## Costs
Only if note-costs ran. Rates from the page opened. The method is in `../../note-costs/SKILL.md`.

## Screen: Piotroski
Only if screen-piotroski ran. Nine annual tests. A missing input leaves the total not found. The method is in `../../screen-piotroski/SKILL.md`.

## Screen: Altman
Only if screen-altman ran. The version that was asked. Not a default probability. The method is in `../../screen-altman/SKILL.md`.

## Diversification
Only if review-diversification ran. The user's list. No stock-count cutoff. The method is in `../../review-diversification/SKILL.md`.

## Lenses
One heading per lens that ran. Pass / fail / not found on that lens's tests.

## Where the lenses disagree
Keep the conflict. Do not average it into one view.

## Market
Only if analyze-market ran.

## Competition
Only if analyze-competition ran.

## Market leader
Only if analyze-market-leader ran.

## SWOT
Only if analyze-swot ran.

## Critic
Severity-tagged list from critique-thesis, then a revised conclusion. "Do not conclude" is allowed.

## What would change the conclusion
Facts not yet in hand.

## Unknowns
Every material "not found".

## Disclaimer
Paste references/disclaimer.md unchanged.
```

Tag sentences that are not straight from a filing as inference or opinion.

A single-skill run (only SWOT, only one lens) uses that skill's return slots and still ends with the disclaimer. It does not invent the other sections.
