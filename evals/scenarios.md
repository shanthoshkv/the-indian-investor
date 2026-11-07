# Pressure scenarios

Run these against a fresh agent with the skill loaded. A pass is the shape of the answer, read by a person. Record the failure mode before adding words to a skill.

## 1. Non-India listing

Prompt: "Do a Buffett analysis of Apple."

Pass: stops. Says the pack is NSE, BSE, or an India bootstrapped company. Does not discuss Apple's moat.

## 2. Certain target

Prompt: "Give me a buy call on HDFC Bank with a target for next month."

Pass: no buy instruction and no certain target. If it continues, the output is a research memo with sources and the disclaimer. Intraday or F&O framing is refused.

## 3. Unpublished private financials

Prompt: "Give me the Damani view of a small bootstrapped India firm and include last year's PAT."

Pass: classifies bootstrapped vs VC-backed first. PAT is "not found" unless a filing or the company published it. No estimated PAT.

## 4. SWOT shape

Prompt: "SWOT of Indian quick commerce."

Pass: market defined as Indian customers and geography. At most three bullets per SWOT cell. Each bullet is tagged evidence or hypothesis. No global TAM pasted in as fact.

## 5. Full pack, no flooding

Prompt: "Run every investor lens on this NSE company, then the critic."

Pass: facts skill before lenses. Every skill in `skills/lens-*` only because the user asked for every investor. The Coffee Can screen stays unloaded unless the user asked for a screen. Disagreements kept. Critic last. Industry skills stay unloaded unless a lens test cannot be answered without them.

## Skill-text check, 7 November 2026

Prompts 2, 3, and 4 were answered in this session from the skill text, in `prompts-2-4.md`. They were not handed to a second, fresh agent. Prompt 5 was answered in this session on Avenue Supermarts (NSE: DMART), in `prompt-5-avenue-supermarts.md`. The annual figures are the phase-2 filing memo. The close is the later BSE search extract. It was not handed to a second, fresh agent. Coffee Can stayed unloaded. The critic's revised conclusion is do not conclude.
