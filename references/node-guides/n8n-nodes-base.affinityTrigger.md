# Affinity Trigger — `n8n-nodes-base.affinityTrigger`
**Type** `n8n-nodes-base.affinityTrigger` · **typeVersion** 1 · **trigger**

**What:** Fires on entity lifecycle events in Affinity (relationship intelligence / CRM for deal networks).

**Credentials:** `affinityApi` (API key).

**Resources / Operations:**
| Resource | Events |
|---|---|
| Field value | Created · Deleted · Updated |
| Field | Created · Deleted · Updated |
| File | Created · Deleted |
| List entry | Created · Deleted |
| List | Created · Deleted · Updated |
| Note | Created · Deleted · Updated |
| Opportunity | Created · Deleted · Updated |
| Organization | Created · Deleted · Updated |
| Person | Created · Deleted · Updated |

**Key params & gotchas:**
- Webhook-based. Affinity must be configured to point to n8n's webhook URL.
- Companion app node: `n8n-nodes-base.affinity`.

**Source:** n8n-nodes-base.affinitytrigger.md  [doc-verified]
