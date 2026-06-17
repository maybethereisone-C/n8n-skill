# Filter — `n8n-nodes-base.filter`
**Type** `n8n-nodes-base.filter` · **core**

**What:** Passes items downstream only when they satisfy one or more conditions; non-matching items are dropped.

**Credentials:** none.

**Resources / Operations:** Single implicit operation — filter items by conditions.

**Key params & gotchas:**
- Conditions are typed (String, Number, Boolean, Date & Time, Array, Object) — pick data type first, then comparison operator.
- Multiple conditions combine with AND or OR; mixing AND/OR in one node is not supported.
- **Ignore Case** option for string comparisons.
- **Less Strict Type Validation** auto-coerces types — useful when facing "wrong type:" errors.
- Items that fail all conditions are silently dropped (not routed to a second output). Use the If node when you need both branches.

**Source:** n8n-nodes-base.filter.md  [doc-verified]
