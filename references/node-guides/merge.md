# Merge — `n8n-nodes-base.merge`
**Type** `n8n-nodes-base.merge` · **core**

**What:** Combines data from two or more workflow branches once all branch data is available.

**Credentials:** none.

**Resources / Operations (Modes):**
| Mode | Description |
|------|-------------|
| Append | Concatenate items from all inputs in order |
| Combine → Matching Fields | Join by field value (inner/outer/left/right join semantics) |
| Combine → Position | Merge by index position |
| Combine → All Possible Combinations | Cartesian product / cross join |
| SQL Query | Write AlaSQL to join/filter inputs as `input1`, `input2`, etc. |
| Choose Branch | Output only Input 1, Input 2, or an empty item |

**Key params & gotchas:**
- **Append** supports more than 2 inputs (added in 1.49.0); older versions max at 2.
- **SQL Query** mode added in 1.49.0.
- **Combine → Matching Fields → Output Type**: Keep Matches (inner), Keep Non-Matches, Keep Everything (outer), Enrich Input 1 (left join), Enrich Input 2 (right join).
- **Clash Handling** option controls what happens when both inputs have the same field name.
- **Fuzzy Compare** treats `"3"` and `3` as equal.
- **Multiple Matches**: Include All Matches or First Match Only.
- Input 1 takes precedence for uneven item counts in position mode — extra Input 2 items are discarded unless **Include Any Unpaired Items** is enabled.
- The node always waits for all connected inputs before executing (synchronization point).

**Source:** n8n-nodes-base.merge.md  [doc-verified]
