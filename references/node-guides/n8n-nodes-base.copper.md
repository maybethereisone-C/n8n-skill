# Copper — `n8n-nodes-base.copper`
**Type** `n8n-nodes-base.copper` · **action**
**What:** Full CRUD for Copper CRM — companies, leads, opportunities, people, projects, tasks, and users.
**Credentials:** copperApi (API key + user email).

## Resources / Operations
| Resource | Operations |
|---|---|
| Company | Create, Delete, Get, Get All, Update |
| Customer Source | Get All |
| Lead | Create, Delete, Get, Get All, Update |
| Opportunity | Create, Delete, Get, Get All, Update |
| Person | Create, Delete, Get, Get All, Update |
| Project | Create, Delete, Get, Get All, Update |
| Task | Create, Delete, Get, Get All, Update |
| User | Get All |

## Key params & gotchas
- Copper credentials require **both** the API key and the email of the Copper user the key belongs to — the email acts as an identifier in API requests.
- **Get All** operations support filtering and sorting; use filters to avoid pulling the entire dataset.
- Custom fields are accessible via `custom_fields` array but require field definition IDs, not names.

**Source:** n8n-nodes-base.copper.md  [doc-verified]
