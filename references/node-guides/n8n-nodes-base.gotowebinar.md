# GoToWebinar — `n8n-nodes-base.goToWebinar`
**Type** `n8n-nodes-base.goToWebinar` · **typeVersion** 1 · **action**
**What:** Manages GoToWebinar webinars, registrants, attendees, co-organizers, panelists, and sessions.
**Credentials:** `goToWebinarOAuth2Api` (OAuth2 — GoToWebinar developer account required).

**Resources / Operations:**

| Resource | Operations |
|---|---|
| Attendee | Get, Get All, Get Details |
| Co-Organizer | Create, Delete, Get All, Re-invite |
| Panelist | Create, Delete, Get All, Re-invite |
| Registrant | Create, Delete, Get, Get All |
| Session | Get, Get All, Get Details |
| Webinar | Create, Get, Get All, Update |

**Key params & gotchas:**
- Webinar and Session keys are GUIDs (not human-readable); store them from Create or Get All responses for use in subsequent operations.
- Registrant > Create requires at minimum `firstName`, `lastName`, and `email`; additional fields (address, phone) depend on the webinar's registration settings.
- Attendee data (actual attendance) is only available **after** a session ends; querying before completion returns empty results.
- Co-Organizer and Panelist Re-invite sends an email but does not update their registration — use it to resend credentials.
- GoToWebinar OAuth tokens expire; n8n auto-refreshes using the refresh token if configured correctly.

**Source:** n8n-nodes-base.gotowebinar.md  [doc-verified]
