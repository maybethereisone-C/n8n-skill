# Error Handling (n8n v2.26.0)

> Node-level error/retry controls, the dedicated Error Workflow pattern, and deliberate-failure wiring for production workflows.

## Node-level error model

Every node carries error/retry fields at the **node level** (siblings of `parameters`, `type`), not inside `parameters`.

| Field | Type | Values / range | Purpose |
|---|---|---|---|
| `onError` | enum | `continueRegularOutput` \| `continueErrorOutput` \| `stopWorkflow` | What happens when the node throws. Modern replacement for legacy `continueOnFail` boolean. |
| `retryOnFail` | bool | — | Retry the node before treating it as failed. |
| `maxTries` | int | 2–5 | Number of attempts when `retryOnFail` is true. |
| `waitBetweenTries` | int | ms | Delay between retries. |
| `alwaysOutputData` | bool | — | Emit an item even on empty/failed result (so downstream still runs). |
| `executeOnce` | bool | — | Run node once for the first item only, ignore the rest. |

### `onError` decision table

| Value | Behavior | Use when |
|---|---|---|
| `stopWorkflow` | Throw, halt the execution, mark it failed (triggers the error workflow). **Default.** | The step is critical; downstream is meaningless without it (auth, required DB write). |
| `continueErrorOutput` | Node grows a 2nd output (error branch); failed items route there, good items continue on output 1. | You want to handle/quarantine failures inline (route to dead-letter, log, retry path). |
| `continueRegularOutput` | Failed item flows out the normal output with an `error` property; workflow continues. | Best-effort enrichment where a failure is non-fatal and you tolerate partial data. |

### JSON example — network node with retry + error branch

```json
{
  "parameters": {
    "method": "GET",
    "url": "https://api.example.com/v1/orders"
  },
  "type": "n8n-nodes-base.httpRequest",
  "typeVersion": 4.2,
  "name": "Fetch Orders",
  "onError": "continueErrorOutput",
  "retryOnFail": true,
  "maxTries": 3,
  "waitBetweenTries": 2000,
  "alwaysOutputData": true
}
```

**RULE:** any node doing network I/O (HTTP Request, API nodes, DB nodes) MUST set `retryOnFail: true` with `maxTries` 3–5 and a non-zero `waitBetweenTries` (backoff). Transient 429/5xx/timeout are the common case.

### `continueOnFail` — legacy naming

Prior to v1.x, the field was a boolean called `continueOnFail`. In v2.x it was replaced by the `onError` enum. `continueOnFail: true` maps to `onError: "continueRegularOutput"`. The legacy field still deserialises but the UI always writes `onError`. Do not write new workflows with `continueOnFail`.

### Error output branch wiring

When `onError` is `continueErrorOutput`, the node exposes a second output index (`1`). Wire the error branch in `connections` from output index `1`:

```json
"connections": {
  "Fetch Orders": {
    "main": [
      [ { "node": "Process Orders", "type": "main", "index": 0 } ],
      [ { "node": "Quarantine + Log", "type": "main", "index": 0 } ]
    ]
  }
}
```

`main[0]` = success items, `main[1]` = error items. The error item carries an `error` object describing the failure.

## Dedicated Error Workflow pattern

A workflow that contains an **Error Trigger** node becomes an "error workflow". Build **one** and assign it to every production workflow.

- Trigger node type: `n8n-nodes-base.errorTrigger`
- Assign per-workflow: **Workflow Settings → Error Workflow** (select the error workflow). It fires whenever that workflow's execution fails (any node with `onError: stopWorkflow` that throws, or an uncaught error).

### Error Trigger payload shape

Source: `_snippets/integrations/builtin/core-nodes/error-trigger/error-data.md`

**Standard execution failure** (most common — any node after the trigger throws):

```json
{
  "execution": {
    "id": "231",
    "url": "https://n8n.example.com/execution/231",
    "retryOf": "34",
    "error": {
      "message": "Example Error Message",
      "stack": "Stacktrace"
    },
    "lastNodeExecuted": "Node With Error",
    "mode": "manual"
  },
  "workflow": {
    "id": "1",
    "name": "Example Workflow"
  }
}
```

Field presence rules:
- `execution.id` / `execution.url` — only present when the execution was saved to the DB. Absent if the trigger node itself failed (workflow never started).
- `execution.retryOf` — only present when the execution is a retry of a prior failed run.

**Trigger-node failure** (error in the workflow's own trigger, e.g. a webhook misconfiguration on activation). The payload shape is different — `execution{}` is minimal; `trigger{}` carries the detail:

```json
{
  "trigger": {
    "error": {
      "context": {},
      "name": "WorkflowActivationError",
      "cause": { "message": "", "stack": "" },
      "timestamp": 1654609328787,
      "message": "",
      "node": { }
    },
    "mode": "trigger"
  },
  "workflow": { "id": "", "name": "" }
}
```

Handle both shapes in your error workflow: check `$json.trigger` exists to distinguish trigger failures from execution failures.

### Reference error workflow

`Error Trigger` → (notify) Slack/email → (audit) append a log row to Sheets/Postgres.

```json
{
  "nodes": [
    {
      "parameters": {},
      "type": "n8n-nodes-base.errorTrigger",
      "typeVersion": 1,
      "name": "Error Trigger"
    },
    {
      "parameters": {
        "select": "channel",
        "text": "=:rotating_light: *{{ $json.workflow.name }}* failed\nNode: {{ $json.execution.lastNodeExecuted }}\nError: {{ $json.execution.error.message }}\nExecution: {{ $json.execution.url }}"
      },
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "name": "Notify Slack",
      "onError": "continueRegularOutput"
    },
    {
      "parameters": {
        "operation": "append",
        "columns": {
          "value": {
            "timestamp": "={{ $now.toISO() }}",
            "workflow": "={{ $json.workflow.name }}",
            "node": "={{ $json.execution.lastNodeExecuted }}",
            "error": "={{ $json.execution.error.message }}",
            "execution_url": "={{ $json.execution.url }}"
          }
        }
      },
      "type": "n8n-nodes-base.googleSheets",
      "typeVersion": 4.5,
      "name": "Append Error Log"
    }
  ],
  "connections": {
    "Error Trigger": { "main": [[
      { "node": "Notify Slack", "type": "main", "index": 0 },
      { "node": "Append Error Log", "type": "main", "index": 0 }
    ]]}
  }
}
```

Set the notify/log nodes themselves to `continueRegularOutput` so a Slack outage doesn't suppress the audit row.

## Deliberate failures & guards

### `stopAndError` — throw on purpose

Source: `docs/flow-logic/error-handling.md` — "Cause a workflow execution failure using Stop And Error"

Use `n8n-nodes-base.stopAndError` to fail the execution intentionally (invalid state, business-rule violation) so it surfaces in the error workflow rather than passing bad data downstream. The node takes a single `errorMessage` parameter (supports expressions). Two modes: **Error Message** (string) and **Error Object** (JSON with `message` + optional `description`).

### Try/catch in Code node

In a Code node (Run Once For Each Item or Run Once For All Items), wrap risky logic in a standard try/catch. To route to the error branch from code, throw an error — if the node's `onError` is `continueErrorOutput` the thrown error lands on `main[1]`. To emit partial results and continue, catch the error, attach it to the item, and return the item normally:

```js
// Run Once For Each Item — soft-fail with error attached
try {
  const result = riskyTransform($input.item.json);
  return { json: result };
} catch (e) {
  return { json: { ...$input.item.json, _error: e.message } };
}
```

To hard-fail from code and trigger the error workflow, re-throw (or don't catch) — the Code node will propagate the exception through `onError: stopWorkflow`.

```json
{
  "parameters": {
    "errorMessage": "=Order {{ $json.id }} has no customer email — aborting"
  },
  "type": "n8n-nodes-base.stopAndError",
  "typeVersion": 1,
  "name": "Abort: missing email"
}
```

### IF-node guard pattern

Validate before acting. Route invalid items to `stopAndError` (hard fail) or a quarantine branch (soft handle).

```
IF (email is empty / amount <= 0 / status != "ready")
  ├─ true  → Stop And Error  (or → Quarantine + Log)
  └─ false → continue happy path
```

Prefer guards over relying on a downstream node to coincidentally fail — guards give clear, attributable error messages.

## Production rule

**Every production workflow MUST:**
1. Have an Error Workflow assigned in Workflow Settings.
2. Set `retryOnFail` + `maxTries` (3–5) + `waitBetweenTries` on every node doing network I/O.
3. Use `continueErrorOutput` to quarantine recoverable failures inline; `stopWorkflow` for critical steps; `stopAndError` for business-rule violations.
