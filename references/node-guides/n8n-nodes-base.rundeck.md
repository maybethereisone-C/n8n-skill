# Rundeck — `n8n-nodes-base.rundeck`
**Type** `n8n-nodes-base.rundeck` · **action**
**What:** Execute Rundeck jobs and retrieve job metadata for ops automation workflows.
**Credentials:** `rundeckApi`

## Resources / Operations
| Resource | Operation |
|----------|-----------|
| Job | Execute a job |
| Job | Get metadata of a job |

## Key params & gotchas
- Job ID is found in the Rundeck dashboard: open the project → JOBS → select the job → copy the smaller string displayed below the job name in the top-left.
- Execute is asynchronous — the response returns an execution ID; poll Rundeck's execution status endpoint (via HTTP Request node) if you need completion confirmation.
- Credentials require the Rundeck server URL and an API token (generated in user profile settings).
- Job options (parameters) can be passed via Additional Fields as key-value pairs.

**Source:** n8n-nodes-base.rundeck.md  [doc-verified]
