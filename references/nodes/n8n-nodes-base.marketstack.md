# Marketstack  (`n8n-nodes-base.marketstack`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: marketstackApi
- resources: endOfDayData, exchange, ticker
- operations: get, getAll

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | endOfDayData | true |  |
