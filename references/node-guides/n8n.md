# n8n — `n8n-nodes-base.n8n`
**Type** `n8n-nodes-base.n8n` · **core**

**What:** Consumes the n8n REST API to manage workflows, executions, and credentials from within a workflow.

**Credentials:** n8n API credential (API key). Does not support SSL — use HTTP Request node for SSL-required instances.

**Resources / Operations:**
| Resource | Operations |
|----------|-----------|
| Audit | Generate (security audit by category) |
| Credential | Create, Delete, Get Schema |
| Execution | Get, Get Many (filterable by workflow/status), Delete |
| Workflow | Publish, Create, Deactivate, Delete, Get, Get Many, Update |

**Key params & gotchas:**
- **Audit → Categories**: Credentials, Database, Filesystem, Instance, Nodes. **Days Abandoned Workflow** defaults to 90.
- **Create Credential → Data** must be a valid JSON object matching the credential type's schema — use Get Schema first.
- **Get Many Executions → Filters**: workflow (list/URL/ID), status (Error/Success/Waiting).
- **Create/Update Workflow → Workflow Object** requires `name`, `nodes`, `connections`, `settings` fields.
- **Get Many Workflows → Filters**: active-only toggle, tags list.
- No SSL support — if the n8n instance requires HTTPS, use the HTTP Request node instead.

**Source:** n8n-nodes-base.n8n.md  [doc-verified]
