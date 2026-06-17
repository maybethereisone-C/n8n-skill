# Workflow Trigger — `n8n-nodes-base.workflowtrigger`

**Type** `n8n-nodes-base.workflowtrigger` · **typeVersion** 1 · **trigger**

**What:** Triggers when the workflow it belongs to is activated or updated. Deprecated — use the n8n Trigger node (`n8n-nodes-base.n8nTrigger`) instead.

**Credentials:** none.

**Resources / Operations:**

| Event | Description |
|---|---|
| Active Workflow Updated | Fires when this workflow is saved while active |
| Workflow Activated | Fires when this workflow is activated |

**Key params & gotchas:**

- **Deprecated** — n8n has moved this functionality to the `n8n-nodes-base.n8nTrigger` node. Do not use in new workflows.
- The node triggers for the same workflow it is added to, not for external workflows.
- Both events can be selected simultaneously.

**Source:** n8n-nodes-base.workflowtrigger.md  [doc-verified]
