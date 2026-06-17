# Invoice Ninja — `n8n-nodes-base.invoiceninja`
**Type** `n8n-nodes-base.invoiceninja` · **typeVersion** 1 · **action**
**What:** Automate Invoice Ninja billing — manage clients, expenses, invoices, payments, quotes, and tasks.
**Credentials:** `invoiceNinjaApi` (API token + base URL for self-hosted).

## Resources / Operations
| Resource | Operations |
|---|---|
| Client | Create, Delete, Get, Get All |
| Expense | Create, Delete, Get, Get All |
| Invoice | Create, Delete, Email, Get, Get All |
| Payment | Create, Delete, Get, Get All |
| Quote | Create, Delete, Email, Get, Get All |
| Task | Create, Delete, Get, Get All |

## Key params & gotchas
- **Invoice→Email** and **Quote→Email** send the document to the client's email directly from Invoice Ninja — requires a configured email provider in IN settings.
- Self-hosted Invoice Ninja requires the **base URL** in the credential (e.g. `https://invoicing.yourdomain.com`).
- Clients have no **Update** operation — to modify a client, delete and recreate, or use the Invoice Ninja UI.
- **Payment→Create** links a payment to an invoice via `invoice_id`; partial payments are supported.
- Invoice Ninja v4 and v5 have different API structures; confirm the credential API version matches your installation.

**Source:** n8n-nodes-base.invoiceninja.md  [doc-verified]
