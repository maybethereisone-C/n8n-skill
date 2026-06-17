# Mocean — `n8n-nodes-base.mocean`
**Type** `n8n-nodes-base.mocean` · **typeVersion** 1 · **action**
**What:** Send SMS and voice messages via the Mocean API (Asia-Pacific focused CPaaS provider).
**Credentials:** Mocean API key + secret (`moceanApi`).
**Resources / Operations:**
| Resource | Operations |
|---|---|
| SMS | Send SMS/Voice message |
| Voice | Send SMS/Voice message |

**Key params & gotchas:**
- Both SMS and Voice resources expose the same "Send SMS/Voice message" operation — the resource selection determines the channel.
- Mocean is primarily used in Southeast Asian markets; verify number format requirements per country.

**Source:** n8n-nodes-base.mocean.md  [doc-verified]
