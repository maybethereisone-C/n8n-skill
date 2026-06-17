# Webflow Trigger  (`n8n-nodes-base.webflowTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: webflowApi, webflowOAuth2Api
- resources: item
- operations: create, delete, get, getAll, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | accessToken |  |  |
| `site` | Site Name or ID | options |  | true |  |
| `event` | Event | options | form_submission | true |  |
| `resource` | Resource | options | item |  |  |
