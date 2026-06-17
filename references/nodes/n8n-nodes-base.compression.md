# Compression  (`n8n-nodes-base.compression`)

- typeVersion (max): **1.1**  | group: transform  | trigger: no
- credentials: —
- operations: compress, decompress

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `operation` | Operation | options | decompress |  |  |
| `binaryPropertyName` | Input Binary Field(s) | string | data | true | op=compress |
| `binaryPropertyName` | Input Binary Field(s) | string | data | true | op=decompress |
| `outputFormat` | Output Format | options |  |  | op=compress |
| `fileName` | File Name | string |  | true | op=compress |
| `binaryPropertyOutput` | Put Output File in Field | string | data |  | op=compress |
| `outputPrefix` | Output File Prefix | string | data | true | op=compress |
| `outputPrefix` | Output Prefix | string | file_ | true | op=decompress |
