# Google BigQuery  (`n8n-nodes-base.googleBigQuery`)

- typeVersion (max): **2.1**  | group: input  | trigger: no
- credentials: googleApi, googleBigQueryOAuth2Api
- resources: database, record
- operations: create, executeQuery, getAll, insert

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | oAuth2 |  |  |
| `resource` | Resource | options | record |  |  |
