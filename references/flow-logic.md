# Flow Logic (n8n v2.26.0)

Control-flow toolkit: when to use each node, exact wiring, decision tables.
Sources: `docs/flow-logic/`, `docs/integrations/builtin/core-nodes/` node docs.

---

## Splitting: IF vs Switch vs Filter

| Node | Outputs | Use when |
|---|---|---|
| **IF** | 2 (true / false) | One binary condition; every item routes one way or the other. Standard guard/branch. |
| **Switch** | N (one per rule + optional fallback) | Multiple mutually-exclusive values of the same field (e.g. `status == "paid" / "pending" / "failed"`). Avoids chaining IFs. |
| **Filter** | 1 (passing items only) | Drop items that don't match; you don't need the rejected set. Equivalent to IF where the false branch is discarded. |

**Decision rule:**
- 1 condition, need both branches → **IF**
- 1 field, ≥3 values → **Switch**
- Need to discard non-matching items with no further use → **Filter**
- Nested IFs beyond 2 levels → refactor to **Switch** or **Code**

IF and Switch are also the loop-termination mechanism: wire the `false` / fallback output back upstream to create a conditional loop; the `true` output exits.

Execution order in multi-branch workflows (v1.0+): each branch completes fully before the next starts, top-to-bottom, left-to-right on canvas. Source: `docs/flow-logic/execution-order.md`.

---

## Merge node modes

Source: `docs/integrations/builtin/core-nodes/n8n-nodes-base.merge.md`

The Merge node waits for all connected inputs before emitting output.

| Mode | Sub-option | SQL analogy | Use when |
|---|---|---|---|
| **Append** | — | UNION ALL | Concatenate items from N inputs in order; no join needed. |
| **Combine › Matching Fields** | Keep Matches | INNER JOIN | Enrich items that exist in both streams by a shared key. |
| | Keep Non-Matches | ANTI JOIN | Find items in one stream absent from the other. |
| | Keep Everything | FULL OUTER JOIN | Keep all items; merge where keys match. |
| | Enrich Input 1 | LEFT JOIN | Keep all of Input 1, add matching fields from Input 2. |
| | Enrich Input 2 | RIGHT JOIN | Keep all of Input 2, add matching fields from Input 1. |
| **Combine › Position** | — | ZIP | Merge item[0]+item[0], item[1]+item[1]…; order matters, not keys. |
| **Combine › All Possible Combinations** | — | CROSS JOIN | Cartesian product; every pair. Use sparingly — output = N×M items. |
| **SQL Query** | AlaSQL | arbitrary SQL | Complex multi-input joins; `input1`, `input2`… are the table names. |
| **Choose Branch** | Input 1 / Input 2 / Empty | — | Conditional pass-through; waits for both inputs, emits only chosen one. |

**Uneven item counts**: Input 1 item count wins. Extra Input 2 items are silently dropped in Combine/Position mode. Use Append if you need all items from both.

**Clash handling** (Combine mode): controls what happens when both inputs have the same field name — prefer Input 1, prefer Input 2, or merge as array. Set explicitly; default silently drops duplicates from Input 2.

---

## Loop Over Items (Split In Batches) mechanics

Source: `docs/integrations/builtin/core-nodes/n8n-nodes-base.splitinbatches.md`

Node type: `n8n-nodes-base.splitInBatches` (UI name: "Loop Over Items").

**Outputs:**
- `loop` (index 0) — emits the current batch; connect downstream processing here, then loop back to the node's input.
- `done` (index 1) — fires once when all batches are exhausted; connect the post-loop continuation here.

**Parameters:**
- `batchSize` — items per iteration. Set to `1` to process items one-by-one (required for nodes that execute only once: RSS Read, CrateDB insert/update, MongoDB insert/update, etc.).
- `options.reset` — when `true`, re-initialises item tracking on each incoming execution rather than continuing where it left off. Use for pagination loops where the total page count is unknown.

**Useful expressions inside the loop:**
```js
// Has the node exhausted all items?
{{ $("Loop Over Items").context["noItemsLeft"] }}   // boolean

// Current zero-based iteration index
{{ $("Loop Over Items").context["currentRunIndex"] }}
```

**Standard wiring pattern:**
```
[Source] → Loop Over Items
              ├── loop → [Process] → [Wait optional] → back to Loop Over Items input
              └── done → [Post-loop node]
```

The Loop Over Items node terminates itself — no IF node needed to stop it.

**Nodes that require explicit loops** (don't auto-iterate): CrateDB/MongoDB/MicrosoftSQL/QuestDB/TimescaleDB insert+update, Redis Info, RSS Read, HTTP Request pagination, Code in "Run Once For All Items" mode, Execute Workflow in "Run Once For All Items" mode. Source: `docs/flow-logic/looping.md`.

---

## Merging data patterns

Source: `docs/flow-logic/merging.md`

| Scenario | Tool |
|---|---|
| Rejoin two branches of a split workflow | **Merge** node (Append or Combine) |
| Combine outputs from two unrelated nodes | **Merge** node wired from both |
| Merge data from multiple loop iterations | **Code** node — use `$input.all()` after the loop, or accumulate in `staticData` |
| Compare two datasets and get diff/intersection | **Compare Datasets** node (outputs up to 4 streams: matches, Input1-only, Input2-only, fuzzy matches) |

---

## Wait node — pause and resume

Source: `docs/integrations/builtin/core-nodes/n8n-nodes-base.wait.md`

Pauses mid-execution; state offloaded to DB for pauses ≥65 s.

| Resume mode | Key config | Typical use |
|---|---|---|
| **After Time Interval** | `waitAmount` + `waitUnit` (seconds/minutes/hours/days) | Rate-limit throttle between batches |
| **At Specified Time** | datetime picker | Retry at a future quota-reset window |
| **On Webhook Call** | `$execution.resumeUrl` (send to external system); optional `Authentication`, `Webhook Suffix` | Async callback from third-party; human approval via URL |
| **On Form Submitted** | Form title, fields, `Respond When` | Manual human-in-the-loop gate |

**`Limit Wait Time`**: set on Webhook/Form modes so a missing callback auto-expires rather than stalling forever.

**`$execution.resumeUrl`**: unique per execution, generated at runtime. Embed in an email/Slack message before the Wait node fires. Multiple Wait nodes in one workflow: use distinct `Webhook Suffix` values per node (suffix must be appended manually — `$execution.resumeUrl` does not auto-include it).

---

## Sub-workflows

Source: `docs/flow-logic/subworkflows.md`, `_snippets/flow-logic/subworkflow-usage.md`, `_snippets/flow-logic/subworkflow-data-flow.md`

### Two-node contract

| Node | Location | Role |
|---|---|---|
| **Execute Sub-workflow Trigger** (`n8n-nodes-base.executeWorkflowTrigger`) | Sub-workflow | Entry point; defines input schema |
| **Execute Workflow** (`n8n-nodes-base.executeWorkflow`) | Parent workflow | Caller; passes data in, receives last-node output |

Data flow: parent Execute Workflow node → sub-workflow Trigger node → … → sub-workflow last node → back to parent Execute Workflow node.

### Input data modes (on the Trigger node)

| Mode | When to use |
|---|---|
| **Define using fields below** | You know the schema; parent node auto-populates field list |
| **Define using JSON example** | Schema known, prefer JSON notation |
| **Accept all data** | Flexible/generic sub-workflow; validate inside |

### Calling the sub-workflow

Reference the sub-workflow by: Database ID (recommended for production), URL, local file, or inline JSON. The sub-workflow ID is the alphanumeric suffix of its URL.

### Error isolation

Each sub-workflow is an independent execution with its own Error Workflow setting and timeout. If the sub-workflow throws unhandled:
- The parent Execute Workflow node surfaces the error.
- Parent node's `onError` governs: `stopWorkflow` kills the parent; `continueErrorOutput` routes to the parent's error branch.

**Pattern:** assign a dedicated Error Workflow to the sub-workflow + set the parent's Execute Workflow node to `onError: continueErrorOutput` so sub-workflow failures are catchable without killing the parent run.

Sub-workflow executions do not count toward plan monthly execution limits.

### Splitting a large workflow into sub-workflows

Use **Sub-workflow conversion** (right-click → context menu on selected nodes) to extract a group of nodes into a new sub-workflow automatically. Or: Execute Sub-workflow node → Database → From list → **Create a sub-workflow**.

---

## textClassifier as semantic router

Use `@n8n/n8n-nodes-langchain.textClassifier` instead of IF/Switch for **3+ semantic categories** — no hardcoded string matching; the LLM decides the bucket.

```
Trigger → textClassifier (categories: billing / technical / general)
  ├── output 0 (billing)   → Billing Agent
  ├── output 1 (technical) → Technical Agent
  └── output 2 (general)   → noOp (or generic reply)
```

Each category becomes an output port; unmatched items route to the fallback port. Course pattern: replace nested IF chains on message intent with a single classifier node — cleaner canvas, handles fuzzy language, no regex maintenance. Attach the same cheap LLM used for routing; it needs `ai_languageModel`.

When NOT to use: exact/deterministic routing (status codes, boolean flags, enum values) → Switch is faster and cheaper.

## Fan-out parallelization

Connect one node's output to multiple downstream agent/processing nodes — n8n runs them **in parallel automatically**:

```
Fetch Article
  ├──→ Summarizer Agent
  ├──→ Sentiment Agent
  └──→ Entity Extractor Agent
         ↓ (all three)
       Merge (Append) → Synthesis Agent
```

Key facts:
- **Merge order is non-deterministic** — the synthesizer must handle any ordering of the three inputs (e.g. label each stream by field name, not position).
- Use **Merge → Append** to collect; each input becomes one item in the merged array.
- Add an **Aggregate** node after Merge if you need all results in one `$json` object before the synthesis agent.
- Course pattern: parallelize independent analysis tasks on the same content (translate + summarize + classify), then synthesize — cuts wall-clock time vs sequential chaining.

## Async polling loop

For long-running external jobs (>30 s) — prefer async+Wait over `run-sync` which blocks the execution thread:

```
POST /jobs → Set (jobId) → Wait (30 s)
→ GET /jobs/{jobId}/status → IF status == "done"?
  true  → GET /jobs/{jobId}/result → continue
  false → IF attempts < maxRetries?
    true  → Set (attempts++) → back to Wait
    false → error branch
```

- **Wait node** (After Time Interval) offloads state to DB and releases the thread.
- **Always add a max-retry counter** — no built-in loop limit; a stuck job otherwise runs indefinitely.
- `attempts` stored in a Set node; check in a second IF before looping back.
- Course pattern: webhook APIs (video rendering, PDF generation, ML inference) all fit this shape. `maxRetries` = 10–20 with 30 s interval covers most jobs under 10 min.

## HITL — generic vs Telegram shortcut

Two distinct HITL patterns in n8n:

**Generic (any channel) — Wait + webhook resume:**

```
Build approval message (include $execution.resumeUrl?approved=true / ?approved=false)
→ Send via Email / Slack / Teams / Gmail / etc.
→ Wait node (resume: On Webhook Call, Limit Wait Time: e.g. 24h)
→ IF $json.query.approved == "true" → approved branch
                                    → denied branch
```

The Wait node pauses execution; the user clicks the URL to resume. Workflow-agnostic, works with any notification channel.

**Telegram shortcut — no Wait node:**

Telegram's `sendMessage` with `inlineKeyboard` buttons can call a **second `telegramTrigger`** (or a Webhook) configured with the approval callback URL. The approval button fires directly to a second trigger, which then continues the flow. This avoids a Wait node but requires two trigger/listener paths and is Telegram-specific.

Course pattern: use the generic Wait+webhook for cross-channel or unknown-channel HITL; use the Telegram inline-keyboard shortcut only when the entire approval flow is Telegram-native and you want the cleaner one-trigger UX.

---

## Splitting & aggregating summary

```
Split:     IF (2 outputs) / Switch (N outputs) / Filter (drop non-matching)
Aggregate: Merge (Append/Combine/SQL) / Compare Datasets / Code
Loop:      Loop Over Items (loop→done outputs) / IF back-edge for condition loops
Pause:     Wait (time / webhook / form)
Modularise: Execute Workflow + Execute Sub-workflow Trigger
```
