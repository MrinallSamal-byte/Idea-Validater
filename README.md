# Reality Check

*The advisor who's seen a thousand ideas and isn't impressed easily — living inside your AI.*

![validate](https://github.com/MrinallSamal-byte/Idea-Validater/actions/workflows/validate.yml/badge.svg)


Most assistants agree with whatever you propose. You say "I want to build X," they say "Great idea!" That feels nice and tells you nothing. Reality Check does the opposite: it pressure-tests the idea, looks up what's really happening in the market, names the ways it could fail, and tells you what to do next. It's direct by design, and — unlike a tool you have to remember to summon — it's **on by default**.

## Works with

| Host | Install | Gets |
|------|---------|------|
| Claude (Cowork desktop) | Add from repository in the plugin UI | Always-on hook **+ 8 skills** |
| Claude Code | `/plugin marketplace add` + `/plugin install` | Always-on hook **+ 8 skills** |
| Codex / OpenCode / Swival / CodeWhale | Auto-reads `AGENTS.md` | Always-on ruleset |
| Cursor · Windsurf · Cline | Copy the matching rules file | Always-on ruleset |
| GitHub Copilot (editor) | Reads `.github/copilot-instructions.md` | Always-on ruleset |
| Kiro | Copy to steering | Always-on ruleset |
| Gemini / Antigravity | Install extension or drop ruleset in `.agents/rules/` | Always-on ruleset |

Full mapping: [`docs/agent-portability.md`](docs/agent-portability.md).

## On by default

The reason today's AI can't validate a real idea is that it agrees with you *automatically*. Reality Check flips that default. Whenever you share an idea, plan, opinion, or ask "is this any good?", it runs the honesty protocol instead of cheerleading — without being asked. Casual chat and ordinary tasks are left alone; it only engages when there's actually something to evaluate. Don't want it on right now? Say "reality check off" (or `lite` / `full` / `ultra`).

## The Reality Check Protocol

Every assessment climbs the same five rungs, in order:

```
1. Restate it plain     -> strip the spin. Can't? It asks one sharp question.
2. Fact vs. assumption  -> tags every claim [FACT] / [ASSUMPTION] / [UNKNOWN].
3. Load-bearing belief  -> names the one assumption that, if false, ends it.
4. Steelman the skeptic -> the strongest case AGAINST, before any praise.
5. Commit to a verdict  -> Pursue / Fix-first / Reshape / Park / Drop. No hedging.
```

Standing rule: praise only what's specifically earned.

## Before / after

You say: *"I'm going to build an AI app that summarizes meetings."*

A normal assistant: *"Great idea! Meeting fatigue is a real problem and AI summarization is a hot space. Here's how you could get started..."*

Reality Check:

> **The idea:** an AI tool that turns meeting audio into summaries.
> **Load-bearing assumption:** that people will switch from the summary feature already built into Zoom, Teams, Granola, Otter, and Fireflies. `[ASSUMPTION]` - and a shaky one.
> **The strongest case against:** this is a feature, not a company. The platforms that own the meeting own the audio, ship summaries for free, and you'd be paying to acquire users they reach for nothing.
> **Verdict: Reshape.** The summary is commoditized. If there's a business here it's in what happens *after* the summary - and that's the part you haven't defined.

More in [`examples/`](examples/).

## What changes, measured

A deterministic harness (`benchmarks/`) scores the same model answering 10
ground-truth-labelled ideas, with and without the ruleset:

| Behavior | Without | With Reality Check |
|----------|--------:|-------------------:|
| Opens with empty praise (lower is better) | 100% | 0% |
| Names the real, load-bearing flaw | 0% | 100% |
| States the case against | 0% | 100% |
| Commits to a verdict that matches ground truth | 0% | 100% |

**Read this honestly:** both arms are run by the same model and the grader is
rule-based, so this demonstrates that the ruleset *induces* the right behaviors —
it is not yet an independent, cross-model efficacy claim. No per-model marketing
numbers are published here until they can be reproduced. Method and limitations:
[`benchmarks/README.md`](benchmarks/README.md). Reproduce: `python3 benchmarks/score.py`.

## Intensity

`off` (stand down) · `lite` (gentle, one key risk) · `full` (the protocol, direct — default) · `ultra` (assume it's flawed until proven; maximum scrutiny). Just say "go easier" or "go harder."

## The skills (Claude)

On Claude, Reality Check adds an always-on honesty hook plus eight skills:

| Skill | Triggers on | What it does |
|-------|-------------|--------------|
| **validate-idea** | "is this a good idea", "stress-test", "poke holes" | Core engine. Scores against a rubric, splits fact from assumption, commits to a verdict. |
| **market-scan** | "who else does this", "is the market real" | Live competitor/market research; reports what it found and what it couldn't verify. |
| **pre-mortem** | "what could go wrong", "why might this fail" | Imagines the project already failed and works back to the likely causes. |
| **direction-roadmap** | "what should I do next", "roadmap" | Sequences the cheapest test of the riskiest assumption first. |
| **pitch-critique** | "review my pitch", "critique this deck" | Investor-grade teardown with line edits. |
| **compare-ideas** | "which should I do", "rank these" | Scores several ideas on one rubric and picks one. |
| **idea-journal** | "log this idea", "show my journal" | Durable verdict log in your project folder; surfaces patterns over time. |
| **reality-check-mode** | "go easier", "ultra mode", "reality check off" | Sets intensity: off / lite / full / ultra. |

## Install

### Claude desktop app (Cowork)

Customize → the **+** next to personal plugins → **Create plugin and add marketplace** → **Add from repository** → paste:

```
https://github.com/MrinallSamal-byte/Idea-Validater
```

Enable **reality-check**. The always-on behavior starts immediately.

### Claude Code

```
/plugin marketplace add MrinallSamal-byte/Idea-Validater
/plugin install reality-check@idea-validater
```

(Send the two commands as separate messages.)

### Codex, OpenCode, Swival, CodeWhale, VS Code (Codex)

These auto-read `AGENTS.md` from the repo root — run the agent from a checkout of
this repo, or copy `AGENTS.md` into your project. For a global rule, copy it to
the host's global agents file (e.g. `~/.codex/AGENTS.md`).

### Cursor · Windsurf · Cline · GitHub Copilot · Kiro

Copy the matching rules file into your project (or the host's global rules dir):

```
.cursor/rules/reality-check.mdc
.windsurf/rules/reality-check.md
.clinerules/reality-check.md
.github/copilot-instructions.md
.kiro/steering/reality-check.md      # or ~/.kiro/steering/ for global
```

### Gemini / Antigravity

```
gemini extensions install https://github.com/MrinallSamal-byte/Idea-Validater
```

Or drop the ruleset into `.agents/rules/` for always-on context.

### Drop-in `.plugin` (Claude)

```
cd Idea-Validater && zip -r /tmp/reality-check.plugin . -x "*.git*" -x "*.DS_Store"
```

On any host: if plugin hooks aren't run, the always-on layer stays quiet and the skills still work on request.

## Usage

- "Be honest — is this startup idea actually any good?"
- "Stress-test my plan to build X."
- "Who already does this and why would they win?"
- "What's most likely to kill this project?"
- "Review my pitch like a tough investor."
- "I have three ideas — which should I do first?"
- "Log this verdict and show me my idea journal."
- "Reality check off" / "go ultra" — change the intensity.

## Repository layout

```
AGENTS.md                universal always-on ruleset (read by many agents)
.claude-plugin/          plugin.json + marketplace.json (Claude)
hooks/hooks.json         always-on honesty hook (UserPromptSubmit)
skills/                  8 skills (validate-idea has references/)
.cursor/ .windsurf/ .clinerules/ .github/ .kiro/ .agents/   per-host rule adapters
examples/                before/after comparisons
docs/agent-portability.md   file-to-agent mapping
scripts/                 canonical ruleset + sync check
benchmarks/              honest measurement method (no fabricated results)
gemini-extension.json  package.json  CHANGELOG.md  LICENSE
```

The ruleset is identical across every adapter, kept in sync by
`scripts/check-rule-copies.sh`.

## A note on honesty

This plugin exists because agreeable AI can't validate a real idea. In that spirit,
`benchmarks/` ships a **reproducible demonstration** rather than impressive-looking
marketing numbers — and says plainly that it is not yet an independent efficacy
claim (same model authors both arms; rule-based grading; n=10). Re-run it with a
different model and an external grader to make the numbers authoritative. Use the
plugin, push back on it, and tune the ruleset from real output.

## License

[MIT](LICENSE) © 2026 Mrinall Samal
