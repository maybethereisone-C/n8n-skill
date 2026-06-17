# Logging & Observability (n8n v2.26.0)

> Exhaustive "every log surface" reference. Cite sources: `logs.md` = hosting/configuration/environment-variables/logs.md; `logging.md` = hosting/logging-monitoring/logging.md; `monitoring.md` = hosting/logging-monitoring/monitoring.md; `otel.md` = hosting/logging-monitoring/opentelemetry.md; `otel-env.md` = hosting/configuration/environment-variables/opentelemetry.md; `log-streaming.md` = log-streaming.md; `insights.md` = insights.md; `insights-env.md` = hosting/configuration/environment-variables/insights.md; `prometheus.md` = hosting/configuration/configuration-examples/prometheus.md; `custom-exec.md` = workflows/executions/custom-executions-data.md; `redaction.md` = workflows/executions/execution-data-redaction.md; `debug.md` = workflows/executions/debug.md

---

## 1. Application logs (N8N_LOG_*)

All variables from `logs.md`.

| Env var | Type | Default | Description |
|---|---|---|---|
| `N8N_LOG_LEVEL` | enum | `info` | `silent` \| `error` \| `warn` \| `info` \| `debug`. Use `info` in prod; `debug` only temporarily — very verbose, can leak data. |
| `N8N_LOG_OUTPUT` | enum | `console` | `console` \| `file` \| `console,file`. Ship to log aggregators requires `file`. |
| `N8N_LOG_FORMAT` | enum | `text` | `text` (human-readable) \| `json` (one JSON object per line: message, level, timestamp, metadata). Use `json` for ELK/Loki/Datadog. |
| `N8N_LOG_FILE_LOCATION` | string | `<n8n-dir>/logs/n8n.log` | Log file path. Requires `N8N_LOG_OUTPUT=file`. |
| `N8N_LOG_FILE_SIZE_MAX` | number | `16` | Max MB per log file before rotation. |
| `N8N_LOG_FILE_COUNT_MAX` | number | `100` | Max rotated log files to keep. |
| `N8N_LOG_CRON_ACTIVE_INTERVAL` | number | `0` | Minutes between logging currently active cron jobs. `0` = disabled. |
| `DB_LOGGING_ENABLED` | boolean | `false` | Enable database-level query logging (TypeORM). |
| `DB_LOGGING_OPTIONS` | enum | `error` | `query` \| `error` \| `schema` \| `warn` \| `info` \| `log` \| `all`. |
| `DB_LOGGING_MAX_EXECUTION_TIME` | number | `1000` | Log a warning for DB queries slower than this many ms. `0` = disabled. |
| `CODE_ENABLE_STDOUT` | boolean | `false` | Forward `console.log` / `print` from Code node to process stdout for **production** executions only. |
| `NO_COLOR` | any | — | Set to any value to strip ANSI color codes from console output. |

**Prod baseline:**
```bash
N8N_LOG_LEVEL=info
N8N_LOG_OUTPUT=console,file
N8N_LOG_FORMAT=json
N8N_LOG_FILE_LOCATION=/var/log/n8n/n8n.log
N8N_LOG_FILE_SIZE_MAX=16
N8N_LOG_FILE_COUNT_MAX=100
```

Source: `logs.md`, `logging.md`.

---

## 2. Log streaming (Enterprise — self-hosted)

Push structured events to external destinations in real time. Configured at **Settings › Log Streaming** or fully via env vars. Source: `log-streaming.md`.

### Enable env-var management (v2.19.0+)
```bash
N8N_LOG_STREAMING_MANAGED_BY_ENV=true
N8N_LOG_STREAMING_DESTINATIONS='[...]'   # JSON array; UI becomes read-only
```

### Event log file vars (for queue-mode multi-process safety)

| Env var | Default | Description |
|---|---|---|
| `N8N_EVENTBUS_LOGWRITER_LOGFULLPATH` | `''` | Absolute path (must end `.log`). Overrides basename + per-process suffix. **Required for queue-mode** — each process needs a unique path to prevent file corruption. |
| `N8N_EVENTBUS_LOGWRITER_LOGBASENAME` | `n8nEventLog` | Ignored when `LOGFULLPATH` is set. |
| `N8N_EVENTBUS_LOGWRITER_KEEPLOGCOUNT` | `3` | Number of event log files to keep. |
| `N8N_EVENTBUS_LOGWRITER_MAXFILESIZEINKB` | `10240` | Max KB per event log file. |
| `N8N_EVENTBUS_LOGWRITER_MAXTOTALMESSAGESPERFILE` | `500000` | Max lines parsed during recovery — prevents memory exhaustion from corrupted files. |
| `N8N_EVENTBUS_LOGWRITER_SYNCFILEACCESS` | `false` | Synchronous file access within thread. |
| `N8N_EVENTBUS_CHECKUNSENTINTERVAL` | `0` | ms interval to re-check unsent events. `0` = disabled. May send events twice. |

### Destination types

Three types: **webhook**, **syslog**, **sentry**. Common fields for all:

| Field | Description |
|---|---|
| `type` | `"webhook"` \| `"syslog"` \| `"sentry"` |
| `label` | Display name |
| `enabled` | boolean |
| `subscribedEvents` | string[] — event names or group prefixes (e.g. `"n8n.audit"`, `"n8n.workflow"`) |
| `anonymizeAuditMessages` | Strip sensitive payload from `n8n.audit.*` events |
| `circuitBreaker` | `{ maxFailures: int, failureWindow: ms }` — stops delivery after repeated failures |

**Webhook** adds: `url`, `method`, `sendQuery`, `sendHeaders`, `headerParameters`, `options` (timeout, proxy, redirect, socket pool).

**Syslog** adds: `host`, `port` (514), `protocol` (`udp`/`tcp`/`tls`), `tlsCa`, `facility`, `app_name`.

**Sentry** adds: `dsn` (Sentry DSN).

### Full event catalog

**Workflow:** Started, Success, Failed, Cancelled  
**Node executions:** Started, Finished  
**Audit** (50+ events including): User login success/failed, signup, updated, deleted, invited, MFA enabled/disabled, credentials CRUD, API key CRUD, workflow CRUD/archive/activate/deactivate, execution deleted/data revealed/reveal failed, package install/update/delete, variable CRUD, external secrets CRUD, token exchange events, role mapping events, personal publishing/sharing restriction changes, 2FA enforcement changes  
**Worker:** Started, Stopped  
**AI node logs:** Memory get/add, output parser, retriever, embeddings (doc/query), document processed, text splitter, tool called, vector store search/populate/update, LLM generated/error  
**Runner:** Task requested, Response received  
**Queue:** Job enqueued/dequeued/completed/failed/stalled

Source: `log-streaming.md`.

---

## 3. Execution data — persistence & pruning

Source: `logs.md` (env vars), general n8n knowledge [unverified for exact var source beyond existing skill].

| Env var | Type | Default | Prod recommendation |
|---|---|---|---|
| `EXECUTIONS_DATA_PRUNE` | bool | — | `true` — must enable or DB grows unbounded |
| `EXECUTIONS_DATA_MAX_AGE` | hours | — | `336` (14 days) |
| `EXECUTIONS_DATA_PRUNE_MAX_COUNT` | int | — | `50000` hard cap on stored executions |
| `EXECUTIONS_DATA_SAVE_ON_ERROR` | `all`\|`none` | — | `all` — failures are your debug trail |
| `EXECUTIONS_DATA_SAVE_ON_SUCCESS` | `all`\|`none` | — | `all`; or `none` at very high volume to save space |
| `EXECUTIONS_DATA_SAVE_ON_PROGRESS` | bool | `false` | `false` — saves after each node; high I/O cost |
| `EXECUTIONS_DATA_SAVE_MANUAL_EXECUTIONS` | bool | — | `true` — keep editor test runs |
| `EXECUTIONS_DATA_HARD_DELETE_BUFFER` | hours | — | `1` (grace before soft-deleted rows are purged) |
| `EXECUTIONS_DATA_PRUNE_HARD_DELETE_INTERVAL` | minutes | — | `15` |
| `EXECUTIONS_DATA_PRUNE_SOFT_DELETE_INTERVAL` | minutes | — | `60` |

**Rule:** `SAVE_ON_ERROR=all` always. Trade `SAVE_ON_SUCCESS=none` only when volume threatens the DB.

**Debug past executions:** In workflow editor › Executions tab — select a failed execution → **Debug in editor** (loads data + pins it at first node). For successful executions → **Copy to editor**. Source: `debug.md`.

---

## 4. Custom execution data (`$execution.customData`)

Attach searchable metadata to any execution. Filterable in the Executions list. Source: `custom-exec.md`.

```js
// Code node (JavaScript)
$execution.customData.set("order_id", "ORD-1234");  // single key
$execution.customData.setAll({"env": "prod", "batch": "42"});  // replace all

// Read back during same execution
const all = $execution.customData.getAll();
const val = $execution.customData.get("order_id");
```

Limits: strings only; key ≤ 50 chars; value ≤ 255 chars; max 10 items per execution.

Also settable via the **Execution Data node** (cannot read back via that node — use Code node to retrieve).

---

## 5. Execution data redaction (Enterprise, v2.16.0+)

Hide node input/output data in the execution viewer while keeping metadata (status, timing, node names) visible. Instance-level enforcement available from v2.26.0. Source: `redaction.md`.

**Per-workflow:** Workflow Settings → **Redact production execution data** / **Redact manual execution data**.

**Instance-wide enforcement:** Settings › Security › Data Redaction. Scopes:
- `Production executions` — recommended: protects live data, keeps manual runs visible for debugging
- `Manual and production executions` — when even test data is sensitive

**What gets redacted:** `item.json` replaced with `{}`, binary data removed, node-author-declared `sensitiveOutputFields` always redacted (cannot be revealed), error messages redacted (type + HTTP status code only).

**Reveal access:** Users with `execution:reveal` scope can temporarily reveal data for a single execution. Actions are logged to the audit trail via log streaming events:
- `n8n.audit.execution.data.revealed`
- `n8n.audit.execution.data.reveal_failure`
- `n8n.audit.redaction-enforcement.updated`

**Not covered by redaction:** Code node `console.log` output, data flowing between nodes, webhook response bodies, outbound auth headers, field-level redaction, database-level encryption.

---

## 6. Prometheus metrics (`/metrics`)

Source: `prometheus.md`, `monitoring.md`.

Disabled by default (not available on n8n Cloud). Enable:
```bash
N8N_METRICS=true
```

Endpoint: `GET <instance>/metrics` — uses [prom-client](https://www.npmjs.com/package/prom-client). Both `main` and `worker` instances can expose metrics.

**Queue metrics** (set `N8N_METRICS_INCLUDE_QUEUE_METRICS=true`, tune with `N8N_METRICS_QUEUE_METRICS_INTERVAL`):

| Metric | Type | Description |
|---|---|---|
| `n8n_scaling_mode_queue_jobs_active` | gauge | Jobs currently being processed across all workers |
| `n8n_scaling_mode_queue_jobs_completed` | counter | Total completed jobs since start |
| `n8n_scaling_mode_queue_jobs_failed` | counter | Total failed jobs since start |
| `n8n_scaling_mode_queue_jobs_waiting` | gauge | Enqueued jobs waiting for pickup |
| `instance_role_leader` | gauge | `1` for leader main, `0` otherwise (multi-main) |

Additional metrics controlled by `N8N_METRICS_INCLUDE_*` env vars (see `hosting/configuration/environment-variables/endpoints.md` for full list) [unverified — endpoints.md not read].

**Health endpoints** (always available on main; disabled by default on workers):
- `GET /healthz` — 200 = instance reachable (does NOT check DB)
- `GET /healthz/readiness` — 200 = DB connected + migrated, ready to accept traffic
- Workers: `QUEUE_HEALTH_CHECK_ACTIVE=true` to enable `/healthz` on worker processes
- Customize path: `N8N_ENDPOINT_HEALTH` env var

---

## 7. OpenTelemetry tracing (self-hosted only, v2.19.0+)

Source: `otel.md`, `otel-env.md`. Note: OTel metrics format is still under development per docs.

### Full env var table

| Env var | Default | Description |
|---|---|---|
| `N8N_OTEL_ENABLED` | `false` | Enable OTel SDK. Must be `true` on every process (main, worker, webhook processor). |
| `N8N_OTEL_EXPORTER_OTLP_ENDPOINT` | `http://localhost:4318` | Base URL of OTLP HTTP collector. n8n appends the traces path automatically. |
| `N8N_OTEL_EXPORTER_OTLP_TRACING_PATH` | `/v1/traces` | Path appended to endpoint. |
| `N8N_OTEL_EXPORTER_OTLP_HEADERS` | — | Comma-separated `key=value` pairs for OTLP requests (auth tokens, tenant headers). Use `_FILE` postfix for secrets. |
| `N8N_OTEL_EXPORTER_SERVICE_NAME` | `n8n` | `service.name` resource attribute on spans. |
| `N8N_OTEL_TRACES_SAMPLE_RATE` | `1.0` | Fraction 0–1 of traces to export. Trace ID ratio sampler — whole trace sampled or dropped. |
| `N8N_OTEL_TRACES_INCLUDE_NODE_SPANS` | `true` | Emit `node.execute` span per node. Set `false` for workflow-level spans only. |
| `N8N_OTEL_TRACES_PRODUCTION_ONLY` | `true` | Export only production execution traces. Set `false` for all. (v2.25.2+) |
| `N8N_OTEL_TRACES_INJECT_OUTBOUND` | `true` | Inject W3C `traceparent`/`tracestate` into outbound HTTP requests. |
| `N8N_OTEL_STARTUP_CONNECTIVITY_TIMEOUT_MS` | `2000` | ms to wait for OTLP endpoint at startup before logging a warning. |

### Span types and attributes

**`workflow.execute` span:**

| Attribute | Description |
|---|---|
| `n8n.workflow.id` | Workflow ID |
| `n8n.workflow.name` | Workflow name |
| `n8n.workflow.version_id` | Version ID |
| `n8n.workflow.node_count` | Node count |
| `n8n.project.id` | Project ID (v2.23.0+) |
| `n8n.execution.id` | Execution ID |
| `n8n.execution.mode` | `manual` \| `webhook` \| `trigger` \| `retry` |
| `n8n.execution.status` | Final status |
| `n8n.execution.is_retry` | `true` if retry |
| `n8n.execution.retry_of` | Original execution ID on retry |
| `n8n.execution.error_type` | Error class name on failure |
| `n8n.continuation.reason` | Span link attribute when workflow resumes after wait |
| `n8n.project.custom.<key>` | Custom project-level attributes (Enterprise, v2.24.0+) |
| `n8n.workflow.custom.<key>` | Custom workflow-level attributes (Enterprise, v2.24.0+) |

**`node.execute` span:**

| Attribute | Description |
|---|---|
| `n8n.node.id` | Node ID |
| `n8n.node.name` | Node name |
| `n8n.node.type` | Node type (e.g. `n8n-nodes-base.httpRequest`) |
| `n8n.node.type_version` | Type version |
| `n8n.node.items.input` | Input item count |
| `n8n.node.items.output` | Output item count |
| `n8n.node.termination_reason` | Why span ended without normal completion |
| `n8n.node.custom.<key>` | Custom node-level attributes (Enterprise, v2.22.0+) |

On node failure: `exception` event with `exception.type`, `exception.message`, `exception.stacktrace`.

**Resource attributes** on all spans: `service.name`, `service.version`, `n8n.instance.id`, `n8n.instance.role`.

**Trace context propagation:**
- Inbound: W3C `traceparent` on webhook triggers → used as parent span
- Outbound: injected into HTTP Request node outbound calls (disable with `N8N_OTEL_TRACES_INJECT_OUTBOUND=false`)
- Sub-workflows: child span links to parent workflow span
- Resumed workflows (after wait): new span links back via span link

### Custom span attributes (Enterprise)

| Level | Where to configure | Span affected | Prefix |
|---|---|---|---|
| Project | Project Settings › Custom Span Attributes | `workflow.execute` | `n8n.project.custom.<key>` |
| Workflow | Workflow Settings › Custom Span Attributes | `workflow.execute` | `n8n.workflow.custom.<key>` |
| Node | Node Settings tab › Custom Span Attributes | `node.execute` | `n8n.node.custom.<key>` |

Programmatic (custom node code only, not Code node):
```typescript
this.setMetadata({ tracing: { 'llm.model': 'gpt-4o', 'llm.token.input': 1500 } });
// → n8n.node.custom.llm.model, n8n.node.custom.llm.token.input on the span
```

---

## 8. Insights (built-in analytics)

Source: `insights.md`, `insights-env.md`.

Available from v1.89.0. Summary banner = all plans (7-day rolling). Dashboard = Pro/Business/Enterprise. Counts **production executions only** (excludes manual, sub-workflow, error workflow executions).

**Metrics collected:** total production executions, failed executions, failure rate, time saved, run time average (including wait node time).

**Time saved configuration (per workflow):**
- **Fixed:** Set minutes per execution in Workflow Settings › Estimated time saved › Fixed
- **Dynamic:** Add **Time Saved** nodes at savings points in the workflow; configure minutes + calculation mode (once per execution or per-item multiplied by item count)

**Data retention tiers:** raw → 1-hour buckets → daily (after `N8N_INSIGHTS_COMPACTION_HOURLY_TO_DAILY_THRESHOLD_DAYS`) → weekly (after `N8N_INSIGHTS_COMPACTION_DAILY_TO_WEEKLY_THRESHOLD_DAYS`)

### Full env var table

| Env var | Default | Description |
|---|---|---|
| `N8N_DISABLED_MODULES` | — | Set to `insights` to disable the feature entirely |
| `N8N_INSIGHTS_MAX_AGE_DAYS` | `365` | Days to keep compacted insights. Max 730 (2 years). |
| `N8N_INSIGHTS_PRUNE_CHECK_INTERVAL_HOURS` | `24` | How often to check and prune old insights data |
| `N8N_INSIGHTS_FLUSH_BATCH_SIZE` | `1000` | Max insights events buffered before flushing to DB |
| `N8N_INSIGHTS_FLUSH_INTERVAL_SECONDS` | `30` | Flush interval in seconds |
| `N8N_INSIGHTS_COMPACTION_INTERVAL_MINUTES` | `60` | How often compaction runs |
| `N8N_INSIGHTS_COMPACTION_BATCH_SIZE` | `500` | Rows compacted per batch |
| `N8N_INSIGHTS_COMPACTION_BATCH_DELAY_MILLISECONDS` | `100` | ms delay between batches (increase to reduce DB load) |
| `N8N_INSIGHTS_COMPACTION_MAX_BATCHES_PER_RUN` | `1000` | Max batches per compaction run (`0` = unlimited) |
| `N8N_INSIGHTS_COMPACTION_MAX_RUNTIME_SECONDS` | `300` | Max seconds per compaction run (`0` = unlimited) |
| `N8N_INSIGHTS_COMPACTION_HOURLY_TO_DAILY_THRESHOLD_DAYS` | `90` | Age in days before hourly rows compact to daily |
| `N8N_INSIGHTS_COMPACTION_DAILY_TO_WEEKLY_THRESHOLD_DAYS` | `180` | Age in days before daily rows compact to weekly |

**DB load tuning:** decrease `INTERVAL_MINUTES` + increase `BATCH_DELAY_MILLISECONDS` + decrease `MAX_BATCHES_PER_RUN` / `MAX_RUNTIME_SECONDS`.

---

## 9. In-workflow logging

### console.log in Code node

```js
// JavaScript Code node
console.log("Processing item", $json.id);  // manual executions: shown in editor Logs panel
// Production executions: goes to stdout ONLY if CODE_ENABLE_STDOUT=true (logs.md)
```

**Warning:** `console.log` output is NOT redacted even when execution data redaction is enabled. Source: `redaction.md`.

### Structured run-log row pattern

Append a structured row at workflow end so you can query/chart/alert on business metrics independently of the n8n DB.

```json
{
  "parameters": {
    "operation": "append",
    "columns": {
      "value": {
        "run_id":          "={{ $execution.id }}",
        "workflow":        "={{ $workflow.name }}",
        "status":          "success",
        "timestamp":       "={{ $now.toISO() }}",
        "items_processed": "={{ $items().length }}",
        "errors":          0
      }
    }
  },
  "type": "n8n-nodes-base.googleSheets",
  "typeVersion": 4.5,
  "name": "Run Log (success)",
  "onError": "continueRegularOutput"
}
```

Mirror from error workflow for failures. Set `onError: continueRegularOutput` so a logging failure never kills the real work.

Standard log fields: `run_id` (`$execution.id`), `workflow` (`$workflow.name`), `status`, `timestamp` (`$now.toISO()`), `items_processed`, `errors`.

### Error workflow alerting

Set **Error Workflow** in Workflow Settings. The error workflow receives `$input.first().json` with execution context (workflow ID, name, execution ID, error message). Route to Slack/email/PagerDuty. Every failed production execution triggers it.

---

## 10. Monitoring & alerting summary

| Concern | How |
|---|---|
| Process alive | `GET /healthz` → HTTP 200 |
| DB connected + ready | `GET /healthz/readiness` → HTTP 200 |
| Worker health | `QUEUE_HEALTH_CHECK_ACTIVE=true` + probe `GET <worker>/healthz` |
| Execution metrics | `N8N_METRICS=true` → `GET /metrics` (Prometheus scrape) |
| Queue depth | `N8N_METRICS_INCLUDE_QUEUE_METRICS=true` → `n8n_scaling_mode_queue_jobs_waiting` |
| Execution visibility | n8n UI › Executions list; filter by status/workflow |
| Failure alerting (push) | Error Workflow → Slack/PagerDuty/email |
| Business metrics (pull) | Run-log table/sheet → dashboard |
| Log aggregation | `N8N_LOG_FORMAT=json` + `N8N_LOG_OUTPUT=file` → ship to Loki/ELK/Datadog |
| Event streaming | Log streaming destinations (webhook/syslog/Sentry) — Enterprise |
| Distributed tracing | OTel → Jaeger/Tempo/Honeycomb — self-hosted only |
| Historical analytics | Insights dashboard — Pro/Business/Enterprise |
| Audit trail | Log streaming `n8n.audit.*` events |

---

## 11. Symptom → log surface table

| Symptom | Where to look |
|---|---|
| Workflow silently fails | n8n UI Executions list (filter status=error); error workflow Slack alert |
| Can't see why a node failed | Executions list → open execution → node output panel; or OTel `node.execute` span exception event |
| Need to replay a failed execution | Editor › Executions tab → **Debug in editor** (pins data, loads into workflow) |
| Missing execution history | Check `EXECUTIONS_DATA_SAVE_ON_ERROR` / `SAVE_ON_SUCCESS`; check `EXECUTIONS_DATA_MAX_AGE` |
| DB growing uncontrollably | Enable `EXECUTIONS_DATA_PRUNE=true`; set `PRUNE_MAX_COUNT`; check `SAVE_ON_SUCCESS=none` |
| Worker jobs stuck / queue backed up | `/metrics` → `n8n_scaling_mode_queue_jobs_waiting`; log streaming Queue events |
| High execution latency | OTel `workflow.execute` / `node.execute` span durations; Insights run time average |
| n8n process not responding | `GET /healthz` (liveness); `GET /healthz/readiness` (DB check) |
| Need audit trail of who changed what | Log streaming `n8n.audit.*` events to syslog/webhook |
| Code node output missing in logs | Set `CODE_ENABLE_STDOUT=true`; note: only production executions, not redacted |
| Execution data leaking sensitive info | Enable execution data redaction per-workflow or instance-wide (Enterprise, v2.26.0+) |
| Redacted data needed for debugging | User with `execution:reveal` scope → Reveal data button; emits audit event |
| AI node chain not observable | Log streaming **AI node logs** event group → LLM generated/error, tool called, vector store events |
| No OTel traces appearing | Check `N8N_OTEL_ENABLED=true` on ALL processes; verify endpoint URL (base, not `/v1/traces`); check `N8N_LOG_LEVEL=debug` for OTel diagnostics |
| Worker spans missing parent context | Set OTel env vars on workers too — workers read parent context from DB |
| Insights not showing data | Verify plan tier; check `N8N_DISABLED_MODULES` not set to `insights`; data only from v1.89.0+ |
| Custom span attributes missing | Requires Enterprise license + `N8N_OTEL_ENABLED=true`; node attrs also need `N8N_OTEL_TRACES_INCLUDE_NODE_SPANS=true` |
| Log shipper not receiving | Confirm `N8N_LOG_FORMAT=json` + `N8N_LOG_OUTPUT=file`; check log file path; verify log streaming destination enabled + circuit breaker not open |
