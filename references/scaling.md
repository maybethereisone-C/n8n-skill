# Scaling n8n (v2.26.0)

> Queue mode, concurrency control, worker setup, webhook processors, binary data, execution pruning, and multi-main HA.
>
> Sources: `hosting/scaling/queue-mode.md`, `hosting/scaling/concurrency-control.md`, `hosting/scaling/execution-data.md`, `hosting/scaling/external-storage.md`, `hosting/scaling/binary-data.md`, `hosting/scaling/overview.md`, `hosting/configuration/environment-variables/queue-mode.md`, `hosting/configuration/environment-variables/executions.md`.

---

## Execution modes

| Mode | Use when | Notes |
|---|---|---|
| `regular` | Single-instance, low-to-medium volume | n8n runs triggers, webhooks, and executions in the same process |
| `queue` | Multi-worker / high-volume / HA | Main receives triggers and webhooks; workers run executions via Redis queue |

```bash
export EXECUTIONS_MODE=queue   # set on main, all workers, and webhook processors
```

**Database:** queue mode requires **PostgreSQL 13+**. SQLite is not supported in queue mode.

**Binary data:** queue mode does not support `filesystem` binary data mode. Use `database` or `s3` (Enterprise) instead.

---

## Queue mode architecture

```
Triggers / Webhooks
        │
    [Main n8n]  ──── publishes execution ID ────▶  [Redis / Bull queue]
        │                                                    │
    [Editor UI]                                   picks up message
                                                            │
                                                    [Worker n8n]
                                                            │
                                               reads workflow from DB
                                               executes workflow
                                               writes results to DB
                                               notifies Redis → Main
```

1. Main handles timers, webhook calls, and the editor. It enqueues execution IDs.
2. Redis (Bull) maintains the queue. Workers pop jobs.
3. Workers fetch workflow data from the DB, execute, write results.
4. Redis notifies main that execution is complete.

Each worker is a Node.js process running in `main` mode with high IOPS for concurrent executions.

---

## Setting up queue mode

### Step 1 — Redis

```bash
# Docker quick-start
docker run --name n8n-redis -p 6379:6379 -d redis

# Required connection env vars on main + all workers
export QUEUE_BULL_REDIS_HOST=<redis-host>
export QUEUE_BULL_REDIS_PORT=6379
export QUEUE_BULL_REDIS_PASSWORD=<strong-password>   # always set in production
export QUEUE_BULL_REDIS_TLS=true                     # always in production
```

Optional Redis settings:

| Variable | Default | Notes |
|---|---|---|
| `QUEUE_BULL_REDIS_DB` | `0` | Change when sharing Redis |
| `QUEUE_BULL_REDIS_USERNAME` | — | For Redis 6+ ACLs |
| `QUEUE_BULL_REDIS_CLUSTER_NODES` | — | `host:port,host:port` list — activates Cluster client, ignores HOST/PORT |
| `QUEUE_BULL_REDIS_DUALSTACK` | `false` | IPv4+IPv6 dual-stack |
| `QUEUE_BULL_REDIS_TIMEOUT_THRESHOLD` | `10000` ms | Time to wait for Redis before n8n exits |
| `QUEUE_BULL_PREFIX` | — | Key prefix for multi-app Redis sharing |

### Step 2 — Shared encryption key

All instances (main + workers) **must** share the same `N8N_ENCRYPTION_KEY`. Workers use it to decrypt credentials from the DB.

```bash
export N8N_ENCRYPTION_KEY=<same-key-as-main>
```

### Step 3 — Start workers

```bash
# npm / CLI
n8n worker --concurrency=10

# Docker
docker run --name n8n-worker \
  -e EXECUTIONS_MODE=queue \
  -e QUEUE_BULL_REDIS_HOST=<redis-host> \
  -e QUEUE_BULL_REDIS_PASSWORD=<password> \
  -e N8N_ENCRYPTION_KEY=<key> \
  -e DB_TYPE=postgresdb \
  -e DB_POSTGRESDB_HOST=<pg-host> \
  docker.n8n.io/n8nio/n8n worker
```

The `--concurrency` flag controls how many jobs a worker executes in parallel (default `10`). Can also be set via `N8N_CONCURRENCY_PRODUCTION_LIMIT` (takes precedence over the flag if not `-1`).

**Recommendation:** set concurrency to **5 or higher** per worker. Low concurrency with many workers exhausts the DB connection pool.

### Step 4 — Credential overwrites in queue mode

If using credential overwrites, set `CREDENTIALS_OVERWRITE_PERSISTENCE=true` so overwrites propagate to workers via pub/sub through the DB.

### Worker server endpoints

Each worker exposes optional endpoints (set `QUEUE_HEALTH_CHECK_ACTIVE=true`):

- `GET /healthz` — is the worker up?
- `GET /healthz/readiness` — are DB and Redis connections ready?
- `GET /metrics` — Prometheus metrics (when `N8N_METRICS=true`)

```bash
export QUEUE_HEALTH_CHECK_ACTIVE=true
export QUEUE_HEALTH_CHECK_PORT=5678   # change if this port conflicts
```

### View running workers (Enterprise)

**Settings > Workers** in the n8n UI shows live worker performance metrics. Enterprise Self-hosted only.

---

## Webhook processors

Webhook processors are an optional additional scaling layer for handling large volumes of incoming webhook requests.

```bash
# Start a webhook processor
n8n webhook

# Docker
docker run --name n8n-webhook \
  -e EXECUTIONS_MODE=queue \
  -e QUEUE_BULL_REDIS_HOST=<redis-host> \
  -e N8N_ENCRYPTION_KEY=<key> \
  -p 5678:5678 \
  docker.n8n.io/n8nio/n8n webhook
```

**Important:** webhook processors need `EXECUTIONS_MODE=queue` and Redis access, just like workers.

### Load balancer routing

When using webhook processors, configure your load balancer:

| Path pattern | Route to |
|---|---|
| `/webhook/*` | Webhook processor pool |
| `/webhook-waiting/*` | Webhook processor pool (human-in-the-loop / "send and wait") |
| `/webhook-test/*` | Main process only (manual test runs) |
| Everything else | Main process (API, UI, static files) |

**Do not** add the main process to the webhook pool — it will receive production webhook load and degrade UI/API performance.

### Disable webhooks on main process

```bash
export N8N_DISABLE_PRODUCTION_MAIN_PROCESS=true
```

Forces all production webhook traffic to webhook processors. Run main separately and exclude it from the webhook pool.

### Set the webhook URL

```bash
export WEBHOOK_URL=https://your-webhook-url.com
```

Required when n8n is behind a reverse proxy so the correct external URL is shown for webhook nodes.

---

## Concurrency control

Source: `hosting/scaling/concurrency-control.md`, `hosting/configuration/environment-variables/executions.md`

### Regular mode

In regular mode, n8n has no concurrency limit by default. This can cause event-loop thrashing under load.

```bash
export N8N_CONCURRENCY_PRODUCTION_LIMIT=20
```

- Applies only to **production executions** (webhook/trigger-started). Does not limit manual, sub-workflow, error, or CLI executions.
- Queued executions are processed in FIFO order when capacity frees up.
- Queued executions cannot be retried. Cancelling removes from queue.
- On restart, n8n resumes queued executions up to the limit and re-enqueues the rest.

### Queue mode

In queue mode, per-worker concurrency is set with the `--concurrency` flag:

```bash
n8n worker --concurrency=10
```

`N8N_CONCURRENCY_PRODUCTION_LIMIT` takes precedence over `--concurrency` if set to a value other than `-1`.

### Evaluation concurrency

AI evaluation test runs use a separate limit:

| License tier | Default parallel test cases |
|---|---|
| Community / Pro | 1 |
| Business | 3 |
| Enterprise | 5 |

Override: `N8N_CONCURRENCY_EVALUATION_LIMIT=<n>`

---

## Offload manual executions to workers

```bash
export OFFLOAD_MANUAL_EXECUTIONS_TO_WORKERS=true
```

Sends manual (editor test-run) executions to workers instead of the main process. Useful when the main process needs to remain lightweight.

---

## Multi-main setup (HA — Enterprise)

Source: `hosting/scaling/queue-mode.md#multi-main-setup`

In queue mode, run multiple main processes for high availability.

**Leader/follower model:**
- **Follower** mains — run regular tasks (API, UI, webhooks).
- **Leader** main — runs regular tasks + at-most-once tasks (cron triggers, pollers, persistent connections, pruning). Leader is elected automatically via Redis TTL key.

**If the leader fails**, a follower takes over leadership automatically. When the previous leader recovers, it becomes a follower.

### Multi-main prerequisites

- All main processes in queue mode, connected to the same Postgres and Redis.
- All main and worker processes on the **same n8n version**.
- All mains behind a load balancer with **sticky sessions (session persistence)** enabled.

```bash
# Enable on ALL main instances
N8N_MULTI_MAIN_SETUP_ENABLED=true
```

### Multi-main tuning

| Variable | Default | Notes |
|---|---|---|
| `N8N_MULTI_MAIN_SETUP_KEY_TTL` | `10` s | TTL of the leader key in Redis. Shorter = faster failover, higher Redis traffic |
| `N8N_MULTI_MAIN_SETUP_CHECK_INTERVAL` | `3` s | How often each main checks if it is the leader |

---

## Binary data at scale

Source: `hosting/scaling/binary-data.md`, `hosting/scaling/external-storage.md`

| Mode | `N8N_DEFAULT_BINARY_DATA_MODE` | Use when |
|---|---|---|
| Memory (default) | `default` | Low-volume, small files; risk of OOM with large files |
| Filesystem | `filesystem` | Single-instance only; not compatible with queue mode |
| Database | `database` | Queue mode without S3; binary data stored in Postgres |
| S3 (Enterprise) | `s3` | Queue mode + large binary data; recommended for enterprise |

### Enabling S3 external storage (Enterprise)

```bash
export N8N_EXTERNAL_STORAGE_S3_HOST=s3.us-east-1.amazonaws.com
export N8N_EXTERNAL_STORAGE_S3_BUCKET_NAME=my-n8n-bucket
export N8N_EXTERNAL_STORAGE_S3_BUCKET_REGION=us-east-1    # no underscores since v2.6.4
export N8N_EXTERNAL_STORAGE_S3_ACCESS_KEY=AKIA...
export N8N_EXTERNAL_STORAGE_S3_ACCESS_SECRET=...

export N8N_AVAILABLE_BINARY_DATA_MODES=filesystem,s3
export N8N_DEFAULT_BINARY_DATA_MODE=s3
```

Or use IAM role / credential provider chain (no hard-coded keys):
```bash
export N8N_EXTERNAL_STORAGE_S3_AUTH_AUTO_DETECT=true
```

**S3 data path format:**
```
workflows/{workflowId}/executions/{executionId}/binary_data/{binaryFileId}
```

**Pruning:** n8n delegates binary data pruning to S3 lifecycle rules. **Configure a bucket lifecycle policy** to auto-delete old objects — n8n does not delete S3 objects itself.

**Note:** if you switch from S3 back to filesystem, n8n still reads S3 data as long as `s3` remains in `N8N_AVAILABLE_BINARY_DATA_MODES` and credentials remain valid.

**Upgrade note (v2.6.4+):** `N8N_EXTERNAL_STORAGE_S3_BUCKET_REGION` must contain only `[a-zA-Z0-9-]` — no underscores.

---

## Execution data pruning

Source: `hosting/scaling/execution-data.md`, `hosting/configuration/environment-variables/executions.md`

Pruning is enabled by default. n8n prunes executions when **either** condition is met:

- **Age:** finished more than `EXECUTIONS_DATA_MAX_AGE` hours ago (default: 336 h / 14 days).
- **Count:** total executions exceed `EXECUTIONS_DATA_PRUNE_MAX_COUNT` (default: 10,000) — deletes oldest first.

**Exceptions:** `new`, `running`, or `waiting` executions are never pruned. Annotated executions (tags, ratings) are never pruned.

```bash
# Production-safe pruning config
export EXECUTIONS_DATA_PRUNE=true
export EXECUTIONS_DATA_MAX_AGE=168           # 7 days
export EXECUTIONS_DATA_PRUNE_MAX_COUNT=50000

# Reduce saved data to control growth
export EXECUTIONS_DATA_SAVE_ON_SUCCESS=none   # don't save successful executions
export EXECUTIONS_DATA_SAVE_ON_ERROR=all      # keep error executions for debugging
export EXECUTIONS_DATA_SAVE_ON_PROGRESS=false
export EXECUTIONS_DATA_SAVE_MANUAL_EXECUTIONS=false
```

**SQLite note:** pruning marks data for deletion but does not reclaim disk space. Run `DB_SQLITE_VACUUM_ON_STARTUP=true` or execute `VACUUM` manually to reclaim space.

### Pruning timeline

1. **Soft-delete:** runs every `EXECUTIONS_DATA_PRUNE_SOFT_DELETE_INTERVAL` minutes (default: 60). Marks old executions.
2. **Hard-delete:** runs every `EXECUTIONS_DATA_PRUNE_HARD_DELETE_INTERVAL` minutes (default: 15). Permanently removes executions that have been soft-deleted for at least `EXECUTIONS_DATA_HARD_DELETE_BUFFER` hours (default: 1h).

---

## Graceful shutdown

```bash
export N8N_GRACEFUL_SHUTDOWN_TIMEOUT=30   # seconds
```

How long the n8n process waits for in-flight work to complete before forcefully exiting. Applies to both main and worker processes. Increase for workflows that are expected to run longer than 30 seconds when a shutdown is triggered.

---

## Workflow auto-deactivation on repeated crashes

```bash
export N8N_WORKFLOW_AUTODEACTIVATION_ENABLED=true
export N8N_WORKFLOW_AUTODEACTIVATION_MAX_LAST_EXECUTIONS=3
```

Automatically unpublishes (deactivates) a workflow after it crashes N consecutive times. Protects instance stability from runaway workflows.

---

## Scaling an AI system (vertical before horizontal)

> This is distinct from the infra queue-mode scaling above — it's about scaling the **AI quality envelope**, not just throughput.

**Perfect one domain end-to-end before adding users or new domains.** That means KB + pipeline + sub-workflows + agent + **evals + monitoring + guardrails** all solid in a single domain first. Horizontal expansion before that point multiplies every flaw:

- Hallucinations multiply proportionally across users.
- Retrieval quality degrades as the vector DB grows (more noise, lower precision).
- Latency rises; outputs get inconsistent across parallel agents.
- Debugging becomes nearly impossible when the failure surface spans multiple domains.

**Mitigations when you do scale out:**

| Problem | Mitigation |
|---|---|
| Retrieval degradation | Strict similarity-score thresholds — reject low-confidence matches, don't guess |
| Cross-domain noise | Segment data into namespaces or separate vector DBs per domain |
| Latency / throughput | Async processing + caching for repeated queries |
| Risky low-confidence answers | **Confidence-threshold gating**: if agent confidence < X, escalate to a human instead of answering |

**Sequence:** nail one domain → add evals + monitoring → confirm guardrails hold → then expand to more users or domains.

---

## Scaling checklist

- [ ] `EXECUTIONS_MODE=queue` set on main, workers, and webhook processors
- [ ] PostgreSQL 13+ as database (not SQLite)
- [ ] `N8N_ENCRYPTION_KEY` identical across all instances
- [ ] Redis authenticated (`QUEUE_BULL_REDIS_PASSWORD`) and TLS-enabled (`QUEUE_BULL_REDIS_TLS=true`)
- [ ] `QUEUE_HEALTH_CHECK_ACTIVE=true` on workers for load-balancer health checks
- [ ] Worker `--concurrency` ≥ 5 (avoid DB connection pool exhaustion)
- [ ] `N8N_CONCURRENCY_PRODUCTION_LIMIT` set in regular mode to prevent event-loop thrashing
- [ ] `EXECUTIONS_DATA_PRUNE=true` and sensible `EXECUTIONS_DATA_MAX_AGE` / `EXECUTIONS_DATA_PRUNE_MAX_COUNT`
- [ ] Binary data mode: `database` or `s3` (Enterprise) in queue mode — not `filesystem`
- [ ] S3 lifecycle policy configured to delete old binary data (if using S3 storage)
- [ ] `N8N_DISABLE_PRODUCTION_MAIN_PROCESS=true` when using dedicated webhook processors
- [ ] Load balancer routes `/webhook/*` and `/webhook-waiting/*` to webhook processor pool; all other paths to main
- [ ] `WEBHOOK_URL` set to the external-facing URL
- [ ] `CREDENTIALS_OVERWRITE_PERSISTENCE=true` in queue mode if using credential overwrites
- [ ] Multi-main: `N8N_MULTI_MAIN_SETUP_ENABLED=true` + sticky sessions on load balancer (Enterprise)
- [ ] `N8N_GRACEFUL_SHUTDOWN_TIMEOUT` tuned to max expected execution duration
- [ ] Per-process event log paths set (`N8N_EVENTBUS_LOGWRITER_LOGFULLPATH`) when workers share a filesystem
