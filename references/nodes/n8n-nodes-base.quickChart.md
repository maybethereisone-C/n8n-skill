# QuickChart  (`n8n-nodes-base.quickChart`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: —

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `chartType` | Chart Type | options | bar |  |  |
| `labelsMode` | Add Labels | options | manually |  |  |
| `labelsUi` | Labels | fixedCollection | {} | true |  |
| `labelsArray` | Labels Array | string |  | true |  |
| `data` | Data | json |  | true |  |
| `output` | Put Output In Field | string | data | true |  |
| `chartOptions` | Chart Options | collection | {} |  |  |
| `datasetOptions` | Dataset Options | collection | {} |  |  |
