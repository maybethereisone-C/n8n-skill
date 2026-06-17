# Agent Craft — the design/judgment layer

> Companion to `ai-agent.md` / `ai-deep.md`. Those tell you *how to wire* an agent. This tells you *whether to build one at all*, *which architecture*, and *how to plan it*. The mechanics are the easy 20%; this judgment layer is the 80% that separates a demo from a system that survives production.

## The escalation ladder — climb only when forced

```
rule-based automation  →  AI-enhanced workflow  →  single agent  →  multi-agent
   (if/switch/code)        (LLM nodes in a          (one brain,       (orchestrator +
                            fixed sequence)          tools, loops)     child agents)
```

**First question, every build: "do we even need AI here?"** Most "agent" requests collapse one or two rungs down once you map them. A form with predefined types `sales|support|general` is a **Switch node**, not an agent. A wall of free text that must be *read and understood* to be routed → that's where AI earns its place (it needs reasoning, not keyword matching).

Climb a rung only when you hit one of three words — **decide / reason / dynamic**:
- need the system to **decide** its own next steps → workflow → agent
- need multi-step **reasoning** over ambiguous input → agent
- need to control tool usage **dynamically** per input → agent

Don't climb for the buzzword. Every rung up costs latency, money, and consistency.

## Agent vs AI-workflow — and 4 reasons to prefer the workflow

A **workflow** (even an AI-enhanced one) runs the *same ordered steps every time* — deterministic, linear, step 1→2→3. An **agent** has tools and a brain and *chooses* which tools to call, in what order, looping until done — non-deterministic. **If the steps are the same order every single run, build a workflow.** Only reach for an agent when the path genuinely varies per input.

The course's worked example: a RAG customer-support flow built **both** ways. The agent version hit its brain 3× (once per tool decision) and could mis-order calls. The workflow version — `email trigger → search Pinecone → filter by score>0.4 → aggregate → one LLM writes the reply → send` — was cheaper, more consistent, and you can see exactly which node erred. Same tools, same AI, better outcome.

Four reasons to default to the deterministic workflow:

1. **Reliability** — guardrails. The flow *cannot* deviate; no risky agent→agent / agent→tool hand-offs where mappings silently break. The 5–10% hallucination rate on "what do I do next?" is designed out entirely.
2. **Cost** — every time an agent finishes a tool call it **returns to its brain**, re-runs the whole system prompt, and decides the next step. Each return is a billed LLM call. Remove the decision and you remove the call. (Free-tier Gemini hides this; on a paid model 3 tool calls = 3 extra invocations.)
3. **Debuggability** — n8n's visual canvas shows you the exact node that went red and the exact bad mapping. An agent hides its failure inside system-prompt tweaks and opaque tool configs.
4. **Scalability** — adding a node to a workflow = plug in a block. Adding a *tool* to an agent forces a system-prompt rewrite to explain the new tool, which **regresses the earlier tools** that were working. More control = better; more agent autonomy = more surface for regression.

(Chains sit between: a chain is a fixed single-shot LLM call with no tool selection and no memory — see `ai-deep.md`. Chain < agent on capability, chain > agent on predictability.)

## The 4 multi-agent architectures

Reach for multi-agent only after a single agent or workflow can't cleanly do the job — forcing an orchestrator onto a simple process just multiplies latency, cost, and hand-off error. The **golden rule below** governs all four.

### 1. Prompt chaining
**When:** a known linear pipeline where each step's output is the next step's input (clean → enrich → write → format).
**Wiring:** `Agent/LLM N --main--> Agent/LLM N+1 --main--> …`. Pure sequence, no router.
**Model per step:** cheapest model that clears each step — a cleanup step gets Flash/Haiku; only the synthesis step (if any) earns a stronger model. Most steps are cheap.

### 2. Routing
**When:** input falls into distinct categories that each need a different specialist (billing vs complaint vs promotion email).
**Wiring:** `classifier (LLM or Text Classifier) → Switch → branch A | branch B | branch C`, each branch its **own** agent with its own persona, model, and tools.
**Model per step:** small/fast classifier up front; each branch sized to its job (a refund branch may need a stronger model than an FYI branch).

### 3. Parallelization
**When:** N independent sub-tasks can run at once and be combined (research 4 angles, score 4 rubrics).
**Wiring:** fan-out → `N agents in parallel → Merge → Aggregate → synthesizer agent`. The synthesizer composes the merged outputs into one answer.
**Model per step:** cheap identical workers on the fan-out legs; one stronger **synthesizer** at the join where quality matters.

### 4. Evaluator-optimizer
**When:** output quality must clear a bar and benefits from iterative critique (draft → critique → revise).
**Wiring:** `optimizer (drafts) → evaluator → IF`. The **evaluator emits a parseable verdict** (`{"pass": false, "feedback": "..."}`). IF false → loop back to the optimizer with the feedback; IF true → exit. A **Set node holds the latest draft** so each loop revises the current best.
**Guard:** ALWAYS add a **max-iteration counter** (Set/increment + IF on count) so a never-passing eval can't loop forever / burn the account.
**Model per step:** optimizer mid-tier; evaluator can often be cheaper but must reliably produce the structured pass/fail.

## Orchestrator specialization

The course's "ultimate assistant": one **orchestrator** (parent) over child agents (email, calendar, contact, content-creator). The orchestrator's *only* job is to read intent and delegate:

> "You're the ultimate assistant. Your job is to send the user's query to the correct tool. You should **never** be writing emails or creating summaries — you just delegate."

Its prompt is short: a role line, a `## Tools` list (one line per child, "use this when…"), a couple rules, one example. Almost no ambiguity. Compare: cramming all 4 children's tools + instructions into one agent → 25-tool prompt nobody can debug.

Why specialize:
- **Reusable components** — once an email agent exists, any future workflow can call it. (Children don't even have to be agents — plain sub-workflows work as tools too.)
- **Per-agent model** — Claude-class for content creation, Flash/Haiku for "look up a contact." You'd never pay top-tier rates to read a row from a sheet.
- **Isolated, testable prompts** — each child's prompt is small and independently verifiable; a regression is local, not global.
- **Memory still passes** — delegating parent→child doesn't lose conversational context; memory passes via the **Execute-Workflow Trigger input schema**. Foundation for multi-turn.

**GOLDEN RULE: minimize data transfer between workflows.** Every hand-off (agent→tool, agent→sub-agent, workflow→workflow) is where mappings break and quality leaks. Fewer hops = fewer failure points.

## Build methodology — wireframe first

**>50% of build time happens in Excalidraw, not in n8n.** Jumping straight into the builder produces messy over-complicated workflows, confusion about where AI is actually needed, and hours of debugging from integrations/structure you didn't foresee. Treat the wireframe like the Lego instruction sheet: two monitors — wireframe left, n8n right.

Questions to answer *on the wireframe*, before a single node:
- **Trigger** — what starts this? (form / email / chat / schedule / webhook)
- **Incoming data shape** — what does the payload look like at the trigger?
- **Branch logic** — one path, or conditional splits? on what?
- **Where is AI *actually* needed?** — which steps need reading/understanding/deciding, and which are plain data manipulation?
- **Enrichment** — where do we need RAG or API calls to pull external context before the next LLM?
- **Integrations** — every app/credential involved.
- **The deciding question:** does the work happen in the **same order every run**? → **workflow**. Does the path vary per input / need decisions? → **agent**.

Wireframing also surfaces the questions you'd otherwise discover mid-build (or mid-client-engagement) — it aligns scope before you commit nodes.

## The 3 context channels

> "An agent is only as good as the context you feed it." Garbage in → hallucination, tool misuse, vague obviously-AI output. Models are pre-trained and smart but have no knowledge of *your* domain, jargon, or process.

Three ways to feed context — use the right one per data type:

1. **System prompt** — *preloaded* role, rules, key business facts. Like briefing an intern on day one: this is your job, here are the rules. Static per agent.
2. **Memory** — *user-specific* short-term history (last N interactions, keyed by session ID = user/email/chat). Stops the agent re-asking what it already knows. Capped (e.g. context-window-length 5) — not unlimited.
3. **RAG / retrieval** — *real-time* facts too large or too fresh for the prompt: hit a knowledge base (vector or relational) or a live API and ground the answer in what comes back.

Pick by data: **structured + exact retrieval → relational DB + SQL** (most business data — profiles, orders, invoices); **unstructured walls of text needing semantic match → vector DB**. Don't vectorize everything because "vector DB" sounds cool — it's a buzzword, not a default.

## Production reality

- **Demos ≠ production.** Almost every cool agent online (the author's own included) is a proof-of-concept. On a single user a stray hallucination is noise; expose it to many users and every edge case, and you scale the hallucinations and failures with the traffic. Even Apple/Google/Amazon ship AI-reliability misses — a beginner won't make a few-day POC production-ready.
- **Scale vertically before horizontally.** Perfect **one** domain end-to-end — its knowledge base, sub-workflows, agent, **plus evals + monitoring + guardrails** — before adding users or new domains. Going wide too early multiplies retrieval degradation, latency, and inconsistency. Mitigations: strict retrieval rules, data segmented by namespace/DB, caching/async for latency, and a confidence threshold that escalates to a human instead of guessing.
- **No-code has limits → go hybrid.** n8n is unbeatable for fast builds, rule-based logic, AI-enhanced workflows, and multi-agent orchestration. But at enterprise scale — millions of records, large-scale auth (OAuth tokens, session mgmt, access control), highly custom decision logic — drop to **custom Python** for the heavy/secure work and keep n8n as the orchestration layer. Best production setups are a mix: n8n to connect and coordinate fast, custom code where it must be robust.
