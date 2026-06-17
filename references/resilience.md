# Resilience & Long-Running Jobs (n8n v2.26.0)

How to build workflows that survive partial failure, never re-do completed work, and don't crash on a flaky API. Apply ALL of these whenever a workflow (a) runs long (minutes–hours), (b) writes to a quota-limited/flaky API, or (c) processes many items.

## Core principle

Never run a long job as one monolithic execution. Make work **batched + checkpointed + idempotent** so any crash resumes from the last good point, not from zero.

## The 8 patterns

### 1. Batch the work (don't pull/process everything in one node)
Use **Loop Over Items** (`n8n-nodes-base.splitInBatches`) or API pagination so each batch is an independent unit. A crash loses at most one batch.
```json
{ "type": "n8n-nodes-base.splitInBatches", "typeVersion": 3,
  "parameters": { "batchSize": 100, "options": {} }, "name": "Loop Batches" }
```

### 2. Checkpoint progress to an external store
After each batch, persist the cursor (last page / last id / offset) to a durable store — a `Checkpoint` row in Google Sheets/Postgres, or workflow **staticData** (`$getWorkflowStaticData('global')`). At START, read the checkpoint and skip already-done work.
```js
// Code node — resume from checkpoint
const s = $getWorkflowStaticData('global');
const startPage = s.lastPage || 0;   // resume point
// ...after a batch succeeds:
s.lastPage = currentPage;            // persisted across executions
```
> n8n has NO native "resume a crashed execution mid-graph" — a fresh run starts clean. Resumability = the checkpoint store YOU build. (This is the [checkpoint-resume] rule applied to n8n.)

### 3. Raw-first staging (never lose an expensive pull)
Save fetched data **immediately** (append raw rows to a Sheet/DB or store as binary) BEFORE any transform. Split into two workflows: **Fetch** (pull → store raw) and **Process** (read raw → transform → final write). A crash in Process never forces a re-pull — re-run Process against the stored raw data.

### 4. Idempotent writes (re-run = no duplicates)
Key every write so replays are safe:
- Google Sheets: **Append or Update** by a key column (not blind Append).
- DB: `upsert` / `ON CONFLICT`.
- Upstream: `n8n-nodes-base.removeDuplicates` on a dedupe key.

### 5. Per-item isolation + dead-letter (one bad item ≠ dead workflow)
Set the flaky write node `onError: "continueErrorOutput"`. Route the error branch to a **dead-letter** sink (a `Failed` Sheet/queue with the item + error + timestamp). Good items keep flowing; failures are retried later, not lost.
```json
{ "type": "n8n-nodes-base.googleSheets", "name": "Save to Sheet",
  "onError": "continueErrorOutput", "retryOnFail": true, "maxTries": 4, "waitBetweenTries": 5000 }
```

### 6. Retry + backoff for transient/quota errors (429, 5xx, timeouts)
Node-level `retryOnFail` + `maxTries` (3–5) + `waitBetweenTries` (rising, e.g. 2s→5s→15s). Tune `batchSize` down + add a `Wait` node between batches to stay under per-minute API quotas (Google Sheets ~ write quota → 429 if hammered).

### 7. Decouple long fetch from processing (sub-workflows)
`n8n-nodes-base.executeWorkflow` to call Fetch and Process as separate executions. Each has its own timeout, retry, and error workflow. Re-run only the part that failed.

### 8. Observe + alert on the failed unit
Assign an Error Workflow (see error-handling.md). Its alert must include **which batch/cursor failed** + the execution URL, so recovery = re-run that batch only. Set `EXECUTIONS_DATA_SAVE_ON_ERROR=all` so the failed run's data is inspectable.

---

## Wait node — resilience uses

Source: `docs/integrations/builtin/core-nodes/n8n-nodes-base.wait.md`

The Wait node pauses execution and offloads state to the database (for pauses ≥65 s). This is the only safe way to sleep inside a long workflow without holding a process thread.

| Resume mode | When to use for resilience |
|---|---|
| **After Time Interval** | Rate-limit throttling between API batches (e.g. 1–2 s between pages). Short waits (<65 s) don't offload to DB. |
| **At Specified Time** | Retry at a known future window (e.g. retry after quota resets at midnight). |
| **On Webhook Call** | Human-in-the-loop approval gates; async third-party callback (send `$execution.resumeUrl` to the service, resume when it POSTs back). |
| **On Form Submitted** | Manual approval/rejection of a flagged item before continuing. |

**`Limit Wait Time`**: always set this on Webhook/Form modes so a missing callback doesn't stall the execution indefinitely. Pair with an alert in the error workflow.

**`$execution.resumeUrl`**: generated at runtime, unique per execution. Pass it to the external system before the Wait node executes. If the workflow has multiple Wait nodes, use `Webhook Suffix` to distinguish them (suffix is NOT auto-appended to `$execution.resumeUrl` — append manually).

### Practical pattern — quota-safe batch loop

```
Loop Over Items (batchSize=50)
  → [process batch]
  → Wait (After Time Interval, 2 s)   ← back to Loop Over Items loop output
  → [done output exits loop]
```

---

## Sub-workflow error isolation

Source: `docs/flow-logic/subworkflows.md`

Sub-workflows run as independent executions. Each has its own:
- **Error Workflow** setting (assign one per sub-workflow independently of the parent).
- **Timeout** (configured in sub-workflow settings).
- **Retry** behaviour.

If a sub-workflow throws and its own error workflow handles it silently (or it uses `continueErrorOutput`), the parent Execute Workflow node can receive an empty/error result without the parent itself failing. Conversely, if the sub-workflow throws unhandled, the Execute Workflow node in the parent propagates the error — the parent's `onError` setting then governs behaviour.

**Isolation strategy:**
1. Give every sub-workflow its own Error Workflow that logs the failure.
2. In the parent, set the Execute Workflow node to `onError: continueErrorOutput` to catch sub-workflow failures as items on the error branch, so one failing sub-call doesn't kill the whole parent run.
3. Sub-workflow executions do NOT count toward plan execution limits (doc: `docs/flow-logic/subworkflows.md`).

---

## Worked example — the 2–3h pull that keeps crashing on Sheet save

**Problem:** pull takes 2–3h; Sheet-save API errors often; a crash kills the run and forces a full re-pull.

**Resilient design:**
1. **Workflow A — Fetch** (Schedule/Manual → Loop Batches over pages):
   - Each page → **append RAW** to a `raw_data` Sheet/DB immediately (pattern 3).
   - After each page, write `lastPage` to a `Checkpoint` store (pattern 2). On restart, resume from `lastPage` — **no re-pull** of completed pages.
   - `Wait` 1–2s between pages + `retryOnFail`/backoff on the fetch (patterns 6).
2. **Workflow B — Process & Save** (triggered after A, or independently re-runnable):
   - Read `raw_data` rows not yet marked done.
   - Save node = **Append or Update by key** (pattern 4, idempotent) + `onError: continueErrorOutput` + retry/backoff (patterns 5–6).
   - Failed rows → `Failed` dead-letter Sheet; successful rows marked `done=true`.
   - Re-running B only retries `Failed`/`not-done` rows — never the whole job.
3. **Error Workflow:** on any crash, alert with the failing batch + execution URL (pattern 8).

**Result:** a crash at hour 2 resumes at the last checkpoint; Sheet-save errors land in dead-letter and retry; nothing is re-pulled or duplicated.

---

## When to apply
Any workflow that is long-running, writes to a flaky/quota-limited API, or processes >~50 items MUST use patterns 1, 2, 4, 5, 6 at minimum. Add 3 + 7 when a re-pull is expensive (like the 2–3h case). This is enforced in production-checklist.md → Resilience.
