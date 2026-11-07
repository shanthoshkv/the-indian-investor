---
name: review-diversification
description: >
  Reads the holdings list the user wrote and reports the concentration
  that list shows, with SEBI's published risk points. Use when the
  user asks whether a list is diversified. Does not pick a stock to
  buy or sell and does not set a stock count.
compatibility: Agent Skills hosts. The user writes the list. No invented stock count.
---

# Diversification

The user's list, read against one SEBI page. Not a portfolio constructor.

The page opened is `https://investor.sebi.gov.in/investment_risk_managment.html`, titled "How to Manage Investment Risks" on the SEBI Investor site. Report these points as that page states them.

- Research the investment, or seek professional help when you cannot do that research.
- Diversify across different asset classes. The page's word is "different".
- Diversify within an asset category, including within the securities market. Two images on the page were not read as text. Do not invent the slices those images draw.
- Market-wide price volatility is not removed by holding more securities. When the market falls, the page says individual securities fall too.
- Match the investment to the horizon. The page says avoid equity markets for a short-term investment, look to securities that can beat inflation for a long-term investment, and avoid volatile or illiquid investments when the money is needed soon. That is the page's general sentence. It is not a buy or a sell of a name on the list.
- The page quotes Benjamin Graham: "Successful investing is about managing risk, not avoiding it."

The page prints no stock count, no sector cap, and no maximum weight. Studies that propose a count of names were not opened. Do not add 10, 15, 30, or any other count.

## Iron rules

1. India only for any filing you open. A non-India line stays a line the user wrote. Do not open that issuer's foreign filing. Anything that asks for a foreign memo: stop and say so.
2. Every figure has source, period, and consolidated or standalone. If it is not in a source, write "not found". Do not estimate silently. A weight the user did not write is not found.
3. INR, with crore or lakh stated, when an amount is in rupees.
4. Separate fact, inference, and opinion. The list is the user's fact. A computed share of a total they wrote is labeled computed.
5. Promoter holding, pledge, related parties, and auditor notes stay in the facts skill when a name on the list is also being analyzed. Do not invent them here.
6. Close with this disclaimer. No buy, sell, or target presented as advice or as a certain outcome.

> This is an educational research memo, not investment advice, not a SEBI-registered recommendation, and not a solicitation to buy or sell any security. Figures are only as good as the filings cited. You decide what to do with them.

## List

Copy `holdings/TEMPLATE.md` to `holdings/<yyyy-mm-dd>.md`. The user fills the lines. You do not add a name, a weight, or a sector. You do not say what to buy or what to sell. Personal lists stay out of the public repo. The template is the file that is tracked.

If the file is missing or the lines are blank, say the list was not written and stop.

Report the count of lines the user wrote, and any name that appears twice. That count is a description of the file. It is not a pass or a fail.

Weights: if the user wrote an amount or a weight on every line, you may report each line's share of that total, labeled computed. If any line has no amount, the shares are not found. Do not fill the gap with zero.

Sector or asset class: only a label the user wrote, or a sector a filing you opened states for that issuer. Do not assign one from memory.

## Kill

Do not call the list diversified enough, too concentrated, or in need of a named change. Do not turn the page's short-term sentence into a sale of a share on the list. One name is what the list shows when the user wrote one name.

## Return

```markdown
## Diversification
- List:
- Lines the user wrote:
- Weights:
- Concentration the list shows:
- What the SEBI page says:
- Result:
- Refuses to opine on:
```

Worked pattern: four names, and the memo says the list fails because a study wants fifteen. That count is not on the page. Do not write it. A missing weight scored as zero, so the largest line looks smaller, is not the list.

## Disclaimer

Paste the disclaimer from the iron rules.
