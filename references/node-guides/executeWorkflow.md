# Execute Sub-workflow — `n8n-nodes-base.executeWorkflow`
**Type** `n8n-nodes-base.executeWorkflow` · **typeVersion** 1.3 · **action / core**
**What:** Calls another n8n workflow as a sub-workflow, optionally passing input data and waiting for its result.
**Credentials:** none.

**Source modes (`source` param):**
| Value | What to supply | Notes |
|---|---|---|
| `database` | Workflow ID (from list or manual entry) | Most common; ID is the alphanumeric string after `/workflow/` in the URL |
| `parameter` | Inline JSON (`workflowJson`) | Embed a workflow definition directly; useful for dynamic/generated workflows |
| `url` | URL (`workflowUrl`) | Loads workflow JSON from a remote URL at execution time |
| `localFile` | File path (`workflowPath`) | Only works on self-hosted n8n with filesystem access |

**Passing input data:**
- When `source=database` + **From list**, the sub-workflow's declared input fields auto-populate as `workflowInputs` — fill or map them.
- If the sub-workflow's Execute Workflow Trigger uses **"Accept all data"** mode, the `workflowInputs` mapper is hidden and all incoming items are forwarded as-is.
- Omitted inputs arrive as `null` in the sub-workflow; enable **Attempt to convert types** to coerce types automatically.

**Mode param:**
- `once` — all input items are bundled into one sub-workflow execution.
- `each` — one sub-workflow execution is spawned per input item (fan-out).

**Wait for sub-workflow (`options.waitForSubWorkflow`):**
- `true` (default) — parent pauses until sub-workflow completes; output items from sub-workflow flow back to parent.
- `false` — parent continues immediately (fire-and-forget); no output from sub-workflow is returned.

**Key gotchas:**
- The sub-workflow must have an **Execute Workflow Trigger** (`n8n-nodes-base.executeWorkflowTrigger`) as its start node — a Webhook or other trigger will not receive calls from this node.
- Error isolation: if the sub-workflow errors and `waitForSubWorkflow=true`, the error propagates to the parent. Set up error handling in the parent or use `waitForSubWorkflow=false` to isolate.
- typeVersion 1.3 — if the node in a workflow shows an "out of date" notice, remove and re-add it to get the latest version with `workflowInputs` mapper support.
- Sub-workflows run in the same n8n instance; this node cannot call workflows on a different n8n instance.
- Credentials used inside the sub-workflow must be accessible to the sub-workflow's owner, not just the parent workflow's owner.

**Minimal example (database, wait):**
```json
{
  "type": "n8n-nodes-base.executeWorkflow",
  "parameters": {
    "source": "database",
    "workflowId": { "__rl": true, "value": "abCDE1f6gHiJKL7", "mode": "id" },
    "options": { "waitForSubWorkflow": true }
  }
}
```

**Source:** `n8n-nodes-base.executeworkflow.md`  [doc-verified]
