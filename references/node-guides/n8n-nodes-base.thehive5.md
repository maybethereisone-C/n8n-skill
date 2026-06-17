# TheHive 5 — `n8n-nodes-base.thehive5`
**Type** `n8n-nodes-base.thehive5` · **typeVersion** 1 · **action**
**What:** Manage security incident response resources in TheHive v5 — alerts, cases, observables, tasks, comments, pages, and task logs.
**Credentials:** `theHive5Api`
**Resources / Operations:**
| Resource | Operations |
|---|---|
| Alert | Create, Delete, Execute Responder, Get, Merge Into Case, Promote to Case, Search, Update, Update Status |
| Case | Add Attachment, Create, Delete Attachment, Delete Case, Execute Responder, Get, Get Attachment, Get Timeline, Search, Update |
| Comment | Create, Delete, Search, Update |
| Observable | Create, Delete, Execute Analyzer, Execute Responder, Get, Search, Update |
| Page | Create, Delete, Search, Update |
| Query | Execute Query |
| Task | Create, Delete, Execute Responder, Get, Search, Update |
| Task Log | Add Attachment, Create, Delete, Delete Attachment, Execute Responder, Get, Search |

**Key params & gotchas:**
- **Use for TheHive API v5 only.** For v3/v4, use `n8n-nodes-base.thehive`.
- Alert→Promote to Case converts a triaged alert into a full case automatically.
- Execute Responder / Execute Analyzer operations call TheHive's Cortex integration — requires Cortex to be configured.
- Query→Execute Query allows raw TheHive query language for complex filtering not covered by other operations.
- Companion trigger: `n8n-nodes-base.thehive5Trigger`.

**Source:** n8n-nodes-base.thehive5.md  [doc-verified]
