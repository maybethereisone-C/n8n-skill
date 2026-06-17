# Bitwarden — `n8n-nodes-base.bitwarden`
**Type** `n8n-nodes-base.bitwarden` · **action**
**What:** Manage Bitwarden Business/Enterprise — collections, events, groups, and members via the Bitwarden Public API.
**Credentials:** Bitwarden credential (client ID + client secret from Organization API Key).

## Resources / Operations
| Resource | Operations |
|---|---|
| Collection | Delete, Get, Get All, Update |
| Event | Get All |
| Group | Create, Delete, Get, Get All, Get Members, Update, Update Members |
| Member | Create, Delete, Get, Get All, Get Groups, Update, Update Groups |

## Key params & gotchas
- This node uses the **Bitwarden Public API** (organizations only) — it does NOT manage individual vault items (logins, notes). Use the Bitwarden CLI for vault item management.
- Requires an **Organization API Key** (Client ID + Client Secret) — found in Organization Settings → API Key.
- **Collection/Create is not available** — collections must be created in the Bitwarden web vault or CLI.
- Group/Update Members and Member/Update Groups take arrays of IDs to fully replace membership — not append.
- Event/Get All returns audit log events; filter by date range and type.

**Source:** n8n-nodes-base.bitwarden.md  [doc-verified]
