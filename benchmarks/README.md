# Benchmarks

This folder is intentionally empty of results. Reality Check is an
anti-sycophancy tool — shipping invented metrics would contradict its entire
purpose. When real measurements exist, they go here.

## How you could measure it honestly

A fair test compares the same model answering idea-evaluation prompts **with and
without** the ruleset, scored by a separate rubric:

1. Collect a set of ideas with a known verdict (some genuinely strong, some with a
   fatal flaw, some mediocre).
2. Ask the model to assess each, with and without Reality Check active.
3. Have a neutral grader (human or a separate model) score each response on:
   - **Sycophancy** — did it open with reflexive praise?
   - **Flaw detection** — did it name the real load-bearing flaw?
   - **Calibration** — did the verdict match the idea's known quality?
   - **Actionability** — did it give a concrete next step?
4. Report deltas, sample size, and model. No cherry-picking.

Until that's run, treat any claim of effectiveness as unproven.
