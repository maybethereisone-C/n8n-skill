# Aggregate — `n8n-nodes-base.aggregate`

**Type** `n8n-nodes-base.aggregate` · **typeVersion** 1 · **core**

**What:** Collects multiple input items (or fields within them) and groups them into a single output item — the inverse of Split Out.

**Credentials:** None.

**Resources / Operations:**

| Aggregate Mode | What it does |
|----------------|-------------|
| Individual Fields | Collects values of a named field across all items into an array |
| All Item Data | Collects entire items into a single list field |

**Key params & gotchas:**
- **Individual Fields → Rename Field**: when aggregating multiple fields you *must* provide output field names for each — leaving them blank causes an error.
- **Merge Lists**: if the field already contains arrays, turn this on to get a flat array instead of array-of-arrays.
- **Keep Missing And Null Values**: by default null/missing values are silently dropped; turn on to preserve nulls as empty entries (important for index-aligned downstream processing).
- **Disable Dot Notation**: turn on if field names literally contain dots (e.g., `a.b` as a key, not a nested path).
- **All Item Data → Include**: use "Specified Fields" or "All Fields Except" to slim down the payload before aggregating.

**Minimal example:**
```
# Collect all "email" fields from N items into one item
Aggregate: Individual Fields
Input Field Name: email
Output Field Name: emails
→ Output: { "emails": ["a@x.com", "b@x.com", ...] }
```

**Source:** n8n-nodes-base.aggregate.md  [doc-verified]
