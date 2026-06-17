# Lemlist — `n8n-nodes-base.lemlist`
**Type** `n8n-nodes-base.lemlist` · **typeVersion** 1 · **action**
**What:** Manage Lemlist cold outreach — leads, campaigns, activities, enrichment, teams, and unsubscribes.
**Credentials:** `lemlistApi` (API key).

## Resources / Operations
| Resource | Operations |
|---|---|
| Activity | Get Many |
| Campaign | Get Many, Get Stats |
| Enrichment | Get (previously completed), Enrich Lead (by email/LinkedIn URL), Enrich Person (by email/LinkedIn URL) |
| Lead | Create, Delete, Get, Unsubscribe |
| Team | Get, Get Credits |
| Unsubscribe | Add (email to list), Delete (from list), Get Many |

## Key params & gotchas
- **Lead→Create** adds a lead to a specific campaign — `campaignId` is required.
- **Lead→Unsubscribe** marks the lead as unsubscribed in Lemlist (stops all future sequences); distinct from **Unsubscribe→Add** which manages the global unsubscribe list.
- **Enrichment→Enrich Lead** vs **Enrich Person**: Lead enrichment is tied to a campaign lead record; Person enrichment is standalone.
- **Campaign→Get Stats** returns open/click/reply rates per campaign — useful for reporting automations.
- **Team→Get Credits** returns remaining enrichment/email verification credits.

**Source:** n8n-nodes-base.lemlist.md  [doc-verified]
