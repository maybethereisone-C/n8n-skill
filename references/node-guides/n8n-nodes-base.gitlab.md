# GitLab — `n8n-nodes-base.gitlab`
**Type** `n8n-nodes-base.gitlab` · **typeVersion** 1 · **action**
**What:** Automates GitLab files, issues, releases, repositories, and users via the GitLab REST API.
**Credentials:** `gitlabApi` (Personal Access Token) or `gitlabOAuth2Api` (OAuth2).

**Resources / Operations:**

| Resource | Operations |
|---|---|
| File | Create, Delete, Edit, Get, List |
| Issue | Create, Create Comment, Edit, Get, Lock |
| Release | Create, Delete, Get, Get All, Update |
| Repository | Get, Get Issues |
| User | Get Repositories |

**Key params & gotchas:**
- Self-hosted GitLab: set the Base URL in credentials to your instance (e.g. `https://gitlab.mycompany.com`); default points to gitlab.com.
- File operations require the project ID (numeric), not just the namespace/path — use Repository > Get to resolve it.
- Issue > Lock is available but GitLab's lock is discussion-level; locked issues still accept certain updates.
- A companion trigger node exists: `n8n-nodes-base.gitlabTrigger` for webhook-driven workflows.

**Source:** n8n-nodes-base.gitlab.md  [doc-verified]
