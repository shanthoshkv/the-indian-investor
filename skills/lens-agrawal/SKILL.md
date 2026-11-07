---
name: lens-agrawal
description: >
  Applies Raamdeo Agrawal's QGLP checklist to an Indian company:
  quality, growth, longevity, and price versus growth. Use when the
  user asks for a QGLP, Raamdeo, or Agrawal view of an NSE or BSE
  company.
compatibility: Agent Skills hosts. India only. Not the Coffee Can screen.
---

# Agrawal lens

Raamdeo Agrawal's QGLP: Quality, Growth, Longevity, Price reasonable versus growth.

This is not the Coffee Can screen and not a second Buffett essay. Quality is return on capital and a competitive fact, not an adjective.

## Iron rules

1. India only. NSE, BSE, or an India bootstrapped company. Anything else: stop and say so. QGLP here is for a listed company with multi-year filings. A private company without those filings: say the checklist cannot be scored, and stop.
2. Every figure has source, period, and consolidated or standalone. If it is not in a source, write "not found". Do not estimate silently.
3. INR, with crore or lakh stated. Indian fiscal year (April–March) unless the filing says otherwise.
4. Separate fact, inference, and opinion.
5. Promoter holding, pledge, related parties, and auditor notes are part of the analysis.
6. Close with this disclaimer. No buy, sell, or target presented as advice or as a certain outcome.

> This is an educational research memo, not investment advice, not a SEBI-registered recommendation, and not a solicitation to buy or sell any security. Figures are only as good as the filings cited. You decide what to do with them.

Take ratios from `../analyze-financials/SKILL.md` if they are not already on the page. Use the same consolidated or standalone choice for every year in the growth window.

## Tests

1. Quality. ROE and ROCE for the years opened, plus one competitive fact (share, cost, distribution, switching cost) with a source. Three years of ratios is the minimum when the filings exist. Adjectives do not pass.
2. Growth. Revenue and PAT growth over that same window, cited. One year is not the growth test. Compute from the filings you opened. If a year is missing, say the window is shorter and do not pass longevity off it.
3. Longevity. Why those growth rates can continue: an Indian industry runway and a company edge. Tag inference. A TAM slide is not longevity.
4. Price versus growth. The sourced multiple and the sourced growth rate, side by side. Whether the price is reasonable versus that growth is an opinion. No target. If price is not sourced, this test is not found. Quality and growth can still be reported.

## Kill

Fail quality when the ratios were not built from filings. Do not borrow a screen's "high ROCE for a decade" label. That is a different test and it is not in this pack.

## Return

```markdown
## Lens: Agrawal (QGLP)
- Quality:
- Growth:
- Longevity:
- Price versus growth:
- Refuses to opine on:
```

When the Buffett lens also ran, do not replace its owner-earnings bridge with this multiple. Note the difference in one line if the two price tests disagree.

Worked pattern: one year of high ROE, and a data website's "ten-year ROCE" label with those years unopened. Quality is not passed. That label is the Coffee Can screen, and it is not this lens.

## Disclaimer

Paste the disclaimer from the iron rules.
