# Execution Data — `n8n-nodes-base.executionData`
**Type** `n8n-nodes-base.executionData` · **core**

**What:** Saves key/value metadata on the current execution so it can be searched in the Executions list.

**Credentials:** none.

**Resources / Operations:**
| Operation | Description |
|-----------|-------------|
| Save Execution Data for Search | Writes key/value pairs to execution metadata |

**Key params & gotchas:**
- `key` max 50 chars; `value` max 512 chars — n8n silently truncates and logs if exceeded.
- Metadata is available during execution via the Code node using `$execution.customData`.
- Only searchable in the Executions list UI; not returned as workflow output.

**Source:** n8n-nodes-base.executiondata.md  [doc-verified]
