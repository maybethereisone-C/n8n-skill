# Wise  (`n8n-nodes-base.wise`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: wiseApi
- resources: account, exchangeRate, profile, quote, recipient, transfer
- operations: create, delete, execute, get, getAll, getBalances, getCurrencies, getStatement

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | account |  |  |
| `profileId` | Profile Name or ID | options |  | true |  |
| `event` | Event | options |  | true |  |
