# Help Scout Trigger — `n8n-nodes-base.helpScoutTrigger`
**Type** `n8n-nodes-base.helpScoutTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires on Help Scout customer support events (conversation and customer changes) via webhook.
**Credentials:** `helpScoutOAuth2Api`

## Events (multiOptions)

| Event | Notes |
|---|---|
| Conversation events | created, updated, deleted, assigned, unassigned, moved, status changed, tag changed, customer replied, user replied |
| Customer events | created, updated |
| Mailbox events | configuration changes |
| Thread events | new thread created |

## Key params & gotchas
- `events` — multiOptions, required, no default; select one or more events.
- OAuth2 only — no API-key credential variant.
- Help Scout's webhook system sends a signed payload; n8n registers the webhook automatically on activation and deregisters on deactivation.
- Companion app node: `n8n-nodes-base.helpScout`.

**Source:** n8n-nodes-base.helpscouttrigger.md + schema  [doc-verified]
