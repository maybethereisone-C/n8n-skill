# Agent Prompting — Reactive Prompting methodology

> Companion to `agent-craft.md`. That file decides *whether and what* to build; this is *how to write the system prompt* once you've committed to an agent.

## Thesis

**A system prompt is code written in natural language.** "You are an email agent. Your job is to assist the user by using your tools to take the correct action." — that's a program, expressed in English instead of Python.

Agents are **autonomous**: unlike ChatGPT there's no back-and-forth, no "make that shorter." The prompt fires once per input and the agent acts. So you only get **one shot** — prompt craft is the difference between a reliable agent and one that hallucinates emails and invents dates.

> **Key rule: keep prompts clear, simple, actionable. LESS IS MORE.**

## Proactive (wrong) vs Reactive (right)

**Proactive** — dump 200 lines up front, then test and debug blind. Problems: you can't know every failure mode in advance; when something breaks you can't tell *which line* caused it; fixing one issue spawns another. You end up adding/removing lines at random, banging your head against the wall.

**Reactive** — start with **nothing**. Add exactly one line to fix exactly one *observed* behavior. Benefits: easy debugging (you know precisely what broke the agent, because you changed one thing), efficient testing (you see real behavior before "hard prompting" a fix in), and you never accrete an over-complicated prompt that's impossible to modify later.

> Learning-to-ride-a-bike analogy: proactive = recite every rule before they pedal ("back straight, lean forward, don't tilt left…") → they fall anyway and you've no idea which advice mattered. Reactive = let them ride, watch the wobble, say only "you're leaning too far left, center your weight." **Start small, observe errors, fix one problem at a time.**

## The reactive loop (procedure)

1. **Bare-minimum / empty prompt + one tool.** No instructions. Run it and test whether the agent calls the tool *unprompted*. (Hook up an email tool, ask it to send an email, see if it figures out the tool on its own.)
2. **Add a rule only when the AI misuses a tool.** Observed: agent tries to write the email itself instead of delegating to the email tool. Fix: add one line — *"You should never write emails. Only call the email tool."* Not before the misuse — after.
3. **Add a concrete `input → correct-action` example only to counter a specific observed failure** ("hard prompting"). Observed: agent sends an email without first looking up the contact. Fix: show it — *Input: "send bob an email…" → 1) use contactAgent to get bob's email → 2) use emailAgent to send → Output: "The email has been sent to bob."* You're training it on the real failure, not a hypothetical.
4. **Debug ONE error at a time.** Change one thing, observe its isolated impact. Never rewrite the whole prompt — modify the single rule causing the problem, so you can attribute the change.
5. **Scale slowly.** add tool → add one prompt line about it → test a few scenarios → if good, add the next tool → if it misbehaves, hard-prompt the fix → test → rinse and repeat. The prompt grows only as fast as observed need.

## The 5-component prompt skeleton

Format the whole prompt in **Markdown with `##` headers**. Not every agent needs every section (a content agent with no tools skips Tools), but this is the shape:

1. **`## Role` / Background** — who the agent is + its overall goal. Sets identity, tone, scope. Without it you get generic, obviously-AI output.
   `You are a [role] AI agent designed to [purpose]. Your goal is to [objective].`
2. **`## Tools`** — list each tool + **when** to use it + any ordering dependency. **The most important section for a tools agent.** Spell out deps explicitly:
   ```
   1. **Contact Database** — Use this to get contact info. You must use this BEFORE the Email Generator tool.
   2. **Email Generator** — Use this to draft follow-up emails.
   ```
   A clear tools section beats hoping the agent guesses correctly in a non-deterministic loop.
3. **`## Context`** — what the agent **receives each run**. The system prompt is fixed but inputs vary (different emails, different articles). Tell it: this is what you'll get, this is what to do with it, this is the end goal. A commonly-forgotten section.
4. **`## Rules` / Instructions** — order-of-ops and anti-hallucination guardrails (`if X do Y; if Z do A`). **But do not over-constrain into a rigid fixed sequence** — if every step must happen in one exact order every time, you don't have an agent, you have a workflow; go build that instead.
5. **`## Examples`** — `input → correct-action` pairs. **Surgical only** — never blind. An example exists to directly counter one observed failure (see loop step 3). Blind examples bloat the prompt; targeted ones lift consistency.

Plus:
- **`## Final Notes`** — inject the current date/time so the agent stops inventing dates: `Here is the current date/time: {{ $now }}`. Add `If unsure about an answer, say "I don't have that information."` (anti-hallucination). May hold rate limits / formatting reminders.
- **`## Output Format`** (optional) — only when output must hit a specific shape (e.g. HTML email with headers + horizontal rules between sections, or a fixed JSON envelope).
- Memory/SOP/error-handling can live inside `## Rules`; promote to their own `##` section only if they get robust enough to warrant it.

## Concrete rules

- **Always inject `{{ $now }}`.** In the live build, the #1 bug was the agent *inventing* dates (made an event for a year-prior date) and *inventing* emails (`michael.scott@example.com` instead of the real `mike@…`). Both fixed by prompt, not config: *"You must always look in the contacts database before creating an event or sending an email — you need the real email address. Never make up someone's email address."* plus giving it `{{ $now }}`.
- **Specialize per agent.** Each agent gets its own narrow prompt with only its own tools — a small, testable program. (See orchestrator specialization in `agent-craft.md`.) Cramming many roles into one prompt is the path to un-debuggable.
- **Use the model's own logged behavior as the source of every new line.** n8n's agent logs show the exact order of operations and how each tool's fields were filled. Read what it actually did, find the one wrong action, write the one line that corrects it. The transcript is your spec — not your imagination of what might go wrong.
