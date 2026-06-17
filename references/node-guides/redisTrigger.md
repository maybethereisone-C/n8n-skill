# Redis Trigger — `n8n-nodes-base.redisTrigger`
**Type** `n8n-nodes-base.redisTrigger` · **typeVersion** 1 · **trigger**
**What:** Subscribes to a Redis Pub/Sub channel and fires the workflow for each published message.
**Credentials:** `redis` (host, port, database index, optional password, TLS).
**Resources / Operations:**
| Trigger type | Notes |
|---|---|
| Pub/Sub channel subscription | Persistent subscriber; one execution per PUBLISH message |

**Key params & gotchas:**
- **Channels** — comma-separated list; supports Redis pattern subscriptions with `*` wildcard (uses `PSUBSCRIBE`).
- This is Redis Pub/Sub — messages are ephemeral. If n8n is offline when a message is published, it is lost. Use Redis Streams (via HTTP node + XREAD) if durability is required.
- The trigger does **not** poll lists or sorted sets — it only subscribes to channels.
- JSON payloads are automatically parsed if the content looks like JSON.

**Source:** n8n-nodes-base.redistrigger.md  [doc-verified]
