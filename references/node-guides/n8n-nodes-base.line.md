# Line — `n8n-nodes-base.line`
**Type** `n8n-nodes-base.line` · **typeVersion** 1 · **action**
**What:** Send LINE Notify push notifications to users or groups.
**Credentials:** `lineNotifyOAuth2Api` (OAuth2 — LINE Notify).

## Resources / Operations
| Resource | Operations |
|---|---|
| Notification | Send (to user or group) |

## Key params & gotchas
- **DEPRECATED**: LINE Notify discontinued service on **April 1, 2025**. This node no longer functions for new integrations.
- Existing workflows using this node will fail; migrate to LINE Messaging API or an alternative notification service.
- For historical reference: the node sent text/image notifications via LINE Notify's OAuth2 token.

**Source:** n8n-nodes-base.line.md  [doc-verified]
