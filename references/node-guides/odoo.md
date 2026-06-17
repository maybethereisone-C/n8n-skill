# Odoo — `n8n-nodes-base.odoo`
**Type** `n8n-nodes-base.odoo` · **typeVersion** 1 · **action**
**What:** Automate Odoo ERP: manage contacts, notes, CRM opportunities, and arbitrary Odoo models via the JSON-RPC API.
**Credentials:** Odoo API (`odooApi`) — URL, database name, username, password (or API key in v14+).
**Resources / Operations:**
| Resource | Operations |
|---|---|
| Contact | Create, Delete, Get, Get All, Update |
| Custom Resource | Create, Delete, Get, Get All, Update |
| Note | Create, Delete, Get, Get All, Update |
| Opportunity | Create, Delete, Get, Get All, Update |

**Key params & gotchas:**
- **Custom Resource** lets you target any Odoo technical model name (e.g., `sale.order`, `account.move`) — powerful for non-standard modules.
- Field names must match Odoo's technical field names (e.g., `partner_id`, `date_order`), not display labels.
- Odoo authentication uses the XML-RPC or JSON-RPC `/web/dataset/call_kw` endpoint — the credential handles this.
- Can be used as an AI tool node.

**Source:** n8n-nodes-base.odoo.md  [doc-verified]
