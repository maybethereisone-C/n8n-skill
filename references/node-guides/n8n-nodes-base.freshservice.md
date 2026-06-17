# Freshservice — `n8n-nodes-base.freshservice`
**Type** `n8n-nodes-base.freshservice` · **action**
**What:** Full ITSM operations on Freshservice — agents, groups, tickets, problems, changes, releases, assets, software, departments, locations, and more.
**Credentials:** freshserviceApi (API key + domain).

## Resources / Operations
| Resource | Operations |
|---|---|
| Agent | Create, Delete, Retrieve, Retrieve All, Update |
| Agent Group | Create, Delete, Retrieve, Retrieve All, Update |
| Agent Role | Retrieve, Retrieve All |
| Announcement | Create, Delete, Retrieve, Retrieve All, Update |
| Asset Type | Create, Delete, Retrieve, Retrieve All, Update |
| Change | Create, Delete, Retrieve, Retrieve All, Update |
| Department | Create, Delete, Retrieve, Retrieve All, Update |
| Location | Create, Delete, Retrieve, Retrieve All, Update |
| Problem | Create, Delete, Retrieve, Retrieve All, Update |
| Product | Create, Delete, Retrieve, Retrieve All, Update |
| Release | Create, Delete, Retrieve, Retrieve All, Update |
| Requester | Create, Delete, Retrieve, Retrieve All, Update |
| Requester Group | Create, Delete, Retrieve, Retrieve All, Update |
| Software | Create, Delete, Retrieve, Retrieve All, Update |
| Ticket | Create, Delete, Retrieve, Retrieve All, Update |

## Key params & gotchas
- Despite the doc mentioning "Freshdesk features" in its description, this is the **Freshservice** (ITSM) API — distinct product with a separate API and credential domain.
- **Ticket Create** requires `subject`, `description`, `requester_id` or `email`, `status`, and `priority` (use integer codes).
- **Change / Problem / Release** are ITIL change management resources — each has its own lifecycle statuses.
- Agent operations need admin-level API key.

**Source:** n8n-nodes-base.freshservice.md  [doc-verified]
