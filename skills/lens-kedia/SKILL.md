---
name: lens-kedia
description: >
  Applies Vijay Kedia's SMILE screen to a smaller Indian listed company:
  small size, medium promoter experience, large aspiration, extra-large
  market. Use when the user asks for a Kedia or SMILE view of an NSE
  or BSE stock.
compatibility: Agent Skills hosts. India listed companies. Screen does not fit index giants.
---

# Kedia lens

Vijay Kedia's SMILE screen for a company listed on NSE or BSE. He states the letters as four tests, not five:

- S — small in size, meaning small in its Indian sector
- MI — medium experience of the promoter
- L — large aspiration
- E — extra-large market potential, in India

Do not add a fifth test to use a spare letter. "Buy right and sit tight" is allowed only after all four are evidenced. It is not a substitute for a missing letter.

## Iron rules

1. India only. NSE, BSE, or an India bootstrapped company. Anything else: stop and say so. This screen is for a listed company. A private company: say the screen needs a listed size, and stop.
2. Every figure has source, period, and consolidated or standalone. If it is not in a source, write "not found". Do not estimate silently.
3. INR, with crore or lakh stated. Indian fiscal year (April–March) unless the filing says otherwise.
4. Separate fact, inference, and opinion.
5. Promoter holding, pledge, related parties, and auditor notes are part of the analysis.
6. Close with this disclaimer. No buy, sell, or target presented as advice or as a certain outcome.

> This is an educational research memo, not investment advice, not a SEBI-registered recommendation, and not a solicitation to buy or sell any security. Figures are only as good as the filings cited. You decide what to do with them.

If market cap, promoter history, or financials are not already on the page, take listed figures from `../analyze-financials/SKILL.md` and the Indian market from `../analyze-market/SKILL.md` only for the L test.

## Fit

He has said he invests in small and mid caps, and in a company that is small in its sector. If the company is the large leader of its Indian market, say S fails and stop the screen. Do not invent a market-cap cutoff in rupees. If you have neither a sourced market cap nor a sourced share of the Indian sector, S is not found and the screen does not pass.

## Tests

1. Small. Small in its Indian sector, shown with a sourced share, or with a sourced market cap and date set next to the sector leader's sourced size. Not found if you have neither.
2. Medium experience. Years the promoter has run this business or a prior one, from the annual report, a filing, or the company's own page. He has used roughly 15–20 years, and having lived through a bad cycle, as an illustration, plus a clean public record. Report the years you found. A first-time promoter with no downcycle on the record fails. An unsourced career is not found. Do not fail a longer tenure on a cutoff you invented.
3. Large aspiration. A capex plan, capacity target, or formal guidance in a filing or presentation. An interview slogan is a hypothesis and cannot pass this test alone.
4. Extra-large market. An Indian customer, geography, and price band, with a cited India size or an explicit "size not found". A global TAM slide does not pass. The company staying small inside that market is the point of E. Size not found does not pass.

## Kill

Do not add "sit tight" when any letter is fail or not found.

## Return

```markdown
## Lens: Kedia
- Fit (smaller listed company):
- Small (S):
- Medium experience (MI):
- Large aspiration (L):
- Extra-large Indian market (E):
- Sit tight (only if all four evidenced):
- Refuses to opine on:
```

## Disclaimer

Paste the disclaimer from the iron rules.
