# Acuity Scheduling Trigger — `n8n-nodes-base.acuitySchedulingTrigger`
**Type** `n8n-nodes-base.acuitySchedulingTrigger` · **typeVersion** 1 · **trigger**

**What:** Fires on appointment lifecycle events from Acuity Scheduling (cloud-based appointment scheduling).

**Credentials:** `acuitySchedulingApi` (user ID + API key).

**Resources / Operations:**
| Event |
|---|
| Appointment canceled |
| Appointment changed |
| Appointment rescheduled |
| Appointment scheduled |
| Order completed |

**Key params & gotchas:**
- Webhook-based trigger; n8n registers the webhook with Acuity automatically on workflow activation.
- "Appointment changed" and "Appointment rescheduled" are distinct events — rescheduled fires specifically when a time slot changes; changed covers other field edits.

**Source:** n8n-nodes-base.acuityschedulingtrigger.md  [doc-verified]
