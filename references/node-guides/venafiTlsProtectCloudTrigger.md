# Venafi TLS Protect Cloud Trigger — `n8n-nodes-base.venafiTlsProtectCloudTrigger`
**Type** `n8n-nodes-base.venafiTlsProtectCloudTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires on certificate lifecycle events in Venafi TLS Protect Cloud (machine identity management).
**Credentials:** `venafiTlsProtectCloudApi` (API key for vaas.venafi.com).
**Resources / Operations:**
| Event category | Notes |
|---|---|
| Certificate expiry / renewal events | Certificate approaching expiry, renewed, revoked |
| Policy / issuance events | Certificate issued, request failed |

**Key params & gotchas:**
- Trigger type: **webhook** — Venafi TLS Protect Cloud pushes events to n8n's webhook URL.
- This node targets the **cloud-based** Venafi TLS Protect (vaas.venafi.com) only; not for on-prem Venafi Trust Protection Platform.
- Used in certificate automation pipelines: trigger renewal workflows or alert on expiry.

**Source:** n8n-nodes-base.venafitlsprotectcloudtrigger.md  [doc-verified]
