# n8n as Code (TypeScript paradigm) — awareness

> Purpose: know that "author n8n workflows as TypeScript, not JSON" exists, recognize it when a user has it, and explain the trade-off. **This skill stays JSON-first** — n8n itself only ingests JSON; TypeScript is an editing layer that always round-trips back to JSON before deploy. Don't adopt the toolchain as a dependency.

## Two things ship a TS authoring layer

| Source | What it is | Maturity |
|---|---|---|
| **n8n native/official MCP** (`@n8n/workflow-sdk`, `json-to-code`/`code-to-json` CLIs) | 1st-party. The native MCP server generates TS against a fluent builder SDK; the model must produce code that type-checks + compiles before it touches the instance. | Public Preview, moving fast (v2.13+ to build/edit). |
| **`EtienneLescot/n8n-as-code`** (`n8nac` CLI + `@n8n-as-code/transformer`) | 3rd-party. Bidirectional JSON↔`.workflow.ts` transform + git-like sync (pull/push/resolve) + VS Code extension. | ~1.4k★, badge **"Beta / Pending Review"**; core-engine README still marked mid-development. Treat as experimental. |

Note: `czlonkowski/n8n-mcp` (the server in `mcp-and-api.md`) is **JSON-only** — it does NOT do TypeScript authoring. Don't attribute the TS path to it.

## What "workflow as code" looks like

A node becomes a decorated class property; routing becomes a method (n8n-as-code form):

```typescript
import { workflow, node, links } from '@n8n-as-code/transformer';

@workflow({ id: 'abc123', name: 'Slack Notifier', active: true })
export class SlackNotifierWorkflow {
  @node()
  Trigger = { type: 'n8n-nodes-base.webhook',
    parameters: { path: '/notify', method: 'POST' }, position: [250, 300] };

  @node()
  Slack = { type: 'n8n-nodes-base.slack',
    parameters: { resource: 'message', operation: 'post', channel: '#alerts',
      text: '={{ $json.message }}' }, position: [450, 300] };

  @links()
  defineRouting() { this.Trigger.out(0).to(this.Slack.in(0)); }
}
```

- Regular nodes wire with `source.out(0).to(target.in(0))`.
- AI/LangChain sub-nodes wire with `.uses()` (arrays for `ai_tool`/`ai_document`, single ref for `ai_languageModel`) — **never** `.out().to()`.
- Transform: `n8nac convert workflow.json --format typescript` (JSON→TS) and `n8nac convert workflow.ts -o workflow.json` (TS→JSON). The reverse re-assigns node UUIDs.

## Why a user would want it

Type-check + compile-time validation, **meaningful git diffs** (property names instead of UUIDs), pre-commit gating (`n8nac validate` on changed `.workflow.ts`), and GitOps source-of-truth (`.workflow.ts` files in the repo, push/pull to the instance with optimistic-concurrency conflict resolution).

## Why this skill stays JSON-first

- **n8n ingests JSON.** TS is inert without `@n8n-as-code/transformer` (or the native SDK) installed — the decorators are runtime `reflect-metadata` calls that must be compiled to JSON to deploy. We already emit deployable JSON directly; adding TS only adds a compile dependency to reach the same artifact.
- **Toolchain weight + beta risk.** n8nac bundles ~91 MB of node-schema assets; roundtrip fidelity on complex workflows (credentials, AI dependency injection, error outputs, name collisions) is the known hard part and unproven at scale. Importing the toolchain imports its immaturity.
- **Our value prop is orthogonal and offline** — bundled templates + 565-node catalog + the error/log/security/resilience production layer. That works on a plane; the TS GitOps loop needs a live toolchain.

## `n8nac` CLI — full command surface

(Source: `EtienneLescot/n8n-as-code` docs. Commands are beta; verify against repo if behaviour seems off.)

### Core convert / sync

```bash
n8nac convert <file>.json --format typescript   # JSON → .workflow.ts
n8nac convert <file>.ts -o <file>.json          # .workflow.ts → JSON (re-assigns node UUIDs)
n8nac convert-batch <dir> --format typescript   # batch-convert a directory
n8nac validate <file>.workflow.ts               # compile + schema check without deploying
n8nac list                                      # list workflows in the configured instance
n8nac pull [<id>]                               # pull workflow(s) from instance → local .ts
n8nac push [<file>.ts]                          # push local .ts → instance (optimistic-concurrency)
n8nac push --verify                             # push + validate round-trip (recommended)
n8nac resolve <file>.ts                         # resolve a push conflict explicitly
n8nac find <query>                              # search workflows by name/tag
```

### env — workspace management

```bash
n8nac env add <name> <url>             # register a new environment (dev/staging/prod)
n8nac env use <name>                   # switch active environment
n8nac env status [--json]              # show current env + auth state
n8nac env list                         # list all registered envs
n8nac env auth set                     # store API key for active env
n8nac env workflowsPath <path>         # set local directory for .workflow.ts files
```

### promote — GitOps-to-prod

```bash
n8nac promote --from <env>             # promote active env's workflows → target env
                                       # reads env registry; handles credential remapping stubs
```

### native-mcp — n8n built-in MCP bridge

```bash
n8nac native-mcp configure             # wire n8nac to n8n's native MCP server
n8nac native-mcp disable               # remove the bridge
n8nac native-mcp doctor                # diagnose connection + auth issues
n8nac native-mcp status                # show bridge health
n8nac native-mcp tools                 # list tools exposed through the bridge
```

### credentials — inventory & recipes

```bash
n8nac credentials inventory            # list all credentials on the instance
n8nac credentials recipes              # show credential patterns for common node combos
n8nac credentials starter-kits         # scaffolding templates for new credential types
n8nac credentials ensure <type>        # create credential if missing (idempotent)
n8nac credentials test <id>            # test a stored credential
```

### skills — node knowledge (maps to `n8nac skills …`)

```bash
n8nac skills node-info <nodeType>      # node metadata (maps to get_node minimal)
n8nac skills node-schema <nodeType>    # full property schema
n8nac skills search <query>            # search nodes
n8nac skills docs <nodeType>           # markdown documentation
n8nac skills examples <nodeType>       # real-world config examples
n8nac skills guides                    # list available topic guides
n8nac skills related <nodeType>        # nodes commonly used alongside this one
```

### execution & audit

```bash
n8nac execution list [--workflowId <id>] [--status error|success|waiting]
n8nac execution get <execId>
```

## Sync discipline

1. **Pull before edit** — always `n8nac pull <id>` before touching a `.workflow.ts`; the instance is the source of truth.
2. **Push after edit** — `n8nac push --verify` (not bare `n8nac push`) to validate round-trip fidelity.
3. **Never use bare filenames as workflow references** across environments — use IDs or env-qualified names.
4. **Conflicts use explicit resolve** — `n8nac resolve <file>.ts`; never accept a blind overwrite.
5. **Optimistic-concurrency rejection** — `push` compares a local ETag/hash against the instance; a stale push is rejected with a conflict error rather than silently overwriting. Always pull the latest before retrying.

## Official native MCP vs community MCP — comparison

*Tested 2026-04-30 on n8n 2.18.5 (source: community benchmark, n8n GitHub discussions).*

| Dimension | n8n official native MCP (built-in) | Community `czlonkowski/n8n-mcp` |
|---|---|---|
| Edit model | Full TypeScript rewrite per change | 19-op diff engine (partial updates) |
| Token cost per iterative edit | Baseline | **28–60× cheaper** for incremental edits |
| Node knowledge | Relies on model training | 1,851 nodes indexed, offline |
| Version / credential / audit surface | Not exposed via MCP | `n8n_workflow_versions`, `n8n_manage_credentials`, `n8n_audit_instance` |
| Template deployment | Not available via MCP | `n8n_deploy_template` |
| Stability | Public Preview; tool names moving fast | Stable; 13+ tools, versioned |
| n8n roadmap | Closing gap; watch docs.n8n.io | Maintained by community |

Recommendation: prefer community MCP for authoring loops requiring iterative refinement; re-evaluate native MCP when n8n v3 lands.

## How to act when a user has it

- If the user already works in `.workflow.ts` / mentions `n8nac` or the native TS SDK: author the **JSON** with this skill, then have them run `n8nac convert <file>.json --format typescript` (or the native `json-to-code`) to bring it into their TS repo. The production layer (error workflow, retries, webhook auth, idempotency) applies identically — it's node-level config, format-agnostic.
- The portable ideas worth borrowing regardless of format: read a `<workflow-map>` / overview first before the full body (token-efficient), and schema-first authoring — never guess a node, look it up (we do this via `node-catalog.md` + `nodes/` schemas; they do it via `n8nac skills node-info`).
- Don't install or recommend installing the n8nac toolchain by default. Mention it exists; let the user opt in.
