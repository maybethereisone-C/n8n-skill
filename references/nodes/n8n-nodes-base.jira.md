# Jira Software  (`n8n-nodes-base.jira`)

- typeVersion (max): **1.1**  | group: output  | trigger: no
- credentials: jiraSoftwareCloudApi, jiraSoftwareCloudOAuth2Api, jiraSoftwareServerApi, jiraSoftwareServerPatApi
- resources: issue, issueAttachment, issueComment, user
- operations: add, changelog, create, delete, get, getAll, notify, remove, transitions, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `jiraVersion` | Jira Version | options | cloud |  |  |
| `resource` | Resource | options | issue |  |  |
| `authenticateWebhook` | Authenticate Incoming Webhook | boolean | false |  |  |
| `incomingAuthentication` | Authenticate Webhook With | options | none |  |  |
| `events` | Events | multiOptions | [] | true |  |
| `additionalFields` | Additional Fields | collection | {} |  |  |
