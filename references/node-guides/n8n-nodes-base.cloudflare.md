# Cloudflare — `n8n-nodes-base.cloudflare`
**Type** `n8n-nodes-base.cloudflare` · **action**
**What:** Manage zone-level authenticated origin pull (TLS client) certificates.
**Credentials:** cloudflareApi (API token or Global API key + email).

## Resources / Operations
| Resource | Operations |
|---|---|
| Zone Certificate | Delete, Get, Get Many, Upload |

## Key params & gotchas
- This node covers **zone-level authenticated origin pull certificates only** — not general DNS, WAF, or Pages operations.
- **Upload** requires the PEM-encoded certificate body and private key as strings; typically pipe from a Read Binary File node.
- Zone ID is required for every operation; find it in the Cloudflare dashboard under the domain's Overview tab.
- Refer to [Cloudflare zone-level auth origin pulls API](https://api.cloudflare.com/#zone-level-authenticated-origin-pulls-properties) for field details.

**Source:** n8n-nodes-base.cloudflare.md  [doc-verified]
