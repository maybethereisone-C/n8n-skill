# Error Trigger — `n8n-nodes-base.errorTrigger`
**Type** `n8n-nodes-base.errorTrigger` · **typeVersion** 1 · **trigger**
**What:** Starts an error workflow when a linked workflow fails; receives the full failure context as input data.
**Credentials:** none.
**Trigger-on:** Failure of any workflow that has this workflow set as its Error Workflow (Settings → Error Workflow).

**Key params & gotchas:**
- No configurable parameters — the node is purely a receiver.
- To wire it up: open the *failing* workflow → Settings → Error Workflow → select the workflow containing this node. The error workflow does **not** need to be activated separately.
- If a workflow contains an Error Trigger, n8n automatically uses that same workflow as its own error workflow by default.
- Cannot be tested via manual execution — the Error Trigger only fires on automatic (production) execution failures.
- Use the [Stop And Error](n8n-nodes-base.stopAndError) node to push custom error messages into the payload received here.

**Error payload emitted (normal node failure):**
```json
[{
  "execution": {
    "id": "231",                          // absent if error is in the trigger node
    "url": "https://n8n.example.com/execution/231",  // absent if error is in the trigger node
    "retryOf": "34",                      // only present on retry executions
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
}]
```

**Error payload when the trigger node itself fails** (activation error — less `execution`, more `trigger`):
```json
{
  "trigger": {
    "error": {
      "context": {},
      "name": "WorkflowActivationError",
      "cause": { "message": "", "stack": "" },
      "timestamp": 1654609328787,
      "message": "",
      "node": { "...": "..." }
    },
    "mode": "trigger"
  },
  "workflow": { "id": "", "name": "" }
}
```

**Accessing fields downstream:**
- `{{ $json.execution.error.message }}` — the error message.
- `{{ $json.execution.lastNodeExecuted }}` — which node failed.
- `{{ $json.execution.url }}` — deep-link to the failed execution (requires DB persistence).
- `{{ $json.workflow.name }}` — name of the failed workflow.

**Source:** `n8n-nodes-base.errortrigger.md` + `_snippets/…/error-data.md`  [doc-verified]
