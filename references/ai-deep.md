# AI Deep — Chains, RAG, Vector Stores, Evaluations, MCP

> Companion to `ai-agent.md`. Covers the non-agent half of the LangChain cluster: chains, the full RAG pipeline wiring, vector-store/embedding/tool sub-nodes, evaluations, and exposing a workflow as an MCP tool. Same rule applies: **wrong `ai_*` connection type = #1 failure.**

The exact connection-type strings (`ai_embedding`, `ai_vectorStore`, `ai_document`, `ai_textSplitter`, `ai_retriever`) and every `typeVersion` here follow n8n's LangChain convention but are **not all quoted verbatim** in the cloned docs — confirm each with `get_node` / `validate_workflow` before publishing. [unverified: literal connection-string spelling + typeVersions]

## Chains vs agents — when each

Source: `examples/understand-chains.md`, `examples/understand-agents.md`, `examples/agent-chain-comparison.md`.

A **chain** runs a fixed, predetermined sequence of component calls. An **agent** is "a chain that makes decisions" — it uses the LLM to pick which tools to call and loops until done.

| | Chain | Agent |
|---|---|---|
| Control flow | fixed sequence | LLM-decided, multi-step loop |
| Tools | ✖ | ✅ (`ai_tool`, 0..N) |
| Memory | ✖ **never** | ✅ (`ai_memory`) |
| Runs per execution | once | many (setup → tool calls → answer) |
| Cost / latency | low, predictable | higher |

**Pick a chain** when the task is deterministic and single-shot: summarize, classify, one-pass extraction, or single-doc Q&A. **Pick an agent** when you need tool selection, multi-step reasoning, or conversational memory.

### The three chain nodes (`examples/understand-chains.md`)

- **Basic LLM Chain** (`chainLlm`) — one LLM call, no tools/memory. Can take an `ai_outputParser`.
- **Question and Answer Chain** (`chainRetrievalQa`) — RAG Q&A. Takes an `ai_languageModel` **and** an `ai_retriever`. The retriever is a Vector Store Retriever or Workflow Retriever (`chainretrievalqa/index.md`).
- **Summarization Chain** (`chainSummarization`) — returns a summary of the input (works with a document loader for large inputs).

None support memory — if you need conversation, use an agent.

## RAG pipeline — the two halves

RAG in n8n is **two separate flows**: an **ingest** flow (load → split → embed → store) and a **query** flow (embed query → similarity search → ground the LLM). Source: `rag-in-n8n.md`, `examples/understand-vector-databases.md`. Try the RAG Starter Template (n8n.io/workflows/5010).

### Ingest wiring (Insert Documents)

```
[fetch source nodes] --main--> Vector Store (Insert Documents)
                                   ▲ ai_embedding   ▲ ai_document
                            Embeddings node     Default Data Loader
                                                     ▲ ai_textSplitter (only if Text Splitting = Custom)
                                                  Text Splitter
```

- **Vector Store node** in **Insert Documents** mode sits on `main` (data flows in via main). It pulls two sub-nodes: an **embedding** (`ai_embedding`) and a **document loader** (`ai_document`).
- **Default Data Loader** (`documentDefaultDataloader`) chunks content. `Text Splitting = Simple` uses a built-in Recursive splitter (chunk 1000 / overlap 200). `Custom` exposes an `ai_textSplitter` slot (`documentdefaultdataloader.md`).
- **Text splitters** (`textsplitterrecursivecharactertextsplitter` recommended; also `charactertextsplitter`, `tokentextsplitter`). Recursive splits by Markdown/HTML/code then chars — best default (`rag-in-n8n.md`).
- Add **metadata** on the loader to enable later metadata filtering (`documentdefaultdataloader.md`).

### Query wiring — three patterns (`vectorstoreinmemory.md`)

Use the **same embedding model** you ingested with, or similarity search is garbage.

1. **Vector store as a tool (agent)** — `AI Agent (ai_tool) → Vector Store node (Retrieve Documents As Tool)`. Set limit + Include Metadata. Simplest agent RAG.
2. **Retriever → QA Chain** — `Q&A Chain (ai_retriever) → Vector Store Retriever (ai_vectorStore) → Vector Store node`. Non-agent RAG.
3. **Vector Store QA Tool** — `AI Agent (ai_tool) → Vector Store Question Answer Tool (ai_vectorStore) → Vector Store node`. The QA tool needs its **own `ai_languageModel`** to summarize chunks before returning — saves tokens on the main (expensive) agent model (`rag-in-n8n.md` pro-tip; `toolvectorstore.md`).

The Vector Store node also has **Get Many** mode to query directly on `main` with no agent/chain (`rag-in-n8n.md`).

### Minimal ingest JSON (wiring only)

```jsonc
{
  "nodes": [
    { "name": "Trigger", "type": "n8n-nodes-base.manualTrigger" },
    { "name": "Vector Store", "type": "@n8n/n8n-nodes-langchain.vectorStoreInMemory",
      "parameters": { "mode": "insert", "memoryKey": "docs" } },
    { "name": "Embeddings OpenAI", "type": "@n8n/n8n-nodes-langchain.embeddingsOpenAi",
      "parameters": { "model": "text-embedding-3-small" } },
    { "name": "Data Loader", "type": "@n8n/n8n-nodes-langchain.documentDefaultDataLoader",
      "parameters": { "textSplittingMode": "custom" } },
    { "name": "Recursive Splitter", "type": "@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter",
      "parameters": { "chunkSize": 1000, "chunkOverlap": 200 } }
  ],
  "connections": {
    "Trigger":            { "main":            [[ { "node": "Vector Store", "type": "main", "index": 0 } ]] },
    "Embeddings OpenAI":  { "ai_embedding":    [[ { "node": "Vector Store", "type": "ai_embedding", "index": 0 } ]] },
    "Data Loader":        { "ai_document":     [[ { "node": "Vector Store", "type": "ai_document", "index": 0 } ]] },
    "Recursive Splitter": { "ai_textSplitter": [[ { "node": "Data Loader", "type": "ai_textSplitter", "index": 0 } ]] }
  }
}
```

Note: the splitter feeds the **loader**, the loader+embeddings feed the **vector store**. Only the trigger uses `main`. (Node type spellings/typeVersions: confirm with `get_node`.)

## Vector store options

All connect the same way (`ai_embedding` in; act as `ai_vectorStore` source or `ai_tool`). Source: root-nodes `vectorstore*` docs.

| Node | Notes |
|---|---|
| `vectorStoreInMemory` ("Simple Vector Store") | **dev only** — RAM, lost on restart, global memory keys (all instance users can read). Env: `N8N_VECTOR_STORE_MAX_MEMORY`, `N8N_VECTOR_STORE_TTL_HOURS` |
| `vectorStorePinecone` | managed, common for production (`examples/vector-store-website.md`) |
| `vectorStoreQdrant` | self-host/managed; strong filtering |
| `vectorStorePGVector` | Postgres + pgvector — reuse your DB |
| `vectorStoreSupabase` | Supabase/pgvector |
| `vectorStoreWeaviate` / `vectorStoreMilvus` / `vectorStoreChroma` / `vectorStoreRedis` / `vectorStoreMongoDbAtlas` / `vectorStoreAzureAiSearch` / `vectorStoreZep` / `vectorStoreOracleDb` | other backends, same wiring |

Most vector store nodes support a **Rerank Results** toggle (add a `cohere` reranker via `ai_reranker`) and metadata filtering on retrieval.

## Embeddings nodes

Turn text → vectors (n8n embeds **text only**, `examples/understand-vector-databases.md`). Connect via `ai_embedding` to the vector store. `embeddingsOpenAi`, `embeddingsGoogleGemini`/`embeddingsGoogleVertex`, `embeddingsCohere`, `embeddingsMistralCloud`, `embeddingsAwsBedrock`, `embeddingsAzureOpenAi`, `embeddingsHuggingFaceInference`, `embeddingsOllama`, `embeddingsOracleDb`. Smaller models (e.g. `text-embedding-3-small`/`ada-002`) are cheap/fast; larger (`text-embedding-3-large`) for accuracy on long/complex docs (`rag-in-n8n.md` FAQ). **The same model must be used for ingest and query.**

## Tool sub-nodes

All connect via `ai_tool` (source = tool, target = agent or MCP Server Trigger). Source: `examples/understand-tools.md`, sub-node docs.

- **`toolHttpRequest`** — HTTP capability. Describe well; declare `placeholderDefinitions` for `{slot}` params or use `$fromAI()`. Reuses HTTP credentials.
- **`toolWorkflow`** ("Call n8n Workflow Tool") — runs another workflow as a tool. **Source**: Database (pick/ID) or Define Below (inline JSON). With Database, define a **Workflow Input Schema** in the sub-workflow, then map **Workflow Inputs** via fixed values, expressions, or `$fromAI()` (`toolworkflow.md`). Best for multi-step/stateful capability you already built.
- **`toolCode`** ("Custom Code Tool") — see the Code Tool pitfall in `ai-agent.md`. Returns a **string**, input bound to `query`/`_query`, **no `$fromAI()`**.
- **Vector store as a tool** — connect a Vector Store node (Retrieve As Tool) directly to `ai_tool`, OR use **`toolVectorStore`** ("Vector Store Question Answer Tool") which summarizes chunks and answers questions; it takes the vector store via `ai_vectorStore` and needs its own LLM. n8n auto-builds the tool description as *"Useful for when you need to answer questions about [node name]…"* — **use only alphanumerics, spaces, dashes, underscores in node names** or the agent errors (`toolvectorstore.md`).
- Other built-ins: `toolCalculator`, `toolWikipedia`, `toolSerpApi`, `toolSearxng`, `toolWolframAlpha`, `toolThink`, `toolMcp` (MCP Client), `agentTool` (subagent). Any app node (Slack, Gmail, Sheets, Postgres…) can also act as a tool (`tools-agent.md`).

## When NOT to use a vector store

Vector stores are for **unstructured text + semantic/fuzzy retrieval**. Do not use them when:

- Data is **structured** (tables, rows, typed fields) → use a relational DB + SQL node. Postgres, MySQL, SQLite all have n8n native nodes. SQL gives exact, deterministic retrieval; embeddings give approximate similarity.
- You need **exact key lookups** (by ID, email, order number) → SQL `WHERE` clause, not cosine distance.
- You need **aggregations** (SUM, COUNT, GROUP BY) → SQL, not a vector similarity search.

Course pattern: "over-vectorization" — developers reflexively embed everything. Before adding a vector store, ask: *can I answer this with a SQL query?* If yes, use SQL. Reserve vectors for freeform document content where exact-match retrieval is impossible.

## Retrieval-score filtering in linear RAG

In a **linear RAG workflow** (Vector Store → Get Many mode → LLM), filter chunks by similarity score before the LLM call — prevents low-quality context from degrading the answer:

```
Vector Store (Get Many) → Filter (score > 0.4) → LLM call
```

- The Vector Store node (Get Many) returns `score` on each chunk.
- Use a **Filter** node: `{{ $json.score > 0.4 }}` (threshold tunable per corpus; 0.35–0.5 typical).
- Easier to control than instructing an agent to self-filter — no extra LLM call, deterministic.

This is less critical in agent RAG (agent decides relevance) but recommended in chain/linear RAG where every chunk goes to the LLM unconditionally.

## Evaluator-optimizer loop — implementation constraints

The evaluator-optimizer pattern (generate → evaluate → revise loop) requires two hard constraints to work reliably:

**1. Evaluator must emit a parseable decision field, not prose.**

The IF node that branches on pass/fail needs a discrete value, not a sentence:

```jsonc
// Evaluator output — correct
{ "passed": true, "feedback": "The summary covers all key points." }

// Evaluator output — wrong (IF node can't branch on this)
{ "result": "The summary looks mostly good but could be improved." }
```

Wire the evaluator as a Basic LLM Chain with `outputParserStructured` forcing `{ passed: boolean, feedback: string }`. The IF node then branches on `{{ $json.passed }}`.

**2. Add a max-iteration counter guard.**

n8n has no built-in loop-iteration limit on condition loops. Without a guard, a persistent evaluator failure loops forever. Pattern:

```
Set (counter = 0) → [generate] → [evaluate] → IF passed?
  true  → exit
  false → IF counter < maxRounds?
    true  → Set (counter++) → back to generate
    false → exit with best-so-far or error
```

Store `counter` in a Set node, check it in a second IF. `maxRounds` = 3–5 is typical.

## memoryPostgresChat vs memoryBufferWindow

| | `memoryBufferWindow` ("Simple Memory") | `memoryPostgresChat` |
|---|---|---|
| Backing store | n8n process RAM | Postgres table |
| Persistence | Lost on restart / redeploy | Survives restarts; cross-session |
| Multi-instance | Scoped to one n8n instance (not shared across replicas) | Shared across any instance pointing at the same DB |
| Setup | Zero — just set `sessionKey` and window size | Requires Postgres credentials + `n8n_chat_histories` table (auto-created) |
| **Use when** | Dev, single-instance, short demos, ephemeral chat | Production, queue mode, multi-replica, persistent user memory |

Course pattern: start with `memoryBufferWindow` during development; swap to `memoryPostgresChat` keyed by `userId` or `chatId` before production. The swap is a one-node change — same `sessionKey` expression, different node type.

## Model-selector (meta-routing) pattern

Route messages to cheap vs expensive models dynamically:

```
Trigger → Router Agent (cheap model, returns { complexity: "simple"|"complex" })
         → Switch (on complexity)
           → "simple" branch → Agent A (gpt-4.1-mini or claude-haiku)
           → "complex" branch → Agent B (gpt-4o or claude-sonnet)
```

Alternatively, a classifier node outputs the model name as a string → downstream agent's model field uses `={{ $json.modelName }}` (if the node supports dynamic model expressions; confirm with `get_node`).

Course pattern: front a multi-agent system with a single cheap classifier that reads the task and routes to the right specialist — keeps frontier-model usage minimal and cost linear with task complexity.

## AI evaluations

Run a test dataset through the workflow and measure output quality. Source: `evaluations/overview.md`, `light-evaluations.md`, `metric-based-evaluations.md`.

**Two modes.** *Light* (pre-deploy): small hand/AI-made dataset, eyeball outputs, no formal metric. *Metric-based* (post-deploy): large dataset (often built from production executions), numeric scores, regression testing across runs.

Dataset lives in a **data table or Google Sheet** with columns for input, (optional) expected/reference output, and actual output (left blank, filled by the run).

Wiring (`light-evaluations.md`):
1. **Evaluation Trigger** (`evaluationTrigger`) — emits one item per dataset row. "Evaluate all" runs the workflow once per row.
2. Wire the trigger's input column(s) into your workflow.
3. **Evaluation node** (`evaluation`), **Set Outputs** operation — write the workflow's actual output back to the dataset column.
4. For metrics: **Set Metrics** operation. Built-in metrics: Correctness (AI, 1–5), Helpfulness (AI, 1–5), String Similarity (0–1 edit distance), Categorization (exact match 0/1), Tools Used (0–1). Plus **Custom Metrics** (compute a number in-flow, map it in).

Gate metric logic behind the **Check If Evaluating** operation so it only runs during evals (avoids cost on production runs). Metric-based eval is **Pro/Enterprise** (community/Starter get one workflow). Concurrency: Community/Pro 1, Business 3, Enterprise 5; self-host override `N8N_CONCURRENCY_EVALUATION_LIMIT` (`metric-based-evaluations.md`). Observe traces with LangSmith via the agent's Tracing Metadata option (`langchain/langsmith.md`).

## Exposing a workflow as an MCP tool

Use the **MCP Server Trigger** node (`n8n-nodes-langchain.mcptrigger`) to make n8n act as an MCP **server** — your workflow's tools become callable by external MCP clients (Claude Desktop, etc.). Source: `mcptrigger.md`, `mcp/accessing-n8n-mcp-server.md`.

Key behavior: unlike normal triggers, the MCP Server Trigger **only connects to tool nodes** (via `ai_tool`) — clients list and call those tools; there is no downstream `main` chain. To expose a whole workflow, attach a **`toolWorkflow`** node to it (`mcptrigger.md`).

```
MCP Server Trigger --ai_tool--> [ toolWorkflow / toolHttpRequest / any tool node ]
```

Parameters: **MCP URL** (test vs production — production registers on publish), **Authentication** (Bearer or Header auth), **Path** (random by default; settable). Transports: **SSE** and **streamable HTTP** (no stdio). Claude Desktop connects via the `mcp-remote` npx proxy (`mcptrigger.md`).

Scaling gotchas: in **queue mode**, route all `/mcp*` traffic to a **single dedicated webhook replica** (SSE needs connection affinity). Behind nginx, disable `proxy_buffering`, gzip, and chunked encoding on the MCP location (`mcptrigger.md`).

**Two distinct MCP features — don't confuse them** (`mcp/accessing-n8n-mcp-server.md`):
- **Instance-level MCP** (Settings → Instance-level MCP) — one connection per instance; clients search/run/build workflows you enable. `execute_workflow` runs the published version by default. Disable self-hosted via `N8N_DISABLED_MODULES=mcp`.
- **MCP Server Trigger node** — per-workflow server exposing only that workflow's tools.

And the inverse: **`toolMcp`** ("MCP Client Tool") lets an n8n agent *consume* an external MCP server's tools (SSE endpoint + auth; include All/Selected/All-Except tools) (`toolmcp.md`).

## Pre-publish checklist

- Exactly one `ai_languageModel` on each agent/chain/autofixing-parser/QA-tool.
- Ingest vs query embeddings model **identical**.
- Splitter→loader→vector-store chain uses `ai_textSplitter`/`ai_document`/`ai_embedding`, **not** `main`.
- Vector-store-as-tool node name has no special characters.
- Run `validate_workflow` (community `n8n-mcp`) — catches missing models and stray `main` links on sub-nodes.
- Confirm every `typeVersion` and `ai_*` connection string with `get_node` — LangChain nodes version frequently.
