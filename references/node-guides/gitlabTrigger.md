# GitLab Trigger — `n8n-nodes-base.gitlabTrigger`
**Type** `n8n-nodes-base.gitlabTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires on GitLab project webhook events (push, MR, issues, pipelines, releases, etc.).
**Credentials:** `gitlabApi` / `gitlabOAuth2Api`

## Events (multiOptions)

| Event | Notes |
|---|---|
| comment | New comment on commit, MR, issue, or snippet |
| confidential_issues | Confidential issue created/updated/deleted |
| confidential_comments | Confidential comment posted |
| deployments | Deployment status changes |
| issue | Issue opened/updated/closed |
| job | Job status changes |
| merge_request | MR opened/updated/merged/closed |
| pipeline | Pipeline status changes |
| push | Commits pushed to a branch |
| release | Release created/updated/deleted |
| tag | Tag pushed |
| wiki_page | Wiki page created/updated |

## Key params & gotchas
- `owner` (repository owner/namespace) and `repository` (project name) — both required strings.
- `events` — multiOptions, required, no default.
- `authentication` — `accessToken` (default) or OAuth2.
- GitLab uses project-level webhooks; the credential must have sufficient scope to create hooks on the target project.

**Source:** n8n-nodes-base.gitlabtrigger.md + schema  [doc-verified]
