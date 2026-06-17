# Edit Fields (Set) — `n8n-nodes-base.set`
**Type** `n8n-nodes-base.set` · **core**

**What:** Sets, overrides, or adds fields on workflow items; can strip all other fields to produce clean output.

**Credentials:** none.

**Resources / Operations:** Single operation — set/edit fields.

**Key params & gotchas:**
- **Mode**: Manual Mapping (GUI drag-and-drop) or JSON Output (write raw JSON with expressions).
- **Keep Only Set Fields**: discards all input fields not explicitly set — use to produce minimal clean items.
- **Include in Output**: controls whether existing input fields are merged into output alongside set fields.
- **Support Dot Notation** (on by default): `name.one` creates nested `{ "name": { "one": ... } }`. Disable to treat dots as literal key characters.
- **Ignore Type Conversion Errors** (Manual Mapping only): silently skips type mismatch instead of erroring.
- **Include Binary Data**: whether to carry binary data through.
- In JSON Output mode, expressions use `{{ }}` syntax and arrays/objects are fully supported.

**Source:** n8n-nodes-base.set.md  [doc-verified]
