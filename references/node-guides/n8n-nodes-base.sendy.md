# Sendy — `n8n-nodes-base.sendy`
**Type** `n8n-nodes-base.sendy` · **action**
**What:** Manage self-hosted Sendy email campaigns and subscriber lists.
**Credentials:** `sendyApi`

## Resources / Operations
| Resource | Operation |
|----------|-----------|
| Campaign | Create |
| Subscriber | Add to list |
| Subscriber | Count subscribers |
| Subscriber | Delete from list |
| Subscriber | Unsubscribe from list |
| Subscriber | Get status |

## Key params & gotchas
- Sendy is **self-hosted** — credentials require your Sendy installation URL and API key from Settings.
- Campaign Create does not send — it creates a draft; sending requires a separate action (not available via this node; use HTTP Request to Sendy's send API endpoint).
- List ID is numeric; find it in the Sendy admin under the list settings URL.
- "Add to list" does not re-subscribe unsubscribed users by default — Sendy prevents re-subscription unless the subscriber explicitly opts back in.
- Subscriber Count returns the confirmed subscriber count for a given list ID.

**Source:** n8n-nodes-base.sendy.md  [doc-verified]
