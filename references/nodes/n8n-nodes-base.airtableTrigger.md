# Airtable Trigger  (`n8n-nodes-base.airtableTrigger`)

- typeVersion (max): **2.2**  | group: trigger  | trigger: yes
- credentials: airtableApi, airtableOAuth2Api, airtableTokenApi
- resources: base, record, table
- operations: append, create, delete, deleteRecord, get, getMany, getSchema, list, read, search, update, upsert

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | airtableApi |  |  |
| `baseId` | Base | resourceLocator |  | true |  |
| `tableId` | Table | resourceLocator |  | true |  |
| `triggerField` | Trigger Field | string |  | true |  |
| `downloadAttachments` | Download Attachments | boolean | false |  |  |
| `downloadFieldNames` | Download Fields | string |  | true |  |
| `additionalFields` | Additional Fields | collection | {} |  |  |
| `deprecated` | This type of connection (API Key) was deprecated and can't be used anymore. Please create a new credential of type 'Access Token' instead. | notice |  |  |  |
| `operation` | Operation | options | read |  |  |
| `application` | Base | resourceLocator |  | true |  |
| `table` | Table | resourceLocator |  | true |  |
| `addAllFields` | Add All Fields | boolean | true |  | op=append |
| `fields` | Fields | string | [] | true | op=append |
| `id` | ID | string |  | true | op=delete |
| `returnAll` | Return All | boolean | true |  | op=list |
| `limit` | Limit | number | 100 |  | op=list |
| `downloadAttachments` | Download Attachments | boolean | false |  | op=list |
| `downloadFieldNames` | Download Fields | string |  | true | op=list |
| `additionalOptions` | Additional Options | collection | {} |  | op=list |
| `id` | ID | string |  | true | op=read |
| `id` | ID | string |  | true | op=update |
| `updateAllFields` | Update All Fields | boolean | true |  | op=update |
| `fields` | Fields | string | [] | true | op=update |
| `options` | Options | collection | {} |  | op=append,op=delete,op=update |
| `resource` | Resource | options | record |  |  |
