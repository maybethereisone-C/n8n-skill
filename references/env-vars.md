# n8n Environment Variables Reference (v2.26.0)

> The ops grep-first reference. Grouped by doc category. For each variable: name | what it does | default | when to set.
>
> Sources: `hosting/configuration/environment-variables/` directory (one file per category).
> Variables marked `/`_FILE` accept a `_FILE` suffix to read the value from a file path (Docker secrets pattern). Task runner image does NOT support `_FILE` suffix.

---

## Deployment

Source: `hosting/configuration/environment-variables/deployment.md`

| Variable | Does | Default | When to set |
|---|---|---|---|
| `N8N_HOST` | Hostname n8n runs on | `localhost` | Always in production — set to actual FQDN |
| `N8N_PORT` | HTTP port n8n listens on | `5678` | When running behind a reverse proxy on a non-standard port |
| `N8N_LISTEN_ADDRESS` | IP address to bind | `::` | Set to `127.0.0.1` when reverse proxy is on same host |
| `N8N_PROTOCOL` | `http` or `https` | `http` | Set `https` when terminating TLS at n8n (not reverse proxy) |
| `N8N_SSL_KEY` | Path to SSL private key | — | When `N8N_PROTOCOL=https` |
| `N8N_SSL_CERT` | Path to SSL certificate | — | When `N8N_PROTOCOL=https` |
| `N8N_EDITOR_BASE_URL` | Public URL for editor, emails, and SAML redirect | — | Always set in production; required for SAML SSO |
| `N8N_PATH` | URL path n8n deploys to | `/` | When running at a subpath (prefer subdomain instead) |
| `N8N_ENCRYPTION_KEY` | Master key encrypting credentials in DB | Random (first launch) | **Always** — set explicitly and identically on all instances |
| `N8N_ENV_FEAT_ENCRYPTION_KEY_ROTATION` | Enable two-layer encryption key rotation | `false` | After full DB backup; one-way change — set on ALL instances |
| `N8N_ENV_FEAT_OAUTH2_JWE` | Enable JWE-encrypted OAuth 2.0 token decryption | `false` | When IdP supports JWE; set on ALL instances (preview feature) |
| `N8N_ENV_FEAT_TOKEN_EXCHANGE` | Enable token exchange for embedding partners | `false` | OEM/embedding deployments only (preview feature) |
| `N8N_OAUTH_JWE_JWKS_PER_MINUTE` | Per-IP rate limit on JWKS endpoint | `60` | Increase if IdP exceeds limit |
| `N8N_USER_FOLDER` | Path where `.n8n` data directory is created | `user-folder` | When mounting persistent storage at a custom path |
| `N8N_DISABLE_UI` | Disable the web editor UI | `false` | Worker-only nodes where no UI is needed |
| `N8N_PREVIEW_MODE` | Run in preview mode | `false` | Internal n8n use |
| `N8N_GRACEFUL_SHUTDOWN_TIMEOUT` | Seconds to wait for in-flight work on shutdown | `30` | Increase for long-running workflow instances |
| `N8N_PROXY_HOPS` | Number of reverse proxies in front of n8n | `0` | Set to match actual proxy count for correct IP forwarding |
| `N8N_PUSH_BACKEND` | UI push channel: `sse` or `websocket` | `websocket` | Use `sse` if WebSocket is blocked by a proxy |
| `N8N_PUBLIC_API_DISABLED` | Disable the REST public API | `false` | Set `true` on instances that don't need external API access |
| `N8N_PUBLIC_API_SWAGGERUI_DISABLED` | Disable the Swagger UI playground | `false` | Set `true` in production to reduce attack surface |
| `N8N_PUBLIC_API_ENDPOINT` | Path prefix for public API | `api` | Rarely changed |
| `N8N_TEMPLATES_ENABLED` | Enable workflow templates | `true` | Set `false` in air-gapped / isolated deployments |
| `N8N_TEMPLATES_HOST` | URL of templates library API | `https://api.n8n.io` | When self-hosting a custom templates library |
| `N8N_DIAGNOSTICS_ENABLED` | Send anonymous telemetry to n8n | `true` | Set `false` for privacy / air-gapped deployments (also disables Ask AI in Code node) |
| `N8N_DIAGNOSTICS_CONFIG_FRONTEND` | Telemetry endpoint config (frontend) | n8n default | Unset when disabling diagnostics |
| `N8N_DIAGNOSTICS_CONFIG_BACKEND` | Telemetry endpoint config (backend) | n8n default | Unset when disabling diagnostics |
| `N8N_VERSION_NOTIFICATIONS_ENABLED` | Notify about new versions / security updates | `true` | Set `false` in air-gapped deployments |
| `N8N_PERSONALIZATION_ENABLED` | Ask personalisation questions on first run | `true` | Set `false` for automated / pre-configured deployments |
| `N8N_REINSTALL_MISSING_PACKAGES` | Auto-reinstall missing npm packages | `false` | Set `true` if community nodes are pre-installed via volume |
| `N8N_TUNNEL_SUBDOMAIN` | Subdomain for n8n tunnel | Random | Dev only; do not use in production |
| `HTTP_PROXY` | Proxy for outbound unencrypted HTTP | — | When n8n is behind a corporate proxy |
| `HTTPS_PROXY` | Proxy for outbound TLS HTTP | — | When n8n is behind a corporate proxy |
| `ALL_PROXY` | Proxy for all outbound HTTP | — | Fallback when specific proxy vars are unset |
| `NO_PROXY` | Comma-separated hosts that bypass proxy | — | When some hosts should not go through proxy |
| `N8N_ENFORCE_GLOBAL_USER_AGENT` | Send RFC-compliant User-Agent on all outbound requests | `false` | Set `true` if upstream WAFs block n8n requests |
| `N8N_GLOBAL_USER_AGENT_VALUE` | Custom User-Agent string | — | Override to hide n8n version from upstream servers |
| `VUE_APP_URL_BASE_API` | Backend API URL for manually built editor-ui | `http://localhost:5678/` | Only when building `n8n-editor-ui` package manually |
| `N8N_DEV_RELOAD` | Auto-reload on source changes | `false` | Development only |
| `N8N_HIRING_BANNER_ENABLED` | Show n8n hiring banner in console | `true` | Set `false` in production to clean up logs |

---

## Database

Source: `hosting/configuration/environment-variables/database.md`

| Variable | Does | Default | When to set |
|---|---|---|---|
| `DB_TYPE` / `_FILE` | Database engine: `sqlite` or `postgresdb` | `sqlite` | Set `postgresdb` for all production and queue-mode deployments |
| `DB_TABLE_PREFIX` | Prefix for all table names | — | When sharing a DB schema with other apps |
| `DB_PING_INTERVAL_SECONDS` | Interval between DB connection health pings (s) | `2` | Rarely changed |
| **PostgreSQL** | | | |
| `DB_POSTGRESDB_DATABASE` / `_FILE` | PostgreSQL database name | `n8n` | Always when using Postgres |
| `DB_POSTGRESDB_HOST` / `_FILE` | PostgreSQL host | `localhost` | Always when using Postgres |
| `DB_POSTGRESDB_PORT` / `_FILE` | PostgreSQL port | `5432` | When Postgres runs on a non-default port |
| `DB_POSTGRESDB_USER` / `_FILE` | PostgreSQL username | `postgres` | Always when using Postgres |
| `DB_POSTGRESDB_PASSWORD` / `_FILE` | PostgreSQL password | — | Always when using Postgres |
| `DB_POSTGRESDB_SCHEMA` / `_FILE` | PostgreSQL schema | `public` | When using a non-default schema |
| `DB_POSTGRESDB_POOL_SIZE` / `_FILE` | Max parallel Postgres connections | `2` | Increase for high-load multi-worker setups; watch DB connection limits |
| `DB_POSTGRESDB_CONNECTION_TIMEOUT` / `_FILE` | Connection timeout (ms) | `20000` | Increase for slow/remote DB hosts |
| `DB_POSTGRESDB_IDLE_CONNECTION_TIMEOUT` / `_FILE` | Idle connection eviction time (ms) | `30000` | Tune for connection pool efficiency |
| `DB_POSTGRESDB_SSL_ENABLED` / `_FILE` | Enable SSL for Postgres connection | `false` (auto-enabled if cert vars set) | Always `true` in production |
| `DB_POSTGRESDB_SSL_CA` / `_FILE` | Path to SSL certificate authority | — | Custom CA for self-signed DB certs |
| `DB_POSTGRESDB_SSL_CERT` / `_FILE` | Path to SSL client certificate | — | mTLS with Postgres |
| `DB_POSTGRESDB_SSL_KEY` / `_FILE` | Path to SSL client private key | — | mTLS with Postgres |
| `DB_POSTGRESDB_SSL_REJECT_UNAUTHORIZED` / `_FILE` | Reject unauthorized SSL connections | `true` | Keep `true`; only disable for testing self-signed certs |
| **SQLite** | | | |
| `DB_SQLITE_POOL_SIZE` | SQLite read pool size; `0` = rollback journal, `>0` = WAL mode | `0` | Set to `>0` (e.g. `4`) for WAL mode on low-traffic single instances |
| `DB_SQLITE_VACUUM_ON_STARTUP` | Run VACUUM on startup to reclaim space | `false` | Set `true` periodically after heavy pruning (blocks startup) |
| **Logging** | | | |
| `DB_LOGGING_ENABLED` | Enable TypeORM DB query logging | `false` | Enable for debugging slow queries |
| `DB_LOGGING_OPTIONS` | Log types: `query`, `error`, `schema`, `warn`, `info`, `log`, `all` | `error` | Set `error` in production; `all` only in dev |
| `DB_LOGGING_MAX_EXECUTION_TIME` | Warn on queries slower than this (ms); `0` = disable | `1000` | Tune for your DB performance baseline |

---

## Executions

Source: `hosting/configuration/environment-variables/executions.md`

| Variable | Does | Default | When to set |
|---|---|---|---|
| `EXECUTIONS_MODE` | Execution mode: `regular` or `queue` | `regular` | Set `queue` for multi-worker scaling |
| `EXECUTIONS_TIMEOUT` | Default workflow timeout (s); `-1` = off | `-1` | Set a sensible ceiling (e.g. `3600`) to prevent runaway executions |
| `EXECUTIONS_TIMEOUT_MAX` | Max timeout users can set per workflow (s) | `3600` | Raise only if workflows legitimately need longer |
| `N8N_AI_TIMEOUT_MAX` | HTTP timeout for AI/LLM nodes (ms) | `3600000` | Increase for slow local AI models |
| `EXECUTIONS_DATA_SAVE_ON_ERROR` | Save data on error: `all` or `none` | `all` | Keep `all` in production for debugging |
| `EXECUTIONS_DATA_SAVE_ON_SUCCESS` | Save data on success: `all` or `none` | `all` | Set `none` on high-volume, low-debug workflows to reduce DB size |
| `EXECUTIONS_DATA_SAVE_ON_PROGRESS` | Save node-level progress data | `false` | Enable only when debugging mid-workflow failures |
| `EXECUTIONS_DATA_SAVE_MANUAL_EXECUTIONS` | Save data for manual test runs | `true` | Set `false` in production if test-run data is not needed |
| `EXECUTIONS_DATA_PRUNE` | Enable rolling deletion of old execution data | `true` | Keep `true`; disabling causes unbounded DB growth |
| `EXECUTIONS_DATA_MAX_AGE` | Age (hours) before execution is eligible for pruning | `336` (14 days) | Tune based on retention requirements |
| `EXECUTIONS_DATA_PRUNE_MAX_COUNT` | Max executions to retain in DB; `0` = unlimited | `10000` | Set to limit based on DB capacity |
| `EXECUTIONS_DATA_HARD_DELETE_BUFFER` | Buffer (hours) before recent data is hard-deleted | `1` | Rarely changed |
| `EXECUTIONS_DATA_PRUNE_HARD_DELETE_INTERVAL` | How often (min) hard deletion runs | `15` | Rarely changed |
| `EXECUTIONS_DATA_PRUNE_SOFT_DELETE_INTERVAL` | How often (min) soft deletion runs | `60` | Rarely changed |
| `N8N_CONCURRENCY_PRODUCTION_LIMIT` | Max concurrent production executions; `-1` = unlimited | `-1` | Set (e.g. `20`) to prevent event-loop thrashing in regular mode |
| `N8N_CONCURRENCY_EVALUATION_LIMIT` | Max parallel test cases in an evaluation run | License tier | Override tier default if needed |
| `N8N_WORKFLOW_AUTODEACTIVATION_ENABLED` | Auto-unpublish workflows after repeated crashes | `false` | Set `true` to protect instance stability |
| `N8N_WORKFLOW_AUTODEACTIVATION_MAX_LAST_EXECUTIONS` | Crash count before auto-unpublish | `3` | Tune based on acceptable crash tolerance |

---

## Queue Mode (Redis / Bull)

Source: `hosting/configuration/environment-variables/queue-mode.md`

| Variable | Does | Default | When to set |
|---|---|---|---|
| `EXECUTIONS_MODE` | Must be `queue` for queue mode | `regular` | Set on main, workers, and webhook processors |
| `OFFLOAD_MANUAL_EXECUTIONS_TO_WORKERS` | Run manual executions on workers instead of main | `false` | Set `true` to offload test-run load from main process |
| `QUEUE_BULL_PREFIX` | Key prefix for all Bull queue keys in Redis | — | When sharing Redis with other apps |
| `QUEUE_BULL_REDIS_HOST` | Redis hostname | `localhost` | Always when using queue mode |
| `QUEUE_BULL_REDIS_PORT` | Redis port | `6379` | When Redis is on a non-default port |
| `QUEUE_BULL_REDIS_DB` | Redis database number | `0` | When sharing Redis with other apps |
| `QUEUE_BULL_REDIS_USERNAME` | Redis username (Redis 6+) | — | When Redis ACLs are enabled |
| `QUEUE_BULL_REDIS_PASSWORD` | Redis password | — | Always — never run Redis without auth in production |
| `QUEUE_BULL_REDIS_TLS` | Enable TLS for Redis connections | `false` | Set `true` in production |
| `QUEUE_BULL_REDIS_DUALSTACK` | Enable IPv4+IPv6 dual-stack on Redis connections | `false` | Dual-stack network environments |
| `QUEUE_BULL_REDIS_CLUSTER_NODES` | Comma-separated `host:port` list for Redis Cluster | — | When using Redis Cluster; overrides HOST/PORT |
| `QUEUE_BULL_REDIS_TIMEOUT_THRESHOLD` | Redis timeout before n8n exits (ms) | `10000` | Increase for slow/remote Redis |
| `QUEUE_HEALTH_CHECK_ACTIVE` | Enable `/healthz` and `/healthz/readiness` on workers | `false` | Set `true` in production for load-balancer health checks |
| `QUEUE_HEALTH_CHECK_PORT` | Port for worker health check server | `5678` | Change if port conflicts with other services |
| `QUEUE_WORKER_LOCK_DURATION` | Lease duration for a worker processing a message (ms) | `60000` | Increase for long-running workflows |
| `QUEUE_WORKER_LOCK_RENEW_TIME` | How often worker renews lease (ms) | `10000` | Must be < `QUEUE_WORKER_LOCK_DURATION` |
| `QUEUE_WORKER_STALLED_INTERVAL` | How often to check for stalled jobs (ms); `0` = never | `30000` | Rarely changed |
| `QUEUE_WORKER_MAX_STALLED_COUNT` | Max re-processing attempts for a stalled job | `1` | Set `0` to disable re-processing of stalled jobs |
| `N8N_GRACEFUL_SHUTDOWN_TIMEOUT` | Seconds workers wait for in-flight jobs before exit | `30` | Increase for long-running workflows |
| **Multi-main (Enterprise)** | | | |
| `N8N_MULTI_MAIN_SETUP_ENABLED` | Enable multi-main HA setup | `false` | Enterprise only; enable on all main instances |
| `N8N_MULTI_MAIN_SETUP_KEY_TTL` | TTL (s) for leader key in Redis | `10` | Rarely changed |
| `N8N_MULTI_MAIN_SETUP_CHECK_INTERVAL` | Leader election check interval (s) | `3` | Rarely changed |

---

## Security

Source: `hosting/configuration/environment-variables/security.md`

| Variable | Does | Default | When to set |
|---|---|---|---|
| `N8N_BLOCK_ENV_ACCESS_IN_NODE` | Block access to env vars in expressions and Code node | `false` | Set `true` in production — prevents secret leakage |
| `N8N_BLOCK_FILE_ACCESS_TO_N8N_FILES` | Block access to `.n8n` directory and config files | `true` | Keep `true`; only override with explicit allowed list |
| `N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS` | Force 0600 permissions on settings file | `false` | Set `true` for stricter file security |
| `N8N_RESTRICT_FILE_ACCESS_TO` | Semicolon-separated allowed directories for file access | — | Set to restrict Code/file nodes to specific paths |
| `N8N_SECURITY_AUDIT_DAYS_ABANDONED_WORKFLOW` | Days before a workflow is flagged as abandoned | `90` | Lower to tighten audit sensitivity |
| `N8N_CONTENT_SECURITY_POLICY` | helmet.js CSP directives object (JSON string) | `{}` | Set `frame-ancestors` when embedding n8n in another app |
| `N8N_SECURE_COOKIE` | HTTPS-only cookies | `true` | Keep `true`; only `false` in HTTP-only dev environments |
| `N8N_SAMESITE_COOKIE` | Cookie SameSite policy: `strict`, `lax`, `none` | `lax` | Set `strict` for maximum protection; `none` requires HTTPS |
| `N8N_GIT_NODE_DISABLE_BARE_REPOS` | Prevent Git node from working with bare repositories | `false` | Set `true` for security when users are untrusted |
| `N8N_GIT_NODE_ENABLE_HOOKS` | Allow Git node to execute Git hooks | `false` | Leave `false` unless explicitly required |
| `N8N_SECURITY_POLICY_MANAGED_BY_ENV` | Manage security policy from env vars | — | Set `true` to enable env-based policy management |

---

## Endpoints

Source: `hosting/configuration/environment-variables/endpoints.md`

| Variable | Does | Default | When to set |
|---|---|---|---|
| `N8N_PAYLOAD_SIZE_MAX` | Max request payload size (MiB) | `16` | Increase for workflows processing large files; ensure infra has headroom |
| `N8N_FORMDATA_FILE_SIZE_MAX` | Max file size in form-data webhook payloads (MiB) | `200` | Tune for large file upload use cases |
| `N8N_METRICS` | Enable `/metrics` Prometheus endpoint | `false` | Set `true` when integrating with Prometheus/Grafana |
| `N8N_METRICS_PREFIX` | Prefix for n8n metric names | `n8n_` | Change to avoid collision with other app metrics |
| `N8N_METRICS_INCLUDE_DEFAULT_METRICS` | Include Node.js/system default metrics | `true` | Disable to reduce metric cardinality |
| `N8N_METRICS_INCLUDE_CACHE_METRICS` | Include cache hit/miss metrics | `false` | Enable for cache performance monitoring |
| `N8N_METRICS_INCLUDE_MESSAGE_EVENT_BUS_METRICS` | Include event bus metrics | `false` | Enable for log-streaming monitoring |
| `N8N_METRICS_INCLUDE_WORKFLOW_ID_LABEL` | Label metrics with workflow ID | `false` | Enable for per-workflow dashboards (increases cardinality) |
| `N8N_METRICS_INCLUDE_NODE_TYPE_LABEL` | Label metrics with node type | `false` | Enable for per-node-type dashboards |
| `N8N_METRICS_INCLUDE_CREDENTIAL_TYPE_LABEL` | Label metrics with credential type | `false` | Enable for credential usage monitoring |
| `N8N_METRICS_INCLUDE_API_ENDPOINTS` | Expose API endpoint metrics | `false` | Enable for API usage analytics |
| `N8N_METRICS_INCLUDE_API_PATH_LABEL` | Label API metrics with path | `false` | Enable for per-path breakdown |
| `N8N_METRICS_INCLUDE_API_METHOD_LABEL` | Label API metrics with HTTP method | `false` | Enable for method-level breakdown |
| `N8N_METRICS_INCLUDE_API_STATUS_CODE_LABEL` | Label API metrics with HTTP status code | `false` | Enable for error rate tracking |
| `N8N_METRICS_INCLUDE_QUEUE_METRICS` | Include queue-mode job metrics | `false` | Set `true` in queue-mode deployments |
| `N8N_METRICS_QUEUE_METRICS_INTERVAL` | How often queue metrics update (s) | `20` | Reduce for more granular queue monitoring |
| `N8N_ENDPOINT_REST` | Path prefix for REST API | `rest` | Rarely changed |
| `N8N_ENDPOINT_WEBHOOK` | Path for production webhooks | `webhook` | Rarely changed |
| `N8N_ENDPOINT_WEBHOOK_TEST` | Path for test webhooks | `webhook-test` | Rarely changed |
| `N8N_ENDPOINT_WEBHOOK_WAIT` | Path for waiting webhooks | `webhook-waiting` | Rarely changed |
| `N8N_ENDPOINT_HEALTH` | Path for health check | `healthz` | Change if path conflicts with existing infra |
| `WEBHOOK_URL` | Override webhook URL shown to external callers | — | Always set when n8n is behind a reverse proxy |
| `N8N_DISABLE_PRODUCTION_MAIN_PROCESS` | Stop main from handling production webhooks | `false` | Set `true` when using dedicated webhook processor nodes |

---

## Nodes

Source: `hosting/configuration/environment-variables/nodes.md`

| Variable | Does | Default | When to set |
|---|---|---|---|
| `NODES_EXCLUDE` | JSON array of node types to block from loading | `["n8n-nodes-base.executeCommand","n8n-nodes-base.localFileTrigger"]` | Add `readWriteFile` and other risky nodes for untrusted users |
| `NODES_INCLUDE` | JSON array of node types to load (allowlist) | — | For strict allowlist of permitted nodes |
| `NODES_ERROR_TRIGGER_TYPE` | Node type to use as Error Trigger | `n8n-nodes-base.errorTrigger` | Override when using a custom error trigger node |
| `N8N_COMMUNITY_PACKAGES_ENABLED` | Enable installation of community nodes | `true` | Set `false` if community nodes are not permitted |
| `N8N_COMMUNITY_PACKAGES_PREVENT_LOADING` | Prevent loading installed community nodes at startup | `false` | Set `true` if a faulty node prevents instance from starting |
| `N8N_UNVERIFIED_PACKAGES_ENABLED` | Allow unverified (non-curated) community nodes | `true` | Set `false` to restrict to verified nodes only |
| `N8N_VERIFIED_PACKAGES_ENABLED` | Show verified community nodes in node panel | `true` | Set `false` to hide verified nodes from UI |
| `N8N_COMMUNITY_PACKAGES_REGISTRY` | NPM registry URL for community packages | `https://registry.npmjs.org` | Set to private registry URL when using `N8N_COMMUNITY_PACKAGES_AUTH_TOKEN` |
| `N8N_COMMUNITY_PACKAGES_AUTH_TOKEN` | Auth token for private npm registry | — | Set when pulling community nodes from a private registry |
| `N8N_CUSTOM_EXTENSIONS` | Path to directories containing custom nodes | — | When deploying custom nodes from the filesystem |
| `NODE_FUNCTION_ALLOW_BUILTIN` | Allowed Node.js built-in modules in Code node (`*` = all) | — (none) | Specify only what workflows actually need |
| `NODE_FUNCTION_ALLOW_EXTERNAL` | Allowed external npm modules in Code node | — (none) | Specify only what workflows actually need |
| `N8N_PYTHON_ENABLED` | Enable Python execution in Code node | `true` | Set `false` if Python Code nodes are not needed |
| `N8N_COMPRESSION_NODE_MAX_DECOMPRESSED_SIZE_BYTES` | Max total decompressed output size (bytes) | `2147483648` (2 GiB) | Lower to protect against decompression bomb attacks |
| `N8N_COMPRESSION_NODE_MAX_ZIP_ENTRIES` | Max entries in a ZIP archive | `5000` | Lower to protect against ZIP bomb attacks |

---

## Binary Data

Source: `hosting/configuration/environment-variables/binary-data.md`, `hosting/scaling/binary-data.md`

| Variable | Does | Default | When to set |
|---|---|---|---|
| `N8N_DEFAULT_BINARY_DATA_MODE` | Storage mode: `default` (memory), `filesystem`, `s3`, `database` | `default` | Set `filesystem` for workflows handling large files; set `s3` (Enterprise) for queue mode with binary data; set `database` for queue mode without S3 |
| `N8N_AVAILABLE_BINARY_DATA_MODES` | Comma-separated list of enabled binary data modes | `filesystem` | Add `s3` when also enabling S3; keeps filesystem readable during migration |
| `N8N_BINARY_DATA_STORAGE_PATH` | Filesystem path for binary data | `N8N_USER_FOLDER/binaryData` | When using a custom persistent volume mount |

**Note:** Queue mode does NOT support `filesystem` binary data mode. Use `s3` (Enterprise) or `database` instead.

---

## Credentials

Source: `hosting/configuration/environment-variables/credentials.md`

| Variable | Does | Default | When to set |
|---|---|---|---|
| `CREDENTIALS_OVERWRITE_DATA` / `_FILE` | JSON blob of credential field overwrites | — | When pre-setting credential fields across all instances (e.g. shared API endpoints) |
| `CREDENTIALS_OVERWRITE_ENDPOINT` | URL to fetch credential overwrites from | — | Dynamic overwrite source |
| `CREDENTIALS_OVERWRITE_PERSISTENCE` | Persist overwrites to DB for queue-mode propagation via pub/sub | `false` | **Required in queue mode** when using credential overwrites |
| `CREDENTIALS_DEFAULT_NAME` | Default name for new credentials | `My credentials` | Customize to match org naming conventions |

---

## User Management, SMTP, and 2FA

Source: `hosting/configuration/environment-variables/user-management-smtp-2fa.md`

| Variable | Does | Default | When to set |
|---|---|---|---|
| `N8N_EMAIL_MODE` | Enable email; set to `smtp` to activate | `smtp` | Required for invite emails, password resets, and sharing notifications |
| `N8N_SMTP_HOST` | SMTP server hostname | — | When email is needed |
| `N8N_SMTP_PORT` | SMTP server port | — | When email is needed |
| `N8N_SMTP_USER` | SMTP username | — | When email is needed |
| `N8N_SMTP_PASS` | SMTP password | — | When email is needed |
| `N8N_SMTP_SSL` | Use SSL for SMTP | `true` | Set `false` only for STARTTLS-only servers |
| `N8N_SMTP_STARTTLS` | Use STARTTLS for SMTP | `true` | Usually leave `true` |
| `N8N_SMTP_SENDER` | From address for n8n emails | — | Set to your org's no-reply address |
| `N8N_SMTP_OAUTH_SERVICE_CLIENT` | OAuth 2LO client ID for SMTP (service account) | — | Google Workspace SMTP OAuth |
| `N8N_SMTP_OAUTH_PRIVATE_KEY` | OAuth 2LO private key for SMTP | — | Google Workspace SMTP OAuth |
| `N8N_UM_EMAIL_TEMPLATES_INVITE` | Path to custom HTML invite email template | — | For branded email customization |
| `N8N_UM_EMAIL_TEMPLATES_PWRESET` | Path to custom HTML password reset template | — | For branded email customization |
| `N8N_UM_EMAIL_TEMPLATES_WORKFLOW_SHARED` | Path to custom workflow-shared notification template | — | For branded email customization |
| `N8N_UM_EMAIL_TEMPLATES_CREDENTIALS_SHARED` | Path to custom credentials-shared notification template | — | For branded email customization |
| `N8N_UM_EMAIL_TEMPLATES_PROJECT_SHARED` | Path to custom project-shared notification template | — | For branded email customization |
| `N8N_USER_MANAGEMENT_JWT_SECRET` | JWT secret for user sessions | Random (generated on start) | Set explicitly for stable sessions across restarts / multi-instance |
| `N8N_USER_MANAGEMENT_JWT_DURATION_HOURS` | JWT expiry (hours) | `168` (7 days) | Reduce for higher-security environments |
| `N8N_USER_MANAGEMENT_JWT_REFRESH_TIMEOUT_HOURS` | Hours before JWT expiry to auto-refresh; `-1` = never | `0` (25% of duration) | Set `-1` to force re-login; set positive value for active sessions |
| `N8N_MFA_ENABLED` | Enable 2FA option for users | `true` | Keep `true`; set `false` only if SSO enforces MFA externally |
| `N8N_INVITE_LINKS_EMAIL_ONLY` | Restrict invite links to email delivery only (not API) | `false` | Set `true` in production to prevent programmatic account creation |
| `N8N_INSTANCE_OWNER_MANAGED_BY_ENV` | Pre-provision instance owner from env vars | — | Set `true` to manage owner via env vars (automated deployments) |

---

## SSO

Source: `hosting/configuration/environment-variables/sso.md`

Available from v2.18.0. Business and Enterprise plans only. Set `N8N_SSO_*` variables via the `settings-env-vars` pattern (set the `_MANAGED_BY_ENV=true` activation flag first). Full variable list is in the snippets referenced by `hosting/configuration/environment-variables/sso.md`; configure via UI at **Settings > SSO** or via env vars.

Key prerequisite: `N8N_EDITOR_BASE_URL` must be set correctly for SAML redirect to work.

---

## Logs

Source: `hosting/configuration/environment-variables/logs.md`

| Variable | Does | Default | When to set |
|---|---|---|---|
| `N8N_LOG_LEVEL` | Log verbosity: `info`, `warn`, `error`, `debug` | `info` | Set `debug` for troubleshooting; `warn` or `error` in low-noise prod |
| `N8N_LOG_OUTPUT` | Log destination: `console`, `file`, or both | `console` | Add `file` when log aggregation from filesystem is needed |
| `N8N_LOG_FORMAT` | Log format: `text` or `json` | `text` | Set `json` in production for structured log aggregation |
| `N8N_LOG_FILE_LOCATION` | Absolute path to log file | `<n8n-dir>/logs/n8n.log` | When `N8N_LOG_OUTPUT` includes `file` |
| `N8N_LOG_FILE_COUNT_MAX` | Max number of log files to keep | `100` | Tune based on retention requirements |
| `N8N_LOG_FILE_SIZE_MAX` | Max log file size (MB) | `16` | Tune based on disk capacity |
| `N8N_LOG_CRON_ACTIVE_INTERVAL` | Minutes between logging active cron jobs; `0` = off | `0` | Enable for debugging cron trigger activity |
| `CODE_ENABLE_STDOUT` | Send Code node `console.log`/`print` to stdout | `false` | Enable for debugging production Code node executions |
| `NO_COLOR` | Disable ANSI color codes in log output | undefined | Set any value when piping logs to a system that strips colors |
| **Log Streaming** | | | |
| `N8N_EVENTBUS_CHECKUNSENTINTERVAL` | How often (ms) to check for unsent events; `0` = off | `0` | Enable for guaranteed delivery to log streaming destinations |
| `N8N_EVENTBUS_LOGWRITER_KEEPLOGCOUNT` | Number of event log files to keep | `3` | Increase for longer local event log retention |
| `N8N_EVENTBUS_LOGWRITER_MAXFILESIZEINKB` | Max event log file size (KB) | `10240` | Tune based on event volume |
| `N8N_EVENTBUS_LOGWRITER_LOGBASENAME` | Base filename for event log files | `n8nEventLog` | Rarely changed |
| `N8N_EVENTBUS_LOGWRITER_LOGFULLPATH` | Absolute path for event log file (overrides basename) | `''` | Set a unique path per process when multiple n8n processes share a filesystem |
| `N8N_EVENTBUS_LOGWRITER_MAXTOTALMESSAGESPERFILE` | Max lines parsed from an event log file on recovery | `500000` | Lower to reduce memory use during recovery from corrupt log |
| `N8N_EVENTBUS_LOGWRITER_SYNCFILEACCESS` | Synchronous file access for event log | `false` | Enable if async writes are causing log corruption |
| `N8N_LOG_STREAMING_MANAGED_BY_ENV` | Manage log streaming destinations from env vars | — | Set `true` for automated deployments |

---

## External Secrets

Source: `hosting/configuration/environment-variables/external-secrets.md`

| Variable | Does | Default | When to set |
|---|---|---|---|
| `N8N_EXTERNAL_SECRETS_UPDATE_INTERVAL` | How often (s) to poll secret providers for updates | `300` (5 min) | Reduce for faster secret rotation propagation; increase to reduce API calls |

**Providers:** 1Password (Connect Server), AWS Secrets Manager, Azure Key Vault, GCP Secrets Manager, HashiCorp Vault, Infisical. Enterprise Self-hosted / Enterprise Cloud only.

---

## External Storage (S3)

Source: `hosting/configuration/environment-variables/external-data-storage.md`, `hosting/scaling/external-storage.md`

| Variable | Does | Default | When to set |
|---|---|---|---|
| `N8N_EXTERNAL_STORAGE_S3_HOST` | S3-compatible storage host | — | e.g. `s3.us-east-1.amazonaws.com` |
| `N8N_EXTERNAL_STORAGE_S3_BUCKET_NAME` | Bucket name | — | Always when using S3 storage |
| `N8N_EXTERNAL_STORAGE_S3_BUCKET_REGION` | Bucket region | — | Must contain only `[a-zA-Z0-9-]` (no underscores) since v2.6.4 |
| `N8N_EXTERNAL_STORAGE_S3_ACCESS_KEY` | S3 access key ID | — | When not using auto-detect |
| `N8N_EXTERNAL_STORAGE_S3_ACCESS_SECRET` | S3 secret access key | — | When not using auto-detect |
| `N8N_EXTERNAL_STORAGE_S3_AUTH_AUTO_DETECT` | Use AWS default credential provider chain | — | Set `true` to use IAM role / environment credentials; ignores access key/secret |

Activate S3 binary storage:
```bash
N8N_AVAILABLE_BINARY_DATA_MODES=filesystem,s3
N8N_DEFAULT_BINARY_DATA_MODE=s3
```

Enterprise license required. Set a bucket lifecycle rule in AWS to auto-delete old objects (n8n delegates binary data pruning to S3).

---

## SSRF Protection

Source: `hosting/configuration/environment-variables/ssrf-protection.md`

| Variable | Does | Default | When to set |
|---|---|---|---|
| `N8N_SSRF_PROTECTION_ENABLED` | Enable SSRF protection for HTTP-making nodes | `false` | **Set `true` in production** — applies to HTTP Request node and others |
| `N8N_SSRF_BLOCKED_IP_RANGES` | CIDR ranges to block; use `default` for standard private ranges | Standard private/reserved | Use `default,<extra-cidr>` to extend; set to `default` alone to use built-in list |
| `N8N_SSRF_ALLOWED_IP_RANGES` | CIDR ranges to allow (takes precedence over blocked) | — | Allowlist specific internal service IPs that workflows legitimately need |
| `N8N_SSRF_ALLOWED_HOSTNAMES` | Hostname patterns to allow (supports wildcards); takes precedence over blocked IPs | — | e.g. `*.n8n.internal,*.company.local` |
| `N8N_SSRF_DNS_CACHE_MAX_SIZE` | DNS cache max size (bytes), LRU eviction | `1048576` (1 MB) | Reduce on memory-constrained instances |

---

## Task Runners

Source: `hosting/configuration/environment-variables/task-runners.md`

### n8n instance variables

| Variable | Does | Default | When to set |
|---|---|---|---|
| `N8N_RUNNERS_ENABLED` | Enable task runners | `false` | Set `true` to enable Code node isolation |
| `N8N_RUNNERS_MODE` | `internal` (child process) or `external` (separate container) | `internal` | Set `external` for maximum isolation (recommended in production) |
| `N8N_RUNNERS_AUTH_TOKEN` | Shared secret authenticating runner to n8n | Random | **Required in external mode** — set explicitly |
| `N8N_RUNNERS_BROKER_PORT` | Port task broker listens on | `5679` | Rarely changed |
| `N8N_RUNNERS_BROKER_LISTEN_ADDRESS` | Address task broker binds to | `127.0.0.1` | Keep loopback; change only when runner is truly external |
| `N8N_RUNNERS_MAX_PAYLOAD` | Max payload size (bytes) between broker and runner | `1073741824` (1 GiB) | Rarely changed |
| `N8N_RUNNERS_MAX_CONCURRENCY` | Concurrent tasks a runner can execute | `5` | Tune based on runner container resources |
| `N8N_RUNNERS_TASK_TIMEOUT` | Max task runtime (s) before runner restarts | `300` | Lower for untrusted user code |
| `N8N_RUNNERS_HEARTBEAT_INTERVAL` | Heartbeat interval (s) | `30` | Rarely changed |
| `N8N_RUNNERS_INSECURE_MODE` | Disable all runner security measures | `false` | **Never set `true` in production** |
| `N8N_RUNNERS_TASK_REQUEST_TIMEOUT` | Timeout (s) for a task to wait for a runner | `60` | Increase if runners are slow to become available |
| `N8N_RUNNERS_MAX_OLD_SPACE_SIZE` | `--max-old-space-size` for runner (MB) | Node.js default | Tune runner memory limit |

### Task runner launcher variables

| Variable | Does | Default | When to set |
|---|---|---|---|
| `N8N_RUNNERS_LAUNCHER_LOG_LEVEL` | Log level for launcher | `info` | Set `debug` for troubleshooting runner connectivity |
| `N8N_RUNNERS_AUTO_SHUTDOWN_TIMEOUT` | Seconds before idle runner shuts down | `15` | Increase to reduce cold-start latency for bursty workloads |
| `N8N_RUNNERS_TASK_BROKER_URI` | URI of task broker (n8n instance) | `http://127.0.0.1:5679` | Set when runner is in a separate container |
| `N8N_RUNNERS_LAUNCHER_HEALTH_CHECK_PORT` | Port for launcher health check | `5680` | Change if port conflicts |

### JavaScript runner variables

| Variable | Does | Default | When to set |
|---|---|---|---|
| `NODE_FUNCTION_ALLOW_BUILTIN` | Allowed Node.js built-ins in Code node | — (none) | Specify minimal set needed by workflows |
| `NODE_FUNCTION_ALLOW_EXTERNAL` | Allowed external npm modules in Code node | — (none) | Specify minimal set; in external mode set via `/etc/n8n-task-runners.json` |
| `N8N_RUNNERS_ALLOW_PROTOTYPE_MUTATION` | Allow runtime prototype mutation | `false` | Set `true` only for modules like puppeteer that require it |
| `GENERIC_TIMEZONE` | Timezone for runner (should match instance) | `America/New_York` | Set to match `GENERIC_TIMEZONE` on the n8n instance |
| `NODE_OPTIONS` | Node.js CLI options | — | e.g. `--max-old-space-size=4096` |

### Python runner variables

| Variable | Does | Default | When to set |
|---|---|---|---|
| `N8N_RUNNERS_STDLIB_ALLOW` | Allowed Python stdlib modules | — (none) | List only what workflows need; `*` allows all |
| `N8N_RUNNERS_EXTERNAL_ALLOW` | Allowed third-party Python modules | — (none) | List only what workflows need; `*` allows all |
| `N8N_RUNNERS_BUILTINS_DENY` | Python built-ins denied in Code node | `eval,exec,compile,open,input,...` | Do not empty in production |
| `N8N_BLOCK_RUNNER_ENV_ACCESS` | Block Python code from reading `os.environ` | `true` | Keep `true`; only `false` if runner env access is explicitly needed |

**Note:** Task runner image does NOT support `_FILE` suffix for any variable.

---

## Workflows

Source: `hosting/configuration/environment-variables/workflows.md`

| Variable | Does | Default | When to set |
|---|---|---|---|
| `N8N_WORKFLOW_CALLER_POLICY_DEFAULT_OPTION` | Who can call a workflow: `any`, `none`, `workflowsFromAList`, `workflowsFromSameOwner` | `workflowsFromSameOwner` | Set `none` to block all sub-workflow calls; `any` for open sub-workflow access |
| `N8N_WORKFLOW_ACTIVATION_BATCH_SIZE` | Workflows to publish in parallel on startup | `1` | Increase for faster startup on instances with many active workflows |
| `N8N_WORKFLOW_TAGS_DISABLED` | Disable workflow tagging | `false` | Set `true` to simplify UI for small teams |
| `N8N_ONBOARDING_FLOW_DISABLED` | Disable onboarding tips on new workflow | `false` | Set `true` for pre-configured or team deployments |
| `WORKFLOWS_DEFAULT_NAME` | Default name for new workflows | `My workflow` | Set to org standard naming |

---

## Workflow History

Source: `hosting/configuration/environment-variables/workflow-history.md`

| Variable | Does | Default | When to set |
|---|---|---|---|
| `N8N_WORKFLOW_HISTORY_PRUNE_TIME` | Hours to retain workflow history versions; `-1` = forever | `-1` | Set a positive value (e.g. `720` = 30 days) to control DB growth |

---

## Source Control

Source: `hosting/configuration/environment-variables/source-control.md`

| Variable | Does | Default | When to set |
|---|---|---|---|
| `N8N_SOURCECONTROL_DEFAULT_SSH_KEY_TYPE` | Default SSH key type for source control: `ed25519` or `rsa` | `ed25519` | Set `rsa` if your Git server does not support ed25519 |

---

## AI Assistant

Source: `hosting/configuration/environment-variables/ai-assistant.md`

| Variable | Does | Default | When to set |
|---|---|---|---|
| `N8N_AI_ASSISTANT_BASE_URL` | Base URL of self-hosted AI assistant service | — | Required for self-hosted n8n to enable the AI Assistant feature |

---

## Licenses

Source: `hosting/configuration/environment-variables/licenses.md`

| Variable | Does | Default | When to set |
|---|---|---|---|
| `N8N_LICENSE_ACTIVATION_KEY` | Activation key for initial license setup | `''` | Set on first deployment to activate Enterprise/Pro features |
| `N8N_LICENSE_AUTO_RENEW_ENABLED` | Auto-renew license | `true` | Set `false` only if n8n cannot reach `license.n8n.io` (air-gapped) |
| `N8N_LICENSE_DETACH_FLOATING_ON_SHUTDOWN` | Release floating entitlements on shutdown | `true` | Set `false` for production instances that must always keep licensed features |
| `N8N_LICENSE_SERVER_URL` | License server URL | `https://license.n8n.io/v1` | Set to internal mirror for air-gapped environments |
| `N8N_LICENSE_TENANT_ID` | License tenant ID | `1` | Only set if explicitly instructed by n8n support |
| `N8N_HIDE_USAGE_PAGE` | Hide the usage and plans page in the UI | `false` | Set `true` for OEM/white-label deployments |
| `https_proxy_license_server` | HTTPS proxy for license server calls (lowercase name) | — | When license server is behind a corporate proxy |

---

## OpenTelemetry

Source: `hosting/configuration/environment-variables/opentelemetry.md` (available from v2.19.0)

| Variable | Does | Default | When to set |
|---|---|---|---|
| `N8N_OTEL_ENABLED` | Enable OpenTelemetry tracing | `false` | Set `true` to export traces to an OTLP collector |
| `N8N_OTEL_EXPORTER_OTLP_ENDPOINT` | OTLP HTTP endpoint base URL | `http://localhost:4318` | Point to your Jaeger / Tempo / OTLP collector |
| `N8N_OTEL_EXPORTER_OTLP_TRACING_PATH` | Path appended to OTLP endpoint for traces | `/v1/traces` | Rarely changed |
| `N8N_OTEL_EXPORTER_OTLP_HEADERS` | Comma-separated `key=value` HTTP headers for OTLP requests | — | `authorization=Bearer <token>` for authenticated collectors |
| `N8N_OTEL_EXPORTER_SERVICE_NAME` | `service.name` attribute on exported spans | `n8n` | Set to distinguish multiple n8n instances |
| `N8N_OTEL_TRACES_SAMPLE_RATE` | Fraction of traces to export (`0`–`1`) | `1.0` | Reduce on high-volume instances to control trace storage costs |
| `N8N_OTEL_TRACES_INCLUDE_NODE_SPANS` | Emit a span per node execution | `true` | Set `false` to export workflow-level spans only |
| `N8N_OTEL_TRACES_PRODUCTION_ONLY` | Export traces only for production executions | `true` | Set `false` to include manual/test executions |
| `N8N_OTEL_TRACES_INJECT_OUTBOUND` | Inject W3C `traceparent`/`tracestate` into outbound HTTP | `true` | Set `false` if downstream services don't support trace context |
| `N8N_OTEL_STARTUP_CONNECTIVITY_TIMEOUT_MS` | Timeout (ms) for startup check of OTLP endpoint | `2000` | Increase if collector is slow to become ready |

---

## Insights

Source: `hosting/configuration/environment-variables/insights.md`

| Variable | Does | Default | When to set |
|---|---|---|---|
| `N8N_DISABLED_MODULES` | Disable modules; set to `insights` to turn off Insights | — | Set `insights` on high-volume instances where Insights adds unwanted DB load |
| `N8N_INSIGHTS_MAX_AGE_DAYS` | Days to retain compacted Insights data (max 730) | `365` | Reduce for smaller DB footprint |
| `N8N_INSIGHTS_FLUSH_BATCH_SIZE` | Max buffered Insights events before flush | `1000` | Rarely changed |
| `N8N_INSIGHTS_FLUSH_INTERVAL_SECONDS` | Flush interval to DB (s) | `30` | Rarely changed |
| `N8N_INSIGHTS_COMPACTION_INTERVAL_MINUTES` | How often compaction runs (min) | `60` | Decrease to reduce data buildup between runs under DB load |
| `N8N_INSIGHTS_COMPACTION_BATCH_SIZE` | Items compacted per batch | `500` | Decrease if compaction causes DB spikes |
| `N8N_INSIGHTS_COMPACTION_BATCH_DELAY_MILLISECONDS` | Delay between compaction batches (ms) | `100` | Increase to throttle compaction I/O |
| `N8N_INSIGHTS_COMPACTION_MAX_BATCHES_PER_RUN` | Max batches per compaction run; `0` = unlimited | `1000` | Decrease to limit each run's work |
| `N8N_INSIGHTS_COMPACTION_MAX_RUNTIME_SECONDS` | Max runtime per compaction run (s); `0` = unlimited | `300` | Decrease to stop runs sooner |
| `N8N_INSIGHTS_COMPACTION_HOURLY_TO_DAILY_THRESHOLD_DAYS` | Age (days) to compact hourly → daily rows | `90` | Decrease to compact sooner and save DB space |
| `N8N_INSIGHTS_COMPACTION_DAILY_TO_WEEKLY_THRESHOLD_DAYS` | Age (days) to compact daily → weekly rows | `180` | Decrease to compact sooner and save DB space |
| `N8N_INSIGHTS_PRUNE_CHECK_INTERVAL_HOURS` | How often (h) to check for data older than max age | `24` | Rarely changed |

---

## Timezone / Localization

Source: `hosting/configuration/environment-variables/timezone-localization.md` (not read — referenced)

| Variable | Does | Default | When to set |
|---|---|---|---|
| `GENERIC_TIMEZONE` | Default timezone for all workflow schedules | `America/New_York` | **Always set** to the correct timezone for your instance; must match task runner `GENERIC_TIMEZONE` |

---

## Miscellaneous

Source: `hosting/configuration/environment-variables/external-hooks.md` (referenced)

| Variable | Does | Default | When to set |
|---|---|---|---|
| `EXTERNAL_FRONTEND_HOOKS_URLS` | URLs for external frontend hook scripts | — | Set to empty string in air-gapped deployments |
| `N8N_DISABLED_MODULES` | Comma-separated modules to disable (e.g. `insights`) | — | Disable specific modules that are not needed |
