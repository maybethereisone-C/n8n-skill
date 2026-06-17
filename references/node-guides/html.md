# HTML — `n8n-nodes-base.html`
**Type** `n8n-nodes-base.html` · **core**

**What:** Generates HTML templates from workflow data, extracts content from HTML using CSS selectors, or converts data to an HTML table.

**Credentials:** none.

**Resources / Operations:**
| Operation | Notes |
|-----------|-------|
| Generate HTML template | Handlebars-style template with `{{}}` expressions; supports inline CSS and JS (not executed) |
| Extract HTML content | CSS selector scraping from JSON string or binary `.html` file |
| Convert to HTML table | Converts all input items to a `<table>` |

**Key params & gotchas:**
- **Extract HTML content → Return Value** options: Attribute (specify attribute name), HTML, Text, Value.
- **Return Array** returns multiple matches as an array vs. first-match string.
- **Skip Selectors** (Text mode) lets you exclude child elements from text extraction.
- **Generate HTML template** can introduce XSS — sanitize any untrusted input before using it in templates.
- Replaces the older `n8n-nodes-base.htmlExtract` node (deprecated at 0.213.0).

**Source:** n8n-nodes-base.html.md  [doc-verified]
