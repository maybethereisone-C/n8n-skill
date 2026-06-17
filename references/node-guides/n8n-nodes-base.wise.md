# Wise — `n8n-nodes-base.wise`
**Type** `n8n-nodes-base.wise` · **typeVersion** 1 · **action**
**What:** Read Wise (TransferWise) account data, manage transfers and quotes, and retrieve exchange rates.
**Credentials:** `wiseApi` (API token; use sandbox token for testing).

## Resources / Operations
| Resource | Operations |
|---|---|
| Account | Get Balances, Get Currencies, Get Statement |
| Exchange Rate | Get |
| Profile | Get, Get All |
| Recipient | Get All |
| Quote | Create, Get |
| Transfer | Create, Delete, Execute, Get, Get All |

## Key params & gotchas
- **Profile ID** is required for most operations — use Profile → Get All first to retrieve it.
- **Execute Transfer** is a separate operation from Create; creating a transfer does not fund it — call Execute after creating.
- The Wise sandbox environment uses different API tokens than production; switch credentials accordingly.
- Account Statement requires a date range and currency code.

**Source:** n8n-nodes-base.wise.md  [doc-verified]
