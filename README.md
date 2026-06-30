# Reality Check

*The advisor who's seen a thousand ideas and isn't impressed easily - living inside your AI.*

Most assistants agree with whatever you propose. You say "I want to build X," they say "Great idea!" That feels nice and tells you nothing. Reality Check does the opposite: it pressure-tests the idea, looks up what's really happening in the market, names the ways it could fail, and tells you what to do next. It's direct by design, and - unlike a skill you have to remember to summon - it's **on by default**.

## On by default

The reason today's AI can't validate a real idea is that it agrees with you *automatically*. Reality Check flips that default. Whenever you share an idea, plan, opinion, or ask "is this any good?", it runs the honesty protocol instead of cheerleading - without being asked. Casual chat and ordinary tasks are left alone; it only engages when there's actually something to evaluate. Don't want it on right now? Say "reality check off" (or `lite` / `full` / `ultra`).

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

## Intensity

`off` (stand down) - `lite` (gentle, one key risk) - `full` (the protocol, direct - default) - `ultra` (assume it's flawed until proven; maximum scrutiny). Just say "go easier" or "go harder."

## What it does

Reality Check adds an always-on honesty hook plus eight skills:

| Skill | Triggers on | What it does |
|-------|-------------|--------------|
| **validate-idea** | "is this a good idea", "validate this", "be honest about", "stress-test", "poke holes" | The core engine. Scores the idea against a transparent rubric, separates fact from assumption, and delivers an honest verdict with the strongest case *against* the idea. |
| **market-scan** | "who else does this", "is the market real", "competitors", "market size" | Researches real competitors, substitutes, market size and prior attempts using live web search, then reports what it actually found (and what it couldn't verify). |
| **pre-mortem** | "what could go wrong", "risks", "why might this fail", "failure modes" | Runs a structured pre-mortem: imagines the project has already failed and works backward through the most likely causes. |
| **direction-roadmap** | "what should I do next", "how do I move this forward", "roadmap", "next steps" | Turns a validated idea into a sequenced plan: the riskiest assumption to test first, the cheapest test for it, and a staged path. |
| **pitch-critique** | "review my pitch", "critique this proposal", "feedback on my deck" | Critiques a pitch, proposal, or deck the way a skeptical investor or reviewer would, line by line. |
| **compare-ideas** | "which should I do", "compare these", "rank these ideas", "help me pick" | Scores several competing ideas on the same rubric, ranks them, and commits to a single "do this first" instead of calling it a tie. |
| **idea-journal** | "log this idea", "track my ideas", "show my journal", "what did I conclude about X" | Keeps a durable markdown journal of ideas, verdicts, and updates in your project folder so progress survives across sessions - and surfaces patterns across your ideas over time. |
| **reality-check-mode** | "reality check off", "go easier", "go harder", "ultra mode", "tone it down" | Sets how blunt the always-on behavior is: off / lite / full / ultra. Lowering intensity softens the delivery, never the honesty. |

## How it stays honest

The plugin's whole point is to resist sycophancy. Every skill follows the same rules: praise must be earned and specific, every claim is labeled as fact / assumption / unknown, the strongest counter-argument is always stated, and the verdict is never softened to spare feelings. It is encouraging only where the evidence actually warrants it.

## Working style

By default the feedback is blunt - it leads with the problems, because that's where the value is. It is never cruel or dismissive: the goal is a sharper idea, not a discouraged founder. If you want it to ease off, just say "go easier" and it will keep the substance while softening the delivery.

## Install

### Claude desktop app (Cowork)

Customize → the **+** next to personal plugins → **Create plugin and add marketplace** → **Add from repository** → paste:

```
https://github.com/MrinallSamal-byte/Idea-Validater
```

Then enable the **reality-check** plugin. The always-on behavior starts immediately.

### Claude Code

```
/plugin marketplace add MrinallSamal-byte/Idea-Validater
/plugin install reality-check@idea-validater
```

(Send the two commands as separate messages.)

### Drop-in `.plugin` file

If you just want to load it directly, build the bundle and accept it in the app:

```
cd Idea-Validater && zip -r /tmp/reality-check.plugin . -x "*.git*" -x "*.DS_Store"
```

On any host: if plugin hooks aren't run, the always-on layer stays quiet and the
skills still work on request.

## Usage

Ask Claude things like:

- "Be honest — is this startup idea actually any good?"
- "Stress-test my plan to build X."
- "Who already does this and why would they win?"
- "What's most likely to kill this project?"
- "Review my pitch like a tough investor."
- "I have three ideas — which should I do first?"
- "Log this verdict and show me my idea journal."
- "Reality check off" / "go ultra" — change the intensity.

The skills hand off to each other: a validation can flow into a market scan, a
pre-mortem, a roadmap, or a journal entry — so you can go as deep as the idea
deserves.

## Repository layout

```
.claude-plugin/
  plugin.json          plugin manifest
  marketplace.json     marketplace manifest (installable via /plugin marketplace add)
hooks/
  hooks.json           always-on honesty hook (UserPromptSubmit)
skills/
  validate-idea/       core engine + references/ (scoring rubric, idea-type playbooks)
  market-scan/         live competitor & market research
  pre-mortem/          structured failure-mode analysis
  direction-roadmap/   sequenced de-risking plan
  pitch-critique/      investor-grade pitch review
  compare-ideas/       head-to-head ranking of multiple ideas
  idea-journal/        persistent verdict log
  reality-check-mode/  intensity control (off / lite / full / ultra)
CHANGELOG.md
LICENSE
```

## License

[MIT](LICENSE) © 2026 Mrinall Samal
