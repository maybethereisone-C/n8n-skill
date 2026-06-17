# Pushcut — `n8n-nodes-base.pushcut`
**Type** `n8n-nodes-base.pushcut` · **action**
**What:** Send rich iOS push notifications with actions via Pushcut (iOS-only notification app).
**Credentials:** `pushcutApi`

## Resources / Operations
| Resource | Operation |
|----------|-----------|
| Notification | Send a notification |

## Key params & gotchas
- Pushcut is **iOS-only** — Android devices are not supported.
- Notifications are defined in the Pushcut app and referenced by name in n8n; the node sends to a named notification definition, not arbitrary text.
- Supports custom actions (shortcuts, URLs) configured on the Pushcut side; n8n triggers the send.
- API key is found in the Pushcut app under Account settings.

**Source:** n8n-nodes-base.pushcut.md  [doc-verified]
