# Intercom — `n8n-nodes-base.intercom`
**Type** `n8n-nodes-base.intercom` · **typeVersion** 1 · **action**
**What:** Manage Intercom companies, leads (visitors), and users (contacts).
**Credentials:** `intercomApi` (Access Token).

## Resources / Operations
| Resource | Operations |
|---|---|
| Company | Create, Get, Get All, Update, List Users |
| Lead | Create, Delete, Get, Get All, Update |
| User | Create, Delete, Get, Get All, Update |

## Key params & gotchas
- **Lead** vs **User**: in Intercom's data model, Leads are anonymous/unidentified visitors; Users are identified (have an `email` or `user_id`). The node exposes them as separate resources.
- **Company→List Users** returns users associated with a company — useful for syncing company membership.
- Intercom uses `user_id` (your system's ID) and `email` as lookup keys — prefer `user_id` for stability since emails can change.
- Intercom API v2+ requires an Access Token (not API key); ensure the credential type matches the Intercom workspace API version.

**Source:** n8n-nodes-base.intercom.md  [doc-verified]
