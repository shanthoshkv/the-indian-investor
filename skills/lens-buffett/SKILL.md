---
name: lens-buffett
description: >
  Applies a Warren Buffett owner lens to an NSE or BSE company or an
  India bootstrapped business: moat, management, owner earnings, and
  price. Use when the user asks for a Buffett, owner-earnings, or
  moat view of an Indian company. India only.
compatibility: Agent Skills hosts. Uses filing figures. Does not analyze non-India listings.
---

# Buffett lens

An owner reading an Indian business. This is not a reason to analyze a company outside India.

## Iron rules

1. India only. NSE, BSE, or an India bootstrapped company. Anything else: stop and say so.
2. Every figure has source, period, and consolidated or standalone. If it is not in a source, write "not found". Do not estimate silently.
3. INR, with crore or lakh stated. Indian fiscal year (April–March) unless the filing says otherwise.
4. Separate fact, inference, and opinion.
5. Promoter holding, pledge, related parties, and auditor notes are part of the analysis.
6. Close with this disclaimer. No buy, sell, or target presented as advice or as a certain outcome.

> This is an educational research memo, not investment advice, not a SEBI-registered recommendation, and not a solicitation to buy or sell any security. Figures are only as good as the filings cited. You decide what to do with them.

If `analyze-financials` has not already produced the evidence table, read `../analyze-financials/SKILL.md` for a listed company, or `../analyze-bootstrapped/SKILL.md` for a private one, and do that first.

## Tests

Each test is pass, fail, or not found.

1. Understandable. Can you say what it sells, to whom, in India, in a few sentences without jargon? Fail if you cannot.
2. Durable moat. Name the mechanism (cost, habit, distribution, license, switching cost, owned assets) and the evidence. A slogan with no evidence is a fail.
3. Able and honest management. In India, promoter control is normal. Judge the public record: pledge, related-party transactions, auditor qualifications or a recent auditor change, and capital allocation (dividend, buyback, dilution, capex that does not earn its cost). Not found on any of those is not a pass.
4. Return on the capital it must reinvest. Use ROE and ROCE from the financials skill across the years opened. Not found if those ratios were not built from a filing.
5. Price versus owner earnings. Build the bridge below only with the assumption written in the sentence. If you cannot separate maintenance capex from growth capex, do not publish a single owner-earnings number. Show PAT, depreciation, and total capex as facts and mark owner earnings "not found". If price or earnings are missing, the test is not found. You may state a sourced price-to-earnings multiple as a fact. Whether it is attractive is an opinion, and it is not a target.

### Owner-earnings bridge

Label the result inference.

- PAT
- plus depreciation and amortisation
- minus maintenance capex (state the rule: depreciation as a proxy, or a split you can point to in the capex note). New stores, new plants, or a capex line larger than depreciation are not maintenance. Unless the note splits them, owner earnings stays not found.
- minus the increase in working capital that consumed cash (or plus a decrease)

## Kill

Stop the lens as a fail when the business cannot be explained, or the moat has no evidence. Do not fill the later tests with praise to offset that.

## India

Ind-AS figures, not US GAAP. Do not import Berkshire's partnership standard. Honesty here is the promoter record in the filings.

## Return

```markdown
## Lens: Buffett
- Understandable:
- Moat:
- Management:
- Reinvestment return:
- Price versus owner earnings:
- India caveat:
- Refuses to opine on:
```

Worked pattern, not a live company: a manufacturer whose customers reorder every month, whose gross margin held up while a peer cut price, and whose pledge column is blank because you never opened the shareholding pattern. Tests 1 and 2 can pass. Test 3 is not found, not a pass.

## Disclaimer

Paste the disclaimer from the iron rules.
