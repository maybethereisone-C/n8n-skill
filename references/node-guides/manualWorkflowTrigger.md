# Manual Trigger — `n8n-nodes-base.manualWorkflowTrigger`
**Type** `n8n-nodes-base.manualWorkflowTrigger` · **trigger**

**What:** Starts a workflow manually via the "Execute Workflow" button; no automatic triggering.

**Credentials:** none.

**Resources / Operations:** Trigger only — no configuration.

**Key params & gotchas:**
- Only one Manual Trigger node is allowed per workflow; adding a second causes an error.
- Use for testing or workflows that should never run automatically.
- Provides no input data — downstream nodes receive an empty item.

**Source:** n8n-nodes-base.manualworkflowtrigger.md  [doc-verified]
