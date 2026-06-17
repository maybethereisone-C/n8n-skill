# Compare Datasets  (`n8n-nodes-base.compareDatasets`)

- typeVersion (max): **2.3**  | group: transform  | trigger: no
- credentials: —

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `infoBox` | Items from different branches are paired together when the fields below match. If paired, the rest of the fields are compared to determine whether the items are the same or different | notice |  |  |  |
| `mergeByFields` | Fields to Match | fixedCollection |  |  |  |
| `resolve` | When There Are Differences | options | preferInput2 |  |  |
| `fuzzyCompare` | Fuzzy Compare | boolean | false |  |  |
| `preferWhenMix` | Prefer | options | input1 |  |  |
| `exceptWhenMix` | For Everything Except | string |  |  |  |
| `options` | Options | collection | {} |  |  |
