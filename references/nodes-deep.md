# Nodes Deep Dive — The ~35 Most-Used Nodes

> Purpose: per-node production guidance for building workflows. Each entry: type, use, key params, snippet, prod tip. Pin `typeVersion` to the catalog `maxVer`; confirm with `get_node` (the indexer under-reports some versions). Inter-node data is always `[{ "json": {...} }]`.

## Triggers

**Manual Trigger** — `n8n-nodes-base.manualTrigger` (v1)
Dev/testing entry point. No params. Replace with a real trigger before publishing.

**Schedule Trigger** — `n8n-nodes-base.scheduleTrigger` (v1.3)
Cron/interval runs. Key: `rule.interval` (seconds/minutes/hours/days, or cron expression).
```json
{ "type": "n8n-nodes-base.scheduleTrigger", "typeVersion": 1.3,
  "parameters": { "rule": { "interval": [{ "field": "cronExpression", "expression": "0 9 * * 1-5" }] } } }
```
Prod tip: cron uses the instance timezone (`settings.timezone`). One trigger per workflow.

**Webhook** — `n8n-nodes-base.webhook` (v2.1)
Inbound HTTP entry. Key: `httpMethod`, `path`, `responseMode` (`onReceived` | `lastNode` | `responseNode`), `authentication`.
```json
{ "type": "n8n-nodes-base.webhook", "typeVersion": 2.1,
  "parameters": { "httpMethod": "POST", "path": "lead-intake", "responseMode": "responseNode" } }
```
Prod tip: **payload is under `$json.body`**, headers under `$json.headers`. Set `authentication` (header/basic) — don't ship open webhooks. Use `responseNode` + Respond to Webhook for custom responses.

**Service triggers** — `gmailTrigger` (v1.4, polling), `telegramTrigger` (v1.3), `slackTrigger` (v1), `postgresTrigger` (v1), `airtableTrigger`, `notionTrigger`, `whatsAppTrigger`.
Prod tip: polling triggers (Gmail/Airtable) cost an interval of latency; push/webhook triggers (Telegram/Slack) are near-instant. Prefer push when offered.

## Core / Control

**Edit Fields (Set)** — `n8n-nodes-base.set`
Set, rename, or compute fields. Use `assignments` (typed) mode. `includeOtherFields` to pass through untouched fields.
```json
{ "type": "n8n-nodes-base.set", "typeVersion": 3.4,
  "parameters": { "assignments": { "assignments": [
    { "name": "fullName", "type": "string", "value": "={{ $json.first }} {{ $json.last }}" } ] } } }
```
Prod tip: prefer Set over a Code node for simple field shaping — readable + validatable.

**If** — `n8n-nodes-base.if`
Two outputs (true/false). `conditions` with typed operators.
Prod tip: validate tools use smart param `branch:"true"`. For 3+ branches use Switch, not nested Ifs.

**Switch** — `n8n-nodes-base.switch`
N outputs by rules or expression. Key: `mode` (`rules`|`expression`), `rules.values`, `fallbackOutput`.
Prod tip: set a fallback output so unmatched items aren't silently dropped.

**Merge** — `n8n-nodes-base.merge`
Combine two inputs. `mode`: `append` | `combine` (by key / by position) | `chooseBranch`.
Prod tip: `combine` + `combineBy: combineByFields` to join on a key (n8n's "SQL join"); set the matching field on both inputs.

**Filter** — `n8n-nodes-base.filter`
Keep items matching conditions (single output; non-matches discarded). Use when you only want survivors; use If when you need both branches.

**Code** — `n8n-nodes-base.code` (v2)
JS/Python custom logic. `mode`: `runOnceForAllItems` (default) | `runOnceForEachItem`.
```json
{ "type": "n8n-nodes-base.code", "typeVersion": 2,
  "parameters": { "language": "javaScript",
    "jsCode": "return items.map(i => ({ json: { id: i.json.id, total: i.json.qty * i.json.price } }));" } }
```
Prod tip: **must return `[{ json: {...} }]`** (array of wrapped objects). Reach for Code only when no node/expression does it. (This is the regular Code node — the AI **Code Tool** has a different contract; see `ai-agent.md`.)

**Loop Over Items (Split In Batches)** — `n8n-nodes-base.splitInBatches`
Process items in chunks. Key: `batchSize`. Wire the loop output back into itself; the "done" output continues.
Prod tip: use for rate-limited APIs — batch + a Wait node between iterations.

**Wait** — `n8n-nodes-base.wait`
Pause: time, webhook resume, or until a timestamp. Prod tip: pairs with Loop for backoff; pairs with Webhook resume for human-in-the-loop approvals.

**No Operation** — `n8n-nodes-base.noOp` (v1)
Passthrough / merge point / readability marker. No effect on data.

**Execute Sub-workflow** — `n8n-nodes-base.executeWorkflow` (v1.3)
Call another workflow as a function. Key: `workflowId`, `mode`. Pairs with `executeWorkflowTrigger` in the child.
Prod tip: extract shared logic (auth, notify, error handling) into sub-workflows — DRY across workflows.

**Respond to Webhook** — `n8n-nodes-base.respondToWebhook`
Returns the HTTP response for a Webhook with `responseMode: responseNode`. Key: `respondWith` (json/text/binary/noData), `responseCode`.
Prod tip: exactly one per request path; place at the true end of the branch.

## Data Transform

**Split Out** — `n8n-nodes-base.splitOut` (v1)
One item with an array field → one item per element. Key: `fieldToSplitOut`.

**Aggregate** — `n8n-nodes-base.aggregate` (v1)
Many items → one item (collect a field into an array, or all data). Inverse of Split Out. Key: `aggregate`, `fieldsToAggregate`.

**Remove Duplicates** — `n8n-nodes-base.removeDuplicates` (v1)
Dedupe within input, or across runs (persisted history). Key: `compare`, `fieldsToCompare`.

**Limit** — `n8n-nodes-base.limit` (v1)
Cap item count. Key: `maxItems`. Prod tip: guardrail before expensive downstream calls.

## Comms / SaaS

**Gmail** — `n8n-nodes-base.gmail`
Resource/operation model. Send: `resource: message`, `operation: send`, `sendTo`, `subject`, `message`. Credential `gmailOAuth2`.
Prod tip: use the node, not SMTP, for Gmail — OAuth + threading handled.

**Slack** — `n8n-nodes-base.slack`
`resource: message`, `operation: post`; `channel`, `text` (or Blocks). Credential `slackOAuth2Api` or `slackApi`.
Prod tip: use channel ID over name; enable retry on rate-limit (429).

**Telegram** — `n8n-nodes-base.telegram` (v1.2)
`resource: message`, `operation: sendMessage`; `chatId`, `text`, `parse_mode`. Credential `telegramApi` (bot token).

**WhatsApp Business Cloud** — `n8n-nodes-base.whatsApp` (v1.1)
Send messages/templates via Meta Cloud API. `operation: send`, `phoneNumberId`, `recipientPhoneNumber`.
Prod tip: outside the 24h session window you can only send approved **templates**, not free-form text.

**Facebook Graph API** — `n8n-nodes-base.facebookGraphApi`
Generic Graph calls (page posts, insights). `httpRequestMethod`, `graphApiVersion`, `node`, `edge`. Credential `facebookGraphApi`.

**HTTP Request** — `n8n-nodes-base.httpRequest`
Fallback for APIs with no node. Key: `method`, `url`, `authentication` (use a predefined credential preset), `sendBody`, `pagination`.
Prod tip: turn on built-in **pagination** instead of looping manually; set retry/timeout. See `node-selection.md` for when this is justified.

## Database

**Postgres** — `n8n-nodes-base.postgres`
`operation`: `select` | `insert` | `update` | `upsert` | `executeQuery`. Credential `postgres`.
```json
{ "type": "n8n-nodes-base.postgres", "typeVersion": 2.6,
  "parameters": { "operation": "executeQuery",
    "query": "SELECT * FROM orders WHERE status = $1", "options": { "queryReplacement": "=pending" } } }
```
Prod tip: **always parameterize** (`$1`, query replacement) — never string-concat user data (SQL injection). Use `insert`/`upsert` ops over raw SQL when possible.

**MySQL** — `n8n-nodes-base.mySql`
Same op model as Postgres; parameterize identically. Credential `mySql`.

## AI (see ai-agent.md for full wiring)

**AI Agent** — `@n8n/n8n-nodes-langchain.agent` (v3.1)
Root agent (Tools Agent). Connect chat model, memory, tools, output parser via **non-`main`** connections. Key: `promptType`, `text`, `options.systemMessage`.

**Chat models** — `lmChatOpenAi`, `lmChatAnthropic`, `lmChatGoogleGemini`, etc. Sub-nodes; connect to the agent via `ai_languageModel`. Confirm `typeVersion` with `get_node`.

**Simple Memory** — `@n8n/n8n-nodes-langchain.memoryBufferWindow` (v1.4)
Window buffer. Connect via `ai_memory`. Key: `sessionKey`, `contextWindowLength`.

**Tools** — `toolHttpRequest` (v1.1), `toolWorkflow` (v1), `toolCode` (v1.3). Connect via `ai_tool`. The agent decides when to call them.

**Structured Output Parser** — `@n8n/n8n-nodes-langchain.outputParserStructured` (v1.3)
Forces JSON output to a schema. Connect via `ai_outputParser`.
