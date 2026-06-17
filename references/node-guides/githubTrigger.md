# GitHub Trigger — `n8n-nodes-base.githubTrigger`
**Type** `n8n-nodes-base.githubTrigger` · **typeVersion** 1.1 · **trigger**
**What:** Fires on GitHub repository webhook events (push, PR, issues, releases, stars, deployments, and 40+ more).
**Credentials:** `githubApi` / `githubOAuth2Api`

## Events (multiOptions)

check_run, check_suite, commit_comment, create, delete, deploy_key, deployment, deployment_status, fork, github_app_authorization, gollum, installation, installation_repositories, issue_comment, label, marketplace_purchase, member, membership, meta, milestone, org_block, organization, page_build, project, project_card, project_column, public, pull_request, pull_request_review, pull_request_review_comment, push, release, repository, repository_import, repository_vulnerability_alert, security_advisory, star, status, team, team_add, watch

## Key params & gotchas
- `owner` + `repository` — both required resource locators.
- `events` — multiOptions, required, no default; must select at least one event type.
- **Owner/admin privileges required** — only repo admins or org owners can register the webhooks this node creates. A notice in the UI confirms this.
- `options` — additional collection (e.g., secret for webhook HMAC verification).
- typeVersion 1.1 adds `workflow` resource support (dispatch, dispatchAndWait, enable/disable).

**Source:** n8n-nodes-base.githubtrigger.md + schema  [doc-verified]
