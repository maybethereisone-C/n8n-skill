# Webflow  (`n8n-nodes-base.webflow`)

- typeVersion (max): **2**  | group: transform  | trigger: no
- credentials: webflowApi, webflowOAuth2Api
- resources: item
- operations: create, delete, deleteItem, get, getAll, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | accessToken |  |  |
| `resource` | Resource | options | item |  |  |
| `site` | Site Name or ID | options |  | true |  |
| `event` | Event | options | form_submission | true |  |
