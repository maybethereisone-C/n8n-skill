# HubSpot Trigger — `n8n-nodes-base.hubspotTrigger`
**Type** `n8n-nodes-base.hubspotTrigger` · **typeVersion** 2.2 · **trigger**
**What:** Fires on HubSpot CRM/CMS events (contacts, companies, deals, tickets, conversations) via webhook.
**Credentials:** `hubspotApi` / `hubspotDeveloperApi` / `hubspotOAuth2Api`

## Events

| Object | Events |
|---|---|
| Company | created, deleted, property_changed |
| Contact | created, deleted, privacy_deleted, property_changed |
| Conversation | created, deleted, new_message, privacy_deletion, property_changed |
| Deal | created, deleted, property_changed |
| Ticket | created, deleted, property_changed |

## Key params & gotchas
- `eventsUi` — fixedCollection, required; default `contact.creation`. Add one or more object+event pairs.
- **One webhook limit:** HubSpot only allows one active webhook per app. Activating a second trigger node deactivates the first. Use a single trigger with multiple events and route downstream with an IF/Switch node.
- `additionalFields` — optional collection for filtering (e.g., `propertyName` for property_changed events).
- `authentication` — `apiKey`, `developerApi`, or OAuth2; Developer API credential needed to register app webhooks.
- Companion app node: `n8n-nodes-base.hubspot`.

**Source:** n8n-nodes-base.hubspottrigger.md + schema  [doc-verified]
