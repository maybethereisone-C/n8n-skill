# Netlify Trigger  (`n8n-nodes-base.netlifyTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: netlifyApi
- resources: deploy, site
- operations: cancel, create, delete, get, getAll

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `siteId` | Site Name or ID | options |  | true |  |
| `event` | Event | options |  | true |  |
| `formId` | Form Name or ID | options |  | true |  |
| `simple` | Simplify | boolean | true |  |  |
| `resource` | Resource | options | deploy | true |  |
