# Grafana — `n8n-nodes-base.grafana`
**Type** `n8n-nodes-base.grafana` · **typeVersion** 1 · **action**
**What:** Manage Grafana dashboards, teams, team members, and org users.
**Credentials:** `grafanaApi` (API key + base URL).

## Resources / Operations
| Resource | Operations |
|---|---|
| Dashboard | Create, Delete, Get, Get All, Update |
| Team | Create, Delete, Get, Get All (Retrieve all), Update |
| Team Member | Add member, Get All, Remove member |
| User | Delete (from org), Get All (in org), Update (in org) |

## Key params & gotchas
- Dashboard **UID** (not numeric ID) is required for Get/Update/Delete — the UID appears in the dashboard URL after `/d/`.
- "Get All Dashboards" searches across all folders; add a **Search** filter to narrow results.
- Team Member operations require knowing the Grafana **user ID** (integer), not the username.
- User operations are scoped to the **current organization** only; switching orgs requires a different API key.

**Source:** n8n-nodes-base.grafana.md  [doc-verified]
