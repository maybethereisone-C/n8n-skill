# Pushover — `n8n-nodes-base.pushover`
**Type** `n8n-nodes-base.pushover` · **action**
**What:** Send push notifications to iOS/Android devices via the Pushover service.
**Credentials:** `pushoverApi`

## Resources / Operations
| Resource | Operation |
|----------|-----------|
| Message | Push (send a notification) |

## Key params & gotchas
- Supports use as an AI tool node.
- Requires both an **API Token** (application key) and a **User Key** (recipient); both are distinct values from Pushover dashboard.
- Priority levels: -2 (lowest, no sound) through 2 (emergency, requires acknowledgement). Priority 2 loops until acknowledged — always set an expiry and retry interval to avoid infinite loops.
- Supports HTML formatting in message body; enable with the `html` flag.
- Device targeting: leave blank to send to all user devices, or specify device name.
- Sound and title customization available in additional parameters.

**Source:** n8n-nodes-base.pushover.md  [doc-verified]
