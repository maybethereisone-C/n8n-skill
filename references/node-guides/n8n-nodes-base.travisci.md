# Travis CI — `n8n-nodes-base.travisci`
**Type** `n8n-nodes-base.travisci` · **typeVersion** 1 · **action**
**What:** Manage Travis CI builds — trigger, cancel, restart, and retrieve build information.
**Credentials:** `travisCiApi`
**Resources / Operations:**
| Resource | Operations |
|---|---|
| Build | Cancel, Get, Get All, Restart, Trigger |

**Key params & gotchas:**
- Trigger Build initiates a new build for a repository — requires repo slug (e.g. `owner/repo`).
- Restart resumes a previously cancelled or errored build from scratch.
- Get All returns builds for a specific repository; supports pagination.

**Source:** n8n-nodes-base.travisci.md  [doc-verified]
