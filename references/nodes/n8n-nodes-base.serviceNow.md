# ServiceNow  (`n8n-nodes-base.serviceNow`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: serviceNowBasicApi, serviceNowOAuth2Api
- resources: attachment, businessService, configurationItems, department, dictionary, incident, tableRecord, user, userGroup, userRole
- operations: create, delete, get, getAll, update, upload

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | oAuth2 |  |  |
| `resource` | Resource | options | user |  |  |
