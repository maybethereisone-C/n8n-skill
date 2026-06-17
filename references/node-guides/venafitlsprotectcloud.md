# Venafi TLS Protect Cloud — `n8n-nodes-base.venafitlsprotectcloud`
**Type** `n8n-nodes-base.venafitlsprotectcloud` · **typeVersion** 1 · **action**
**What:** Manage TLS certificates and certificate requests in Venafi TLS Protect Cloud (VaaS).
**Credentials:** `venafitlsprotectcloudApi` (API key from Venafi TLS Protect Cloud).
**Resources / Operations:**
| Resource | Operations |
|----------|-----------|
| Certificate | Delete, Download, Get, Get Many, Renew |
| Certificate Request | Create, Get, Get Many |

**Key params & gotchas:**
- Certificate Request (Create) initiates issuance; the actual Certificate resource is separate and issued asynchronously.
- Download returns the certificate in PEM/DER depending on options — specify format explicitly.
- A companion trigger node exists: `n8n-nodes-base.venafitlsprotectcloudtrigger` for event-driven flows.
- Related: `n8n-nodes-base.venafitlsprotectdatacenter` for on-prem Venafi installations.

**Source:** n8n-nodes-base.venafitlsprotectcloud.md  [doc-verified]
