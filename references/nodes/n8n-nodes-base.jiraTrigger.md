# Jira Trigger  (`n8n-nodes-base.jiraTrigger`)

- typeVersion (max): **1.1**  | group: trigger  | trigger: yes
- credentials: jiraSoftwareCloudApi, jiraSoftwareCloudOAuth2Api, jiraSoftwareServerApi, jiraSoftwareServerPatApi
- resources: issue, issueAttachment, issueComment, user
- operations: add, changelog, create, delete, get, getAll, notify, remove, transitions, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `jiraVersion` | Jira Version | options | cloud |  |  |
| `authenticateWebhook` | Authenticate Incoming Webhook | boolean | false |  |  |
| `incomingAuthentication` | Authenticate Webhook With | options | none |  |  |
| `events` | Events | multiOptions | [] | true |  |
| `additionalFields` | Additional Fields | collection | {} |  |  |
| `resource` | Resource | options | issue |  |  |
