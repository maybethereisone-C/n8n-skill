# FileMaker  (`n8n-nodes-base.filemaker`)

- typeVersion (max): **1**  | group: input  | trigger: no
- credentials: —

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `action` | Action | options | record |  |  |
| `layout` | Layout Name or ID | options |  | true |  |
| `recid` | Record ID | number |  | true |  |
| `offset` | Offset | number | 1 |  |  |
| `limit` | Limit | number | 100 |  |  |
| `getPortals` | Get Portals | boolean | false |  |  |
| `portals` | Portals Name or ID | options | [] |  |  |
| `responseLayout` | Response Layout Name or ID | options |  |  |  |
| `queries` | Queries | fixedCollection | {} |  |  |
| `setSort` | Sort Data? | boolean | false |  |  |
| `sortParametersUi` | Sort | fixedCollection | {} |  |  |
| `setScriptBefore` | Before Find Script | boolean | false |  |  |
| `scriptBefore` | Script Name or ID | options |  | true |  |
| `scriptBeforeParam` | Script Parameter | string |  |  |  |
| `setScriptSort` | Before Sort Script | boolean | false |  |  |
| `scriptSort` | Script Name or ID | options |  | true |  |
| `scriptSortParam` | Script Parameter | string |  |  |  |
| `setScriptAfter` | After Sort Script | boolean | false |  |  |
| `scriptAfter` | Script Name or ID | options |  | true |  |
| `scriptAfterParam` | Script Parameter | string |  |  |  |
| `fieldData` | fieldData | string | {} |  |  |
| `modId` | Mod ID | number |  |  |  |
| `fieldsParametersUi` | Fields | fixedCollection | {} |  |  |
| `script` | Script Name or ID | options |  | true |  |
| `scriptParam` | Script Parameter | string |  |  |  |
