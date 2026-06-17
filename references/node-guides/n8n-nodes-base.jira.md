# Jira Software — `n8n-nodes-base.jira`
**Type** `n8n-nodes-base.jira` · **typeVersion** 1 · **action**
**What:** Full Jira issue lifecycle management — create, update, search, attach files, comment, and manage users.
**Credentials:** `jiraSoftwareCloudApi` (cloud: email + API token) or `jiraSoftwareServerApi` (self-hosted: URL + credentials).

## Resources / Operations
| Resource | Operations |
|---|---|
| Issue | Get Changelog, Create, Delete, Get, Get All, Send Email Notification, Get Transitions, Update |
| Issue Attachment | Add, Get, Get All, Remove |
| Issue Comment | Add, Get, Get All, Remove, Update |
| User | Create, Delete, Retrieve |

## Key params & gotchas
- **Issue→Get All** supports JQL via **Add Option → JQL**; use `project=KEY` to filter by project (e.g. `project=n8n`). Without JQL it returns all issues across all projects — expensive on large instances.
- **Issue→Get Transitions** returns available workflow transitions from the current status; use the returned transition ID in **Update** to change issue status.
- **Issue Attachment→Add** accepts binary data from upstream nodes (e.g. Read Binary File); set the correct MIME type.
- Jira Cloud uses email + API token; Jira Server uses username + password or PAT — credential type must match.
- **Issue→Send Email Notification** adds to Jira's mail queue — not immediate; depends on Jira's email configuration.

**Source:** n8n-nodes-base.jira.md  [doc-verified]
