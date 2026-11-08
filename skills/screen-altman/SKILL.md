---
name: screen-altman
description: >
  Computes Altman's Z-score for an NSE or BSE company from filings
  and a sourced market value. Use when the user asks for an Altman
  or Z-score. The private-firm and non-manufacturer versions run
  only when asked. Not a default probability and not for a bank.
compatibility: Agent Skills hosts. India listed companies. No invented cutoffs.
---

# Altman screen

A screen, not a lens, and not a default probability. The equations were read from Edward Altman's notes, the file `library/altman-z-score-notes.pdf` saved from the NYU faculty archive (`https://archive.nyu.edu/bitstream/2451/26762/2/S-CDM-02-11.pdf`). Cite that file. Do not mix the three equations. Name the one you computed.

The 1968 sample is 66 US manufacturers, 33 that filed under Chapter X from 1946 through 1965 and 33 paired firms that did not, with assets about $1 million to $25 million. The ratios come from one annual statement before distress. The notes say asset turnover differs across countries, and that a model built for one industry is a better fit for that industry. This pack has no India industry model. Do not invent one. Say the issuer is outside that sample.

When the user says Altman or Z-score and does not name a version, compute Z. If the issuer is not a manufacturer, say the notes call the four-variable model more appropriate for non-manufacturers, and still compute Z when every Z input was opened. Label it as the 1968 equation applied outside that sample. Do not switch versions on your own.

## Iron rules

1. India only. NSE or BSE. Anything else: stop and say so. Z on a private company needs a market value. If none was sourced, Z is not found. Do not switch to the private-firm model unless the user asked for it.
2. Every figure has source, period, and consolidated or standalone. If it is not in a source, write "not found". Do not estimate silently.
3. INR, with crore or lakh stated. Indian fiscal year (April–March) unless the filing says otherwise.
4. Separate fact, inference, and opinion.
5. Promoter holding, pledge, related parties, and auditor notes stay in the memo when this screen is part of a full memo. The score does not pass on a clean promoter.
6. Close with this disclaimer. No buy, sell, or target presented as advice or as a certain outcome.

> This is an educational research memo, not investment advice, not a SEBI-registered recommendation, and not a solicitation to buy or sell any security. Figures are only as good as the filings cited. You decide what to do with them.

Take the statement from `../analyze-financials/SKILL.md`. Local file first: `../read-filings/SKILL.md`. A bank or an RBI-regulated NBFC: stop. The notes do not fit a loan book, and this pack did not open a bank model. `../analyze-financials/references/lenders.md` is the lender path. Do not score one.

Use one statement, one period, consolidated or standalone. Do not mix a quarter into an annual score. If any input below is not found, the score is not found. Do not compute a partial score. A printed dash is nil. A blank cell is not found.

## Z, the 1968 equation

Z = 1.2 X1 + 1.4 X2 + 3.3 X3 + 0.6 X4 + 1.0 X5. No constant term.

- X1. Working capital divided by total assets. Working capital is current assets minus current liabilities, same statement date.
- X2. Retained earnings divided by total assets. Use the retained-earnings or surplus line in the equity note. Other equity left as one bundle is not that line. Total equity is not retained earnings. If the note was not opened, X2 is not found.
- X3. EBIT divided by total assets. EBIT is the definition in `../analyze-financials/references/statements.md`: profit before exceptional items, tax, and finance cost. If exceptional items are left in, say so. The denominator is total assets on that statement date, not average capital employed. This is not ROCE.
- X4. Market value of equity divided by book value of total liabilities. Market value is a market cap the exchange page prints. If that page prints no market cap, use a sourced close times the share count the filing prints, and label the product computed. Do not multiply a company-printed P/E by earnings. Do not replace a printed exchange market cap with that product. If the two differ, use the printed market cap and say the product disagrees. No sourced market value: X4 is not found and Z is not found. A last price from a broker MCP is not this market value. That method is `../use-mcp/SKILL.md`. Total liabilities is the liabilities total, or total equity and liabilities minus equity. Say which. Borrowings alone are not total liabilities.
- X5. Revenue from operations divided by total assets. Total income is not sales unless the filing shows they are the same line.

Bounds, for Z only. The original tests used a cutoff of 2.675. The notes say the model was accurate on the original tests when scores were below 1.81 or above 2.99, and that 1.81 is the lower bound of the zone of ignorance. A score from 1.81 to 2.99 is that zone. Report the score and those bounds. Do not call the zone a pass or a fail. Do not invent an India cutoff. Do not assign a bond rating or a default probability. The notes discuss US rating averages. Those averages are not this issuer.

## Z', only when the user asks for the private-firm model

Z' = 0.717 X1 + 0.847 X2 + 3.107 X3 + 0.420 X4 + 0.998 X5.

X1, X2, X3, and X5 are the same lines as in Z. X4 is book value of equity divided by book value of total liabilities. Say which equity line. Do not use a market price. The notes say the cutoffs change. The file that was read does not print the new zone numbers. Write "not found" for the zones. Do not copy 1.81, 2.99, or 2.675 onto Z'. Do not copy zone numbers from a secondary page.

## Z'', only when the user asks for the non-manufacturer or emerging-markets version

Z'' = 6.56 X1 + 3.26 X2 + 6.72 X3 + 1.05 X4. There is no sales term.

X4 is book value of equity divided by book value of total liabilities, as in Z'. The notes say a score below 1.10 indicates a distressed condition. They do not print an upper bound in the file that was read. Do not call a score above 1.10 safe. Do not add 3.25 unless the user asks for the emerging-markets bond-equivalent score. If they do, add 3.25, label that sum separately, and say the notes add it so that zero lines up with a D-rated bond. Do not turn the sum into a rating letter.

## Kill

A Z built from Z'' coefficients is not Z. A market value taken from a printed P/E is not X4. A score with one input missing is not a score.

## Return

```markdown
## Screen: Altman
- Which model:
- Sample the notes describe:
- Period and statement type:
- X1 working capital / total assets:
- X2 retained earnings / total assets:
- X3 EBIT / total assets:
- X4 equity / total liabilities:
- X5 sales / total assets:
- Score:
- Bounds the notes print for this model:
- Result:
- Refuses to opine on:
```

Leave X5 as "not in this model" when the model is Z''. For Z', say X4 is book equity.

Worked pattern: Z computed from a company-printed P/E times earnings. The score is not found. A score of 2.2 called a pass sits in the zone of ignorance. Say the zone. Do not call it a pass.

## Disclaimer

Paste the disclaimer from the iron rules.
