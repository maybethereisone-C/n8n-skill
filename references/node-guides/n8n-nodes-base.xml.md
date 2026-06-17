# XML — `n8n-nodes-base.xml`

**Type** `n8n-nodes-base.xml` · **typeVersion** 1 · **core**

**What:** Converts data between JSON and XML in either direction.

**Credentials:** none.

**Resources / Operations:**

| Mode | Description |
|---|---|
| JSON to XML | Serializes a JSON property to an XML string |
| XML to JSON | Parses an XML string property into a JSON object |

**Key params & gotchas:**

- **Property Name** — the field on the item that contains the data to convert (default `data`). The result overwrites that same field.
- **If XML is in a binary file** — use Extract from File node first to get a text string, then pipe into XML node.
- **Attribute Key** (option, default `$`) — prefix used to access XML attributes in the JSON representation. Change if your data uses `$` as a field name.
- **Character Key** (option, default `_`) — prefix for text content in mixed-content nodes.
- **JSON→XML options worth knowing:** `Headless` omits the `<?xml?>` declaration; `Root Name` sets the outer element; `Cdata` wraps text in `<![CDATA[...]]>` only when needed.
- **XML→JSON options worth knowing:** `Explicit Array` always wraps child nodes in arrays (safer for downstream `.map()` calls); `Ignore Attributes` drops all XML attributes; `Normalize Tags` lowercases tag names for consistent field access.

**Source:** n8n-nodes-base.xml.md  [doc-verified]
