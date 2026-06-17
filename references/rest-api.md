# n8n Public REST API — Complete Reference

> Source files: `docs/api/index.md`, `docs/api/authentication.md`, `docs/api/pagination.md`,
> `docs/api/api-reference.md`, `docs/api/n8n-cli/index.md`, `docs/hosting/cli-commands.md`
>
> See `mcp-and-api.md` for the three-path overview (MCP community / native MCP / REST) and the
> `POST /workflows/{id}/activate` gotcha. This file is the dense endpoint + CLI reference.

---

## Auth

| Item | Detail |
|---|---|
| Header | `X-N8N-API-KEY: <key>` on every request |
| Create key | **Settings → n8n API** → Create API key → set Label + Expiration |
| Delete key | **Settings → n8n API** → Delete → Delete Forever |
| Availability | Not available during free trial; upgrade required |

### Enterprise: scoped keys

Non-enterprise keys have full access. Enterprise keys can be scoped to minimum required permissions.

**Workflow scopes**

| Scope | Action |
|---|---|
| `workflow:create` | Create workflows |
| `workflow:read` | Read workflow + details |
| `workflow:list` | List workflows |
| `workflow:update` | Update a workflow |
| `workflow:delete` | Delete / archive / unarchive |
| `workflow:move` | Transfer to another project |
| `workflow:activate` | Activate or deactivate (publish/unpublish) |
| `workflowTags:list` | Read tags on a workflow |
| `workflowTags:update` | Update tags on a workflow |

**Execution scopes**

| Scope | Action |
|---|---|
| `execution:read` | Retrieve execution + details |
| `execution:list` | List executions |
| `execution:retry` | Retry a failed execution |
| `execution:stop` | Stop a running execution |
| `execution:delete` | Delete an execution |
| `executionTags:list` | Read annotation tags on an execution |
| `executionTags:update` | Update annotation tags on an execution |

**Credential scopes**

| Scope | Action |
|---|---|
| `credential:create` | Create credentials |
| `credential:read` | Read credential + schema |
| `credential:list` | List credentials |
| `credential:update` | Update a credential |
| `credential:delete` | Delete a credential |
| `credential:move` | Transfer to another project |

**Other resource scopes** (abbreviated)

| Resource | Available scopes |
|---|---|
| `tag` | create, read, list, update, delete |
| `user` | create, read, list, changeRole, delete |
| `variable` | create, list, update, delete |
| `project` | create, list, update, delete |
| `folder` | create, read, list, update, delete |
| `sourceControl` | pull |
| `securityAudit` | generate |
| `insights` | read |
| `communityPackage` | install, list, uninstall, update |
| `dataTable` | create, read, list, update, delete |
| `dataTableColumn` | create, read, update, delete |
| `dataTableRow` | create, read, update, delete, upsert |

---

## Base paths

| Deployment | Base URL |
|---|---|
| Self-hosted | `<N8N_HOST>:<N8N_PORT>/<N8N_PATH>/api/v1` |
| Cloud | `<instance>.app.n8n.cloud/api/v1` |

Current API version: **v1**. Playground (self-hosted only): `…/api/v1/docs`.

Do not use `/rest/` — that is the internal Editor UI API, OEM/embed-only, subject to change.

---

## Pagination

Default page size: **100**. Maximum: **250**.

| Query param | Type | Description |
|---|---|---|
| `limit` | integer | Page size (1–250) |
| `cursor` | string | Opaque cursor from previous response's `nextCursor` |

Response envelope:

```json
{
  "data": [ /* array of objects */ ],
  "nextCursor": "MTIzZTQ1NjctZTg5Yi0xMmQzLWE0NTYtNDI2NjE0MTc0MDA"
}
```

When `nextCursor` is absent or `null`, you are on the last page.

```bash
# Page 1
curl "$BASE/workflows?active=true&limit=150" -H "$H"
# Page 2
curl "$BASE/workflows?active=true&limit=150&cursor=<nextCursor>" -H "$H"
```

---

## Resource groups and key endpoints

### Workflows

| Method | Path | Description |
|---|---|---|
| `GET` | `/workflows` | List workflows. Params: `active` (bool), `tags`, `name`, `projectId`, `excludePinnedData`, `limit`, `cursor` |
| `POST` | `/workflows` | Create workflow. Body: `{ name, nodes, connections, settings }`. `active` field in body is **ignored** — workflow always lands inactive. |
| `GET` | `/workflows/{id}` | Get workflow by ID |
| `PATCH` | `/workflows/{id}` | Update workflow |
| `DELETE` | `/workflows/{id}` | Delete workflow |
| `POST` | `/workflows/{id}/activate` | **Publish/activate** — separate call required after create |
| `POST` | `/workflows/{id}/deactivate` | Unpublish/deactivate |
| `PUT` | `/workflows/{id}/transfer` | Move workflow to another project. Body: `{ destinationProjectId }` |
| `GET` | `/workflows/{id}/tags` | List tags on workflow |
| `PUT` | `/workflows/{id}/tags` | Set tags on workflow. Body: `[{ id }]` |

Key semantics:
- `POST /workflows` + `POST /workflows/{id}/activate` are **always two calls**. n8n 2.0 renamed active/inactive → Publish/Unpublish but the API uses `/activate` and `/deactivate`.
- Workflow JSON nodes use full type prefix: `n8n-nodes-base.slack` (not `nodes-base.slack`).
- Pin `typeVersion` to the node catalog's `maxVer`.

### Executions

| Method | Path | Description |
|---|---|---|
| `GET` | `/executions` | List executions. Params: `workflowId`, `status` (error/success/waiting/running), `includeData` (bool), `limit`, `cursor` |
| `GET` | `/executions/{id}` | Get single execution with full node data |
| `DELETE` | `/executions/{id}` | Delete an execution |
| `POST` | `/executions/{id}/retry` | Retry a failed execution |
| `POST` | `/executions/{id}/stop` | Stop a running execution |

### Credentials

| Method | Path | Description |
|---|---|---|
| `GET` | `/credentials` | List credentials. Params: `name`, `type`, `limit`, `cursor` |
| `POST` | `/credentials` | Create credential. Body: `{ name, type, data }` |
| `GET` | `/credentials/{id}` | Get credential (schema only; sensitive data not returned) |
| `PATCH` | `/credentials/{id}` | Update credential |
| `DELETE` | `/credentials/{id}` | Delete credential |
| `PUT` | `/credentials/{id}/transfer` | Move to another project |
| `GET` | `/credentials/schema/{credentialTypeName}` | Get JSON schema for a credential type (find `credentialTypeName` in exported workflow JSON) |

### Tags

| Method | Path | Description |
|---|---|---|
| `GET` | `/tags` | List all tags. Params: `limit`, `cursor` |
| `POST` | `/tags` | Create tag. Body: `{ name }` |
| `GET` | `/tags/{id}` | Get tag |
| `PATCH` | `/tags/{id}` | Update tag |
| `DELETE` | `/tags/{id}` | Delete tag |

### Users

| Method | Path | Description |
|---|---|---|
| `GET` | `/users` | List users. Params: `limit`, `cursor`, `includeRole` |
| `GET` | `/users/{id}` | Get user by ID or email |
| `POST` | `/users` | Invite/create users. Body: `[{ email, role }]` |
| `DELETE` | `/users/{id}` | Delete user |
| `PATCH` | `/users/{id}/role` | Change user's global role |

### Variables

| Method | Path | Description |
|---|---|---|
| `GET` | `/variables` | List instance variables |
| `POST` | `/variables` | Create variable. Body: `{ key, value }` |
| `PATCH` | `/variables/{id}` | Update variable |
| `DELETE` | `/variables/{id}` | Delete variable |

### Projects

| Method | Path | Description |
|---|---|---|
| `GET` | `/projects` | List projects |
| `POST` | `/projects` | Create project. Body: `{ name }` |
| `PATCH` | `/projects/{id}` | Update project |
| `DELETE` | `/projects/{id}` | Delete project |

### Source control

| Method | Path | Description |
|---|---|---|
| `POST` | `/source-control/pull` | Pull changes from connected git repository into the instance |

### Audit

| Method | Path | Description |
|---|---|---|
| `POST` | `/audit` | Generate security audit report. Body: optional `{ additionalOptions }` |

---

## Minimal curl examples

```bash
H="X-N8N-API-KEY: $N8N_API_KEY"
BASE="https://your-instance/api/v1"

# List active workflows (page 1, up to 50)
curl "$BASE/workflows?active=true&limit=50" -H "$H"

# Create workflow (lands INACTIVE)
curl -X POST "$BASE/workflows" -H "$H" -H "Content-Type: application/json" \
  -d @workflow.json

# Activate (publish) — always a second call
curl -X POST "$BASE/workflows/{id}/activate" -H "$H"

# Retry a failed execution
curl -X POST "$BASE/executions/{id}/retry" -H "$H"

# List last 20 failed executions for a workflow
curl "$BASE/executions?workflowId={id}&status=error&limit=20" -H "$H"
```

---

## n8n CLI (public API wrapper)

The `@n8n/cli` package wraps the same `/api/v1` surface. Preferred by coding agents over raw curl.

**Status:** Beta (as of v2.26). Use for local dev, CI/CD, and AI agent integration. Not for production-critical paths.

### Install and configure

```bash
# Zero-install
npx @n8n/cli workflow list

# Or global install
npm install -g @n8n/cli

# Configure once
n8n-cli config set-url https://your-instance.n8n.cloud
n8n-cli config set-api-key YOUR_API_KEY
n8n-cli config show          # verify

# Or use env vars (no config file)
export N8N_URL=https://your-instance.n8n.cloud
export N8N_API_KEY=your_api_key

# Or inline flags (highest priority)
n8n-cli --url=https://... --api-key=n8n_api_xxxxx workflow list
```

Config precedence: `--flags` > `N8N_URL`/`N8N_API_KEY` env vars > `~/.n8n-cli/config.json` (mode `0600`).

### Command surface

| Topic | Commands |
|---|---|
| `workflow` | `list`, `get`, `create`, `update`, `delete`, `activate`, `deactivate`, `tags`, `transfer` |
| `execution` | `list`, `get`, `retry`, `stop`, `delete` |
| `credential` | `list`, `get`, `schema`, `create`, `delete`, `transfer` |
| `project` | `list`, `get`, `create`, `update`, `delete`, `members`, `add-member`, `remove-member` |
| `tag` | `list`, `create`, `update`, `delete` |
| `variable` | `list`, `create`, `update`, `delete` |
| `data-table` | `list`, `get`, `create`, `delete`, `rows`, `add-rows`, `update-rows`, `upsert-rows`, `delete-rows` |
| `user` | `list`, `get` |
| `config` | `set-url`, `set-api-key`, `show` |
| `source-control` | `pull` |
| `skill` | `install` |
| `audit` | (top-level) |
| `login` / `logout` | (top-level) |

### Output formats

| Format | Flag | Use case |
|---|---|---|
| Table (default) | `--format=table` | Human-readable terminal output |
| JSON | `--format=json` | Pipe to `jq`, programmatic use |
| ID-only | `--format=id-only` | Pipe to `xargs`, scripting |

### Common examples

```bash
# List and inspect
n8n-cli workflow list
n8n-cli workflow get <id>
n8n-cli execution list --status=error --limit=10

# Create from JSON (stdin)
cat workflow.json | n8n-cli workflow create --stdin

# Credential schema then create
n8n-cli credential schema gmailOAuth2
n8n-cli credential create --type=gmailOAuth2 --name='My Gmail' --file=cred.json

# Transfer workflow to project
n8n-cli workflow transfer <id> --project=<projectId>

# Deactivate all workflows (batch via id-only + xargs)
n8n-cli workflow list --format=id-only | xargs -I{} n8n-cli workflow deactivate {}

# Pull Claude Code skill
n8n-cli skill install --global   # then type /n8n-cli in Claude Code
```

---

## Server CLI (same-machine admin — not the public API)

Runs directly on the n8n host. No API key; direct DB access. Most commands work even when n8n is stopped.

```bash
# Execute a workflow by ID
n8n execute --id <ID>

# Publish / unpublish (requires restart to take effect if n8n is running)
n8n publish:workflow --id=<ID>
n8n publish:workflow --id=<ID> --versionId=<VERSION_ID>   # specific historical version
n8n unpublish:workflow --id=<ID>
n8n unpublish:workflow --all

# Export
n8n export:workflow --all --output=backups/latest/
n8n export:workflow --id=<ID> --published --output=published.json
n8n export:credentials --backup --output=backups/latest/
n8n export:credentials --all --decrypted --output=plain.json  # WARNING: secrets in plain text

# Import (deactivates all workflows by default)
n8n import:workflow --input=file.json
n8n import:workflow --separate --input=backups/latest/
n8n import:workflow --separate --input=backups/ --activeState=fromJson  # multi-main only
n8n import:credentials --input=file.json

# DB migration between types
n8n export:entities --outputDir=./outputs --includeExecutionHistoryDataTables=true
n8n import:entities --inputDir=./outputs --truncateTables=true

# License
n8n license:clear
n8n license:info

# User management
n8n user-management:reset
n8n mfa:disable --email=user@example.com
n8n ldap:reset

# Security audit
n8n audit
```

Key CLI vs API-CLI difference:

| | Server CLI (`n8n`) | n8n CLI (`n8n-cli` / `@n8n/cli`) |
|---|---|---|
| Runs on | Same host as n8n | Any machine with network |
| Auth | Direct DB | API key |
| n8n running required | No (most commands) | Yes |
| Best for | Backups, emergencies, migrations | Developers, CI/CD, AI agents |
