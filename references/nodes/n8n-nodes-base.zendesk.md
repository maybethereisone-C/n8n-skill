# Zendesk  (`n8n-nodes-base.zendesk`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: zendeskApi, zendeskOAuth2Api
- resources: organization, ticket, ticketField, user
- operations: changed, count, create, delete, get, getAll, getOrganizations, getRelatedData, greater_than, is, is_not, less_than, not_changed, not_value, not_value_previous, recover, search, update, value, value_previous

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | apiToken |  |  |
| `resource` | Resource | options | ticket |  |  |
| `service` | Service | options | support | true |  |
| `options` | Options | collection | {} |  |  |
| `conditions` | Conditions | fixedCollection | {} |  |  |
