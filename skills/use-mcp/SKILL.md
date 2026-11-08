---
name: use-mcp
description: >
  Uses an MCP server the user connected, including Zerodha's hosted
  Kite server, for a quote, a holding, or an account read. Use when
  the user asks to add an MCP server or to read one they connected.
  Does not place an order. A broker quote is not the exchange close.
compatibility: Agent Skills hosts. Optional server. No API keys in the repo. No orders.
---

# MCP servers

An option, not a default source. This pack does not ship a server and does not connect one for you. A server that is not connected in this session is not found. Do not invent a tool, an argument, or a figure.

Call a tool only when the user asked for that read and the tool's schema is available in this session. Name the server, the tool, and the time the tool returned. A filing still wins. The order is in `../indian-investor/references/sources.md`.

## Iron rules

1. India only. NSE, BSE, or an India bootstrapped company. A non-India instrument: stop. A derivative, including NFO, MCX, and CDS: stop. Do not turn that row into an F&O tip or an intraday call.
2. Every figure has source, period, and consolidated or standalone when a statement is involved. A broker quote has the tool name and the timestamp the tool returned. If the tool did not return it, write "not found". Do not estimate silently.
3. INR, with crore or lakh stated when you convert. Do not convert a rupee quote into crore unless you show the arithmetic and label it computed.
4. Separate fact, inference, and opinion. The tool's row is the fact. What it means for the business is not this skill.
5. Promoter holding, pledge, related parties, and auditor notes stay in the facts skill. A broker holding is not the promoter percent and not the pledge.
6. Close with this disclaimer. No buy, sell, or target presented as advice or as a certain outcome. Do not place, modify, or cancel an order.

> This is an educational research memo, not investment advice, not a SEBI-registered recommendation, and not a solicitation to buy or sell any security. Figures are only as good as the filings cited. You decide what to do with them.

## Add a server

The user adds the server in their own client. Copy `mcp/TEMPLATE.md` to `mcp/<name>.md` and fill the name and the endpoint. Leave the secret blank. Personal notes stay out of the public repo. The template is the file that is tracked.

Do not write a `.mcp.json` into this repo. Do not write an API key, an API secret, a password, or a TOTP into a file, a chat reply, or a tool argument. If a tool needs a sign-in, point at the client's login. Do not collect the password.

Zerodha's hosted server is the one that was opened. Read `references/kite.md` before calling it. Any other server uses the same rules, and only the tools that session actually exposes. Do not assume another server has Kite's tool names.

## What a read may be

A last price, a quote, OHLC, or a candle is the broker's figure. It is not the NSE or BSE close. The exchange close lives in `../analyze-financials/references/statements.md`. If the exchange page was not opened, that close stays not found. Do not multiply a last price by the share count and call the product a market cap. Do not use a broker last price as the market value in `../screen-altman/SKILL.md`.

Holdings, positions, margins, mutual-fund units, and existing orders are the account's rows on that tool's clock. They are not the written list in `../review-diversification/SKILL.md` unless the user asks to copy them. If they ask, copy the template to a gitignored file and write only the columns the tool returned. Do not add a name. Do not say what to sell. Mutual-fund units on the account are not an AMFI scheme disclosure. That disclosure is `../analyze-funds/SKILL.md`.

A candle history is not an annual filing and not an annual ratio. Do not mix it into ROCE, the F-score, or Z.

## What this skill does not call

Do not call a tool that places, modifies, or cancels an order or a trigger. On the Kite server that was read, those names are `place_order`, `modify_order`, `cancel_order`, `place_gtt_order`, `modify_gtt_order`, and `delete_gtt_order`. If the user asks to buy, sell, place, modify, or cancel, stop. Reading an order that already exists is allowed when they ask what the account shows. It is not an instruction to change it.

A tool this skill does not name, whose schema says it places or cancels an order, is in the same stop list.

## Return

If they only asked how to add a server, return the setup and do not call a tool.

```markdown
## Broker
- Server:
- Signed in:
- Tool and what it returned:
- What it does not replace:
- Refuses to opine on:
```

Worked pattern: the user asks for the exchange close and the reply uses a broker last price as that close. The broker figure can sit in this section. The exchange close stays not found until the exchange page is opened.

## Disclaimer

Paste the disclaimer from the iron rules.
