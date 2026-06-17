# Venafi TLS Protect Datacenter — `n8n-nodes-base.venafitlsprotectdatacenter`
**Type** `n8n-nodes-base.venafitlsprotectdatacenter` · **typeVersion** 1 · **action**
**What:** Manage TLS certificates and policies in self-hosted Venafi TLS Protect (TPP / Datacenter).
**Credentials:** `venafitlsprotectdatacenterApi` (username + password + TPP server URL).
**Resources / Operations:**
| Resource | Operations |
|----------|-----------|
| Certificate | Create, Delete, Download, Get, Get Many, Renew |
| Policy | Get |

**Key params & gotchas:**
- Unlike the Cloud variant, this node supports Certificate Create (not just requests) and Policy Get.
- Certificates are identified by DN (Distinguished Name / path in the policy tree), not UUID.
- Policy Get retrieves the certificate policy folder settings, useful for validating allowed SANs/key lengths before issuance.
- Related: `n8n-nodes-base.venafitlsprotectcloud` for the SaaS variant.

**Source:** n8n-nodes-base.venafitlsprotectdatacenter.md  [doc-verified]
