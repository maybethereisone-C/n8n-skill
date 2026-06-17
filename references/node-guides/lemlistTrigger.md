# Lemlist Trigger — `n8n-nodes-base.lemlistTrigger`
**Type** `n8n-nodes-base.lemlistTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires when a Lemlist email outreach event occurs (send, open, reply, bounce, unsubscribe, LinkedIn activity, Aircall, etc.).
**Credentials:** `lemlistApi` (API key).
**Resources / Operations:**
| Event | Notes |
|---|---|
| `*` | All events |
| Emails Sent / Opened / Clicked / Replied / Bounced / Failed / Unsubscribed | Email channel |
| LinkedIn Invite / Sent / Replied / Visit Done/Failed / Voice Note | LinkedIn channel |
| Aircall Created / Done / Ended / Interested / Not Interested | Aircall channel |
| Api Done / Failed / Interested / Not Interested | API step |
| Attracted / Contacted / Hooked / Warmed / Interested / Not Interested / Paused / Resumed / Skipped | Lead lifecycle |
| Custom Domain Errors / Connection Issue / Send Limit Reached / Lemwarm Paused | System alerts |
| Opportunities Done | Opportunity tracking |

**Key params & gotchas:**
- Select `*` to catch all events in a single trigger node; use a Switch node downstream to branch by event type.
- The event payload includes `campaignId`, `leadEmail`, and event-specific fields — structure varies per event type.
- Webhook is registered automatically on workflow activation.

**Source:** n8n-nodes-base.lemlisttrigger.md  [doc-verified]
