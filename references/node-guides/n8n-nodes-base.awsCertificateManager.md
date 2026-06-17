# AWS Certificate Manager — `n8n-nodes-base.awsCertificateManager`
**Type** `n8n-nodes-base.awsCertificateManager` · **action**
**What:** Manage SSL/TLS certificates in AWS Certificate Manager (ACM).
**Credentials:** AWS credential (access key + secret, with ACM permissions).

## Resources / Operations
| Resource | Operations |
|---|---|
| Certificate | Delete, Get, Get Many, Get Metadata, Renew |

## Key params & gotchas
- No "Create" operation — ACM certificates are requested via DNS/email validation flows not exposed here. Use AWS Console or CLI to issue; manage with this node.
- **Get Metadata** returns full certificate details including domain names, status, and expiry.
- **Renew** triggers ACM's managed renewal — only works for certificates already in PENDING_VALIDATION or ISSUED state.
- Requires IAM permissions: `acm:DescribeCertificate`, `acm:DeleteCertificate`, `acm:ListCertificates`, `acm:RenewCertificate`.

**Source:** n8n-nodes-base.awscertificatemanager.md  [doc-verified]
