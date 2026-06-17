# Google Workspace Admin — `n8n-nodes-base.gsuiteadmin`
**Type** `n8n-nodes-base.gsuiteadmin` · **typeVersion** 1 · **action**
**What:** Administer Google Workspace users, groups, and ChromeOS devices via the Admin SDK.
**Credentials:** `googleApi` / `googleOAuth2Api` — requires Admin SDK scope; must be a Workspace super-admin or delegated admin.

## Resources / Operations
| Resource | Operations |
|---|---|
| ChromeOS Device | Get, Get Many, Update, Change Status |
| Group | Create, Delete, Get, Get Many, Update |
| User | Create, Delete, Get, Get Many, Update, Add to Group, Remove from Group |

## Key params & gotchas
- **Custom Fields** on User→Get: choose `Don't Include` / `Custom` (specify schema names) / `Include All`. Requesting all fields on large orgs can be slow.
- User **Add to Group** / **Remove from Group** use the user's primary email or immutable user ID — not display name.
- ChromeOS **Change Status** accepts `DEPROVISION`, `DISABLE`, `REENABLE`, `PRE_PROVISIONED`.
- Requires a service account with **domain-wide delegation** or an OAuth2 credential with `https://www.googleapis.com/auth/admin.directory.*` scopes.
- Operations apply to the **primary domain** of the credential; multi-domain Workspace needs care with `customer` vs `domain` params.

**Source:** n8n-nodes-base.gsuiteadmin.md  [doc-verified]
