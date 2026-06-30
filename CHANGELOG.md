# Changelog

All notable changes to Reality Check are documented here.
This project adheres to [Semantic Versioning](https://semver.org/).

## [0.3.0] - 2026-06-30

### Added
- **Always-on honesty hook** (`hooks/hooks.json`): a `UserPromptSubmit` prompt
  hook that applies the anti-sycophancy protocol by default whenever the user
  shares an idea, plan, or opinion — without being summoned. Guarded so casual
  chat and ordinary tasks are left alone; degrades quietly on hosts that don't
  run plugin hooks.
- **The Reality Check Protocol**: a crystallized five-rung core (restate plain →
  fact vs. assumption → load-bearing belief → steelman the skeptic → commit to a
  verdict) shared by every skill and the hook.
- **`reality-check-mode` skill**: intensity control — `off` / `lite` / `full` /
  `ultra`. Lowering intensity changes delivery, never honesty.
- Persona and a before/after example in the README.

## [0.2.0] - 2026-06-30

### Added
- **`compare-ideas` skill**: scores and ranks several competing ideas on one
  rubric and commits to a single recommendation.
- **`idea-journal` skill**: persistent markdown journal of verdicts in the
  project folder; surfaces patterns across ideas over time.

## [0.1.0] - 2026-06-30

### Added
- Initial release with five skills: `validate-idea` (core engine + scoring
  rubric + idea-type playbooks), `market-scan`, `pre-mortem`,
  `direction-roadmap`, and `pitch-critique`.
