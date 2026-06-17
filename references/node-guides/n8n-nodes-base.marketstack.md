# marketstack — `n8n-nodes-base.marketstack`
**Type** `n8n-nodes-base.marketstack` · **typeVersion** 1 · **action**
**What:** Fetch stock market data — end-of-day prices, exchange info, and ticker details via marketstack API.
**Credentials:** `marketstackApi` (API key).

## Resources / Operations
| Resource | Operations |
|---|---|
| End-of-Day Data | Get All (OHLCV + volume for a symbol) |
| Exchange | Get (exchange details by MIC code) |
| Ticker | Get (ticker/symbol details) |

## Key params & gotchas
- **End-of-Day Data→Get All** requires a stock symbol (e.g. `AAPL`) and optionally date range filters; returns historical OHLCV data.
- Free tier only supports US markets and HTTP (not HTTPS) — use a paid plan for global markets and HTTPS.
- **Exchange** lookup uses MIC codes (e.g. `XNAS` for NASDAQ), not exchange names.
- marketstack is lowercase by brand convention — match exactly in n8n node search.
- Real-time data is not available; the earliest available date depends on subscription tier.

**Source:** n8n-nodes-base.marketstack.md  [doc-verified]
