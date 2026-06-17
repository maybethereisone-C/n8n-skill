# n8n Runtime Execution Model (v2.26)

> Purpose: how n8n actually *runs* a workflow at execution time — node order across branches, how items flow node→node, main vs sub-node connections, manual vs production executions, what triggers re-runs, and the determinism rules an author must respect. Pairs with workflow-schema.md (static JSON shape) and data-and-binary.md (the item contract).

## Execution order: v1 vs v0 (legacy)

n8n's node execution order depends on the workflow's `settings.executionOrder` (set per workflow; see workflows/settings.md). The version is **baked at creation time** by the n8n version that made the workflow — but you set it explicitly in JSON and should always pin `"v1"`.

| | **v1 (recommended)** | **v0 (legacy)** |
|---|---|---|
| Strategy | Runs each branch **in full, one at a time** — completes one branch before starting the next. | Runs the **first node of every branch, then the second node of every branch**, and so on (breadth-first across branches). |
| Branch order | By canvas position: **topmost → bottommost**; ties broken **leftmost → first**. | Effectively undefined relative to author intent; depends on internal ordering. |
| Determinism | Deterministic and position-driven. | Non-deterministic for author reasoning once branches exist. |

Source: flow-logic/execution-order.md, workflows/settings.md. **Always emit `"executionOrder": "v1"`.** Under v1, branch ordering is decided purely by node `position` `[x,y]` — so the canvas layout you author *is* the execution order. Two branches at equal `y` run left-to-right by `x`.

```
        ┌── Branch A (y=200) ── A1 → A2 → A3 ──┐   runs 1st (topmost)
Trigger ┤                                       │
        └── Branch B (y=400) ── B1 → B2 ───────┘   runs 2nd
```
Under v1 the full A1→A2→A3 chain completes before B1 starts. Under v0, A1 then B1, then A2 then B2, etc.

## How items flow node → node

- Every connection carries an **array of items** (see data-and-binary.md). A node receives that array on an input port and emits an array on each output port.
- **Implicit looping:** a node processes *each input item individually* and performs its configured operation per item — no explicit loop needed. A Trello "Create Card" fed 2 items creates 2 cards, one per item (data/data-structure.md).
- Expressions evaluate **per item**: `{{ $json.x }}` resolves to the current item's `x` as the node iterates.
- A node with no input items typically does not run its operation (zero items in → zero out), unless **Always Output Data** is set — then it emits one empty item even on no data (workflows/components/nodes.md). Be careful enabling this on IF nodes: it can cause an infinite loop (per the node-settings doc).
- **Execute Once** (node setting): the node runs a single time using only the **first** input item and ignores the rest (workflows/components/nodes.md).

## Multiple-input nodes and branch joins

- A node fed by two upstream branches (e.g. Merge) has multiple **input ports** (index 0, 1, …). Connections target a specific input via the `index` field in the connection entry (see workflow-schema.md connections contract).
- Under v1, because branches complete in turn, an upstream branch's data is fully available before a join node downstream of both branches runs. A Merge node that combines items from multiple inputs is exactly the case that breaks `.item` lineage downstream (multiple matching items) — see data-and-binary.md.

## Main connections vs sub-node connections

n8n has two structurally different connection roles (workflow-schema.md, connections contract):

| Connection type | Direction of "flow" | Examples | Runtime behavior |
|---|---|---|---|
| `main` | Data flows **forward**, source output → target input. | Every standard node. | Drives execution order; carries the item array. |
| `ai_*` (`ai_languageModel`, `ai_tool`, `ai_memory`, `ai_embedding`, `ai_document`, …) | **Sub-node attaches up** into a root node; the root *pulls* the capability on demand. | LangChain: Chat Model, Tool, Memory, Vector Store feeding an AI Agent. | Sub-node does **not** execute as a step in the main left-to-right order. It runs when the root node invokes it (possibly many times, e.g. a tool called per agent reasoning step). |

Consequence: a sub-node (a model/tool/memory) is **not** part of the main item-flow chain. It has no place in the topmost-to-bottommost branch ordering; it executes reactively when its parent root node asks for it. Wire these with the matching `ai_*` connection type, never `main`. [unverified: the canonical list of `ai_*` connection-type names is not enumerated in the read docs; treat the set above as representative, confirm against node-catalog.md / the specific LangChain node.]

## Manual / partial executions vs production executions

| Aspect | Manual (editor) execution | Production execution |
|---|---|---|
| Trigger | User clicks **Execute Workflow** / **Execute step** in the editor. | Active workflow fired by its trigger (webhook, schedule, app event). |
| Scope | Can run a **single node** ("Execute step") or the whole graph; supports partial re-runs from a node. | Always the full graph from the trigger. |
| Pinned data | **Used.** Pinned node output replaces real execution for that node. | **Ignored** — data pinning is dev-only, not available in production (data/data-pinning.md). |
| Mock / edited data | Available (Code/Set/Customer Datastore mocking, edited pinned data). | Not available — editing pinned data is dev-only (data/data-pinning.md). |
| Saved? | Controlled by **Save manual executions** setting. | Controlled by **Save successful / Save failed production executions** settings (workflows/settings.md). |
| Redaction | **Redact manual execution data** setting. | **Redact production execution data** setting; an instance admin can enforce redaction instance-wide and lock it on (workflows/settings.md). |

**Save execution progress** (workflows/settings.md): when on, n8n persists data after each node, so a failed workflow can **resume from where it stopped** instead of restarting — at the cost of added latency.

## What triggers (re-)execution

- **Trigger node fires:** webhook hit, schedule/cron tick, polling trigger detecting new data, or an app event. This is the only way a production run starts.
- **Manual run / partial run:** user-initiated from the editor; can re-execute a node and everything downstream.
- **Error workflow:** if `settings.errorWorkflow` is set, a failure in this workflow triggers *that* workflow as a separate execution (workflows/settings.md).
- **Retry on fail** (node setting): a failed node **reruns itself** until it succeeds (bounded by its retry config), without restarting the whole workflow (workflows/components/nodes.md).
- **Per-node error routing** via **On Error** (workflows/components/nodes.md): *Stop Workflow* halts everything; *Continue* proceeds to the next node using the last valid data; *Continue (using error output)* proceeds and routes error info down a dedicated error output for handling.

## Determinism rules (author checklist)

1. **Pin `executionOrder: "v1"`** — never leave it to legacy/default. Branch order then equals canvas geometry.
2. **Lay branches out intentionally:** topmost branch (smallest `y`) runs first; ties resolve leftmost (`x`). Position is not cosmetic under v1 — it is the order contract.
3. **Don't depend on cross-branch timing under v0.** If you inherit a v0 workflow with branch-order assumptions, migrate to v1 and re-verify.
4. **Don't assume a node runs on empty input** unless **Always Output Data** is set — and avoid that on IF (loop risk).
5. **Pinned/mock data is a dev illusion:** a workflow that "works" in the editor on pinned data may behave differently in production where pinning is ignored. Verify with a real trigger before activating.
6. **Sub-nodes (`ai_*`) are pulled, not stepped** — don't reason about them as positioned nodes in the main order.
```
