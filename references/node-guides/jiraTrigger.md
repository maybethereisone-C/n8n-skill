# Jira Trigger — `n8n-nodes-base.jiraTrigger`
**Type** `n8n-nodes-base.jiraTrigger` · **typeVersion** 1.1 · **trigger**
**What:** Fires on Jira issue lifecycle events via webhook (supports Jira Cloud and Server/Data Center).
**Credentials:** `jiraSoftwareCloudApi` / `jiraSoftwareCloudOAuth2Api` / `jiraSoftwareServerApi` / `jiraSoftwareServerPatApi`

## Events (multiOptions)

issue-related: jira:issue_created, jira:issue_updated, jira:issue_deleted, jira:worklog_created, jira:worklog_updated, jira:worklog_deleted, comment_created, comment_updated, comment_deleted, issuelink_created, issuelink_deleted, attachment_created, attachment_deleted, sprint_created, sprint_started, sprint_closed, sprint_updated, board_created, board_deleted, board_configuration_changed, project_created, project_updated, project_deleted, user_created, user_updated, user_deleted

## Key params & gotchas
- `jiraVersion` — `cloud` (default) or `server`; determines which credential types and API endpoints to use.
- `events` — multiOptions, required, no default; select at least one.
- `authenticateWebhook` — boolean (default false); set true to require HMAC signature validation on incoming payloads. When enabled, set `incomingAuthentication`.
- `additionalFields` — optional collection for JQL filtering (restrict webhook to specific projects or issue types).
- typeVersion 1.1 adds Server PAT auth support.
- Companion app node: `n8n-nodes-base.jira`.

**Source:** n8n-nodes-base.jiratrigger.md + schema  [doc-verified]
