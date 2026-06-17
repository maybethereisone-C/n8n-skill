# Evaluation — `n8n-nodes-base.evaluation`
**Type** `n8n-nodes-base.evaluation` · **typeVersion** 1 · **action / core**
**What:** Performs evaluation lifecycle operations inside an AI evaluation workflow — writes results back to a dataset, logs numeric metrics to n8n's Evaluations tab, or branches based on whether the current execution is an evaluation run.
**Credentials:** Google Sheets OAuth2 (only required when `source=googleSheets`).

**Operations:**

| Operation | Purpose |
|---|---|
| `setOutputs` | Write evaluation results (actual outputs, expected outputs, scores) back to the dataset (data table or Google Sheet) |
| `setMetrics` | Record named numeric metric values visible in the workflow's **Evaluations** tab |
| `checkIfEvaluating` | Branches execution — one path for evaluation runs, another for normal runs |

**setOutputs params:**
- `source` — `dataTable` (default) or `googleSheets`.
- When `dataTable`: select data table by name or ID.
- When `googleSheets`: requires Google Sheets credential + spreadsheet document + sheet (same sheet used in the paired Evaluation Trigger node).
- **Outputs** section: add name/value pairs — `Name` = column header, `Value` = expression resolving to the value to write.

**setMetrics params:**
- **Metrics to Return** section: add name/value pairs. `Value` must resolve to a **numeric** type — non-numeric values will error.
- Results appear under the workflow's **Evaluations** tab after the evaluation run completes.

**checkIfEvaluating:**
- No parameters. Provides two output branches: evaluation path and normal-execution path.
- Use to skip expensive/side-effect steps (e.g., sending real emails) during evaluation runs.

**Key gotchas:**
- Always pair with an **Evaluation Trigger** (`n8n-nodes-base.evaluationTrigger`) as the workflow's start node — that node feeds rows from the dataset one at a time.
- The `setOutputs` target (data table or Google Sheet) should be the **same** dataset used by the paired Evaluation Trigger.
- `setMetrics` values must be numeric; use a Code or Set node to compute scores before passing them here.
- This is a core n8n node (not a LangChain node) despite being used exclusively in AI evaluation workflows.

**Related node:** Evaluation Trigger — `n8n-nodes-base.evaluationTrigger` (see below).

---

# Evaluation Trigger — `n8n-nodes-base.evaluationTrigger`
**Type** `n8n-nodes-base.evaluationTrigger` · **typeVersion** 1 · **trigger**
**What:** Starts an evaluation workflow by reading rows from a dataset (data table or Google Sheet) one at a time in sequence, feeding each row as an input item to the rest of the workflow.
**Credentials:** Google Sheets OAuth2 (only when `source=googleSheets`).

**Key params:**
- `source` — `dataTable` or `googleSheets`.
- `limitRows` / `maxRows` — cap the number of dataset rows processed per evaluation run (useful during development; default off).
- `filters` (Google Sheets only) — filter rows by column value so only matching rows are evaluated.

**Gotchas:**
- Rows are processed **sequentially**, not in parallel — each row is a separate execution cycle.
- The Evaluation Trigger does not fire on normal workflow activation; it only runs when an evaluation is triggered via the **Evaluations** tab.

**Source:** `n8n-nodes-base.evaluation.md` + `n8n-nodes-base.evaluationtrigger.md`  [doc-verified]
