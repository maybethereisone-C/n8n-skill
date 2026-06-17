# ServiceNow — `n8n-nodes-base.servicenow`
**Type** `n8n-nodes-base.servicenow` · **action**
**What:** Read/write ServiceNow ITSM data — incidents, table records, users, and reference lookups for business services, departments, configuration items, and dictionary.
**Credentials:** `serviceNowOAuth2Api` or Basic Auth

## Resources / Operations
| Resource | Operation |
|----------|-----------|
| Business Service | Get All |
| Configuration Items | Get All |
| Department | Get All |
| Dictionary | Get All |
| Incident | Create, Delete, Get, Get All, Update |
| Table Record | Create, Delete, Get, Get All, Update |
| User | Create, Delete, Get, Get All, Update |
| User Group | Get All |
| User Role | Get All |

## Key params & gotchas
- **Table Record** is the generic resource for any ServiceNow table (not just `incident`); use it to access custom or non-standard tables by specifying the table name.
- Incident Create requires at minimum a `short_description`; `assignment_group` and `category` are typically mandatory in production instances.
- Record IDs are `sys_id` (32-char hex string) — not the human-readable INC0001234 number. Use Get All with a filter to resolve numbers to sys_ids.
- Dictionary Get All is useful for discovering field names and types on a table before constructing payloads.
- OAuth2 is preferred; Basic Auth works but requires an account with appropriate ACLs.
- ServiceNow instance URL format: `https://<instance>.service-now.com`.

**Source:** n8n-nodes-base.servicenow.md  [doc-verified]
