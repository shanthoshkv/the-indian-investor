# Changelog

All notable changes to this skill pack are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Version numbers follow the manifest in `.claude-plugin/plugin.json`.

## [Unreleased]

### Not in 0.1.0 yet

- Live dry runs from the phase plan: one large NSE or BSE name, an industry-only pass on that name, one smaller listed name, and one private bootstrapped name.
- Phase 5 Claude Code subagent wrappers under `.claude/agents/`. Those wait until a real memo shows the main chat filling up.
- A Coffee Can screen, and any investor whose public method is still too thin to write without inventing a checklist.

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

[0.1.0]: https://github.com/shanthoshkv/the-indian-investor/releases/tag/v0.1.0
