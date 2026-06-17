# Chargebee Trigger  (`n8n-nodes-base.chargebeeTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: chargebeeApi
- resources: customer, invoice, subscription
- operations: after, before, cancel, create, delete, gt, gte, is, is_not, list, lt, lte, pdfUrl

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `events` | Events | multiOptions | [] | true |  |
| `resource` | Resource | options | invoice |  |  |
| `operation` | Operation | options | create |  | res=customer |
| `properties` | Properties | collection | {} |  | res=customer,op=create |
| `operation` | Operation | options | list |  | res=invoice |
| `maxResults` | Max Results | number | 10 |  | res=invoice,op=list |
| `filters` | Filters | fixedCollection | after |  | res=invoice,op=list |
| `invoiceId` | Invoice ID | string |  | true | res=invoice,op=pdfUrl |
| `operation` | Operation | options | delete |  | res=subscription |
| `subscriptionId` | Subscription ID | string |  | true | res=subscription,op=cancel |
| `endOfTerm` | Schedule End of Term | boolean | false |  | res=subscription,op=cancel |
| `subscriptionId` | Subscription ID | string |  | true | res=subscription,op=delete |
