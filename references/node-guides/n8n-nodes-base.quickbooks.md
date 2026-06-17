# QuickBooks Online — `n8n-nodes-base.quickbooks`
**Type** `n8n-nodes-base.quickbooks` · **action**
**What:** Manage QuickBooks Online accounting entities — bills, customers, employees, estimates, invoices, items, payments, purchases, transactions, and vendors.
**Credentials:** `quickBooksOAuth2Api`

## Resources / Operations
| Resource | Operation |
|----------|-----------|
| Bill | Create, Delete, Get, Get All, Update |
| Customer | Create, Get, Get All, Update |
| Employee | Create, Get, Get All, Update |
| Estimate | Create, Delete, Get, Get All, Send, Update |
| Invoice | Create, Delete, Get, Get All, Send, Update, Void |
| Item | Get, Get All |
| Payment | Create, Delete, Get, Get All, Send, Update, Void |
| Purchase | Get, Get All |
| Transaction | Get Report |
| Vendor | Create, Get, Get All, Update |

## Key params & gotchas
- Supports use as an AI tool node.
- Uses OAuth2 — tokens expire and require periodic reauthorization; QBO production tokens have a 101-day refresh expiry.
- **Send** operations (Invoice, Estimate, Payment) email the document to the customer — ensure customer email is set.
- **Void** differs from **Delete**: Void zeroes out the transaction and keeps audit history; Delete removes it entirely.
- Transaction → Get Report runs a QBO financial report (P&L, Balance Sheet, etc.) — report type is a required parameter.
- QBO sandbox and production are separate environments with separate credentials.
- Custom fields require using Additional Fields and QBO's custom field API names.

**Source:** n8n-nodes-base.quickbooks.md  [doc-verified]
