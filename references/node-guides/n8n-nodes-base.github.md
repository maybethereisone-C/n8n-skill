# GitHub — `n8n-nodes-base.github`
**Type** `n8n-nodes-base.github` · **typeVersion** 1 · **action**
**What:** Automates GitHub repos, files, issues, releases, reviews, users, and Actions workflows.
**Credentials:** `githubApi` (Personal Access Token) or `githubOAuth2Api` (OAuth2).

**Resources / Operations:**

| Resource | Operations |
|---|---|
| File | Create, Delete, Edit, Get, List |
| Issue | Create, Create Comment, Edit, Get, Lock |
| Organization | Get Repositories |
| Release | Create, Delete, Get, Get Many, Update |
| Repository | Get, Get Issues, Get License, Get Profile, Get Pull Requests, List Popular Paths, List Referrers |
| Review | Create, Get, Get Many, Update |
| User | Get Repositories, Invite |
| Workflow | Disable, Dispatch, Enable, Get, Get Usage, List |

**Key params & gotchas:**
- File Edit requires the blob SHA of the current file — retrieve it with File > Get first, or the update will fail with a 422.
- Workflow > Dispatch requires the workflow to have a `workflow_dispatch` trigger in its YAML; dispatching a workflow without it silently fails or 422s.
- Issue > Lock requires a lock reason (off-topic, too heated, resolved, spam); omitting it causes a validation error.
- PAT scopes needed: `repo` for private repos, `workflow` for Workflow operations, `admin:org` for Org ops.

**Source:** n8n-nodes-base.github.md  [doc-verified]
