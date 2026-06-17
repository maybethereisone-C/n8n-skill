# Stripe Trigger  (`n8n-nodes-base.stripeTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: stripeApi
- resources: balance, charge, coupon, customer, customerCard, meterEvent, source, token
- operations: add, create, delete, get, getAll, remove, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `events` | Events | multiOptions | [] | true |  |
| `apiVersion` | API Version | string |  |  |  |
| `resource` | Resource | options | balance |  |  |
