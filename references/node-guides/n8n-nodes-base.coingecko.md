# CoinGecko — `n8n-nodes-base.coingecko`
**Type** `n8n-nodes-base.coingecko` · **action**
**What:** Fetch cryptocurrency market data (prices, OHLC, history, tickers, events) from CoinGecko — no auth required.
**Credentials:** none (CoinGecko free tier is public).

## Resources / Operations
| Resource | Operations |
|---|---|
| Coin | Get OHLC candlestick chart, Get current data, Get All, Get historical data (by date), Get market pairs, Get historical market data (with granularity), Get current price (multi-currency), Get tickers |
| Event | Get All |

## Key params & gotchas
- No credentials required for the free public API; no credential field appears in the node.
- Can be used as an AI tool node.
- **Get historical market data** granularity (hourly vs daily) is auto-determined by CoinGecko based on the date range — you cannot override it.
- Coin IDs are CoinGecko slugs (e.g., `bitcoin`, `ethereum`), not ticker symbols.
- Free-tier rate limit is ~10–50 calls/min; add a Wait node for bulk lookups.

**Source:** n8n-nodes-base.coingecko.md  [doc-verified]
