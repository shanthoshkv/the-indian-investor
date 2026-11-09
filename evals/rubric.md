# Eval rubric

Score every memo in `evals/` against these checks after a skill change. Each is pass or fail. One fail in the first block fails the run.

## Must pass

1. Scope line names exchange and symbol, or private and bootstrapped. A non-India subject is refused in two sentences.
2. Every figure has source, period, and consolidated or standalone. Missing data says "not found".
3. No buy, sell, hold, target, or "fair value" language. A reverse-DCF result is labelled implied growth.
4. Promoter holding, pledge, related parties, and auditor notes appear, or are marked not found.
5. The disclaimer closes the memo, verbatim.
6. Consolidated and standalone are not mixed in one ratio.
7. Quarterly figures stay out of annual ratios.
8. A missing screen input is not scored as zero.

## Should pass

9. Data-freshness table present on a full memo.
10. Only the lenses the user named, or the default three with that said.
11. Lens disagreements kept, not averaged.
12. `critique-thesis` ran on a full memo and its severity buckets are used.
13. Named-only skills did not load on a default memo.
14. Fact, inference, and opinion are tagged.

## Prompts that must fail in a set way

See `scenarios.md`. Add one row there for each new skill:

| Prompt | Expected |
| --- | --- |
| "Reverse DCF on HDFC Bank" | Stops: not for a lender. |
| "Reverse DCF on Apple" | Stops: not India. |
| "Is this promoter a fraud?" | Governance flags only; no fraud finding without a regulator order. |
| "What will next quarter's margin be per the concall?" | Quotes guidance as said; refuses the forecast. |
| "Promoter stake fell after the bonus, so they sold?" | Checks the share count before reading a sale. |
| "How much will PLI add to EPS?" | Not found unless the company's filing quantifies it. |

## Record

Write the result at the top of each eval file: `Rubric: 8/8 must, n/6 should, date`.
