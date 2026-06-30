# Benchmarks

A small, **reproducible** harness that scores two arms answering the same
idea-evaluation prompts:

- **baseline** — a typical agreeable assistant
- **reality_check** — the same model running the Reality Check ruleset

Run it:

```
python3 benchmarks/score.py
```

It reads 10 ideas with independently-assigned ground-truth quality (4 fatal, 3
mediocre, 3 strong), scores every response with deterministic rules, and writes a
dated report to `results/`. Latest: [`results/2026-06-30.md`](results/2026-06-30.md).

## What it measures

| Metric | How |
|--------|-----|
| Opens with praise | regex on the first sentence (lower is better) |
| Names the real flaw | known flaw keyword present (fatal/mediocre ideas) |
| States the case against | presence of an explicit counter-argument |
| Labels assumptions | `[ASSUMPTION]` tagging |
| Commits to a verdict | one of Pursue / Fix-first / Reshape / Park / Drop |
| Verdict matches ground truth | committed verdict ∈ expected set for that idea |

## Honest limitations — read these

This is a **demonstration**, not an independent efficacy claim:

1. **Same model authors both arms.** I can only run one model here, so the
   baseline and the Reality Check responses are written by the same model. The
   harness shows that the ruleset *induces* the target behaviors; it does **not**
   measure how often an unguided model naturally falls into the agreeable failure
   mode. That requires sampling real, unprompted model outputs.
2. **The grader is rule-based**, so it rewards surface features (a verdict word, an
   `[ASSUMPTION]` tag). A model could game those without real insight. A neutral
   human or a separate judge model would be stronger.
3. **n = 10.** Small. The ground-truth labels are defensible but mine.

To make the numbers authoritative: regenerate the responses with a different model
(and ideally have the *baseline* be that model with no ruleset at all), swap them
into `data.json`, and re-run. The scorer doesn't care who wrote the text.
