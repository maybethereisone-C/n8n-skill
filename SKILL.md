---
name: n8n
description: Build, debug, and operate production-grade n8n workflows. Use when the task mentions n8n, a workflow/automation, an n8n node, building/fixing/importing a workflow JSON, the AI Agent / LangChain nodes, or operating an n8n instance via MCP/REST API. Covers the full built-in node catalog, workflow JSON schema, expressions, Code nodes, plus error handling, logging, and security for ship-ready workflows.
---

# n8n — production-grade workflow builder

This skill makes you an expert n8n (v2.26.0) builder. It pulls the best of the public n8n skills into one place and adds the layer they omit: **error handling, logging, and security**. Default to building workflows that are production-ready, not just workflows that run.

## The production mandate (non-negotiable)

Every workflow you design or modify must satisfy these before you call it done:

1. **Right node, not HTTP-for-everything.** If a dedicated built-in node exists (e.g. `whatsApp`, `facebookGraphApi`, `gmail`, `slack`, `googleSheets`, `postgres`), use it instead of raw `httpRequest`. → `references/node-selection.md`
2. **Error handling.** Every workflow has an Error Workflow assigned; every node doing network I/O sets `retryOnFail` + `maxTries`; failures route or stop deliberately via `onError`. → `references/error-handling.md`
3. **Logging/observability.** Execution data + log env configured; a structured run-log row written for prod runs. → `references/logging-observability.md`
4. **Security.** No inline secrets — credentials only. Public webhooks require auth. SSRF/rate-limit guarded. → `references/security.md`
5. **Pinned typeVersions + validation.** Confirm each node's current typeVersion; run the ship gate — `python3 scripts/validate-workflow.py <file.json>` (JSON / node-field / connection-integrity / import-id checks). → `references/production-checklist.md`
6. **Resilience for long/flaky jobs.** If a workflow runs long, hits a quota-limited/flaky API, or processes many items: batches + checkpoint-resume + raw-first staging + idempotent writes + dead-letter + backoff — so a crash never re-pulls or duplicates work. → `references/resilience.md`

When you finish a workflow, run `references/production-checklist.md` as an actual gate.

## Build decision flow

```
1. Clarify the trigger (schedule / webhook / manual / app event) and the outcome.
2. For each step: search references/node-catalog.md for a DEDICATED node.
   - Found → read its deep guide references/node-guides/<type>.md (ops, gotchas, example). Not found → httpRequest (justified).
3. Wire nodes: connections are keyed by SOURCE NODE NAME (references/workflow-schema.md).
   Data flows as [{json:{...}}]. Use expressions (references/expressions.md) for dynamic values.
4. Add the production layer: error workflow, retries, logging, secured trigger.
5. Validate: typeVersions pinned, no inline secrets, ship-gate passed.
```

## Reference index — read the file that matches the task

Every reference is doc-grounded against the official n8n docs (v2.26). Read the one that matches; don't load all.

**Core authoring**
| File | Read when |
|---|---|
| `references/workflow-schema.md` | Workflow JSON shape, node object, connections-by-NAME, settings, import gotchas |
| `references/execution-model.md` | Execution order v1, item flow, branch ordering, main vs `ai_*` sub-nodes, determinism |
| `references/data-and-binary.md` | Item `{json,binary,pairedItem}` contract, lineage, binary modes, item linking |
| `references/expressions.md` | Every `$`-var (`$json`/`$node`/`$()`/`$now`…), Luxon, JMESPath, transform cookbook |
| `references/code-node.md` | Code node JS/Python (native runner) + AI Code Tool — exact return contracts |
| `references/code-cookbook.md` | Task→minimal Code snippet cookbook (aggregate, dedupe, paginate, binary…) |

**Nodes**
| File | Read when |
|---|---|
| `references/node-catalog.md` | Find a node / its type + max typeVersion (565 indexed) |
| `references/node-selection.md` | Choosing a node; resisting the HTTP-for-everything anti-pattern |
| `references/node-guides/<type>.md` | **Per-node deep guide for ~every built-in node** — ops, gotchas, minimal example. Grep this dir by node name first |
| `references/nodes-deep.md` | Cross-cutting deep config of the most-used nodes |
| `references/community-nodes.md` | Installing / using community (3rd-party) nodes |

**AI / LangChain**
| File | Read when |
|---|---|
| `references/ai-agent.md` | AI Agent + every `ai_*` sub-node (model/memory/tool/parser/embedding…), `$fromAI`, HITL |
| `references/ai-deep.md` | Chains vs agents, RAG pipeline wiring, vector stores, tools, evaluations, workflow-as-MCP-tool |
| `references/agent-craft.md` | **Judgment layer**: agent-vs-workflow decision, the 4 multi-agent architectures, orchestrator design, wireframe-first, context channels, scale vertically |
| `references/agent-prompting.md` | **Reactive prompting**: start-empty + one-change-at-a-time, the 5-component system-prompt skeleton |

**Flow & resilience**
| File | Read when |
|---|---|
| `references/flow-logic.md` | IF/Switch/Filter, Merge modes, Loop Over Items, Wait, sub-workflows |
| `references/error-handling.md` | Error workflow + Error Trigger payload, `onError`, retries, Stop And Error |
| `references/resilience.md` | Long/flaky/bulk jobs: batching, checkpoint-resume, idempotency, dead-letter, backoff |

**Ops**
| File | Read when |
|---|---|
| `references/logging-observability.md` | Every log surface: `N8N_LOG_*`, log streaming, exec data, Prometheus, OTel, Insights |
| `references/security.md` | Credentials, webhook auth, encryption key, external secrets, SSRF, RBAC, task-runner isolation |
| `references/env-vars.md` | **Full environment-variable reference (170+)**, grouped — the ops lookup table |
| `references/scaling.md` | Queue mode, workers, Redis, concurrency, multi-main HA, graceful shutdown |
| `references/production-checklist.md` | Final ship gate before declaring done |

**API & integration**
| File | Read when |
|---|---|
| `references/mcp-and-api.md` | Connect Claude to a live n8n; the 3 paths (n8n-mcp / native MCP / REST) |
| `references/rest-api.md` | Full public REST endpoint reference + scopes + n8n CLI surface |
| `references/webhooks.md` | Webhook lifecycle, response modes, Respond-to-Webhook, Wait/resume URLs |
| `references/execution-debugging.md` | Executions: list/inspect/retry/debug, partial vs production, pin data, custom data |
| `references/n8n-as-code.md` | User authors workflows as TypeScript (native SDK / n8n-as-code); why we stay JSON-first |
| `references/template-sources.md` | Where to get ready-made templates (official lib, top GitHub repos) |

## Templates (~2,390, topic-organized)

`templates/` holds ~2,390 secret-scrubbed reference workflows in 19 topic folders (AI-Agents, RAG-and-Vector, Gmail-and-Email, Slack, Telegram, WhatsApp, Discord, Social-Media, Google-Sheets-and-Drive, Notion, Airtable, Database, Forms-and-Surveys, PDF-and-Documents, HR-and-Recruitment, WordPress, DevOps, Web-Scraping, Other-Integrations). Each folder has a README. Find one fast:
```
python3 scripts/search-templates.py search "<query>"     # FTS over all topics
python3 scripts/validate-workflow.py <file.json>         # before reuse
```
Treat as references — `credentials` are id-refs (remap to yours), and apply the production layer before shipping. Master index: `templates/README.md`.

## Operating a live instance

To create/edit workflows on a running n8n: prefer the **community n8n-mcp** server (search/validate/manage) or n8n's **native built-in MCP** (generates TypeScript, self-validates). Fall back to the **REST API** `/api/v1/` with header `X-N8N-API-KEY` (activate via `POST /api/v1/workflows/{id}/activate`). Note the nodeType format gotcha: search/validate tools use `nodes-base.slack`; workflow JSON uses `n8n-nodes-base.slack`. → `references/mcp-and-api.md`

## Scripts (stdlib, no deps)

- `validate-workflow.py <file.json …>` — ship gate: JSON, node fields, connection integrity, import-id, trigger checks. Exit 1 on FAIL.
- `workflow-to-mermaid.py <file.json>` — render a workflow as a Mermaid `graph TD` for review/docs.
- `search-templates.py index | search "<q>"` — SQLite-FTS search over bundled `templates/`.
- `extract-schemas.py [N8N_SRC]` — regenerate the 540 per-node schemas + `node-catalog.md`.
- `index-nodes.py` / `index-templates.py` — lighter catalog/template indexers.
- `run-evals.py validate | list | show <id>` — behavioral self-tests (`evals/`): query→expected-behavior checklists that prove a gotcha is still taught. `validate` is the CI gate. Add an eval when you add a gotcha.

Re-run `extract-schemas.py` after upgrading n8n. (Some adapted from Zie619/n8n-workflows, MIT.)
