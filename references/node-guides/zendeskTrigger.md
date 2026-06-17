# Zendesk Trigger — `n8n-nodes-base.zendeskTrigger`
**Type** `n8n-nodes-base.zendeskTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires on Zendesk support ticket events (ticket created, updated, status changed, etc.) via Zendesk webhook + trigger.
**Credentials:** `zendeskApi` (API token + email + subdomain) or `zendeskOAuth2Api`.
**Resources / Operations:**
| Event | Notes |
|---|---|
| Ticket Created | New support ticket opened |
| Ticket Status Changed | Ticket moves to new status (open/pending/solved/closed) |
| Ticket Priority Changed | Priority level changed |
| Ticket Assigned | Ticket assigned to agent/group |
| Ticket Updated | Any field on the ticket updated |
| Ticket Solved | Ticket marked as solved |

**Key params & gotchas:**
- Trigger type: **webhook** — n8n creates a Zendesk Webhook + Trigger (automation rule) in Zendesk on workflow activation; these must be cleaned up manually if the workflow is deleted without deactivating first.
- Zendesk "Triggers" (their term for automation rules) evaluate conditions; n8n sets up a catch-all trigger that posts to n8n's webhook URL.
- The payload is a JSON body configured by the Zendesk trigger template — it includes ticket ID, subject, status, priority, requester, assignee.
- To filter to specific events (e.g. only "solved"), add an IF node downstream on `ticket.status`.
- Zendesk subdomain is required in credentials (e.g. `mycompany` for `mycompany.zendesk.com`).

**Source:** n8n-nodes-base.zendesktrigger.md  [doc-verified]
