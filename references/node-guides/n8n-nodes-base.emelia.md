# Emelia — `n8n-nodes-base.emelia`
**Type** `n8n-nodes-base.emelia` · **action**
**What:** Manage Emelia cold-email campaigns and contact lists.
**Credentials:** emeliApi (API key).

## Resources / Operations
| Resource | Operations |
|---|---|
| Campaign | Add Contact, Create, Get, Get All, Pause, Start |
| Contact List | Add Contact, Get All |

## Key params & gotchas
- **Campaign Add Contact** adds a contact directly to a running or paused campaign — the contact will enter the sequence from step 1.
- **Campaign Pause / Start** controls send state; pausing mid-sequence preserves contact position.
- A companion trigger node exists: `n8n-nodes-base.emeliaTrigger` for event-driven responses to campaign events.
- Contact List "Add" is for list management separate from campaigns.

**Source:** n8n-nodes-base.emelia.md  [doc-verified]
