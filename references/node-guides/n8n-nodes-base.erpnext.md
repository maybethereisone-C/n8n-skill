# ERPNext — `n8n-nodes-base.erpNext`
**Type** `n8n-nodes-base.erpNext` · **action**
**What:** Full CRUD on any ERPNext/Frappe document type (Sales Order, Purchase Invoice, Customer, etc.).
**Credentials:** erpNextApi (host URL + API key + API secret) or erpNextTokenApi.

## Resources / Operations
| Resource | Operations |
|---|---|
| Document | Create, Delete, Retrieve, Retrieve All, Update |

## Key params & gotchas
- **DocType** is a required field — enter the ERPNext document type name exactly (e.g., `Sales Order`, `Customer`); capitalization matters.
- **Retrieve All** supports filters as an array of `[doctype, field, operator, value]` tuples (Frappe query format).
- **Update** does a partial update (PATCH); only specified fields are changed.
- Document names are typically auto-generated strings like `SAL-ORD-00001`; use Retrieve All with filters to look them up.
- Can be used as an AI tool node.
- "Operation not supported" error indicates a missing ERPNext module or permission.

**Source:** n8n-nodes-base.erpnext.md  [doc-verified]
