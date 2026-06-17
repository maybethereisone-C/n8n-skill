# Aggregate  (`n8n-nodes-base.aggregate`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: —

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `aggregate` | Aggregate | options | aggregateIndividualFields |  |  |
| `fieldsToAggregate` | Fields To Aggregate | fixedCollection | false |  |  |
| `destinationFieldName` | Put Output in Field | string | data |  |  |
| `include` | Include | options | allFields |  |  |
| `fieldsToExclude` | Fields To Exclude | string |  |  |  |
| `fieldsToInclude` | Fields To Include | string |  |  |  |
| `options` | Options | collection | {} |  |  |
