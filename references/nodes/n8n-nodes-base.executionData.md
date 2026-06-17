# Execution Data  (`n8n-nodes-base.executionData`)

- typeVersion (max): **1.1**  | group: input  | trigger: no
- credentials: —
- operations: save

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `notice` | Save important data using this node. It will be displayed on each execution for easy reference and you can filter by it.<br />Filtering is available on Pro and Enterprise plans. <a href='https://n8n.io/pricing/' target='_blank'>More Info</a> | notice |  |  |  |
| `operation` | Operation | options | save |  |  |
| `dataToSave` | Data to Save | fixedCollection | {} |  | op=save |
