# Compare Datasets — `n8n-nodes-base.compareDatasets`

**Type** `n8n-nodes-base.compareDatasets` · **typeVersion** 3 · **core**

**What:** Compares two input streams item-by-item and routes results to four output branches: In A Only, Same, Different, In B Only.

**Credentials:** None.

**Resources / Operations:**

| Output Branch | Contains |
|---------------|---------|
| In A only | Items present in Input A but not B |
| Same | Items identical in both inputs |
| Different | Items present in both but with field differences |
| In B only | Items present in Input B but not A |

**Key params & gotchas:**
- Comparison is **two-stage**: first match items by the key field(s) you specify, then compare all remaining fields to determine same vs. different.
- **Fuzzy Compare**: number `3` and string `"3"` treated as equal when on. Off = strict type matching.
- **When There Are Differences → Use a Mix of Versions**: lets you specify a primary source and per-field exceptions — useful for merging patches.
- **Fields to Skip Comparing** (option): ignore volatile fields like `updatedAt` that change every sync without meaning a real difference.
- **Multiple Matches → Include First Match Only**: prevents duplicate Same items when both datasets contain repeated rows.
- Requires two input connections (Input A and Input B); wire accordingly on the canvas.

**Source:** n8n-nodes-base.comparedatasets.md  [doc-verified]
