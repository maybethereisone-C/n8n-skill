# Activation Trigger — `n8n-nodes-base.activationTrigger`

**Type** `n8n-nodes-base.activationTrigger` · **typeVersion** 1 · **trigger**

**What:** Fires when the workflow itself is activated, updated, or when n8n starts — useful for self-notification on workflow state changes. **Deprecated** — replaced by the n8n Trigger and Workflow Trigger nodes.

**Credentials:** None.

**Resources / Operations (trigger events):**

| Event | Fires When |
|-------|-----------|
| Activation | Workflow is published (activated) |
| Start | n8n instance starts or restarts |
| Update | Workflow is saved while active |

**Key params & gotchas:**
- **Deprecated**: use `n8n-nodes-base.n8nTrigger` or `n8n-nodes-base.workflowTrigger` for new workflows.
- The trigger fires for the workflow it is *added to* — no need for a separate error/notification workflow.
- Cannot be tested via manual runs; only fires on real activation/update/restart events.
- If the workflow contains this node, it uses itself as the triggered workflow (no external linkage needed).

**Source:** n8n-nodes-base.activationtrigger.md  [doc-verified]
