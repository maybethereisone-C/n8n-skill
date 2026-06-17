# Google Sheets  (`n8n-nodes-base.googleSheets`)

- typeVersion (max): **4.7**  | group: input,output  | trigger: no
- credentials: googleApi, googleSheetsOAuth2Api, googleSheetsTriggerOAuth2Api
- resources: sheet, spreadsheet
- operations: append, appendOrUpdate, clear, create, delete, deleteSpreadsheet, lookup, read, remove, update, upsert

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | hidden | triggerOAuth2 |  |  |
| `event` | Trigger On | options | anyUpdate | true |  |
| `includeInOutput` | Include in Output | options | new |  |  |
| `options` | Options | collection | {} |  |  |
| `resource` | Resource | options | sheet |  |  |
| `operation` | Operation | options | read |  | res=sheet |
| `sheetId` | Spreadsheet ID | string |  | true | res=sheet |
| `range` | Range | string | A:F | true | res=sheet,op=create,op=delete,op=remove |
| `toDelete` | To Delete | fixedCollection | {} | true | res=sheet,op=delete |
| `rawData` | RAW Data | boolean | false |  | res=sheet,op=read |
| `dataProperty` | Data Property | string | data |  | res=sheet,op=read |
| `rawData` | RAW Data | boolean | false |  | res=sheet,op=update,op=upsert |
| `dataProperty` | Data Property | string | data |  | res=sheet,op=update,op=upsert |
| `dataStartRow` | Data Start Row | number | 1 |  | res=sheet,op=append,op=create,op=clear,op=delete,op=remove |
| `keyRow` | Key Row | number | 0 |  | res=sheet,op=clear,op=create,op=delete,op=remove |
| `lookupColumn` | Lookup Column | string |  | true | res=sheet,op=lookup |
| `lookupValue` | Lookup Value | string |  |  | res=sheet,op=lookup |
| `key` | Key | string | id |  | res=sheet,op=update,op=upsert |
| `options` | Options | collection | RAW |  | res=sheet,op=append,op=lookup,op=read,op=update,op=upsert |
| `operation` | Operation | options | create |  | res=spreadsheet |
| `title` | Title | string |  |  | res=spreadsheet,op=create |
| `sheetsUi` | Sheets | fixedCollection | {} |  | res=spreadsheet,op=create |
| `options` | Options | collection | {} |  | res=spreadsheet,op=create |
| `simple` | Simplify | boolean | true |  | res=sheet,op=create |
| `options` | Options | collection | 0aa55c |  | res=sheet,op=create |
| `id` | Sheet ID | string |  | true | res=sheet,op=remove |
