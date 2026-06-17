# Harvest — `n8n-nodes-base.harvest`
**Type** `n8n-nodes-base.harvest` · **typeVersion** 1 · **action**
**What:** Manage time tracking, projects, invoices, expenses, contacts, and users in Harvest.
**Credentials:** `harvestApi` (OAuth2 or Personal Access Token + Account ID).

## Resources / Operations
| Resource | Operations |
|---|---|
| Client | Create, Delete, Get, Get All, Update |
| Company | Get (currently authenticated company) |
| Contact | Create, Delete, Get, Get All, Update |
| Estimate | Create, Delete, Get, Get All, Update |
| Expense | Create, Delete, Get, Get All, Update |
| Invoice | Create, Delete, Get, Get All, Update |
| Project | Create, Delete, Get, Get All, Update |
| Task | Create, Delete, Get, Get All, Update |
| Time Entry | Create (duration), Create (start/end), Delete, Delete External Ref, Get, Get All, Restart, Stop, Update |
| User | Create, Delete, Get, Get All, Get Authenticated User, Update |

## Key params & gotchas
- Time Entry has **two create paths**: duration-based (hours float) vs. start/end timestamps — choose based on whether the timer is running or already complete.
- **Restart** / **Stop** on Time Entry only works if the entry is currently running; calling Stop on a stopped entry errors.
- The **Account ID** is required in the credential and appears in Harvest's URL (`https://ACCOUNTID.harvestapp.com`).
- Invoices and Estimates are separate billing concepts; Invoices are billable, Estimates are pre-approval.

**Source:** n8n-nodes-base.harvest.md  [doc-verified]
