# Rundeck  (`n8n-nodes-base.rundeck`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: rundeckApi
- resources: job
- operations: execute, getMetadata

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | job |  |  |
| `operation` | Operation | options | execute |  |  |
| `jobid` | Job ID | string |  | true | res=job,op=execute |
| `arguments` | Arguments | fixedCollection | {} |  | res=job,op=execute |
| `filter` | Filter | string |  |  | res=job,op=execute |
| `jobid` | Job ID | string |  | true | res=job,op=getMetadata |
