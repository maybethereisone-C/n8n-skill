# Date & Time — `n8n-nodes-base.dateTime`

**Type** `n8n-nodes-base.dateTime` · **typeVersion** 2 · **core**

**What:** Manipulates and formats date/time values using Luxon under the hood.

**Credentials:** None.

**Resources / Operations:**

| Operation | What it does |
|-----------|-------------|
| Add to a Date | Add N time units to a date |
| Extract Part of a Date | Pull year/month/week/day/hour/minute/second |
| Format a Date | Convert to a preset or custom Luxon token format |
| Get Current Date | Return now (optionally with time) |
| Get Time Between Dates | Calculate difference in chosen units |
| Round a Date | Round up or down to nearest unit |
| Subtract From a Date | Subtract N time units from a date |

**Key params & gotchas:**
- All operations output to **Output Field Name** (you name it); enable **Include Input Fields** to pass all existing fields through alongside the new date field.
- **Format a Date → From Date Format**: set this if n8n misparses your input date (e.g., ambiguous `DD/MM/YYYY` vs `MM/DD/YYYY`). Uses Luxon tokens — case-sensitive.
- **Get Current Date → Timezone**: leave blank to use the n8n instance timezone; set explicitly (e.g., `Asia/Bangkok`) to override. Use `GMT` for UTC+0 (not `UTC`).
- **Use Workflow Timezone** option on Format: when on, interprets the input in the workflow's configured timezone rather than its embedded timezone.
- **Get Time Between Dates → Output as ISO String**: produces `P1Y3M13D` ISO 8601 duration format instead of separate numeric fields per unit.
- Custom format tokens are Luxon tokens (e.g., `yyyy-MM-dd'T'HH:mm:ss`) — tokens are case-sensitive (`MM` = month, `mm` = minute).

**Source:** n8n-nodes-base.datetime.md  [doc-verified]
