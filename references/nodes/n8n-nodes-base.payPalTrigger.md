# PayPal Trigger  (`n8n-nodes-base.payPalTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: payPalApi
- resources: payout, payoutItem
- operations: cancel, create, get

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `events` | Event Names or IDs | multiOptions | [] | true |  |
| `resource` | Resource | options | payout |  |  |
