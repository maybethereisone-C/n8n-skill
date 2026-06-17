# Item Lists  (`n8n-nodes-base.itemLists`)

- typeVersion (max): **3.1**  | group: input  | trigger: no
- credentials: —
- resources: itemList
- operations: aggregateItems, concatenateItems, limit, removeDuplicates, sort, splitOutItems, summarize

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | hidden | itemList |  |  |
| `operation` | Operation | options | splitOutItems |  |  |
| `fieldToSplitOut` | Field To Split Out | string |  | true | res=itemList,op=splitOutItems |
| `include` | Include | options | noOtherFields |  | res=itemList,op=splitOutItems |
| `fieldsToInclude` | Fields To Include | fixedCollection | {} |  | res=itemList,op=splitOutItems |
| `aggregate` | Aggregate | options | aggregateIndividualFields |  | res=itemList,op=aggregateItems |
| `fieldsToAggregate` | Fields To Aggregate | fixedCollection | false |  | res=itemList,op=aggregateItems |
| `destinationFieldName` | Put Output in Field | string | data |  | res=itemList,op=aggregateItems |
| `include` | Include | options | allFields |  | res=itemList,op=aggregateItems |
| `fieldsToExclude` | Fields To Exclude | fixedCollection | {} |  | res=itemList,op=aggregateItems |
| `fieldsToInclude` | Fields To Include | fixedCollection | {} |  | res=itemList,op=aggregateItems |
| `compare` | Compare | options | allFields |  | res=itemList,op=removeDuplicates |
| `fieldsToExclude` | Fields To Exclude | fixedCollection | {} |  | res=itemList,op=removeDuplicates |
| `fieldsToCompare` | Fields To Compare | fixedCollection | {} |  | res=itemList,op=removeDuplicates |
| `type` | Type | options | simple |  | res=itemList,op=sort |
| `sortFieldsUi` | Fields To Sort By | fixedCollection | {} | true | res=itemList,op=sort |
| `code` | Code | string |  |  | res=itemList,op=sort |
| `maxItems` | Max Items | number | 1 |  | res=itemList,op=limit |
| `keep` | Keep | options | firstItems |  | res=itemList,op=limit |
| `options` | Options | collection | {} |  | res=itemList,op=removeDuplicates |
| `options` | Options | collection | {} |  | res=itemList,op=sort |
| `options` | Options | collection | {} |  | res=itemList,op=splitOutItems,op=aggregateItems |
