---
name: lens-damani
description: >
  Applies Radhakishan Damani's filters to an Indian business: whether
  you would build it, what earnings multiple you would assign, whether
  you would lend to the promoter, plus debt, cash flow, and repeat
  demand. Use when the user asks for a Damani, DMart, or Radhakishan
  view of an NSE, BSE, or India bootstrapped company.
compatibility: Agent Skills hosts. India only. Methods, not a biography.
---

# Damani lens

Radhakishan Damani's filters on an Indian business. Chandrakant Sampat's "simple, little debt, free cash flow, low capex" test lives in tests 4 and 5. It is not a separate skill.

## Iron rules

1. India only. NSE, BSE, or an India bootstrapped company. Anything else: stop and say so.
2. Every figure has source, period, and consolidated or standalone. If it is not in a source, write "not found". Do not estimate silently.
3. INR, with crore or lakh stated. Indian fiscal year (April–March) unless the filing says otherwise.
4. Separate fact, inference, and opinion.
5. Promoter holding, pledge, related parties, and auditor notes are part of the analysis.
6. Close with this disclaimer. No buy, sell, or target presented as advice or as a certain outcome.

> This is an educational research memo, not investment advice, not a SEBI-registered recommendation, and not a solicitation to buy or sell any security. Figures are only as good as the filings cited. You decide what to do with them.

Listed facts come from `../analyze-financials/SKILL.md` if they are not already on the page. Private facts come from `../analyze-bootstrapped/SKILL.md`.

## Tests

Each test is pass, fail, or not found.

1. Would I put my own money into building this business? The product is simple and demand repeats (people buy it again without a new story). Evidence or fail. A clever technology story with no repeat purchase is a fail.
2. What earnings multiple would I assign, and is the price below it? The multiple is an opinion and must be justified from this business (cash, durability, how much capital it needs). Copying the peer median is not this test. If you cannot justify a multiple, write "not found". Compare to price only when price and earnings are both sourced. No target price.
3. Would I lend to this promoter? Use pledge, related parties, auditor notes, and any SEBI order you actually opened. No public record is "not found", and not found is not a pass.
4. Little or no debt, and working capital. Report net debt, interest cover, lease liabilities, and whether payables fund inventory and receivables. "High debt" is allowed only with those figures. If the figures are missing, this test is not found, not a kill. A grocery or retail format is not evidence of negative working capital.
5. Free cash flow and maintenance capex. Cash from operations minus capex, labeled, with the period. Low maintenance capex is a fact only if the capex note supports it. Otherwise "not found".
6. Government discretion. If a license, tariff, or tender is the thing that protects profits, say so. It is a risk on this lens. It is not an automatic fail when the business is otherwise simple and cash-generative.
7. Core versus trading, only if the user asks how this lens would classify a holding. Core means the tests that passed would still pass after a scare. Trading means the first sign of trouble ends the idea. Label this opinion. Do not tell the reader to buy either bucket.

## Kill

Fail the lens on a clever story, on debt that failed test 4 with figures, or on a promoter test that failed. Do not fail test 4 from an adjective.

## Return

```markdown
## Lens: Damani
- Build it:
- Multiple versus price:
- Lend to the promoter:
- Debt and working capital:
- Cash flow and capex:
- Government discretion:
- Core versus trading (only if asked):
- India caveat:
- Refuses to opine on:
```

Worked pattern: a grocery chain that owns its stores, sells food people buy every week, and whose payables exceed inventory. Tests 1 and 4 can pass on those facts. Test 2 still needs a price and a multiple you can justify. Test 3 still needs the promoter record. Owning the stores is evidence on capex and on test 1. It is not a pass on the multiple.

## Disclaimer

Paste the disclaimer from the iron rules.
