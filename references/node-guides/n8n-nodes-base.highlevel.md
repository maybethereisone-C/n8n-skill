# HighLevel — `n8n-nodes-base.highlevel`
**Type** `n8n-nodes-base.highlevel` · **typeVersion** 1 · **action**
**What:** Manage HighLevel CRM contacts, opportunities, tasks, and calendar appointments.
**Credentials:** `highLevelOAuth2Api` (OAuth2 — sub-account or agency key).

## Resources / Operations
| Resource | Operations |
|---|---|
| Contact | Create or Update (upsert), Delete, Get, Get Many, Update |
| Opportunity | Create, Delete, Get, Get Many, Update |
| Task | Create, Delete, Get, Get Many, Update |
| Calendar | Book Appointment, Get Free Slots |

## Key params & gotchas
- **Contact→Create or Update** is an upsert by email/phone — if a contact with that email already exists, it updates rather than creating a duplicate.
- **Calendar→Get Free Slots** requires a `calendarId` and a date range; slots are returned in the calendar's timezone.
- **Calendar→Book Appointment** requires a `calendarId`, `contactId`, `startTime`, and `endTime` — all must be ISO 8601 with timezone.
- HighLevel's API is sub-account scoped; the credential must be authorized for the specific location/sub-account.

**Source:** n8n-nodes-base.highlevel.md  [doc-verified]
