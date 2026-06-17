# Execute Sub-workflow Trigger — `n8n-nodes-base.executeWorkflowTrigger`
**Type** `n8n-nodes-base.executeWorkflowTrigger` · **trigger**

**What:** Starts a workflow when called by another workflow via Execute Sub-workflow or Call n8n Workflow Tool nodes.

**Credentials:** none.

**Resources / Operations:** Trigger only — no configurable operations.

**Key params & gotchas:**
- Must be the first node in the workflow.
- Fired by `n8n-nodes-base.executeWorkflow` or `n8n-nodes-langchain.toolWorkflow`; cannot be triggered by URL or schedule.
- Data passes in from the calling workflow and is available as normal `$json` items on output.
- Useful for breaking large workflows into reusable sub-workflows.

**Source:** n8n-nodes-base.executeworkflowtrigger.md  [doc-verified]
