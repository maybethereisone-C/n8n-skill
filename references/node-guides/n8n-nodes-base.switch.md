# Switch — `n8n-nodes-base.switch`

**Type** `n8n-nodes-base.switch` · **typeVersion** 3.4 · **core**

**What:** Routes each item to one or more outputs based on comparison rules or a computed index — multi-branch IF.

**Credentials:** none.

**Resources / Operations:**

| Mode | Description |
|---|---|
| Rules | Declarative comparison rules per output (data-type-aware) |
| Expression | Write an expression returning the output index number |

**Key params & gotchas:**

- **Rules mode** — each rule defines data type + comparator (equal, contains, startsWith, regex, after, etc.) and maps matching items to a numbered output. Outputs are 0-indexed.
- **Rename Output** — per-rule label shown on the canvas; purely cosmetic, doesn't affect routing.
- **Fallback Output** (Rules option) — items matching no rule go to `None` (dropped), `Extra Output` (new pin), or `Output 0`. Default is `None` (silent drop — easy to lose data).
- **Send data to all matching outputs** (Rules option) — OFF by default (first match wins); turn ON for fan-out when multiple rules can match.
- **Less Strict Type Validation** — allows n8n to coerce types before comparison (e.g. string `"5"` matches number `5`).
- **Expression mode** — set `Number of Outputs` and write an expression for `Output Index` that returns an integer `0..N-1`. Items landing outside the range are dropped silently.
- Unlike IF, Switch can have any number of outputs and items can be duplicated to multiple outputs when fan-out is enabled.

**Source:** n8n-nodes-base.switch.md  [doc-verified]
