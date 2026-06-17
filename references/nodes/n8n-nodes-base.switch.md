# Switch  (`n8n-nodes-base.switch`)

- typeVersion (max): **3.4**  | group: transform  | trigger: no
- credentials: —
- operations: after, before, contains, endsWith, equal, larger, largerEqual, notContains, notEndsWith, notEqual, notRegex, notStartsWith, regex, smaller, smallerEqual, startsWith

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `mode` | Mode | options | rules |  |  |
| `output` | Output | number | 0 |  |  |
| `dataType` | Data Type | options | number |  |  |
| `value1` | Value 1 | boolean | false |  |  |
| `rules` | Routing Rules | fixedCollection | equal |  |  |
| `fallbackOutput` | Fallback Output | options |  |  |  |
| `outputsAmount` | Outputs Amount | number | 4 |  |  |
| `numberOutputs` | Number of Outputs | number | 4 |  |  |
| `options` | Options | collection | none |  |  |
