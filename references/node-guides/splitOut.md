# Split Out — `n8n-nodes-base.splitOut`
**Type** `n8n-nodes-base.splitOut` · **core**

**What:** Splits a single item containing a list/array field into one item per list element.

**Credentials:** none.

**Resources / Operations:** Single operation — split array field into items.

**Key params & gotchas:**
- **Field to Split Out**: the field containing the array. Use `$binary` expression for binary data inputs.
- **Include**: No Other Fields, All Other Fields, or Selected Other Fields (comma-separated field list).
- **Destination Field Name**: renames the split field in output items.
- **Disable Dot Notation**: prevents `parent.child` notation in field references.
- **Include Binary**: carry binary data from input into each output item.
- Inverse of Aggregate node's "All Item Data Into a Single List" mode.

**Source:** n8n-nodes-base.splitout.md  [doc-verified]
