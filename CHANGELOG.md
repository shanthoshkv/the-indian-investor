# Changelog

All notable changes to this skill pack are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Version numbers follow the manifest in `.claude-plugin/plugin.json`.

## [Unreleased]

### Added

- `read-filings`. A file under `filings/<issuer>/` is read before the exchange. The shapes come from Avenue Supermarts files opened on this machine: the FY26 annual report, the quarter ended 30 September 2026 inline XBRL, the 10 October 2026 board PDF, the NSE shareholding-page shell, and the ICRA rationale dated 5 January 2026. Column XIV was on the page. The company rows were not. The October 2026 rating link was not opened. The PDFs stay gitignored.
- `review-decision` and `decisions/TEMPLATE.md`. The user writes what they did. A later reread checks only that list against the next annual report. Claude wrapper in `.claude/agents/review-decision.md`.
- Capital versus profit, and where the cash went, in `analyze-financials/references/statements.md`. Computed. No hurdle. A commitment is not cash spent. A quotation of the buy-back regulations is not a buyback.
- `diff-results`. The new quarter against the last memo's "what would change the conclusion" list. The quarter stays out of the annual ratios. Claude wrapper in `.claude/agents/diff-results.md`.
- `skills/indian-investor/references/circle.md`. An empty list leaves the gate open and the memo says the circle is not filled. A filled list stops a company outside it.
- `note-costs`. Brokerage, delivery STT, and holding-period tax only from a page opened. Claude wrapper in `.claude/agents/note-costs.md`.
- Avenue Supermarts from the files that opened, in `evals/filings-avenue-supermarts.md`. Pledge is not found. The income-tax rate is not found. No hurdle. Circle not filled.

### Changed

- The router, source order, memo contract, critic checklist, and `analyze-financials` point at those methods.
- `filings/` and personal files under `decisions/` stay gitignored. `decisions/TEMPLATE.md` stays in the repo.

## [0.2.0] - 2026-11-07

### Added

- Phase 2 dry run on Avenue Supermarts (NSE: DMART) for the year ended 31 March 2026, in `evals/phase-2-avenue-supermarts.md`.
- Phase 3 industry dry run on the same company, in `evals/phase-3-avenue-supermarts-industry.md`. Market size is not found. The table has two listed rows. The leader section does not paste that table. Share is not found. The critic says do not conclude who leads.
- Phase 4 SMILE dry run on Thangamayil Jewellery for the year ended 31 March 2026, in `evals/phase-4-thangamayil-smile.md`. "Sit tight" is not added.
- Phase 4 bootstrapped dry run on Zoho, in `evals/phase-4-zoho-bootstrapped.md`. Revenue is not found. Austin and Chennai are both stated. The India-headquarters gate is not cleared.
- Claude Code wrappers in `.claude/agents/` for the lenses, `critique-thesis`, and `screen-coffee-can`. Each reads the matching skill and adds no investment test. The original wait, until a Phase 2 memo filled the chat, did not trip: that memo is a file. Codex does not read these files.
- Price, Regulation 31 pledge, and a governance series in `analyze-financials`. Sector line notes for jewellery, retail stores, IT services, pharmaceuticals, and insurers. A compare section in the memo contract.
- `lens-prasad`, `lens-bakshi`, `lens-andrade`, and `screen-coffee-can`. None is in the default lens set.
- Jhunjhunwala and QGLP on Thangamayil Jewellery, in `evals/thangamayil-jhunjhunwala-agrawal.md`. The exchange close was not opened.
- Lender dry run on City Union Bank for the year ended 31 March 2026, in `evals/city-union-bank-lender.md`.
- Skill-text answers to eval prompts 2–4, in `evals/prompts-2-4.md`. Not a second agent.
- `analyze-flows`, for market-wide FII/FPI and DII cash. NSE-only and the NSE+BSE+MSEI series stay apart. NSDL and CDSL are the confirmed FPI pages. Not in the default memo. Not an F&O tip. Claude wrapper in `.claude/agents/analyze-flows.md`. Illustration for 6 November 2026 in `evals/flows-2026-11-06.md`: NSE rows from a search extract, NSDL amounts not found, BSE fetch denied.
- The same flows skill now also reads NSDL calendar-year nets, quarterly nets when that page was opened, category-wise assets under custody with a printed year or as-on date, and a fortnightly sector file. A pilot host is named if that is the file opened. No numeric sector or AUC eval was frozen.
- `analyze-deals`, `analyze-funds`, `analyze-actions`, and `analyze-rating`. Named only. Claude wrappers in `.claude/agents/`. A deal is not the promoter percent. A scheme portfolio is not the market-wide DII net. A bonus or an index change is not a better business. A news line is not the rationale.
- Avenue Supermarts price and pledge in `evals/dmart-price-pledge.md`. BSE close 3,166.00 on 23 October 2026 is a search extract. Direct fetch was not completed. NSE was not opened. The page's printed market cap was not replaced by shares times the close. Regulation 31 was not opened, so pledge stays not found.
- Quarter and half year ended 30 September 2026 in `evals/dmart-quarter-fy27.md`. Consolidated and unaudited, from an XBRL search extract. The limited-review label is the board letter. Direct fetches were denied. Not mixed into the FY26 ratios.
- SAST rows, rating rows with the rationale unopened, corporate actions with the exchange page unopened, and an AMFI index with no scheme line: `evals/dmart-deals-sast.md`, `evals/dmart-rating.md`, `evals/dmart-actions.md`, `evals/dmart-funds.md`.
- Eval prompt 5 on Avenue Supermarts, in `evals/prompt-5-avenue-supermarts.md`. All nine `lens-*` skills, then the critic. Coffee Can stayed unloaded. Answered in this session from the phase-2 filing memo plus the pages named there. Not a second agent. Revised conclusion: do not conclude.

### Changed

- `analyze-financials` now requires lease liabilities beside borrowings, treats a printed dash as nil and a blank extracted cell as not found, drops a cash-flow net-change line that does not bridge, and refuses to infer negative working capital from a grocery format.
- `lens-damani` and `lens-buffett` carry the same two limits: grocery is not evidence of negative working capital, and new-store capex is not maintenance capex.

## [0.1.0] - 2026-11-06

### Added

- Router skill `indian-investor`, with scope, source order, memo contract, and disclaimer.
- Critic skill `critique-thesis`.
- Listed-company skill `analyze-financials`, including a separate lenders note for banks and NBFCs.
- Industry skills: `analyze-market`, `analyze-competition`, `analyze-market-leader`, `analyze-swot`.
- Investor lenses: Buffett, Munger, Damani, Jhunjhunwala, Kedia (SMILE), and Agrawal (QGLP).
- Private-company skill `analyze-bootstrapped`, which stops when the company is mainly VC- or PE-funded.
- `scripts/link-skills.ps1`, so Claude Code and Codex read the same `skills/` folders.
- `evals/scenarios.md` with five pressure prompts.
- `AGENTS.md` and `CLAUDE.md` for the India-only rules.

[0.2.0]: https://github.com/shanthoshkv/the-indian-investor/releases/tag/v0.2.0
[0.1.0]: https://github.com/shanthoshkv/the-indian-investor/releases/tag/v0.1.0
