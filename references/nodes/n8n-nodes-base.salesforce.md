# Salesforce  (`n8n-nodes-base.salesforce`)

- typeVersion (max): **1.1**  | group: output  | trigger: no
- credentials: salesforceJwtApi, salesforceOAuth2Api
- resources: account, attachment, case, contact, customObject, document, flow, lead, opportunity, search, task, user
- operations: <, <=, >, >=, addComment, addNote, addToCampaign, create, delete, equal, get, getAll, getSummary, invoke, query, update, upload, upsert

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | oAuth2 |  |  |
| `resource` | Resource | options | lead |  |  |
| `triggerOn` | Trigger On | options |  |  |  |
| `customObject` | Custom Object Name or ID | options |  | true |  |
