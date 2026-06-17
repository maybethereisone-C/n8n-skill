# Splunk — `n8n-nodes-base.splunk`
**Type** `n8n-nodes-base.splunk` · **typeVersion** 1 · **action**
**What:** Manage Splunk alerts, search configurations, search jobs, results, and users via the Splunk REST API.
**Credentials:** `splunkApi`
**Resources / Operations:**
| Resource | Operations |
|---|---|
| Fired Alert | Get a fired alerts report |
| Search Configuration | Delete, Get, Get Many |
| Search Job | Create, Delete, Get, Get Many |
| Search Result | Get Many |
| User | Create, Delete, Get, Get Many, Update |

**Key params & gotchas:**
- Search jobs are async — create a job, then poll Get until complete before fetching Search Results.
- "Get Many" on Search Results retrieves results from a specific completed job (requires job ID).
- Splunk credentials typically use token-based auth against a specific host:port.

**Source:** n8n-nodes-base.splunk.md  [doc-verified]
