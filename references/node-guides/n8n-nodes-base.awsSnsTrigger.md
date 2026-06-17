# AWS SNS Trigger — `n8n-nodes-base.awsSnsTrigger`
**Type** `n8n-nodes-base.awsSnsTrigger` · **typeVersion** 1 · **trigger**

**What:** Receives notifications from AWS SNS (Simple Notification Service) topics via HTTP/S subscription.

**Credentials:** `aws` (access key ID, secret access key, region).

**Resources / Operations:**
| Event |
|---|
| New AWS SNS event (any message published to the subscribed SNS topic) |

**Key params & gotchas:**
- Webhook-based. n8n auto-subscribes to the SNS topic; AWS sends a confirmation request first — n8n handles the subscription confirmation automatically.
- n8n's webhook URL must be publicly reachable over HTTPS (SNS requires HTTPS endpoints).
- The SNS message arrives as a JSON envelope; actual payload is in `$.Message` (string, may need `JSON.parse()`).
- Companion app node: `n8n-nodes-base.awsSns`.

**Source:** n8n-nodes-base.awssnstrigger.md  [doc-verified]
