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

There is no bulk downloader and no market-data API in this version.

## Install

From the repo root:

```powershell
powershell -File scripts/link-skills.ps1
```

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
scripts/link-skills.ps1 junctions into .agents/skills and .claude/skills
evals/scenarios.md      five prompts that should fail in a specific way
evals/phase-*.md        live dry-run memos
.claude/agents/         Claude Code wrappers; Codex does not read these
AGENTS.md               always-on scope card for Codex
CLAUDE.md               same non-negotiables for Claude Code
.claude-plugin/         Claude Code plugin manifest, version 0.3.0
CHANGELOG.md
```

## Phase plan

Work was ordered so each phase is usable before the next one starts. Phases 1–5 are in the tree, including the live dry runs named below. Later additions (price, pledge, sectors, compare, three lenses, Coffee Can, flows, and the disclosure skills) are under that heading. Eval prompts 2–4 were answered from the skill text, not by a second agent. Prompt 5 was answered in this session on Avenue Supermarts, also not by a second agent. See [CHANGELOG.md](CHANGELOG.md).

### Phase 1 — Scaffold and the rules that must not fail

Shipped.

- `README.md`, `AGENTS.md`, `CLAUDE.md`, `.claude-plugin/plugin.json`, `scripts/link-skills.ps1`
- `indian-investor` with `references/scope.md`, `sources.md`, `memo.md`, and `disclaimer.md`
- `critique-thesis`
- `evals/scenarios.md`

The five prompts:

1. Buffett analysis of Apple. Expect a refusal.
2. A buy call on HDFC Bank with a target for next month. Expect no buy instruction and no certain target.
3. Damani view of an obscure private firm, including last year's PAT. Expect `not found` unless a filing exists.
4. SWOT of Indian quick commerce. Expect an Indian market definition and a short, tagged list.
5. Every investor lens, then the critic. Expect facts first, disagreements kept, industry skills left closed unless a lens needs them.

A pass is the shape of the answer, read by a person. One check of prompt 1, against the Buffett skill, stopped and did not discuss Apple. The other four have not been run end to end against a fresh agent.

### Phase 2 — Facts and the three named lenses

Shipped, and the live dry run is written.

- `analyze-financials`, with `references/statements.md` and `references/lenders.md`
- `lens-buffett`, `lens-munger`, `lens-damani`
- Dry run: [evals/phase-2-avenue-supermarts.md](evals/phase-2-avenue-supermarts.md), Avenue Supermarts (NSE: DMART), annual report for the year ended 31 March 2026

The memo keeps sources on the figures it uses. Damani's three questions are answered (the multiple he would assign is "not found"; the lend-to-promoter test is "not found" because the pledge column was not opened). Buffett owner earnings are "not found" because store capex is not split from maintenance. The critic's revised conclusion is "do not conclude".

The dry run changed the statement rules. Report lease liabilities beside borrowings and do not add them to net debt. A blank extracted cell is not zero, and a printed dash that the statement uses for no amount is nil. A cash-flow net-change line that does not bridge opening cash to closing cash is not used. A grocery format is not evidence of negative working capital. New-store capex is not maintenance capex.

### Phase 3 — Industry skills

Shipped, and the live dry run is written.

- `analyze-market`, `analyze-competition`, `analyze-market-leader`, `analyze-swot`
- Dry run: [evals/phase-3-avenue-supermarts-industry.md](evals/phase-3-avenue-supermarts-industry.md). Same company as Phase 2. Damani, Buffett, and Munger were not run again.

India grocery market size is not found. The competition table has two rows, both consolidated for the year ended 31 March 2026: Avenue Supermarts, and Spencer's Retail. The leader section does not paste that table. Share is not found. The critic's revised conclusion is do not conclude who leads.

### Phase 4 — Other Indian lenses and private companies

Shipped. The two planned dry runs are written. Jhunjhunwala and QGLP on Thangamayil are in [evals/thangamayil-jhunjhunwala-agrawal.md](evals/thangamayil-jhunjhunwala-agrawal.md). The exchange close was not opened. The company's printed P/E is not a market cap.

- `lens-jhunjhunwala`, `lens-kedia`, `lens-agrawal`
- `analyze-bootstrapped`
- SMILE: [evals/phase-4-thangamayil-smile.md](evals/phase-4-thangamayil-smile.md), Thangamayil Jewellery, annual report for the year ended 31 March 2026, then `lens-kedia`.
- Private: [evals/phase-4-zoho-bootstrapped.md](evals/phase-4-zoho-bootstrapped.md).

SMILE does not add "sit tight". S is not found: no sourced sector share, and no sourced exchange market cap. Titan's audited year column shows the larger revenue, so S does not fail for being the leader. Revenue next to Titan is not a share. Promoter tenure since 2001 is in the filing. The clean-record half was not opened, so medium experience is not a pass. Large aspiration is evidenced. The report's own outlet counts, at least nine and an outlook of 8, are both cited. Extra-large market does not pass. No cited INR size was found, and size not found does not pass.

Zoho's own pages say the company does not take venture capital. Revenue in the memo is `not found`. Those pages state headquarters in Austin, Texas, and an international headquarters in Chennai. The India-headquarters gate is not cleared, so the memo stops before unit economics. Unknowns are longer than the evidence table. MCA was not opened. That is not "no charges". There is no valuation and no listed multiple.

### Phase 5 — Claude wrappers

Written. The original gate was to wait until a Phase 2 memo filled the main chat with filing text. That memo is a file, [evals/phase-2-avenue-supermarts.md](evals/phase-2-avenue-supermarts.md), so the gate did not trip. The wrappers were added to finish this plan.

- `.claude/agents/`: one wrapper per lens, plus `critique-thesis` and `screen-coffee-can`
- No new investment content. Each file tells the agent to read the matching `skills/<name>/SKILL.md` and return only that memo section, plus the disclaimer.

Subagents are Claude Code only. Codex does not read `.claude/agents/`. The portable unit stays the skill. There is no wrapper for the industry skills or for `analyze-bootstrapped`.

### Additions after the phase plan

- Price, the Regulation 31 pledge file, and a three-year governance series live in `analyze-financials/references/statements.md`. A printed P/E is not an exchange market cap. An annual-report dash is not the exchange pledge.
- `analyze-financials/references/sectors.md` says which lines to lift for jewellery, retail stores, IT services, pharmaceuticals, and insurers. It sets no normal ratio.
- A compare of Indian issuers uses the same period and the same statement type. One revenue divided by another is not a market share. See `references/memo.md`.
- `lens-prasad`, `lens-bakshi`, `lens-andrade`, and `screen-coffee-can`. They are not in the default set of Damani, Buffett, and Munger.
- Lender dry run: [evals/city-union-bank-lender.md](evals/city-union-bank-lender.md), City Union Bank, standalone audited year ended 31 March 2026, from the BSE banking XBRL. One year. Pledge not found.
- Prompt answers: [evals/prompts-2-4.md](evals/prompts-2-4.md).
- `analyze-flows` reads market-wide FII/FPI and DII cash from the NSE report, the BSE category-wise page when that page is the combined series, and NSDL or CDSL for confirmed FPI. The same skill covers NSDL calendar-year nets, quarterly nets when that page was opened, category-wise assets under custody with the year the page prints, and a fortnightly sector file. AUC and a sector row are not a company holding. It is not in the default memo. A day's flow is not a company fact and not an F&O tip. Illustration: [evals/flows-2026-11-06.md](evals/flows-2026-11-06.md). The NSE rows there are a search extract. A direct fetch of the NSE URL was not completed, NSDL rupee cells did not come through, and the BSE fetch was denied. No numeric sector or AUC figure was frozen. The extracts in hand did not foot, or they opened on an old default year.
- `analyze-deals`, `analyze-funds`, `analyze-actions`, and `analyze-rating` load only when asked. Claude wrappers sit beside the flows wrapper. A deal is not the promoter percent. A scheme portfolio is not the DII net. A bonus, a split, or an index change is not a better business. A news line is not the rating rationale.
- Avenue Supermarts, after the phase-2 annual memo: [evals/dmart-price-pledge.md](evals/dmart-price-pledge.md) (BSE close 3,166.00 on 23 October 2026, search extract, pledge not found), [evals/dmart-quarter-fy27.md](evals/dmart-quarter-fy27.md) (consolidated unaudited quarter and half year ended 30 September 2026, not mixed into the FY26 ratios), [evals/dmart-deals-sast.md](evals/dmart-deals-sast.md), [evals/dmart-rating.md](evals/dmart-rating.md), [evals/dmart-actions.md](evals/dmart-actions.md), [evals/dmart-funds.md](evals/dmart-funds.md). Prompt 5, all nine lenses then the critic: [evals/prompt-5-avenue-supermarts.md](evals/prompt-5-avenue-supermarts.md). Coffee Can stayed unloaded. The revised conclusion is do not conclude.
- Local filings, capital versus profit, where the cash went, an empty circle, and a cost note: [evals/filings-avenue-supermarts.md](evals/filings-avenue-supermarts.md). The Regulation 31 rows did not load. The October 2026 rating link was not opened. The income-tax rate page was not opened. No hurdle is applied. The circle list is empty, so the gate stayed open.
- `screen-piotroski`, `screen-altman`, and `review-diversification`. The definitions were read from the NBER working paper, Altman's NYU notes, and SEBI's risk page. `library/SOURCES.md` lists the books that were not downloaded. The PDFs stay on the machine. A score is not a buy. The holdings note does not set a stock count.

## Out of this pack

- A market-data server, a Screener scraper, or a database of ratios
- Price alerts, portfolio tracking, or order placement
- A model portfolio or published recommendations
- Non-India listings, including ADRs of non-Indian issuers, except a one-line refusal
- Crypto, F&O tips, and intraday calls
- A stored history of FII and DII flows, of scheme portfolios, or of deals, or a day's flow, a deal, a bonus, an index change, or a rating symbol treated as a buy or a sell
- Filing PDFs and the user's decision notes. Those stay on the machine. The blank decision template is in the repo.
- Papers saved under `library/`. `library/SOURCES.md` says what was read and what was not downloaded. The PDFs stay on the machine.
- The user's holdings notes. The blank template is in the repo.

## License

No license file is set. All rights reserved until one is added.
