# Google Docs  (`n8n-nodes-base.googleDocs`)

- typeVersion (max): **2**  | group: input  | trigger: no
- credentials: googleApi, googleDocsOAuth2Api
- resources: document
- operations: create, get, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | serviceAccount |  |  |
| `resource` | Resource | options | document |  |  |
