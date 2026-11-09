# The Indian Investor

Research skills for **Indian markets only**: companies listed on the NSE or BSE, and India-headquartered bootstrapped companies.

The pack is a set of [Agent Skills](https://agentskills.io). The same `SKILL.md` folders work in Claude Code, Codex, Cursor, GitHub Copilot, and Gemini CLI. A skill is a folder with YAML frontmatter (`name`, `description`) and instructions the agent loads when the task matches.

Memos cite filings. They are educational research. They are not investment advice, not SEBI-registered research, and not a buy, sell, or price target.

```
This is an educational research memo, not investment advice, not a
SEBI-registered recommendation, and not a solicitation to buy or sell
any security. Figures are only as good as the filings cited. You decide
what to do with them.
```

## Ask for a memo

Open this repo in the agent after running the link script below.

| You say | What runs |
| --- | --- |
| "Analyze this NSE company." | Router. Facts first, then Damani, Buffett, and Munger, then the critic. |
| "Damani only on this BSE name." | Financials, then `lens-damani`, then the disclaimer. |
| "SWOT of Indian quick commerce." | `analyze-swot` and `analyze-market`. Three bullets per cell. |
| "Buffett analysis of Apple." | Stop. Apple is outside India. |
| "What did FIIs and DIIs do in the cash market?" | `analyze-flows`. Not part of a company memo unless you ask. |
| "Who bought this stock in a bulk or block deal?" | `analyze-deals`. A row is not the promoter percent. |
| "Which mutual fund holds this stock?" | `analyze-funds`. A market-wide DII net is not a scheme holding. |
| "What was the bonus, the dividend, or the index change?" | `analyze-actions`. An action is not a better business. |
| "What did the rating agency say?" | `analyze-rating`. A news line is not the rationale. |
| "Reread the decision I wrote last year." | `review-decision`. It checks that note. It does not say what to buy. |
| "What changed in this quarter versus the last memo?" | `diff-results`. The quarter stays out of the annual ratios. |
| "What did the trade cost?" | `note-costs`. A rate that was not on the page is not found. |
| "Run a Piotroski screen." | `screen-piotroski`. A missing input leaves the total not found. Not a buy list. |
| "What is the Altman Z-score?" | `screen-altman`. Z unless you name the private-firm or non-manufacturer version. Not a default probability. |
| "Is this holdings list diversified?" | `review-diversification`. Your list. No stock-count cutoff. |
| "Add Zerodha, or read the broker MCP I connected." | `use-mcp`. Optional. A broker quote is not the exchange close. No orders. |
| "What growth does this price imply?" | `value-reverse-dcf`. Implied growth from sourced FCF. Not a target or a fair value. |
| "Any governance red flags?" | `check-governance`. Auditor, KMP churn, SEBI orders, money to the group, pledge. A flag is not fraud. |
| "Did management deliver on what they said on calls?" | `read-concall`. Delivered, missed, moved, or open. Guidance is not a fact. |
| "How has the promoter and FII stake moved?" | `track-shareholding`. Eight quarters from Regulation 31. Share-count changes checked first. |
| "Does PLI or a new duty affect this sector?" | `note-policy`. Official notification only. Effect only if the company filed it. |

Name a lens when you want it. If you name none on a full company memo, the default set is Damani, Buffett, and Munger. Industry skills run when you ask about the market, rivals, or leadership, or when a lens cannot answer without them.

## Skills

| Skill | Role |
| --- | --- |
| `indian-investor` | Router. Scope gate, source order, memo shape. |
| `analyze-financials` | P&L, balance sheet, cash flow, pledge, related parties, auditor. Banks and NBFCs use `references/lenders.md`. |
| `analyze-market` | Indian customer, geography, and price band. No global TAM as evidence. |
| `analyze-competition` | Up to five NSE or BSE peers, then unlisted rivals marked unverified. |
| `analyze-market-leader` | Who leads and what holds the lead. Does not paste the peer table again. |
| `analyze-swot` | Three bullets per cell, each tagged evidence or hypothesis. |
| `analyze-bootstrapped` | Private India companies. Stops when funding is mainly VC or PE. |
| `critique-thesis` | Attacks the draft. "Do not conclude" is an allowed result. |
| `lens-buffett` | Understandable business, moat, promoter record, owner earnings, price. |
| `lens-munger` | How it fails in India, bias in the bull case, quality at a fair price. |
| `lens-damani` | Would you build it, what multiple would you assign, would you lend to the promoter. |
| `lens-jhunjhunwala` | India growth versus a company-specific edge. More willing to pay for growth than Damani. |
| `lens-kedia` | SMILE as Vijay Kedia states it: small in the sector, medium experience, large aspiration, extra-large Indian market. |
| `lens-agrawal` | QGLP: quality, growth, longevity, price versus growth. |
| `lens-prasad` | Nalanda's screens: high return on capital, no turnaround, no forecast. |
| `lens-bakshi` | Customer float and expensed moat spend. A high reported multiple is not itself a fail. |
| `lens-andrade` | Capital cycle. Dominance with a light balance sheet. Not quality at any price. |
| `screen-coffee-can` | Ten filed years of revenue growth and return on capital. A screen, not a lens. |
| `analyze-flows` | Market-wide FII/FPI and DII cash. NSE-only and the combined series stay apart. Calendar nets, assets under custody, and a sector file stay market-wide. Not a company fact. |
| `analyze-deals` | Block deals, bulk deals, and SAST or insider rows for one company. Not the promoter percent. |
| `analyze-funds` | One scheme's month-end portfolio from AMFI or the AMC. Not the market-wide DII net. |
| `analyze-actions` | Dividend, split, bonus, buyback, and index add or drop. Not a better business. |
| `analyze-rating` | The rating symbol on the exchange filing. The reason only if the rationale file was opened. |
| `read-filings` | Local annual report, XBRL, Regulation 31, and rating PDF, read before the exchange. A missing file stays not found. |
| `review-decision` | The user's decision note, reread against the next annual report. Not a buy. |
| `diff-results` | The new quarter against the last memo's change list. Not an annual ratio. |
| `note-costs` | Brokerage, STT, and holding-period tax from the page opened. |
| `screen-piotroski` | Nine annual fundamental signals from filings opened. A missing input is not a zero. A screen, not a lens. |
| `screen-altman` | The 1968 Z-score, or Z' or Z'' when that version is asked. Not a default probability. Not for a bank. |
| `review-diversification` | The holdings list you wrote, with SEBI's risk page. No stock count. |
| `use-mcp` | An MCP server you connect yourself, including Zerodha's hosted Kite server. Not a filing. No orders. |
| `value-reverse-dcf` | The growth the market cap implies, from sourced FCF. Not a target. `scripts/reverse_dcf.py` does the solve. |
| `check-governance` | Auditor resignation, KMP churn, SEBI orders, money to the group, pledge trend. A flag is not fraud. |
| `read-concall` | Earnings-call statements checked against later filings. Guidance is not a fact. |
| `track-shareholding` | Eight quarters of promoter, pledge, FPI, MF, and public percent. Not a deal list. |
| `note-policy` | PLI, customs, GST, and regulator circulars from the official page. A policy is not a profit figure. |

Lenses disagree on purpose. Damani is less willing to pay for growth than Jhunjhunwala. Agrawal's price test is not Buffett's owner-earnings bridge. The memo keeps both results.

People left out, because a public checklist was too thin to write without inventing one: Ashish Kacholia, Nemish Shah, Dolly Khanna, Porinju Veliyath, Ramesh Damani, Utpal Sheth. Chandrakant Sampat's "simple, little debt, free cash flow, low capex" test sits inside `lens-damani`. Coffee Can is `screen-coffee-can`. Piotroski and Altman are screens, loaded only when asked. `review-diversification` reads a holdings list you write. It does not set a stock count. None of these is a default lens.

## Rules the agent must keep

1. India only. NSE, BSE, or an India bootstrapped company. Anything else stops.
2. Every figure has a source, a period, and consolidated or standalone. Missing data is `not found`.
3. INR, with crore or lakh stated. Fiscal year is April–March unless the filing says otherwise.
4. Fact, inference, and opinion stay separate.
5. Promoter holding, pledge, related parties, and auditor notes are part of a listed-company analysis.
6. The disclaimer closes every full memo. No buy, sell, or certain target.

Source order, in `skills/indian-investor/references/sources.md`:

A file saved under `filings/<issuer>/` is read first (`read-filings`). The list below is what you open when that folder does not already hold the filing.

1. Company annual report, quarterly results, investor presentation.
2. BSE and NSE filings, including the shareholding pattern.
3. SEBI disclosures when the question is insiders, pledges, or a takeover.
4. The sector regulator when it changes the business.
5. Screener, Trendlyne, Tijori, or Moneycontrol only as a way to find the filing. If they disagree with the filing, the filing wins.

There is no bulk downloader and no market-data API in this version. A broker MCP you connect yourself is optional. The method is `use-mcp`. This pack does not ship that server and does not place an order.

## Install

From the repo root:

```powershell
powershell -File scripts/link-skills.ps1
```

macOS or Linux: `sh scripts/link-skills.sh` (symlinks instead of junctions).

The script creates directory junctions. Edit `skills/` only, then re-run the script if you add a skill folder. The junctions are gitignored because they store absolute paths.

| Host | Path the script fills | How you call a skill |
| --- | --- | --- |
| Codex, Cursor, Copilot, Gemini CLI | `.agents/skills/<name>/` | `/indian-investor`, or the host's skill menu |
| Claude Code, this folder open as the project | `.claude/skills/<name>/` | `/indian-investor`, `/lens-damani` |
| Claude Code plugin | `skills/` plus `.claude-plugin/plugin.json` | `/the-indian-investor:lens-damani` |

User-wide install: junction or copy a skill folder into `~/.agents/skills/` or `~/.claude/skills/`. Install the whole pack together. Lenses point at sibling skills, so one folder copied alone cannot find the financials skill.

## Layout

```
skills/                 canonical SKILL.md folders
  indian-investor/      router and shared references
  analyze-*/            evidence skills
  lens-*/               investor checklists
  critique-thesis/
scripts/link-skills.*   links into .agents/skills and .claude/skills
scripts/reverse_dcf.py  implied-growth solver for value-reverse-dcf
evals/rubric.md         pass/fail checks for every eval
docs/history.md         phase plan and dry-run notes
evals/scenarios.md      five prompts that should fail in a specific way
evals/phase-*.md        live dry-run memos
.claude/agents/         Claude Code wrappers; Codex does not read these
AGENTS.md               always-on scope card for Codex
CLAUDE.md               same non-negotiables for Claude Code
.claude-plugin/         Claude Code plugin manifest, version 0.5.0
CHANGELOG.md
```

## History

The phase plan, dry runs, and per-release notes are in [docs/history.md](docs/history.md) and [CHANGELOG.md](CHANGELOG.md).

## Out of this pack

- A shipped market-data server, a Screener scraper, or a database of ratios. A broker MCP you connect is `use-mcp`. It is not bundled.
- Price alerts, a stored portfolio history, or order placement. `use-mcp` does not send an order.
- A model portfolio or published recommendations
- Non-India listings, including ADRs of non-Indian issuers, except a one-line refusal
- Crypto, F&O tips, and intraday calls
- A stored history of FII and DII flows, of scheme portfolios, or of deals, or a day's flow, a deal, a bonus, an index change, or a rating symbol treated as a buy or a sell
- Filing PDFs and the user's decision notes. Those stay on the machine. The blank decision template is in the repo.
- Papers saved under `library/`. `library/SOURCES.md` says what was read and what was not downloaded. The PDFs stay on the machine.
- The user's holdings notes. The blank template is in the repo.
- API keys, API secrets, and passwords. The MCP template has no secret field. Personal notes under `mcp/` stay on the machine.

## License

No license file is set. All rights reserved until one is added.
