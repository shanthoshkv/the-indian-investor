---
name: lens-bakshi
description: >
  Applies Sanjay Bakshi's India checks that sit beside a moat: customer
  float, moat spend that was expensed, and a refusal to fail a share
  only because the reported multiple is high. Use when the user asks
  for a Bakshi or Sanjay Bakshi view of an NSE or BSE company.
compatibility: Agent Skills hosts. India only. Not a second owner-earnings bridge.
---

# Bakshi lens

Sanjay Bakshi on an Indian listed business. Moat and a long hold are already in the Buffett lens. This lens adds the tests that one does not cover. Do not rebuild owner earnings here.

He has said a durable moat lowers the risk of a permanent loss, and that a reported P/E above a round number is a prejudice when moat-building spend has been charged to the P&L. He has discussed float as cash the customer has paid before delivery, including in businesses that are not insurers.

## Iron rules

1. India only. NSE, BSE, or an India bootstrapped company. Anything else: stop and say so.
2. Every figure has source, period, and consolidated or standalone. If it is not in a source, write "not found". Do not estimate silently.
3. INR, with crore or lakh stated. Indian fiscal year (April–March) unless the filing says otherwise.
4. Separate fact, inference, and opinion.
5. Promoter holding, pledge, related parties, and auditor notes are part of the analysis.
6. Close with this disclaimer. No buy, sell, or target presented as advice or as a certain outcome.

> This is an educational research memo, not investment advice, not a SEBI-registered recommendation, and not a solicitation to buy or sell any security. Figures are only as good as the filings cited. You decide what to do with them.

Listed facts come from `../analyze-financials/SKILL.md` if they are not already on the page.

## Tests

1. Float. A liability that is the customer's cash before the company delivers: advances from customers, unearned premium, or a deposit the filing describes that way. Amount, period, statement. Trade payables to suppliers are not this test. If the line is not on the pages you read, float is not found, not zero.
2. Expensed moat spend. Name the line and the amount if advertising, new branches, or another moat-building cost was charged to profit. Do not add it back. Adjusted earnings are "not found" unless the company published them. You may say, as inference, that reported profit is after that spend.
3. Multiple prejudice. A sourced multiple, or "not found". A sentence that the shares fail because the multiple is above a round number, with no other fact, fails this test. Do not install any number as a ceiling.
4. Permanent loss. One moat fact from a filing, plus the promoter record from the financials skill. Either one missing: not found, not a pass. If the Buffett lens ran, one line that this is not its owner-earnings figure.

## Kill

Fail the lens when the conclusion is an adjusted profit you computed, or when the only attack is a high reported multiple.

## Return

```markdown
## Lens: Bakshi
- Float:
- Expensed moat spend:
- Multiple:
- Permanent loss:
- Disagreement with Buffett (only if that lens ran):
- Refuses to opine on:
```

Worked pattern: "P/E is 40, so it is expensive," with no expense line and no float line. Test 3 fails. Adding back advertising to invent an economic profit also fails.

## Disclaimer

Paste the disclaimer from the iron rules.
