# Keap Trigger  (`n8n-nodes-base.keapTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: keapOAuth2Api
- resources: company, contact, contactNote, contactTag, ecommerceOrder, ecommerceProduct, email, file
- operations: create, createRecord, delete, get, getAll, send, update, upload, upsert

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `eventId` | Event Name or ID | options |  | true |  |
| `rawData` | RAW Data | boolean | false |  |  |
| `resource` | Resource | options | company |  |  |
