# SSH  (`n8n-nodes-base.ssh`)

- typeVersion (max): **1**  | group: input  | trigger: no
- credentials: —
- resources: command, file
- operations: download, execute, upload

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | password |  |  |
| `resource` | Resource | options | command |  |  |
| `operation` | Operation | options | execute |  | res=command |
| `command` | Command | string |  |  | res=command,op=execute |
| `cwd` | Working Directory | string | / | true | res=command,op=execute |
| `operation` | Operation | options | upload |  | res=file |
| `binaryPropertyName` | Input Binary Field | string | data | true | res=file,op=upload |
| `path` | Target Directory | string |  | true | res=file,op=upload |
| `path` | Path | string |  | true | res=file,op=download |
| `binaryPropertyName` | File Property | string | data | true | res=file,op=download |
| `options` | Options | collection | {} |  | res=file,op=upload,op=download |
