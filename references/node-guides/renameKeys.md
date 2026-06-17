# Rename Keys — `n8n-nodes-base.renameKeys`
**Type** `n8n-nodes-base.renameKeys` · **core**

**What:** Renames keys in JSON items — either by explicit old→new mapping or by regex pattern.

**Credentials:** none.

**Resources / Operations:** Single operation — rename keys.

**Key params & gotchas:**
- Add multiple rename pairs with **Add new key**; each pair specifies **Current Key Name** and **New Key Name**.
- **Regex option**: provide a Regular Expression and **Replace With** value; affects all matching keys including ones already renamed in the same pass.
- Regex options: **Case Insensitive**, **Max Depth** (`-1` = unlimited, `0` = top-level only).
- Warning: regex can unintentionally rename keys you've just renamed if they match the pattern.

**Source:** n8n-nodes-base.renamekeys.md  [doc-verified]
