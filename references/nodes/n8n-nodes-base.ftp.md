# FTP  (`n8n-nodes-base.ftp`)

- typeVersion (max): **1**  | group: input  | trigger: no
- credentials: —
- operations: delete, download, list, rename, upload

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `protocol` | Protocol | options | ftp |  |  |
| `operation` | Operation | options | download |  |  |
| `path` | Path | string |  | true | op=delete |
| `options` | Options | collection | {} |  | op=delete |
| `path` | Path | string |  | true | op=download |
| `binaryPropertyName` | Put Output File in Field | string | data | true | op=download |
| `options` | Options | collection | {} |  | op=download |
| `oldPath` | Old Path | string |  | true | op=rename |
| `newPath` | New Path | string |  | true | op=rename |
| `options` | Options | collection | {} |  | op=rename |
| `path` | Path | string |  | true | op=upload |
| `binaryData` | Binary File | boolean | true |  | op=upload |
| `binaryPropertyName` | Input Binary Field | string | data | true | op=upload |
| `fileContent` | File Content | string |  |  | op=upload |
| `options` | Options | collection | {} |  | op=upload |
| `path` | Path | string | / | true | op=list |
| `recursive` | Recursive | boolean | false | true | op=list |
| `options` | Options | collection | {} |  | op=list |
