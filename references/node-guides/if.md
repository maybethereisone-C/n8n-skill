# If — `n8n-nodes-base.if`
**Type** `n8n-nodes-base.if` · **core**

**What:** Splits workflow into two branches (true/false) based on one or more conditions.

**Credentials:** none.

**Resources / Operations:** Single operation — conditional branch split.

**Key params & gotchas:**
- Two outputs: **true** (items meeting conditions) and **false** (items not meeting conditions).
- Conditions are typed (String, Number, Boolean, Date & Time, Array, Object).
- Multiple conditions: combine with AND (all must match) or OR (any must match); mixing AND/OR not supported.
- For more than two output branches use `n8n-nodes-base.switch`.
- When paired with a Merge node, n8n waits for both branches before merging — be aware of execution order implications with the If+Merge pattern.

**Source:** n8n-nodes-base.if.md  [doc-verified]
