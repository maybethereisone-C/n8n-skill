# Read/Write Files from Disk  (`n8n-nodes-base.readWriteFile`)

- typeVersion (max): **1.1**  | group: input  | trigger: no
- credentials: —
- operations: read, write

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `info` | Use this node to read and write files on the same computer running n8n. To handle files between different computers please use other nodes (e.g. FTP, HTTP Request, AWS). | notice |  |  |  |
| `operation` | Operation | options | read |  |  |
