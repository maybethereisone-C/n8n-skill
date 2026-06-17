# Pipedrive Trigger — `n8n-nodes-base.pipedriveTrigger`
**Type** `n8n-nodes-base.pipedriveTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires when a Pipedrive CRM event occurs (deal, person, organization, activity, etc.) via webhook.
**Credentials:** `pipedriveApi` (API token) or `pipedriveOAuth2Api`.
**Resources / Operations:**
| Object | Events |
|---|---|
| Deal | Added, updated, deleted, merged |
| Person | Added, updated, deleted, merged |
| Organization | Added, updated, deleted, merged |
| Activity | Added, updated, deleted |
| Note | Added, updated, deleted |
| Pipeline / Stage | Added, updated, deleted |
| Product | Added, updated, deleted |
| User | Added, updated |

**Key params & gotchas:**
- n8n auto-registers the Pipedrive webhook on activation.
- Each trigger node maps to one object + action combination — use multiple nodes or the generic Webhook node for multi-object flows.
- The payload includes `current` (new state) and `previous` (old state) objects — useful for detecting field-level changes.
- Pipedrive sends both `added` and `updated` events on merge operations.

**Source:** n8n-nodes-base.pipedrivetrigger.md  [doc-verified]
