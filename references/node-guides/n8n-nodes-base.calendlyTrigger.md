# Calendly Trigger — `n8n-nodes-base.calendlyTrigger`
**Type** `n8n-nodes-base.calendlyTrigger` · **typeVersion** 1 · **trigger**

**What:** Fires when Calendly bookings are created or canceled.

**Credentials:** `calendlyApi` (personal access token).

**Resources / Operations:**
| Event |
|---|
| Event created |
| Event canceled |

**Key params & gotchas:**
- Webhook-based. Calendly **requires** the callback URL to be a **public HTTPS** URL — local testing requires a tunnel (ngrok, Cloudflare Tunnel) and `N8N_WEBHOOK_URL` set to the public HTTPS address.
- **Only fires for Calendly-managed bookings** — creating/editing an event directly in Google Calendar (or other connected calendars) does NOT trigger this node.
- Only one webhook per Calendly app is allowed; testing URL and production URL cannot both be active simultaneously. Unpublish the workflow to test, then republish.

**Source:** n8n-nodes-base.calendlytrigger.md  [doc-verified]
