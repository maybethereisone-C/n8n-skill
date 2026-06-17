# n8n Trigger — `n8n-nodes-base.n8nTrigger`
**Type** `n8n-nodes-base.n8nTrigger` · **trigger**

**What:** Fires when the containing workflow is published/updated, or when the n8n instance starts/restarts.

**Credentials:** none.

**Resources / Operations:** Trigger only.

**Key params & gotchas:**
- **Events** (select one or more): `Published Workflow Updated`, `Instance started`, `Workflow Published`.
- Scope is **self-referential** — only responds to events in its own workflow; changes to other workflows do not trigger it.
- Useful for bootstrapping tasks on instance restart or self-modifying workflow patterns.

**Source:** n8n-nodes-base.n8ntrigger.md  [doc-verified]
