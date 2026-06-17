# PayPal  (`n8n-nodes-base.payPal`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: payPalApi
- resources: payout, payoutItem
- operations: cancel, create, get

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | payout |  |  |
| `events` | Event Names or IDs | multiOptions | [] | true |  |
