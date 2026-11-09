---
name: critique-thesis
description: >
  Attacks an Indian-company research memo for missing filings, mixed
  consolidated and standalone figures, pledge and related-party gaps,
  and advice language. Use when the user asks for a critique, red team,
  bear case, or a check of an India investment thesis.
compatibility: >
  Agent Skills hosts. Reads the draft memo and, when a filing is cited,
  the filing. India only.
---

# Critique thesis

Attack the memo in front of you. Do not write a second bull case. Do not offer a price target.

## Iron rules

1. India only. NSE, BSE, or an India bootstrapped company. Anything else: stop and say so.
2. Every figure has source, period, and consolidated or standalone. If it is not in a source, write "not found". Do not estimate silently.
3. INR, with crore or lakh stated. Indian fiscal year (April–March) unless the filing says otherwise.
4. Separate fact, inference, and opinion.
5. Promoter holding, pledge, related parties, and auditor notes are part of the analysis.
6. Close with this disclaimer. No buy, sell, or target presented as advice or as a certain outcome.

> This is an educational research memo, not investment advice, not a SEBI-registered recommendation, and not a solicitation to buy or sell any security. Figures are only as good as the filings cited. You decide what to do with them.

## Checklist

Mark each item pass, fail, or not applicable. A fail needs the sentence in the memo that caused it.

- Figures with no source, period, or consolidated/standalone label.
- Consolidated and standalone mixed in one ratio or one sentence.
- Promoter holding, pledge, related parties, or auditor notes missing on a listed company.
- Other income versus profit, or cash from operations versus PAT, not mentioned when the statements were in scope.
- Bull case that is only a higher multiple.
- Two lenses disagreed and the memo averaged them or dropped one.
- Market defined with a global TAM, or a non-India peer set treated as the Indian market.
- Bootstrapped or private company given listed-company precision (revenue, margin, retention) without a filing.
- Language that tells the reader to buy, sell, hold, or expect a price.
- A company-printed P/E used as an exchange market cap, or an annual-report dash or Nil used as the Regulation 31 pledge.
- One issuer's revenue divided by another's and called a market share.
- A Coffee Can pass, or a QGLP pass, on years whose filings were not opened.
- An NSE-only cash net blended with the NSE+BSE+MSEI net, a day's market flow used as a reason to buy or sell a named stock, or a portal flow used when the exchange or depository page was opened and they differ.
- A bulk or block deal used as the promoter percent, a market-wide DII figure used as a named fund's holding, a bonus, split, or index change used as a change in the business, or a news line used as the credit-rating rationale.
- The circle file listed industries and the memo still analyzed a company outside them, a hurdle rate on capital versus profit that no filing prints, a quarterly figure mixed into an annual ratio inside a results diff, or a brokerage, STT, or tax rate that was not on the page opened.
- An F-score or a Z-score printed when an input was not opened, a missing input scored as zero, a quarter used as the annual F, Z mixed with Z' or Z'', a zone number the notes did not print, or a stock-count cutoff on the diversification note.
- Growth on a low base (a year after a loss, a strike, or a plant shutdown) presented as a run rate, with no base-year sentence.
- PAT that rises on exceptional items, other income, a deferred-tax credit, or a one-time gain, presented as operating growth.
- Only the survivors compared: peers or a past cycle chosen because they did well, with no mention of the ones that did not.
- A reverse-DCF implied growth called a fair value or a target, a discount rate called the company's cost of equity, or a terminal growth at or above the discount rate.
- A governance flag called fraud without a regulator order, a concall promise used as a fact, or a shareholding percent change read as a sale when the share count changed.
- The data-freshness table missing, or a stale filing used while a later quarter was filed.
- A broker quote used as the exchange close or as a market cap, an order described as sent, a derivative row turned into an F&O tip, or a figure from a server that was not connected.

## Return

```markdown
## Critic
- Breaks the thesis: ...
- Weakens it: ...
- Nit: ...

## Revised conclusion
One paragraph. "Do not conclude" is a valid conclusion.

## Disclaimer
[paste the disclaimer]
```

Severity:

- Breaks the thesis: a missing or contradicted fact the conclusion depends on.
- Weakens it: a real gap that leaves the conclusion standing only as a hypothesis.
- Nit: wording or order. Do not use this bucket to hide a broken figure.

If the memo survives, say what you checked and that you did not find a breaking gap. Do not invent a weakness to look rigorous.
