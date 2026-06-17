# AI Agent — LangChain Cluster Architecture

> Purpose: build n8n AI Agent workflows correctly. The hard part is the **wiring**: sub-nodes attach to the root agent via special connection types, NOT `main`.

## The architecture

The root **AI Agent** (`@n8n/n8n-nodes-langchain.agent`, v3.1) runs on the `main` data flow. Everything it needs — the LLM, memory, tools, output parser — are **sub-nodes** connected via dedicated connection types:

| Sub-node role | Connection type | Example node |
|---|---|---|
| LLM | `ai_languageModel` | `lmChatOpenAi`, `lmChatAnthropic`, `lmChatGoogleGemini` |
| Memory | `ai_memory` | `memoryBufferWindow`, `memoryPostgresChat` |
| Tool | `ai_tool` | `toolHttpRequest`, `toolWorkflow`, `toolCode`, vector store (as tool), `toolVectorStore` |
| Output parser | `ai_outputParser` | `outputParserStructured`, `outputParserAutofixing` |

Connection direction: the **sub-node is the source**, the **agent is the target**. In `connections`, the key is the sub-node's name and the connection-type array (e.g. `"ai_languageModel"`) points at the agent. Only the trigger→agent→next-node path uses `"main"`.

### All 8 ai_* connection types (the whole cluster)

The agent itself consumes only the first four. The other four (`ai_embedding`, `ai_vectorStore`, `ai_document`, `ai_textSplitter`) wire **sub-nodes to each other** inside a RAG pipeline — they never plug into the agent directly. Full pipeline wiring is in `ai-deep.md`.

| Connection type | Source sub-node | Target (consumer) | Cardinality on target |
|---|---|---|---|
| `ai_languageModel` | chat model (`lmChat*`) | agent, chain, autofixing parser, QA tool | exactly **1** (required) |
| `ai_memory` | `memory*` | agent (NOT chains) | 0..1 |
| `ai_tool` | tool node, vector store, `agentTool`, `toolMcp` | agent, MCP Server Trigger | 0..N (agent needs ≥1) |
| `ai_outputParser` | `outputParser*` | agent, Basic LLM Chain | 0..1 |
| `ai_embedding` | `embeddings*` | vector store node | 1 on each vector store |
| `ai_vectorStore` | vector store node | retriever, `toolVectorStore` | 1 |
| `ai_document` | document loader | vector store node (insert mode) | 1 |
| `ai_textSplitter` | text splitter | document loader (custom mode) | 0..1 |

`ai_retriever` and `ai_reranker` also exist (retriever→QA chain; reranker→vector store). The exact connection-type strings and `typeVersion` for every node above are **not quoted verbatim in the docs** — confirm with `get_node`/`validate_workflow` before publishing. [unverified: connection-string spelling for ai_embedding/ai_vectorStore/ai_document/ai_textSplitter/ai_retriever/ai_reranker — inferred from n8n LangChain convention, not the cloned docs]

## Annotated JSON — Agent + model + memory + tool

```jsonc
{
  "nodes": [
    { "name": "When chat message received", "type": "@n8n/n8n-nodes-langchain.chatTrigger",
      "typeVersion": 1.1, "position": [0, 0], "parameters": {} },

    { "name": "AI Agent", "type": "@n8n/n8n-nodes-langchain.agent", "typeVersion": 3.1,
      "position": [260, 0],
      "parameters": { "promptType": "auto",
        "options": { "systemMessage": "You are a support assistant. Use tools for live data." } } },

    { "name": "OpenAI Chat Model", "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "typeVersion": 1.2, "position": [120, 200],
      "parameters": { "model": "gpt-4.1-mini", "options": { "temperature": 0.2 } } },

    { "name": "Simple Memory", "type": "@n8n/n8n-nodes-langchain.memoryBufferWindow",
      "typeVersion": 1.4, "position": [300, 200],
      "parameters": { "sessionKey": "={{ $json.sessionId }}", "contextWindowLength": 10 } },

    { "name": "Order Lookup", "type": "@n8n/n8n-nodes-langchain.toolHttpRequest",
      "typeVersion": 1.1, "position": [480, 200],
      "parameters": { "toolDescription": "Look up an order by ID",
        "method": "GET",
        "url": "https://api.shop.test/orders/{orderId}",
        "placeholderDefinitions": { "values": [
          { "name": "orderId", "description": "The order ID to fetch", "type": "string" } ] } } }
  ],
  "connections": {
    "When chat message received": { "main": [[ { "node": "AI Agent", "type": "main", "index": 0 } ]] },
    "OpenAI Chat Model": { "ai_languageModel": [[ { "node": "AI Agent", "type": "ai_languageModel", "index": 0 } ]] },
    "Simple Memory":     { "ai_memory":        [[ { "node": "AI Agent", "type": "ai_memory", "index": 0 } ]] },
    "Order Lookup":      { "ai_tool":          [[ { "node": "AI Agent", "type": "ai_tool", "index": 0 } ]] }
  }
}
```

Note: the three sub-nodes have **no `main` connection** — they only feed the agent through their typed connection. The agent needs exactly one `ai_languageModel`; memory/parser are optional; tools are 0..N.

## Agent types

There is now **one agent type: the Tools Agent**. The per-type selector (Conversational, ReAct, Plan-and-execute, OpenAI Functions, SQL) was **removed in v1.82.0** — every `agent` node now behaves as a Tools Agent, which was always the recommended setting (`root-nodes/n8n-nodes-langchain.agent/index.md`). Old workflows set to "Tools Agent" keep working. The Tools Agent implements LangChain tool-calling: it advertises each tool's schema to the model and passes the output parser to the model as a formatting tool (`tools-agent.md`).

Supported chat models for tool-calling: OpenAI, Anthropic, Groq, Mistral Cloud, Azure OpenAI (`tools-agent.md`) — plus others in the catalog. `agentTool` (`@n8n/n8n-nodes-langchain.agentTool`) wraps an agent so it can be an `ai_tool` of another agent (subagent pattern). HITL review steps inside a subagent work correctly (`human-in-the-loop-tools.md`).

### Agent parameters and options

Source: `tools-agent.md`.

- **Prompt** (`promptType`) — `auto` pulls the chat-trigger message; `define` lets you set the text/expression.
- **Require Specific Output Format** — toggles the `ai_outputParser` slot (see Structured output below).

Options (under "Add Option"):
- **System Message** — the priming prompt; default is "You are a helpful assistant" (`intro-tutorial.md`). Keep it tight; sent every turn.
- **Max Iterations** — caps the agent's tool-call/reasoning loops per execution (prevents runaway loops).
- **Return Intermediate Steps** — emits the tool-call trace in the output for debugging.
- **Tracing Metadata** — attaches metadata for observability (e.g. LangSmith, `langchain/langsmith.md`).
- **Automatically Passthrough Binary Images** — forwards binary images to multimodal models.
- **Enable Streaming** — on by default; streams tokens to the user as generated. Requires a streaming-capable trigger: Chat Trigger, or Webhook with **Response Mode = Streaming** (`tools-agent.md`).

The agent runs **multiple times per execution** — initial pass, one run per tool call, then a final run to answer (`examples/understand-agents.md`). Budget tokens accordingly.

## Structured output

Attach `outputParserStructured` via `ai_outputParser` and enable "Require Specific Output Format" on the agent. The parser holds a JSON schema; the agent's `output` becomes a typed object.
```jsonc
{ "name": "Parser", "type": "@n8n/n8n-nodes-langchain.outputParserStructured", "typeVersion": 1.3,
  "parameters": { "schemaType": "manual",
    "inputSchema": "{ \"type\":\"object\", \"properties\":{ \"sentiment\":{\"type\":\"string\"}, \"score\":{\"type\":\"number\"} }, \"required\":[\"sentiment\",\"score\"] }" } }
```
For flaky models, wrap with `outputParserAutofixing` so a parse failure triggers an LLM repair pass. The autofixing parser needs its **own** `ai_languageModel` connection (it makes a repair LLM call). Other parsers: `outputParserItemList` (splits output into a list of items).

## Memory types

All memory nodes connect via `ai_memory` and are keyed by `sessionKey`. **Chains can't use memory — only agents can** (`examples/understand-chains.md`, `examples/understand-memory.md`).

| Node | Backing store | Use when |
|---|---|---|
| `memoryBufferWindow` ("Simple Memory") | n8n process RAM | dev / single-instance; easiest. `contextWindowLength` caps turns kept (default 5) |
| `memoryPostgresChat` | Postgres | durable, multi-session, production |
| `memoryRedisChat` | Redis | fast durable sessions |
| `memoryMongoChat` | MongoDB | Mongo shops |
| `memoryMotorhead` / `memoryZep` / `memoryXata` | hosted services | managed memory, summarization (Zep) |

`memoryManager` ("Chat Memory Manager") is a regular-flow node for advanced ops — read/insert/delete messages programmatically, not an agent slot (`examples/understand-memory.md`).

Caution: Simple Memory in RAM is lost on restart and is **not** scoped per workflow on a shared instance.

## $fromAI() in tool params — canonical runtime-fill

`$fromAI()` is the **canonical technique for having the agent populate pre-configured tool fields at call time**. Used in any tool node's parameter field (Gmail, Sheets, HTTP, etc.) so the agent decides values, not the workflow author. Course pattern: wire `gmailTool`, `googleSheetsTool`, etc. with every content field as a `$fromAI()` expression — the agent fills them when it decides to invoke the tool.

```javascript
// In a Gmail tool's "Subject" field:
={{ $fromAI('subject', 'the email subject line', 'string') }}
// In a Sheets tool's "Value" field:
={{ $fromAI('row_data', 'JSON object for the new row', 'json') }}
```

Key constraint: **only works inside `ai_tool`-connected nodes** (toolHttpRequest, toolWorkflow, app nodes acting as tools). Does NOT work in toolCode or in regular flow nodes.

## Sub-workflow-as-tool pattern

Expose a full workflow (multi-step, stateful) as an agent tool via `toolWorkflow`:

1. **Sub-workflow**: starts with `Execute Sub-workflow Trigger` → define a typed input schema in `workflowInputs.values` (gives the agent clear param names/types).
2. **Parent**: add `toolWorkflow` node → reference the sub-workflow by Database ID → map each input field with a `$fromAI()` expression.
3. **Memory continuity**: pass `chatId` / `sessionId` through the sub-workflow's input schema and use it as the `sessionKey` on whatever memory node is inside the sub-workflow — otherwise the agent's conversation context is lost across the tool hop.

Course pattern: complex capabilities (multi-API orchestration, DB writes, email + calendar combos) are built as standalone workflows, then surfaced to a top-level agent as `toolWorkflow` tools — keeps the main canvas clean and each capability independently testable.

## 3 context channels for an agent

Three independent layers feed context to an agent LLM call; each has a dedicated mechanism:

| Channel | Mechanism | When to use |
|---|---|---|
| **System prompt** | `options.systemMessage` on the agent node | Static role definition, hard constraints, output format instructions |
| **Memory** | `ai_memory` sub-node (`memoryBufferWindow` / `memoryPostgresChat`) | Conversation history; ephemeral or persistent across sessions |
| **RAG** | Vector store tool or Q&A chain; retrieved at query time | Dynamic knowledge from documents/unstructured text |

All three can be active simultaneously. See `ai-deep.md` for full RAG wiring; memory comparison table below.

## $fromAI() — full signature

`$fromAI(key, description?, type?, defaultValue?)` lets the **model supply** a tool parameter at call time. Source: `examples/using-the-fromai-function.md`.

| Arg | Type | Req | Notes |
|---|---|---|---|
| `key` | string | ✅ | 1–64 chars, `[A-Za-z0-9_-]` only |
| `description` | string | ✖ | hint for the model |
| `type` | string | ✖ | `string` (default) \| `number` \| `boolean` \| `json` |
| `defaultValue` | any | ✖ | fallback if model omits it |

```javascript
{{ $fromAI('email') }}
{{ $fromAI("numItemsInStock", "Number of items in stock", "number", 5) }}
Generated by AI: {{ $fromAI("subject") }}   // mix static + dynamic
```

Args are **hints, not references** — the model finds/asks for the value; in chat it may ask the user. The stars/"Let the model define this parameter" button auto-writes the expression (overwrites manual values). **Only works for tools connected to the Tools Agent.** It does **NOT** work in the Code Tool or other non-tool cluster sub-nodes (`using-the-fromai-function.md`).

## Human-in-the-loop (HITL) tool gating

Require human approval before the agent runs a sensitive tool (send/delete/purchase). Source: `human-in-the-loop-tools.md`.

Wiring: click the **Tools** connector → **Human review** section → pick a channel → connect the gated tools to the review step's tool connector. On a gated call the workflow **pauses**, sends the request, and resumes on **Approve** (tool runs with AI input) or **Deny** (canceled; agent told). HITL can gate all tools or just selected ones; the review channel can differ from the chat channel.

Channels: Chat, Slack, Discord, Telegram, Microsoft Teams, Gmail, WhatsApp Business Cloud, Google Chat, Microsoft Outlook.

In the review-message expression, `$tool.name` = the tool node's canvas name, `$tool.parameters` = the call's params (including `$fromAI()` fields):
```
The AI wants to use {{ $tool.name }} with parameters:
{{ JSON.stringify($tool.parameters, null, 2) }}
```
Best practice: describe the HITL setup and denial handling in the **system message** so the agent responds gracefully to rejections. Subagent HITL steps work too.

## Tools

**`toolHttpRequest`** — gives the agent an HTTP capability. Describe it well (`toolDescription`); declare params via `placeholderDefinitions` so the model fills `{placeholder}` slots. Reuses HTTP auth/credentials.

**`toolWorkflow`** (`Call n8n Sub-Workflow Tool`) — exposes an entire workflow as a tool. Best for multi-step or stateful capabilities you've already built. Pass inputs via `$fromAI()` mapped to the sub-workflow's fields.

**`$fromAI()`** — inside a tool's params, `={{ $fromAI('city', 'target city', 'string') }}` lets the **model supply** that value at call time. Works in `toolHttpRequest` and `toolWorkflow` parameters.

### Code Tool pitfall (read this)

`@n8n/n8n-nodes-langchain.toolCode` (v1.3) is **not** the regular Code node. Different contract:

- It must **return a STRING**. For structured data, `JSON.stringify(result)` — returning a bare object/array fails.
- Input is bound to `query` / `_query` (the model's call string). **Not renameable.**
- It does **NOT** support `$fromAI()` — using it throws *"No execution data available"*.

If you need `$fromAI()` typed params or object returns, use `toolWorkflow` (call a sub-workflow with a Code node inside) instead of `toolCode`.

| | Regular Code (`nodes-base.code`) | Code Tool (`langchain.toolCode`) |
|---|---|---|
| Returns | `[{ json: {...} }]` | a **string** |
| Input | `items` / `$json` | `query` / `_query` (fixed) |
| `$fromAI()` | n/a | ❌ throws |

## Production tips

- **Model choice** — small/fast model (e.g. mini-tier) for routing/extraction; reserve a frontier model for hard reasoning. Set low `temperature` for tool-using agents.
- **Token cost** — memory + tool schemas + system prompt are sent every turn. Trim `contextWindowLength` (e.g. 5–10) and keep `systemMessage` tight.
- **Memory windowing** — `memoryBufferWindow.contextWindowLength` caps history; for durable multi-session memory use `memoryPostgresChat` keyed by `sessionKey`.
- **Guardrails** — constrain with a strict `systemMessage`, structured output parser, and a Switch/Filter after the agent to validate before side-effects. Cap tool count; over-many tools degrade selection.
- **Validate** — run `validate_workflow` (community `n8n-mcp` validates AI Agent wiring) before publishing; it catches missing `ai_languageModel` and stray `main` links on sub-nodes.
- Confirm every `typeVersion` with `get_node` — LangChain nodes version frequently.
