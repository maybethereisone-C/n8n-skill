# Loop Over Items (Split in Batches) — `n8n-nodes-base.splitInBatches`
**Type** `n8n-nodes-base.splitInBatches` · **core**

**What:** Loops through items in configurable batch sizes, emitting chunks via the **loop** output and final combined result via the **done** output.

**Credentials:** none.

**Resources / Operations:** Single operation — batch loop.

**Key params & gotchas:**
- **Batch Size**: number of items per iteration emitted through the loop output.
- **Reset** option: when enabled, treats each incoming data set as fresh (resets internal counter). Useful for paginated API polling where you don't know page count in advance.
- Two outputs: `loop` (current batch, feeds back into the cycle) and `done` (all processed items combined, exits the loop).
- Most n8n nodes already process all items natively — only use this node when a downstream node processes only the first item (e.g., RSS Feed Read), to respect rate limits, or for paginated calls.
- Context variables inside the loop:
  - `{{$("Loop Over Items").context["noItemsLeft"]}}` → `true` when no more batches remain.
  - `{{$("Loop Over Items").context["currentRunIndex"]}}` → current iteration index.
- Always include a valid exit condition when using Reset + If to build dynamic pagination loops — an infinite loop will stall the execution.

**Source:** n8n-nodes-base.splitinbatches.md  [doc-verified]
