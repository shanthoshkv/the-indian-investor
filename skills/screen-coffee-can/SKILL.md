---
name: screen-coffee-can
description: >
  Applies Saurabh Mukherjea's Coffee Can screen to an NSE or BSE
  company: a decade of return on capital and revenue growth, year by
  year, from filings. Use when the user asks for a Coffee Can screen.
  Not a lens, not QGLP, and not a buy list.
compatibility: Agent Skills hosts. India listed companies. No data-website averages.
---

# Coffee Can screen

A screen, not a temperament. It does not replace `lens-agrawal`.

The two-metric statement Mukherjea gave in public (Republic Media Network, India Economic Summit, 28 November 2025, as reported): look at the last 10 years, minimum 15% return on capital, minimum 10% revenue growth. That is the screen this skill runs unless the user asks for the later one.

The later description, from his September 2026 conversation about *The Art of Enduring*: 15 years, return on capital employed above 15% in every year and not as an average, and median revenue growth above India's nominal GDP growth. Use it only when the user asks. The GDP growth figure needs a named source. An unsourced "about 12%" does not pass.

Do not use a Screener query or a newspaper stock list as the screen. Do not add a market-cap floor. Those show up in other people's screens. They are not the two-metric statement.

## Iron rules

1. India only. NSE or BSE. Anything else: stop and say so. A private company has no listed decade to open. Stop.
2. Every figure has source, period, and consolidated or standalone. If it is not in a source, write "not found". Do not estimate silently.
3. INR, with crore or lakh stated. Indian fiscal year (April–March) unless the filing says otherwise.
4. Separate fact, inference, and opinion.
5. Promoter holding, pledge, related parties, and auditor notes stay in the memo when this screen is part of a full memo. The screen itself does not pass on a clean promoter.
6. Close with this disclaimer. No buy, sell, or target presented as advice or as a certain outcome.

> This is an educational research memo, not investment advice, not a SEBI-registered recommendation, and not a solicitation to buy or sell any security. Figures are only as good as the filings cited. You decide what to do with them.

Take each year from `../analyze-financials/SKILL.md`. A bank or an RBI-regulated NBFC uses `../analyze-financials/references/lenders.md`. Do not put the non-financial ROCE on a loan book. For a lender, the later screen's ROE test is the one that applies, and only if the user asked for that later screen. The original two-metric statement did not swap in ROE.

## Tests

1. Window. Ten fiscal years for the original screen, fifteen for the later one. Each year was opened from a filing. A "10-year CAGR" or a "10-year average ROCE" on a data website does not open the years. Fewer opened years: say how many, and the screen is not passed.
2. Revenue. Each opened year grew at least 10% for the original screen. For the later screen, the median growth must beat a cited nominal GDP growth. One missing year fails the window, not a silent skip.
3. Return on capital. Each opened year at least 15%, using ROCE from `statements.md`, unless you are on the later screen and the issuer is a lender, in which case ROE. If you use a return the company prints under another name, say so. Do not insert a second cutoff.
4. Price is not a filter. Report a sourced multiple only if a lens asked for it. Do not turn a pass into a buy.

## Kill

Fail the screen when any opened year misses a hurdle, or when the pass depends on years you did not open.

## Return

```markdown
## Screen: Coffee Can
- Which statement of the screen:
- Years opened:
- Revenue growth, each year:
- Return on capital, each year:
- Result:
- Refuses to opine on:
```

Worked pattern: a website says sales CAGR 18% and average ROCE 22% for ten years, and the filings were not opened. The screen is not passed.

## Disclaimer

Paste the disclaimer from the iron rules.
