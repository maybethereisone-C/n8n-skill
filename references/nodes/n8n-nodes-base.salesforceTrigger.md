# Salesforce Trigger  (`n8n-nodes-base.salesforceTrigger`)

- typeVersion (max): **1.1**  | group: trigger  | trigger: yes
- credentials: salesforceJwtApi, salesforceOAuth2Api
- resources: account, attachment, case, contact, customObject, document, flow, lead, opportunity, search, task, user
- operations: <, <=, >, >=, addComment, addNote, addToCampaign, create, delete, equal, get, getAll, getSummary, invoke, query, update, upload, upsert

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `triggerOn` | Trigger On | options |  |  |  |
| `customObject` | Custom Object Name or ID | options |  | true |  |
| `authentication` | Authentication | options | oAuth2 |  |  |
| `resource` | Resource | options | lead |  |  |
