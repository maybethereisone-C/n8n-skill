# Okta — `n8n-nodes-base.okta`
**Type** `n8n-nodes-base.okta` · **typeVersion** 1 · **action**
**What:** Manage Okta user accounts: create, read, update, and delete users in your Okta organization.
**Credentials:** Okta API token (`oktaApi`) — Okta domain + API token (or OAuth 2.0 service app).
**Resources / Operations:**
| Resource | Operations |
|---|---|
| User | Create, Delete, Get, Get Many, Update |

**Key params & gotchas:**
- **Create** requires at minimum `firstName`, `lastName`, `email`, and `login` (usually same as email). New users are created in `STAGED` status unless `activate: true` is passed.
- **Delete** deactivates then permanently removes a user — this is irreversible. To just deactivate, use **Update** to set `status: DEPROVISIONED`.
- **Get Many** supports filtering with Okta's filter expression syntax (e.g., `status eq "ACTIVE"`).
- The credential domain must be your Okta org URL (e.g., `https://yourorg.okta.com`).

**Source:** n8n-nodes-base.okta.md  [doc-verified]
