# Mautic — `n8n-nodes-base.mautic`
**Type** `n8n-nodes-base.mautic` · **typeVersion** 1 · **action**
**What:** Full contact lifecycle management in Mautic open-source marketing automation — contacts, companies, campaigns, segments, and email sending.
**Credentials:** `mauticApi` (base URL + username + password) or `mauticOAuth2Api` (OAuth2).

## Resources / Operations
| Resource | Operations |
|---|---|
| Campaign Contact | Add to Campaign, Remove from Campaign |
| Company | Create, Delete, Get, Get All, Update |
| Company Contact | Add Contact to Company, Remove Contact from Company |
| Contact | Create, Delete, Edit Points, Add/Remove from Do-Not-Contact List, Get, Get All, Send Email, Update |
| Contact Segment | Add to Segment, Remove from Segment |
| Segment Email | Send |

## Key params & gotchas
- **Contact→Edit Points** adjusts a contact's lead score by delta value (positive or negative) — used for behavioral scoring automation.
- **Contact→Add/Remove Do-Not-Contact** manages the DNC list (GDPR compliance) — removing from DNC re-enables marketing.
- **Contact→Send Email** sends a specific Mautic email template to a single contact immediately (not via campaign).
- **Segment Email→Send** dispatches a segment email to all contacts in a segment — use with care; this fires immediately.
- Mautic base URL must include the scheme and path (e.g. `https://mautic.yourdomain.com`).
- Mautic API must be enabled in Mautic settings (Configuration → API Settings → Enable HTTP basic auth API).

**Source:** n8n-nodes-base.mautic.md  [doc-verified]
