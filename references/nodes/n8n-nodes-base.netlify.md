# Netlify  (`n8n-nodes-base.netlify`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: netlifyApi
- resources: deploy, site
- operations: cancel, create, delete, get, getAll

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | deploy | true |  |
| `siteId` | Site Name or ID | options |  | true |  |
| `event` | Event | options |  | true |  |
| `formId` | Form Name or ID | options |  | true |  |
| `simple` | Simplify | boolean | true |  |  |
