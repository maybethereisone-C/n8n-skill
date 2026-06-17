# Stripe  (`n8n-nodes-base.stripe`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: stripeApi
- resources: balance, charge, coupon, customer, customerCard, meterEvent, source, token
- operations: add, create, delete, get, getAll, remove, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | balance |  |  |
| `events` | Events | multiOptions | [] | true |  |
| `apiVersion` | API Version | string |  |  |  |
