# Security (n8n v2.26.0)

> Credential handling, webhook auth, secrets, SSRF/HTTP risks, encryption key management, external secrets providers, RBAC/projects, 2FA/SSO, task-runner isolation, and hardening checklist for production n8n.

## Credentials — never hardcode secrets

Secrets (API keys, tokens, passwords, connection strings) MUST live in n8n **credentials**, never in node `parameters`. Credentials are stored encrypted (see `N8N_ENCRYPTION_KEY`) and referenced by id, keeping them out of exported JSON and shared workflows.

### WRONG — inline key in parameters

```json
{
  "parameters": {
    "url": "https://api.example.com/data",
    "headerParameters": {
      "parameters": [
        { "name": "Authorization", "value": "Bearer sk_live_4eC39Hq..." }
      ]
    }
  },
  "type": "n8n-nodes-base.httpRequest"
}
```

The secret is now in the workflow JSON — leaked on export, in git, in the editor, to anyone with workflow read access.

### RIGHT — credential reference

```json
{
  "parameters": {
    "url": "https://api.example.com/data",
    "authentication": "predefinedCredentialType",
    "nodeCredentialType": "httpHeaderAuth"
  },
  "type": "n8n-nodes-base.httpRequest",
  "credentials": {
    "httpHeaderAuth": { "id": "17", "name": "Example API key" }
  }
}
```

The secret lives only in the encrypted credential store; the workflow references it by id.

## Webhook security

A `n8n-nodes-base.webhook` node exposes a public URL. The `authentication` parameter has four options:

| Value | Mechanism | Notes |
|---|---|---|
| `none` | Open endpoint | **Never** for production unless behind a gateway/WAF doing auth. |
| `basicAuth` | HTTP Basic (user/pass) | Credential-backed. Use only over HTTPS. |
| `headerAuth` | Static header name+value (e.g. `X-API-Key`) | Common for service-to-service. |
| `jwtAuth` | Signed JWT validation | Best for tokens issued by an IdP; validates signature + claims. |

```json
{
  "parameters": {
    "httpMethod": "POST",
    "path": "orders-intake",
    "authentication": "headerAuth"
  },
  "type": "n8n-nodes-base.webhook",
  "typeVersion": 2,
  "credentials": {
    "httpHeaderAuth": { "id": "21", "name": "Webhook intake key" }
  }
}
```

**Rules:**
- Require `basicAuth`, `headerAuth`, or `jwtAuth` on **every** public webhook. `none` is only acceptable behind an authenticating proxy.
- **Validate the payload** immediately after the webhook (IF/Set/Code guard): check required fields, types, and ranges; reject with `stopAndError` on malformed input. Never trust webhook bodies.
- Prefer a hard-to-guess `path` and rotate webhook auth credentials periodically.

## Encryption key management

Source: `hosting/configuration/configuration-examples/encryption-key.md`, `hosting/securing/encryption-key-rotation.md`, `hosting/configuration/environment-variables/deployment.md`

### Instance key (`N8N_ENCRYPTION_KEY`)

n8n generates a random key on first launch and saves it to `~/.n8n`. In production:

```bash
export N8N_ENCRYPTION_KEY=<cryptographically-random-string>
```

- **Must be identical across all instances** (main + all workers + webhook processors in queue mode). Workers use it to decrypt credentials fetched from the database.
- Treat it as a top-tier secret: store it in your secret manager, never in the repo or a `.env` file committed to version control.
- If it changes, existing credentials become undecryptable.

### Two-layer key model (v2.26)

When `N8N_ENV_FEAT_ENCRYPTION_KEY_ROTATION=true`:

- **Instance key** (`N8N_ENCRYPTION_KEY`) — master key, never rotated, protects the data encryption keys.
- **Data encryption key** — directly encrypts credential data, stored encrypted in the DB. This is the key you rotate via UI or API.

Rotation re-encrypts records to the new key lazily (next time each record is updated). Previous-key data remains readable.

```bash
# Enable on ALL instances (main + workers) simultaneously
N8N_ENV_FEAT_ENCRYPTION_KEY_ROTATION=true
```

**One-way change** — take a full DB backup first. Never disable the flag after data has been written in the new format; older n8n versions cannot read it. Source: `hosting/securing/encryption-key-rotation.md`

### Rotation via API

`POST /encryption/keys` (requires `encryptionKey:manage` scope). n8n never returns key material in API responses — only metadata (ID, algorithm, status, timestamps).

## External secrets providers

Source: `external-secrets.md`, `hosting/configuration/environment-variables/external-secrets.md`

**Enterprise Self-hosted / Enterprise Cloud only.** Supported providers:

| Provider | Notes |
|---|---|
| 1Password (Connect Server) | Requires self-hosted Connect Server; item fields become secret properties |
| AWS Secrets Manager | IAM: needs `ListSecrets`, `BatchGetSecretValue`, `GetSecretValue` |
| Azure Key Vault | — |
| GCP Secrets Manager | — |
| HashiCorp Vault | HCP Vault Secrets (cloud) is NOT supported; self-hosted Vault only |
| Infisical | — |

Reference secrets in credential fields with `{{ $secrets.<vault-name>.<secret-name> }}`. n8n only supports **plaintext** secret values (not JSON objects).

**Refresh interval:** `N8N_EXTERNAL_SECRETS_UPDATE_INTERVAL` (default `300` s / 5 min). Secrets are pulled on a schedule, not on every execution.

**Vault scopes (v2.13+):**
- **Global vault** — all instance credentials can reference it (owners/admins only in personal projects).
- **Project vault** — restricted to a specific project's credentials; admins assign vaults per project.

**Multi-vault support (v2.10+):** multiple vaults per provider are supported.

## RBAC and projects

Source: `external-secrets.md` (project vaults section), n8n docs on RBAC

| Control | Practice |
|---|---|
| Credential scope | Grant each credential the **minimum** API scopes needed (read-only where possible). One credential per integration/purpose, not a shared god-token. |
| Sharing | Share credentials/workflows only with the users/projects that need them; default to private. |
| Workflow caller policy | `N8N_WORKFLOW_CALLER_POLICY_DEFAULT_OPTION` — default `workflowsFromSameOwner`; set to `none` to block all sub-workflow calls or `any` only if intentional. |
| Owner account | Protect the instance **owner**; enable **2FA** for owner and all members. |
| Queue mode isolation | Workers execute workflow code — isolate workers (separate network segment, no access to secrets beyond `N8N_ENCRYPTION_KEY`, least-priv DB/credentials). |
| Invite links | Set `N8N_INVITE_LINKS_EMAIL_ONLY=true` to prevent API exposure of invite URLs; accounts require email verification. Source: `hosting/securing/restrict-by-email-verification.md` |

**Rule:** least privilege everywhere — narrowest credential scopes, private-by-default sharing, 2FA on, and isolated workers in queue mode.

## 2FA and SSO

Source: `hosting/securing/set-up-sso.md`, `hosting/configuration/environment-variables/user-management-smtp-2fa.md`

**2FA:**
- Enabled by default (`N8N_MFA_ENABLED=true`). Set to `false` only if an external SSO enforces MFA. n8n ignores this if existing users already have 2FA on.
- Enforce 2FA for the instance owner and all admins.

**SSO (Business and Enterprise plans):**
- Supports SAML and OIDC.
- Configure via UI (Settings > SSO) or environment variables (available from v2.18.0 via `N8N_SSO_*` variables in `hosting/configuration/environment-variables/sso.md`).
- Set `N8N_EDITOR_BASE_URL` to the correct public URL — it is used as the SAML redirect URL.

**JWE token decryption for OAuth 2.0 (preview, v2.21+):**

Lets your IdP encrypt OAuth 2.0 access/ID tokens as JWE; only your n8n instance can decrypt them.

```bash
N8N_ENV_FEAT_OAUTH2_JWE=true   # set on ALL instances (main + workers)
```

n8n generates an RSA key pair on startup, publishes the public key at `<host>/rest/.well-known/jwks.json` (rate-limited by `N8N_OAUTH_JWE_JWKS_PER_MINUTE`, default 60/min). Your IdP must use `RSA-OAEP-256` key encryption algorithm. Source: `hosting/securing/oauth2-jwe-token-decryption.md`

## HTTP Request / SSRF risk

The HTTP Request node will call any URL it's given. If a URL (or part of it) comes from **user input**, the node can be coerced into hitting internal services — SSRF (e.g. `http://169.254.169.254/` cloud metadata, internal admin APIs).

### Built-in SSRF protection (v2.12+)

Source: `hosting/securing/ssrf-protection.md`, `hosting/configuration/environment-variables/ssrf-protection.md`

```bash
N8N_SSRF_PROTECTION_ENABLED=true
```

When enabled, n8n validates all outbound HTTP from user-controllable nodes against blocked/allowed ranges, **including redirect targets and DNS resolution** (prevents DNS-rebinding bypass).

Default blocked ranges when enabled:

| Range | Type |
|---|---|
| `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16` | RFC 1918 private |
| `127.0.0.0/8`, `::1/128` | Loopback |
| `169.254.0.0/16`, `fe80::/10` | Link-local |
| `fc00::/7`, `fd00::/8` | IPv6 unique local |
| Reserved/special-purpose ranges | — |

Extend: `N8N_SSRF_BLOCKED_IP_RANGES=default,100.0.0.0/8`

Allowlist legitimate internal services (takes precedence over blocklist):

```bash
N8N_SSRF_ALLOWED_HOSTNAMES=*.n8n.internal,*.company.local
N8N_SSRF_ALLOWED_IP_RANGES=10.0.1.0/24,10.0.2.50/32
```

**Warning:** SSRF protection is application-level defense-in-depth. Network-level controls (firewalls, security groups) must be your primary line of defense.

Additional mitigations in workflow design:
- **Allowlist** permitted hosts/schemes before the HTTP node (IF/Code guard). Reject internal/loopback/link-local ranges.
- Never pass raw user input straight into `url`.
- Apply **rate limiting + backoff** on outbound calls: set `retryOnFail` + `waitBetweenTries`, and throttle batch loops.

### DNS cache

`N8N_SSRF_DNS_CACHE_MAX_SIZE` (default `1048576` bytes / 1 MB, LRU eviction) — controls DNS resolution cache size for SSRF checks.

## File-system access controls

Source: `hosting/configuration/environment-variables/security.md`

| Variable | Default | What it does |
|---|---|---|
| `N8N_BLOCK_FILE_ACCESS_TO_N8N_FILES` | `true` | Blocks access to all files in `.n8n` directory and user-defined config files |
| `N8N_RESTRICT_FILE_ACCESS_TO` | (none) | Semicolon-separated list of allowed directories for file operations |
| `N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS` | `false` | Set `true` to enforce 0600 on settings file (owner r/w only) |
| `N8N_BLOCK_ENV_ACCESS_IN_NODE` | `false` | Set `true` to block env var access in expressions and Code node |

## Task-runner isolation

Source: `hosting/securing/hardening-task-runners.md`, `hosting/configuration/environment-variables/task-runners.md`

Task runners execute Code node JavaScript/Python. Default (`internal`) mode runs the runner as a child process of n8n. For stronger isolation:

**External mode** — runner runs as a separate container:
```bash
N8N_RUNNERS_MODE=external
N8N_RUNNERS_AUTH_TOKEN=<shared-secret>   # required in external mode
```

**Hardening checklist for task runner containers:**

1. **Distroless image** — append `-distroless` to the Docker tag (e.g. `2.26.0-distroless`). Removes shells, package managers, and other attack-surface tools.
2. **Run as `nobody`** — UID/GID 65532; prevents root container process.
3. **Read-only root filesystem** — mount minimal `emptyDir` to `/tmp` only.
4. **AppArmor profile** — deny reads of `/proc/[0-9]*/{environ,mounts}` to prevent secret leakage from process environment:
   ```
   audit deny @{PROC}/[0-9]*/{environ,mounts} rwl,
   ```
5. **Block env access from Python** — `N8N_BLOCK_RUNNER_ENV_ACCESS=true` (default `true`). Set `false` only if explicitly needed.
6. **Do not set `N8N_RUNNERS_INSECURE_MODE=true`** in production (disables all runner security measures).
7. **Restrict module imports** — leave `NODE_FUNCTION_ALLOW_BUILTIN` and `NODE_FUNCTION_ALLOW_EXTERNAL` unset (default: no modules allowed in Code node). Only add specific modules that are required.
8. **Python built-ins deny list** — `N8N_RUNNERS_BUILTINS_DENY` defaults to blocking `eval`, `exec`, `compile`, `open`, etc. Do not empty this in production.
9. **Broker listens on loopback** — `N8N_RUNNERS_BROKER_LISTEN_ADDRESS` defaults to `127.0.0.1`. Keep it there; do not expose to `0.0.0.0` unless the runner is truly external with auth.

## Node blocking

Source: `hosting/securing/blocking-nodes.md`, `hosting/configuration/environment-variables/nodes.md`

```bash
# Default blocked (execute command + local file trigger)
NODES_EXCLUDE: "[\"n8n-nodes-base.executeCommand\", \"n8n-nodes-base.localFileTrigger\"]"

# Block additional high-risk nodes
NODES_EXCLUDE: "[\"n8n-nodes-base.executeCommand\", \"n8n-nodes-base.readWriteFile\"]"
```

Run the security audit (`n8n audit` CLI, `POST /audit` API, or n8n node) to surface: unprotected webhooks, risky nodes in use, community/custom nodes, stale credentials, and SQL injection risks in Execute Query fields.

`N8N_SECURITY_AUDIT_DAYS_ABANDONED_WORKFLOW` (default `90`) — days before a workflow is flagged as abandoned (not executed).

## Content-Security-Policy and cookies

Source: `hosting/configuration/environment-variables/security.md`

```bash
N8N_CONTENT_SECURITY_POLICY='{ "frame-ancestors": ["https://your-portal.example.com"] }'
N8N_SECURE_COOKIE=true          # HTTPS-only cookies (default true)
N8N_SAMESITE_COOKIE=strict      # or lax (default); none requires HTTPS
```

## Network isolation (air-gap / telemetry opt-out)

Source: `hosting/configuration/configuration-examples/isolation.md`

```bash
N8N_DIAGNOSTICS_ENABLED=false
N8N_VERSION_NOTIFICATIONS_ENABLED=false
N8N_TEMPLATES_ENABLED=false
EXTERNAL_FRONTEND_HOOKS_URLS=
N8N_DIAGNOSTICS_CONFIG_FRONTEND=
N8N_DIAGNOSTICS_CONFIG_BACKEND=
```

## Disable the public API

Source: `hosting/securing/disable-public-api.md`

```bash
N8N_PUBLIC_API_DISABLED=true
# Or disable just the Swagger UI playground
N8N_PUBLIC_API_SWAGGERUI_DISABLED=true
```

## Production hardening checklist

Source: `hosting/securing/overview.md` + vars from across the docs

- [ ] `N8N_ENCRYPTION_KEY` set explicitly and identically on all instances (main + workers)
- [ ] Encryption key stored in a secret manager, **not** in the repo
- [ ] `N8N_ENV_FEAT_ENCRYPTION_KEY_ROTATION=true` enabled after taking a full DB backup (one-way)
- [ ] `N8N_SSRF_PROTECTION_ENABLED=true` — enable built-in SSRF protection
- [ ] `N8N_BLOCK_FILE_ACCESS_TO_N8N_FILES=true` (default) — verify not overridden
- [ ] `N8N_BLOCK_ENV_ACCESS_IN_NODE=true` — prevents env var leakage via expressions
- [ ] `N8N_RESTRICT_FILE_ACCESS_TO=<allowed-paths>` — lock down filesystem access
- [ ] `N8N_MFA_ENABLED=true` (default) — enforce for owner and all admins
- [ ] `N8N_INVITE_LINKS_EMAIL_ONLY=true` — prevent API exposure of invite URLs
- [ ] `N8N_SECURE_COOKIE=true` (default) — HTTPS-only cookies
- [ ] `NODES_EXCLUDE` — block `executeCommand`, `readWriteFile`, and other risky nodes
- [ ] All public webhooks use `basicAuth`, `headerAuth`, or `jwtAuth` — not `none`
- [ ] `N8N_PUBLIC_API_DISABLED=true` if API is not in use
- [ ] `N8N_DIAGNOSTICS_ENABLED=false` for air-gapped or privacy-sensitive deployments
- [ ] Task runners in external mode with distroless image, `nobody` user, read-only FS, AppArmor
- [ ] `NODE_FUNCTION_ALLOW_BUILTIN` / `NODE_FUNCTION_ALLOW_EXTERNAL` — unset unless specific modules are required
- [ ] `N8N_RUNNERS_AUTH_TOKEN` set when using external task runner mode
- [ ] `N8N_GIT_NODE_DISABLE_BARE_REPOS=true` if Git node is available to untrusted users
- [ ] SSO configured (Business/Enterprise) with MFA enforced at IdP
- [ ] `N8N_ENV_FEAT_OAUTH2_JWE=true` if IdP supports JWE-encrypted tokens (preview)
- [ ] External secrets provider configured (Enterprise) — no raw secrets in credential fields
- [ ] Run `n8n audit` (CLI / API) periodically and address findings
- [ ] DB behind TLS (`DB_POSTGRESDB_SSL_ENABLED=true`, `DB_POSTGRESDB_SSL_REJECT_UNAUTHORIZED=true`)
- [ ] Redis behind TLS (`QUEUE_BULL_REDIS_TLS=true`) and authenticated (`QUEUE_BULL_REDIS_PASSWORD`)
- [ ] Reverse proxy terminates TLS; set `N8N_PROXY_HOPS` to match reverse-proxy depth
