# HubSpot  (`n8n-nodes-base.hubspot`)

- typeVersion (max): **2.2**  | group: output  | trigger: no
- credentials: hubspotApi, hubspotDeveloperApi, hubspotOAuth2Api
- resources: company, contact, contactList, deal, engagement, form, ticket
- operations: add, create, delete, get, getAll, getFields, getRecentlyCreated, getRecentlyCreatedUpdated, getRecentlyModified, remove, search, searchByDomain, submit, update, upsert

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `eventsUi` | Events | fixedCollection | contact.creation | true |  |
| `additionalFields` | Additional Fields | collection | {} |  |  |
| `authentication` | Authentication | options | apiKey |  |  |
| `resource` | Resource | options | deal |  |  |
