# Redis — `n8n-nodes-base.redis`
**Type** `n8n-nodes-base.redis` · **action**
**What:** Key-value operations on a Redis instance — get, set, delete, increment, pattern-search keys, and publish to Pub/Sub channels.
**Credentials:** `redis`

## Resources / Operations
| Operation |
|-----------|
| Delete a key |
| Get value of a key |
| Get generic Redis instance info |
| Increment a key by 1 (atomic; creates key if absent) |
| Keys — return all keys matching a pattern |
| Set value of a key |
| Publish message to a Redis channel |

## Key params & gotchas
- Supports use as an AI tool node.
- **Increment** is atomic (INCR); safe for distributed counters without race conditions.
- **Keys** uses `KEYS pattern` (e.g., `user:*`) — this blocks Redis on large keyspaces; prefer `SCAN` patterns in production or scope the pattern tightly.
- **Publish** sends to a Pub/Sub channel; subscribers must already be listening — this node is publish-only, not subscribe.
- Set supports optional TTL (expiry in seconds) via Additional Fields.
- A companion trigger node (`n8n-nodes-base.redisTrigger`) handles Pub/Sub subscriptions.
- Credentials: host, port, password (optional), database index, TLS toggle.

**Source:** n8n-nodes-base.redis.md  [doc-verified]
