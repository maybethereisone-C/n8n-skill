# Merge  (`n8n-nodes-base.merge`)

- typeVersion (max): **4.2**  | group: transform  | trigger: no
- credentials: —

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `mode` | Mode | options | append |  |  |
| `join` | Join | options | left |  |  |
| `propertyName1` | Property Input 1 | string |  | true |  |
| `propertyName2` | Property Input 2 | string |  | true |  |
| `output` | Output Data | options | input1 |  |  |
| `overwrite` | Overwrite | options | always |  |  |
| `combinationMode` | Combination Mode | options | mergeByFields |  |  |
| `mergeByFields` | Fields to Match | fixedCollection |  |  |  |
| `joinMode` | Output Type | options | keepMatches |  |  |
| `outputDataFrom` | Output Data From | options | both |  |  |
| `chooseBranchMode` | Output Type | options | waitForBoth |  |  |
