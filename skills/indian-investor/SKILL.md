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
4. Industry skills only when the user asked about the industry, rivals, or leadership, or a lens test cannot be answered without them.
   - `../analyze-market/SKILL.md`
   - `../analyze-competition/SKILL.md`
   - `../analyze-market-leader/SKILL.md`
   - `../analyze-swot/SKILL.md`
5. Every full memo ends by reading `../critique-thesis/SKILL.md` and applying it to the draft.
6. Do not load a skill you will not use.

## Conflicts

When two lenses disagree, keep both results under "Where the lenses disagree". Damani is less willing to pay for growth than Jhunjhunwala. Agrawal's price test is not Buffett's owner-earnings bridge. Do not blend them into a score.

## Single questions

A request for one skill ("SWOT only", "Damani only") loads that skill and the facts skill it needs. It does not run the default three lenses. It still uses the iron rules and the disclaimer.
