---
name: indian-investor
description: >
  Routes India-only equity research on NSE and BSE listings and India
  bootstrapped companies. Use when the user asks to analyze, study, or
  compare an Indian company, Indian stock, NSE or BSE name, or wants a
  research memo. Do not use for non-India listings, crypto, F&O tips,
  or intraday calls.
compatibility: >
  Agent Skills hosts (Claude Code, Codex, Cursor, Copilot, Gemini CLI).
  Needs web or file access to read public filings. No market-data API.
---

# Indian investor

Router for this pack. Read `references/scope.md`, `references/sources.md`, `references/memo.md`, and `references/disclaimer.md` before writing. Do not restate each lens here.

## Iron rules

1. India only. NSE, BSE, or an India bootstrapped company. Anything else: stop and say so.
2. Every figure has source, period, and consolidated or standalone. If it is not in a source, write "not found". Do not estimate silently.
3. INR, with crore or lakh stated. Indian fiscal year (April–March) unless the filing says otherwise.
4. Separate fact, inference, and opinion.
5. Promoter holding, pledge, related parties, and auditor notes are part of the analysis.
6. Close with the disclaimer in `references/disclaimer.md`. No buy, sell, or target presented as advice or as a certain outcome.

## Order

1. Scope gate. Name the issuer, NSE or BSE symbol, or private India company. Classify bootstrapped vs VC- or PE-backed. If the name is ambiguous, ask one question and stop.
2. Facts before opinions. Listed: read `../analyze-financials/SKILL.md` and follow it. Private: read `../analyze-bootstrapped/SKILL.md` and follow it. Do not open a persona first.
3. Lenses the user named, and no others. If they named none on a full company memo, use Damani, Buffett, and Munger, and say that is the default set.
   - `../lens-buffett/SKILL.md`
   - `../lens-munger/SKILL.md`
   - `../lens-damani/SKILL.md`
   - `../lens-jhunjhunwala/SKILL.md`
   - `../lens-kedia/SKILL.md`
   - `../lens-agrawal/SKILL.md`
   - `../lens-prasad/SKILL.md`
   - `../lens-bakshi/SKILL.md`
   - `../lens-andrade/SKILL.md`
   The Coffee Can screen is `../screen-coffee-can/SKILL.md`. Load it only when the user asks for that screen. It is not a lens and it is not in the default set.
4. Industry skills only when the user asked about the industry, rivals, or leadership, or a lens test cannot be answered without them.
   - `../analyze-market/SKILL.md`
   - `../analyze-competition/SKILL.md`
   - `../analyze-market-leader/SKILL.md`
   - `../analyze-swot/SKILL.md`
5. Every full memo ends by reading `../critique-thesis/SKILL.md` and applying it to the draft.
6. Do not load a skill you will not use. These load only when the user asks. They are not part of the default company memo.
   - `../analyze-flows/SKILL.md` for FII, FPI, DII, or institutional cash buying and selling, including a calendar net, assets under custody, or a sector file when that page was opened.
   - `../analyze-deals/SKILL.md` for block deals, bulk deals, or SAST or insider disclosures of one company.
   - `../analyze-funds/SKILL.md` for a named scheme's month-end holding.
   - `../analyze-actions/SKILL.md` for a dividend, split, bonus, buyback, or index add or drop.
   - `../analyze-rating/SKILL.md` for a credit-rating symbol or its rationale.

## Conflicts

When two lenses disagree, keep both results under "Where the lenses disagree". Damani is less willing to pay for growth than Jhunjhunwala. Agrawal's price test is not Buffett's owner-earnings bridge. Prasad does not forecast and does not underwrite a turnaround. Andrade marks a high return while leaders add capacity as a cycle. Bakshi's float test is not the owner-earnings bridge. Coffee Can is a decade screen, not QGLP. Do not blend them into a score.

## Compare

When the user asks to compare Indian issuers, follow the Compare section in `references/memo.md`. Run the facts skill for each issuer before any lens.

## Flows

When the user asks about FII, FPI, DII, or institutional cash buying and selling, read `../analyze-flows/SKILL.md` and follow it. Do not load it on a company memo unless they asked. A market flow is not a company fact. A calendar net, assets under custody, and a sector file stay in that skill. They are still market-wide.

## Named only

Flows stay in the section above. These also stay unloaded on a default company memo.

- Block, bulk, SAST, or insider rows: `../analyze-deals/SKILL.md`. A deal is not the promoter percent.
- A named scheme's month-end portfolio: `../analyze-funds/SKILL.md`. A market-wide DII net is not that holding.
- Dividend, split, bonus, buyback, or an index add or drop: `../analyze-actions/SKILL.md`. An action is not a better business.
- A credit-rating symbol or rationale: `../analyze-rating/SKILL.md`. A news line is not the rationale.

## Single questions

A request for one skill ("SWOT only", "Damani only") loads that skill and the facts skill it needs. It does not run the default three lenses. It still uses the iron rules and the disclaimer.
