# Keap — `n8n-nodes-base.keap`
**Type** `n8n-nodes-base.keap` · **typeVersion** 1 · **action**
**What:** Automate Keap (formerly Infusionsoft) CRM — contacts, companies, tags, notes, orders, products, emails, and files.
**Credentials:** `keapOAuth2Api` (OAuth2).

## Resources / Operations
| Resource | Operations |
|---|---|
| Company | Create, Get All |
| Contact | Create/Update (upsert), Delete, Get, Get All |
| Contact Note | Create, Delete, Get, Get All, Update |
| Contact Tag | Add Tags (list), Delete Tag, Get All Tags |
| Ecommerce Order | Create, Delete, Get, Get All |
| Ecommerce Product | Create, Delete, Get, Get All |
| Email | Create Record (log sent email), Get All Sent, Send Email |
| File | Delete, Get All, Upload |

## Key params & gotchas
- **Contact→Create/Update** upserts by email; the `duplicate_option` param controls behavior when duplicates exist.
- **Contact Tag→Add Tags** accepts a list of tag IDs — not tag names; look up IDs via the Keap UI or API first.
- **Email→Create Record** logs an already-sent email to a contact's history — it does not send; use **Send Email** for actual sending.
- **Ecommerce Order→Create** requires a `contact_id` and at least one line item with a product ID.
- OAuth2 access tokens expire; n8n handles refresh automatically if the credential is OAuth2.

**Source:** n8n-nodes-base.keap.md  [doc-verified]
