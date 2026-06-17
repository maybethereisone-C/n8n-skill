# Filter  (`n8n-nodes-base.filter`)

- typeVersion (max): **2.3**  | group: transform  | trigger: no
- credentials: —
- operations: after, before, contains, endsWith, equal, isEmpty, isNotEmpty, larger, largerEqual, notContains, notEndsWith, notEqual, notRegex, notStartsWith, regex, smaller, smallerEqual, startsWith

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `conditions` | Conditions | fixedCollection | equal |  | op=isEmpty,op=isNotEmpty |
| `combineConditions` | Combine Conditions | options | AND |  |  |
| `conditions` | Conditions | filter | {} |  |  |
| `options` | Options | collection | {} |  |  |
