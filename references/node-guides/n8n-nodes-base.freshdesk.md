# Freshdesk — `n8n-nodes-base.freshdesk`
**Type** `n8n-nodes-base.freshdesk` · **action**
**What:** Manage Freshdesk support contacts and tickets.
**Credentials:** freshdeskApi (API key + domain, e.g., `yourcompany.freshdesk.com`).

## Resources / Operations
| Resource | Operations |
|---|---|
| Contact | Create, Delete, Get, Get All, Update |
| Ticket | Create, Delete, Get, Get All, Update |

## Key params & gotchas
- The **domain** in credentials must be the subdomain only (e.g., `yourcompany`), not the full URL.
- **Ticket Create** requires at minimum `subject`, `description`, `email` (requester), and `status`/`priority` (numeric codes: priority 1=Low…4=Urgent; status 2=Open, 3=Pending, 4=Resolved, 5=Closed).
- **Ticket Update** uses ticket ID (integer); retrieve tickets first to get IDs dynamically.
- **Get All** contacts/tickets paginates at 30/page; enable "Return All" to auto-paginate.

**Source:** n8n-nodes-base.freshdesk.md  [doc-verified]
