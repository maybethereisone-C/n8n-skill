# AWS Textract  (`n8n-nodes-base.awsTextract`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: —
- operations: analyzeExpense

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `operation` | Operation | options | analyzeExpense |  |  |
| `binaryPropertyName` | Input Data Field Name | string | data | true | op=analyzeExpense |
| `simple` | Simplify | boolean | true |  | op=analyzeExpense |
