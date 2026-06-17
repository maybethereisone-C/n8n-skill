# Pushcut Trigger — `n8n-nodes-base.pushcutTrigger`
**Type** `n8n-nodes-base.pushcutTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires when a Pushcut iOS notification action is tapped, allowing iOS Shortcuts + n8n automation from iPhone/iPad.
**Credentials:** `pushcutApi` (API key from the Pushcut app).
**Resources / Operations:**
| Trigger | Notes |
|---|---|
| Integration Trigger action | Fires when the user taps the configured action in a Pushcut notification |

**Key params & gotchas:**
- **Manual pairing required in the Pushcut app:** the user must configure a notification action pointing to the n8n integration trigger — see setup steps below.
- Setup: Pushcut app → Notification → Add Action → Server tab → Integration tab → Integration Trigger → select the n8n action name.
- The action name set in n8n and the Pushcut app must match.
- Works only from an iOS/iPadOS device running the Pushcut app; there is no Android client.
- Great for "tap notification → trigger complex automation" personal workflows.

**Source:** n8n-nodes-base.pushcuttrigger.md  [doc-verified]
