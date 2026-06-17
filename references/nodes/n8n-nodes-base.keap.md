# Keap  (`n8n-nodes-base.keap`)

- typeVersion (max): **1**  | group: input  | trigger: no
- credentials: keapOAuth2Api
- resources: company, contact, contactNote, contactTag, ecommerceOrder, ecommerceProduct, email, file
- operations: create, createRecord, delete, get, getAll, send, update, upload, upsert

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | company |  |  |
| `eventId` | Event Name or ID | options |  | true |  |
| `rawData` | RAW Data | boolean | false |  |  |
