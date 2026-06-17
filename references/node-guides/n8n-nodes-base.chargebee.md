# Chargebee — `n8n-nodes-base.chargebee`
**Type** `n8n-nodes-base.chargebee` · **action**
**What:** Manage Chargebee subscriptions, customers, and invoices for subscription billing workflows.
**Credentials:** Chargebee API key credential (site name + API key).

## Resources / Operations
| Resource | Operations |
|---|---|
| Customer | Create |
| Invoice | Get All (list), Get PDF URL |
| Subscription | Cancel, Delete |

## Key params & gotchas
- Very limited operation set — only create customer, list/get invoices, cancel/delete subscriptions. For updates, plan changes, or other operations use the HTTP Request node with Chargebee's REST API.
- **Invoice/Get PDF URL** returns a time-limited URL to download the invoice PDF.
- **Subscription/Cancel** vs **Delete**: Cancel ends the subscription at period end (or immediately); Delete permanently removes it from Chargebee — use Cancel for standard churn flows.
- **Site name** in the credential is the subdomain: `<site>.chargebee.com`.
- Chargebee webhook triggers are handled via n8n's Webhook node, not a dedicated trigger node.

**Source:** n8n-nodes-base.chargebee.md  [doc-verified]
