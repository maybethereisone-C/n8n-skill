# Limit — `n8n-nodes-base.limit`
**Type** `n8n-nodes-base.limit` · **core**

**What:** Truncates the item list to a maximum count, keeping either the first or last N items.

**Credentials:** none.

**Resources / Operations:** Single operation — limit items.

**Key params & gotchas:**
- **Max Items**: maximum number of items to keep.
- **Keep**: `First Items` (head) or `Last Items` (tail).
- Items beyond the limit are silently dropped — not routed elsewhere.

**Source:** n8n-nodes-base.limit.md  [doc-verified]
