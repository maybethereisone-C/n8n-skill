# Default Data Loader  (`@n8n/n8n-nodes-langchain.documentDefaultDataLoader`)

- typeVersion (max): **1.1**  | group: transform  | trigger: no
- credentials: —

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `notice` | This will load data from a previous step in the workflow. <a href="/templates/1962" target="_blank">Example</a> | notice |  |  |  |
| `dataType` | Type of Data | options | json | true |  |
| `jsonMode` | Mode | options | allInputData | true |  |
| `binaryMode` | Mode | options | allInputData | true |  |
| `loader` | Data Format | options | auto | true |  |
| `jsonData` | Data | string |  | true |  |
| `binaryDataKey` | Input Data Field Name | string | data | true |  |
| `textSplittingMode` | Text Splitting | options | simple | true |  |
| `options` | Options | collection | {} |  |  |
