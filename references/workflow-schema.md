# n8n Workflow JSON Schema (v2.26.0)

> Purpose: the exact JSON shape an AI agent must emit for a valid n8n workflow — top-level fields, the node object, the connections-by-NAME contract, and the runtime data contract between nodes.

## Top-level anatomy

A workflow is one JSON object. `nodes` (array) and `connections` (object) are the load-bearing fields; the rest are metadata.

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `nodes` | array | yes | Each node object — see below. |
| `connections` | object | yes | Keyed by **source node NAME**. Empty `{}` is valid (single-node workflow). |
| `settings` | object | recommended | Execution config. `{}` is valid. See settings table. |
| `pinData` | object | no | Keyed by node NAME → array of pinned items `[{json:{...}}]`. Used for test/dev so a node returns fixed data instead of executing. |
| `staticData` | object\|null | no | Persisted state across executions (e.g. last-polled ID for trigger dedupe). `null` when unused. |
| `tags` | array | no | `[{ "name": "..." , "id": "..." }]`. Often `[]`. |
| `meta` | object | no | e.g. `{ "instanceId": "...", "templateCredsSetupCompleted": true }`. |
| `name` | string | API-side | Workflow title. Present in API payloads; absent in some hand-exports. |
| `active` | boolean | API-side | Do NOT rely on this on create — public `/api/v1/` ignores `active` on POST; activate via `POST /api/v1/workflows/{id}/activate`. |
| `id`, `versionId`, `createdAt`, `updatedAt` | — | runtime | Assigned by n8n. Never author these by hand. |

## The node object

```jsonc
{
  "parameters": { /* node-type-specific; shape depends on type + typeVersion */ },
  "name": "HTTP Request",          // UNIQUE per workflow; this string is the connection key
  "type": "n8n-nodes-base.httpRequest",  // full type id (see node-catalog.md)
  "typeVersion": 4.2,              // pin to the node's current max version
  "position": [400, 300],         // [x, y] canvas coords; purely visual, but required
  "id": "a1b2c3d4-0000-0000-0000-000000000001",  // UUID, unique per node
  "credentials": {                 // optional; keyed by credential type
    "httpHeaderAuth": { "id": "12", "name": "My Header Auth" }
  },
  "disabled": false,               // optional; skips the node when true
  "notes": "optional doc string",  // optional
  "continueOnFail": false          // optional; pass errors downstream instead of halting
}
```

Rules:
- `name` must be **unique** within the workflow — it is the primary key used by `connections`, `$node["Name"]`, and `pinData`.
- `id` must be a unique **UUID v4** per node. Do NOT use human-readable ids (`"http-1"`): n8n's editor binds form state and the credential picker by node id, so a non-UUID id causes subtle UI breakage (fields/credentials won't attach) even though the JSON imports fine.
- `credentials`: **omit the whole block if you don't have the real credential id.** A placeholder like `{ "id": "REPLACE_ME" }` permanently disables the credential selector in the UI ("no credentials yet") and forces node recreation. No block → n8n shows a clean "select credential" picker the user can fill.
- `type` + `typeVersion` together determine the legal `parameters` shape. Always look up the current max `typeVersion` (see node-catalog.md) — stale versions are a known autofix target and can silently drop parameters.
- `position` is `[x, y]`. Convention: trigger near `[250, 300]`, then step right by ~220px per node so the graph is readable. **Under `executionOrder: "v1"`, position is also the branch-order contract** — topmost (smallest `y`) branch runs first, ties leftmost (`x`). Not cosmetic; see execution-model.md.

### Node-level behavior settings (sibling to `parameters`, from the editor Settings tab)

These map to the UI node Settings tab (workflows/components/nodes.md) and live at node level, not inside `parameters`:

| Setting | Effect |
|---|---|
| **Always Output Data** | Node emits one empty item even when it would return nothing. Avoid on IF nodes — can cause an infinite loop. |
| **Execute Once** | Node runs a single time using only the **first** input item; ignores the rest. |
| **Retry On Fail** (`retryOnFail`, `maxTries`, `waitBetweenTries`) | On failure the node reruns itself until it succeeds, without restarting the workflow. |
| **On Error** (`onError`) | `stopWorkflow` halts everything; `continueRegularOutput` proceeds with the last valid data; `continueErrorOutput` proceeds and routes error info down a dedicated **error output** port. |

## connections — keyed by NAME (the #1 gotcha)

`connections` maps a **source node's NAME** → output type (`"main"`) → an array-of-arrays. The outer array is indexed by **output port** (port 0 first); each inner array lists every destination fed by that port.

```jsonc
"connections": {
  "Webhook": {
    "main": [
      [ { "node": "HTTP Request", "type": "main", "index": 0 } ]   // output 0 → HTTP Request input 0
    ]
  },
  "HTTP Request": {
    "main": [
      [ { "node": "IF", "type": "main", "index": 0 } ]
    ]
  },
  "IF": {
    "main": [
      [ { "node": "Slack", "type": "main", "index": 0 } ],          // output 0 = TRUE branch
      [ { "node": "NoOp",  "type": "main", "index": 0 } ]           // output 1 = FALSE branch
    ]
  }
}
```

- Each target entry: `{ "node": <target NAME>, "type": "main", "index": <target input port> }`.
- A single port can fan out to multiple targets — list them all in the same inner array.
- Multi-output nodes (IF, Switch) use multiple inner arrays — outer index = output port.
- **Rename gotcha:** because connections key on NAME (not id), renaming a node breaks every reference. If you rename `"HTTP Request"` → `"Fetch API"`, you MUST update: the `connections` top-level key, every `{ "node": ... }` that targets it, any `$node["HTTP Request"]` expressions, and any `pinData` key. The n8n editor does this automatically; an LLM editing raw JSON must do it manually.
- AI/LangChain nodes also use non-`main` connection types (e.g. `ai_languageModel`, `ai_tool`, `ai_memory`) under the same structure — sub-node NAME → `"ai_tool"` → `[[ { node, type, index } ]]`. These `ai_*` connections attach a sub-node *up* into a root node; the sub-node is pulled on demand and is NOT part of the main left→right execution order (see execution-model.md).
- The `index` in each target entry is the **target input port** — a multi-input node (e.g. Merge) is fed by setting different `index` values (port 0, 1, …). Source output port = outer-array index; target input port = the entry's `index`.

## Runtime data contract between nodes

Every node passes data as an **array of items**, each item wrapping its payload under `json` (plus optional `binary`):

```js
[
  { "json": { "orderId": 1, "total": 42 }, "binary": {} },
  { "json": { "orderId": 2, "total": 17 } }
]
```

- Reference the current item's payload in expressions as `$json` (e.g. `{{ $json.orderId }}`).
- **From n8n 0.166.0+**, Code/Function nodes auto-wrap a bare object in an array and auto-add a missing `json` key. **Custom-built nodes must add the `json` key themselves.** (data/data-structure.md)
- **Webhook payloads** arrive nested: the request body is under `$json.body` (also `$json.headers`, `$json.query`, `$json.params`).
- A node processes each item individually, applying its operation per item (e.g. 2 items in → 2 records created). Full item/binary/`pairedItem` contract lives in **data-and-binary.md**.

### binary data

Binary (files, images) lives under the item's `binary` key, keyed by a property name (default `data`):

```jsonc
{
  "json": { "fileName": "report.pdf" },
  "binary": {
    "data": {
      "data": "<base64>",          // payload (or a filesystem ref when binary-mode=filesystem)
      "mimeType": "application/pdf",
      "fileName": "report.pdf",
      "fileExtension": "pdf"
    }
  }
}
```

### paired items (item lineage)

Items carry `pairedItem` linkage so n8n can trace a downstream item back to the input item it derived from. This powers `$node["X"].json` lookups against the correct source item. Code nodes should preserve it when transforming 1:1 — return `{ json: {...}, pairedItem: { item: i } }` (index into `$input.all()`), or rely on auto-pairing for simple maps. Mismatched/missing pairing causes "Can't get data for expression" errors when a later node references an upstream node by name.

## settings fields

```jsonc
"settings": {
  "executionOrder": "v1",              // ALWAYS "v1" for modern workflows (deterministic order)
  "saveExecutionProgress": true,
  "saveManualExecutions": true,
  "saveDataSuccessExecution": "all",   // "all" | "none"
  "saveDataErrorExecution": "all",
  "errorWorkflow": "<workflowId>",     // run another workflow on failure
  "timezone": "America/New_York",      // overrides instance default; affects $now / Cron
  "executionTimeout": 3600             // seconds; -1 = no limit
}
```
Set `"executionOrder": "v1"` on every authored workflow — the legacy order is non-deterministic with branches.

## How an LLM should build the JSON

1. Pick node types. For each, look up the full `type` id and the **current max `typeVersion`** from node-catalog.md. Prefer a dedicated node over a Code node.
2. Build each node object: `parameters` (matching that type+version), unique `name`, `type`, `typeVersion`, `position` (lay out left→right), unique UUID `id`, plus `credentials`/`disabled` as needed.
3. Wire `connections` **by node NAME**, output-port-indexed. Multi-output nodes (IF/Switch) get one inner array per port.
4. Add `settings` (`executionOrder: "v1"`), and `pinData` only for test fixtures.
5. Self-check before emitting: every `connections` key and every `{ "node": ... }` target matches an existing node `name` exactly; node names and ids are unique; multi-output ports are ordered correctly; webhook reads use `$json.body`.

## Minimal complete example (Webhook → Set → Respond)

```json
{
  "name": "Echo Order",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "echo-order",
        "responseMode": "responseNode"
      },
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [250, 300],
      "id": "11111111-1111-1111-1111-111111111111"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            { "id": "f1", "name": "orderId", "type": "number", "value": "={{ $json.body.orderId }}" },
            { "id": "f2", "name": "status",  "type": "string", "value": "received" }
          ]
        },
        "options": {}
      },
      "name": "Set Fields",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [470, 300],
      "id": "22222222-2222-2222-2222-222222222222"
    },
    {
      "parameters": { "respondWith": "allIncomingItems", "options": {} },
      "name": "Respond",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1.1,
      "position": [690, 300],
      "id": "33333333-3333-3333-3333-333333333333"
    }
  ],
  "connections": {
    "Webhook":   { "main": [[ { "node": "Set Fields", "type": "main", "index": 0 } ]] },
    "Set Fields":{ "main": [[ { "node": "Respond",    "type": "main", "index": 0 } ]] }
  },
  "settings": { "executionOrder": "v1" },
  "staticData": null,
  "tags": []
}
```

## Import gotchas (verified on n8n v2.26.4)

- **CLI `import:workflow` requires a top-level `"id"`** in the file, or it fails with `SQLITE_CONSTRAINT: NOT NULL constraint failed: workflow_entity.id`. The UI "Import from File" auto-generates an id; the CLI does not. When emitting JSON for CLI import, include `"id"` (any unique string) + `"active": false`.
- A node's error/retry settings (`onError`, `retryOnFail`, `maxTries`, `waitBetweenTries`) live at the **node level**, sibling to `type`/`parameters` — not inside `parameters`. Verified: a workflow with these imported cleanly and n8n preserved `typeVersion` exactly (scheduleTrigger 1.2, set 3.4, httpRequest 4.2, googleSheets 4.7).
- Resource-locator params (documentId, sheetName) use the `{ "__rl": true, "value": "...", "mode": "id|list|url" }` shape.
