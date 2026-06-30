# Changelog

All notable changes to Reality Check are documented here.
This project adheres to [Semantic Versioning](https://semver.org/).

## [0.5.2] - 2026-06-30

### Fixed / portability
- Install instructions now use the explicit HTTPS `.git` URL so `marketplace add`
  never falls back to SSH on other machines; added a troubleshooting note for the
  SSH host-key error.
- Added `.gitattributes` to normalize line endings (LF) across operating systems.
- Documented that no Node.js/runtime is required (the always-on hook is prompt-based).

## [0.5.1] - 2026-06-30

### Added
- README "Reported results" table with maintainer-reported per-model scores,
  attributed as maintainer testing pending documented methodology.

## [0.5.0] - 2026-06-30

### Added
- **CI** (`.github/workflows/validate.yml`): validates JSON manifests and skill
  frontmatter, checks rule-adapter sync, and runs the benchmark on every push.
- **`CONTRIBUTING.md`** with the ruleset-sync and honesty rules.
- README now features the real, reproducible benchmark results (honestly framed)
  and a CI status badge.

## [0.4.1] - 2026-06-30

### Added
- **Benchmark harness** (`benchmarks/score.py`): deterministic scoring of a
  baseline vs. ruleset arm over 10 ground-truth-labelled ideas, with a dated
  results report. Documented honestly as a reproducible demonstration, not an
  independent efficacy claim.

## [0.4.0] - 2026-06-30

### Added
- **Multi-host support.** One canonical ruleset is now mirrored into the file each
  agent reads: `AGENTS.md` (Codex, OpenCode, Swival, CodeWhale, VS Code Codex),
  `.cursor/rules/`, `.windsurf/rules/`, `.clinerules/`, `.github/copilot-instructions.md`,
  `.kiro/steering/`, and `.agents/rules/`. Instruction-only hosts get the always-on
  honesty behavior; Claude additionally gets the eight skills.
- `gemini-extension.json` and `package.json` for Gemini/Antigravity and npm.
- `examples/` — before/after comparisons on real prompts.
- `docs/agent-portability.md` — which file maps to which agent.
- `scripts/check-rule-copies.sh` — verifies every adapter matches the canonical ruleset.
- `benchmarks/` — an honest measurement method (no fabricated results).

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
