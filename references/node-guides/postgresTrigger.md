# Postgres Trigger — `n8n-nodes-base.postgresTrigger`
**Type** `n8n-nodes-base.postgresTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires when rows are inserted, updated, or deleted in a PostgreSQL table, or when a message is published to a LISTEN channel.
**Credentials:** `postgres` (host, port, database, user, password, SSL).
**Resources / Operations:**
| Mode | Trigger on |
|---|---|
| Listen and Create Trigger Rule | INSERT / UPDATE / DELETE on a table |
| Listen to Channel | NOTIFY on a named channel |

**Key params & gotchas:**
- **Auto-manages DB objects:** on workflow activation n8n creates a Postgres trigger function + trigger on the target table; on deactivation it removes them. If activation fails partway, stale triggers may remain — clean up manually with `DROP TRIGGER` / `DROP FUNCTION`.
- **Permissions required:** the credential user needs `TRIGGER` privilege on the table plus `CREATE` on the schema (effectively superuser or table owner for most setups).
- **Listen to Channel** mode lets you use `pg_notify('channel', payload)` from your own procedures — n8n just listens; it does **not** create any DB objects in this mode.
- Works over a persistent connection (not polling) — near-real-time delivery.
- Test mode (manual trigger test in editor) also creates the trigger temporarily; it is removed when test listening stops.

**Minimal example (Insert trigger):**
```
Postgres Trigger
  - Mode: Listen and Create Trigger Rule
  - Table: orders
  - Events: Insert
→ receives { new: { id, product, qty, ... } }
```

**Source:** n8n-nodes-base.postgrestrigger.md  [doc-verified]
