# urlscan.io — `n8n-nodes-base.urlscanio`
**Type** `n8n-nodes-base.urlscanio` · **typeVersion** 1 · **action**
**What:** Submit URLs for security scanning and retrieve scan results from urlscan.io.
**Credentials:** `urlscanioApi` (API key from urlscan.io account).
**Resources / Operations:**
| Resource | Operations |
|----------|-----------|
| Scan | Get (by UUID), Get All (search), Perform (submit new scan) |

**Key params & gotchas:**
- "Perform" (submit) returns a UUID; the actual scan takes 10–30 seconds to complete. Use a Wait node or poll with Get before reading results.
- Get All uses urlscan.io's Elasticsearch query syntax for filtering (e.g., `domain:example.com`).
- Scans are public by default on free accounts — submitted URLs are visible to all users.
- Can be used as an AI tool sub-node.

**Source:** n8n-nodes-base.urlscanio.md  [doc-verified]
