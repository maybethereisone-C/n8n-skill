# GetResponse — `n8n-nodes-base.getResponse`
**Type** `n8n-nodes-base.getResponse` · **action**
**What:** Manage GetResponse email marketing contacts.
**Credentials:** getResponseApi (API key) or getResponseOAuth2Api.

## Resources / Operations
| Resource | Operations |
|---|---|
| Contact | Create, Delete, Get, Get All, Update Properties |

## Key params & gotchas
- **Create** requires a `campaignId` (list ID) — contacts are always added to a specific campaign/list.
- **Update Properties** allows changing custom fields, name, and tags — not email address (email is the immutable identifier).
- Contact lookup by email requires **Get All** with a filter; there is no direct "Get by email" operation.
- "Operation not supported" error applies to features limited to paid GetResponse plans.

**Source:** n8n-nodes-base.getresponse.md  [doc-verified]
