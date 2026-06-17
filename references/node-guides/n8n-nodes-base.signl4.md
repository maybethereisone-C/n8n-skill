# SIGNL4 — `n8n-nodes-base.signl4`
**Type** `n8n-nodes-base.signl4` · **action**
**What:** Send and resolve mobile alerting notifications via SIGNL4 (targeted at field service and ops teams).
**Credentials:** `signl4Api`

## Resources / Operations
| Resource | Operation |
|----------|-----------|
| Alert | Send an alert |
| Alert | Resolve an alert |

## Key params & gotchas
- SIGNL4 credential uses a **team secret** (webhook token) from the SIGNL4 team settings — not username/password.
- Alerts support title, message, color coding, and custom parameters for mobile display.
- **Resolve** requires the `X-S4-ExternalEventId` that was set when the alert was originally sent — always set a meaningful external event ID on send for later resolution.
- Alerts are routed to on-call team members based on SIGNL4 duty scheduling.
- Useful for escalation workflows: send alert → wait for response or timeout → auto-resolve or escalate.

**Source:** n8n-nodes-base.signl4.md  [doc-verified]
