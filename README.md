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

Lenses disagree on purpose. Damani is less willing to pay for growth than Jhunjhunwala. Agrawal's price test is not Buffett's owner-earnings bridge. The memo keeps both results.

People considered and left out, because a public checklist was too thin to write without inventing one: Ashish Kacholia, Nemish Shah, Dolly Khanna, Porinju Veliyath, Ramesh Damani, Utpal Sheth. Chandrakant Sampat's "simple, little debt, free cash flow, low capex" test sits inside `lens-damani`. Coffee Can is a screen, not a temperament, and it is not in this version.

## Rules the agent must keep

1. India only. NSE, BSE, or an India bootstrapped company. Anything else stops.
2. Every figure has a source, a period, and consolidated or standalone. Missing data is `not found`.
3. INR, with crore or lakh stated. Fiscal year is April–March unless the filing says otherwise.
4. Fact, inference, and opinion stay separate.
5. Promoter holding, pledge, related parties, and auditor notes are part of a listed-company analysis.
6. The disclaimer closes every full memo. No buy, sell, or certain target.

Source order, in `skills/indian-investor/references/sources.md`:

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
AGENTS.md               always-on scope card for Codex
CLAUDE.md               same non-negotiables for Claude Code
.claude-plugin/         Claude Code plugin manifest, version 0.1.0
CHANGELOG.md
```

## Phase plan

Work was ordered so each phase is usable before the next one starts. Phases 1–4 are in the tree at 0.1.0. The live company dry runs, and Phase 5, are still open. See [CHANGELOG.md](CHANGELOG.md).

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

Shipped as files. The live dry run is not done.

- `analyze-financials`, with `references/statements.md` and `references/lenders.md`
- `lens-buffett`, `lens-munger`, `lens-damani`

Still to do: one dry run on a single large listed name with an annual report available. Check that sources are present, Damani's three questions are answered, Buffett's maintenance-capex assumption is written down, and the critic finds a real weakness or says the memo survived.

### Phase 3 — Industry skills

Shipped as files. The live dry run is not done.

- `analyze-market`, `analyze-competition`, `analyze-market-leader`, `analyze-swot`

Still to do: an industry-only pass on the same company. The leader skill must not paste the competition table.

### Phase 4 — Other Indian lenses and private companies

Shipped as files. The live dry runs are not done.

- `lens-jhunjhunwala`, `lens-kedia`, `lens-agrawal`
- `analyze-bootstrapped`

Still to do: one smaller listed name through SMILE, and one private bootstrapped name. The private run must contain `not found` where revenue was never published.

### Phase 5 — Claude wrappers, only if a real memo floods the chat

Not started.

- `.claude/agents/*.md`, one thin wrapper per lens and one for the critic
- No new investment content in those files. Each wrapper reads the matching skill and returns that memo section.

Subagents are Claude Code only. Codex does not read `.claude/agents/`. The portable unit stays the skill. Phase 5 waits until a Phase 2 memo shows the main conversation filling up with filing text.

## Out of this pack

- A market-data server, a Screener scraper, or a database of ratios
- Price alerts, portfolio tracking, or order placement
- A model portfolio or published recommendations
- Non-India listings, including ADRs of non-Indian issuers, except a one-line refusal
- Crypto, F&O tips, and intraday calls

## License

No license file is set. All rights reserved until one is added.
