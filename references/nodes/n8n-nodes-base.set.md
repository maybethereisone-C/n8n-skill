# Set  (`n8n-nodes-base.set`)

- typeVersion (max): **3.4**  | group: input  | trigger: no
- credentials: —

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `keepOnlySet` | Keep Only Set | boolean | false |  |  |
| `values` | Values to Set | fixedCollection | propertyName |  |  |
| `options` | Options | collection | {} |  |  |
| `mode` | Mode | options | manual |  |  |
| `duplicateItem` | Duplicate Item | boolean | false |  |  |
| `duplicateCount` | Duplicate Item Count | number | 0 |  |  |
| `duplicateWarning` | Item duplication is set in the node settings. This option will be ignored when the workflow runs automatically. | notice |  |  |  |
| `include` | Include in Output | options | all |  |  |
| `includeOtherFields` | Include Other Input Fields | boolean | false |  |  |
| `includeFields` | Fields to Include | string |  |  |  |
| `excludeFields` | Fields to Exclude | string |  |  |  |
