# Jenkins — `n8n-nodes-base.jenkins`
**Type** `n8n-nodes-base.jenkins` · **typeVersion** 1 · **action**
**What:** Trigger and inspect Jenkins CI builds, manage jobs, and control the Jenkins instance lifecycle.
**Credentials:** `jenkinsApi` (base URL + username + API token).

## Resources / Operations
| Resource | Operations |
|---|---|
| Build | List Builds |
| Instance | Cancel Quiet Down, Quiet Down (prepare for shutdown), Restart (immediate), Safe Restart (wait for jobs), Safe Shutdown (wait), Shutdown (immediate) |
| Job | Copy Job, Create Job, Trigger Job, Trigger Job with Parameters |

## Key params & gotchas
- **Job→Trigger** fires a build immediately; **Trigger with Parameters** passes key-value build params (used with parameterized pipelines).
- **Instance→Quiet Down** prevents new builds from starting — required before graceful shutdown; **Cancel Quiet Down** resumes normal operation.
- **Job→Copy** duplicates an existing job's config into a new job name — useful for templating similar pipelines.
- Jenkins API token (not password) is required for the credential — generate it under user → Configure → API Token.
- The doc lists "Trigger a specific job" twice — one is likely the parameterized variant; both map to the same resource.

**Source:** n8n-nodes-base.jenkins.md  [doc-verified]
