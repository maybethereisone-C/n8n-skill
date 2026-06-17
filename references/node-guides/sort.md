# Sort — `n8n-nodes-base.sort`
**Type** `n8n-nodes-base.sort` · **core**

**What:** Sorts a list of items by field value, randomly, or via custom JavaScript comparator.

**Credentials:** none.

**Resources / Operations:** Single operation — sort items.

**Key params & gotchas:**
- **Type**: Simple (field-based ascending/descending), Random (shuffle), Code (custom JS comparator).
- **Simple**: add multiple fields with **Add Field To Sort By**; each has Ascending/Descending toggle. **Disable Dot Notation** option available.
- **Code**: enter JavaScript sort function body — good for multi-key or computed sorts.
- Uses JavaScript's default `Array.sort` semantics (elements coerced to strings for comparison in Simple mode) — be aware of numeric string ordering (`"10" < "9"` lexicographically).

**Source:** n8n-nodes-base.sort.md  [doc-verified]
