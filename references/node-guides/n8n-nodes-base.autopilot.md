# Autopilot — `n8n-nodes-base.autopilot`
**Type** `n8n-nodes-base.autopilot` · **action**
**What:** Manage contacts, lists, and journeys in Autopilot (legacy — now Ortto). Incompatible with the new Ortto API.
**Credentials:** Autopilot API key credential.

## Resources / Operations
| Resource | Operations |
|---|---|
| Contact | Create/Update, Delete, Get, Get All |
| Contact Journey | Add contact to list |
| Contact List | Add contact to list, Check if on list, Get all contacts on list, Remove from list |
| List | Create, Get All |

## Key params & gotchas
- **Branding change warning:** Autopilot rebranded to Ortto. This node only works with the old Autopilot API — the new Ortto API is incompatible.
- Contact/Create/Update upserts by email — if the email already exists the contact is updated.
- Contact Journey "Add to list" adds the contact to a journey trigger list, initiating the journey.
- Contact List and Contact Journey both deal with lists but serve different purposes: Contact List manages list membership; Contact Journey triggers automation.

**Source:** n8n-nodes-base.autopilot.md  [doc-verified]
