# Course-Examples — pedagogical workflow index

24 workflows that teach "how to think" about n8n AI patterns.
These are the conceptual layer; the scraped library in other `templates/` folders is the breadth layer.

| # | File | Pattern it teaches |
|---|------|--------------------|
| 1 | `1) RAG Pipeline & Chatbot.json` | RAG ingestion + retrieval — Google Drive trigger → chunk → embed (OpenAI) → Pinecone → chat agent |
| 2 | `2) Customer Support Workflow.json` | Classify-then-route — Gmail trigger → text classifier → RAG lookup → reply |
| 3 | `3) LinkedIn Workflow.json` | Social-media automation — form/schedule trigger → content generation → post |
| 4 | `4) Invoice Workflow.json` | Document processing — extract structured data from PDF/email attachment → store |
| 5 | `5) API Calls in n8n.json` | HTTP node patterns — auth, pagination, error-handling in plain HTTP request nodes |
| 6 | `6) Perplexity.json` | LLM-as-search — calling Perplexity API as a research tool node inside an agent |
| 7 | `7) Firecrawl Extract Template.json` | Web scraping to structured data — Firecrawl → LLM extraction → output schema |
| 8 | `8) Apify.json` | Managed scraping actor — trigger Apify run, poll for result, parse dataset |
| 9 | `9) OpenAI Image Gen.json` | Multimodal output — prompt → DALL-E/GPT-4o image → store/send |
| 10 | `10) Product Videos.json` | Long async pipeline — form trigger → agent → convert/render → Drive → Gmail (uses Wait node) |
| 11 | `11) RAG Workflow vs RAG Agent.json` | RAG workflow vs RAG agent comparison — side-by-side: deterministic retrieval chain vs agent-driven retrieval |
| 12 | `12) Technical Analyst Agent vs Workflow.json` | Agent vs workflow decision — Telegram trigger → sub-workflow tools vs direct LLM call |
| 13 | `13) First AI Agent.json` | Minimal tool-calling agent — chat trigger + Gmail/Calendar/Sheets tools + memory |
| 14 | `14) Supabase Postgres.json` | Postgres-backed RAG — vectorStoreSupabase + pgvector + memoryPostgresChat for persistent sessions |
| 15 | `15) Orchestrator Architecture.json` | Orchestrator pattern — master agent delegates to specialist sub-agents via toolWorkflow |
| 16 | `16) Prompt Chaining.json` | Sequential prompt chaining — multi-LLM chain (Anthropic → DeepSeek → Gemini → OpenAI) with Google Docs I/O |
| 17 | `17) Routing.json` | LLM-based routing — Gmail trigger → textClassifier → branch to Gmail or Telegram tool |
| 18 | `18) Parallelization.json` | Parallel fan-out — chat trigger → split → parallel LLM calls → aggregate/merge |
| 19 | `19) Evaluator Optimizer.json` | Evaluator-optimizer loop — generator agent + critic agent + if-node retry until quality threshold |
| 20 | `20) HITL Example Flows.json` | Human-in-the-loop (HITL) — Telegram approval gate mid-workflow before agent continues |
| 21 | `21) Error Logger.json` | Error handling & logging — errorTrigger → Google Sheets log + Slack alert |
| 22 | `22) Dynamic Brain.json` | Dynamic tool selection — agent chooses tools at runtime based on task context |
| 23 | `23) Voice Email Agent.json` | Voice + async webhook — voice input → STT → agent → reply via email (voice-webhook pattern) |
| AI | `AI-Mention-Tracker-Simple.json` | Async polling — schedule trigger monitors external source for keyword mentions, stores hits |

## How to use these

1. **Before building a new AI workflow**, find the closest pattern above and open that JSON in n8n to study the node graph.
2. **Patterns 11 & 12** are the most important for decision-making: they show exactly when to use an agent vs a fixed workflow.
3. **Pattern 15** (Orchestrator) + **Pattern 18** (Parallelization) together cover multi-agent fan-out architecture.
4. **Patterns 19–20** cover quality control: evaluator-optimizer for automated quality loops, HITL for human checkpoints.
5. **Pattern 21** (Error Logger) should be adapted and attached to every production workflow.
