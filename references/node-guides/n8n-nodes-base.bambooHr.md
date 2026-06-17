# BambooHR — `n8n-nodes-base.bambooHr`
**Type** `n8n-nodes-base.bambooHr` · **action**
**What:** Manage BambooHR employee records, documents, files, and company reports.
**Credentials:** BambooHR API key credential (subdomain + API key).

## Resources / Operations
| Resource | Operations |
|---|---|
| Company Report | Get |
| Employee | Create, Get, Get All, Update |
| Employee Document | Delete, Download, Get All, Update, Upload |
| File (company) | Delete, Download, Get All, Update, Upload |

## Key params & gotchas
- **Subdomain** is required in the credential — it's the `<subdomain>` in `https://<subdomain>.bamboohr.com`.
- Employee/Get All returns a list with minimal fields by default — use the **Fields** param to specify which fields to include.
- Employee Document vs File: Employee Documents are attached to a specific employee; Files are company-level documents.
- Upload operations require binary data from a previous node; set the **Binary Property** param.
- Download returns binary data — pipe to Write Binary File node to save.
- Company Report/Get requires a report ID — find it in BambooHR's Reports section.

**Source:** n8n-nodes-base.bamboohr.md  [doc-verified]
