# Wise Trigger  (`n8n-nodes-base.wiseTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: wiseApi
- resources: account, exchangeRate, profile, quote, recipient, transfer
- operations: create, delete, execute, get, getAll, getBalances, getCurrencies, getStatement

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `profileId` | Profile Name or ID | options |  | true |  |
| `event` | Event | options |  | true |  |
| `resource` | Resource | options | account |  |  |
