# n8n Form Trigger — `n8n-nodes-base.formTrigger`
**Type** `n8n-nodes-base.formTrigger` · **trigger**

**What:** Starts a workflow when a user submits an n8n-hosted form; generates the form page automatically.

**Credentials:** Basic Auth (optional) or none.

**Resources / Operations:** Trigger only.

**Key params & gotchas:**
- Two URLs: **Test URL** (active while editor open) and **Production URL** (active when workflow published). Switch before going live.
- **Form Path** sets a custom slug (replaces auto-generated UUID).
- **Respond When**: `Form Is Submitted` (immediate) or `Workflow Finishes` (waits for execution; errors surface to user).
- Element types: Checkboxes, Custom HTML, Date, Dropdown, Email, File, Hidden Field, Number, Password, Radio Buttons, Text, Textarea.
- Allowed HTML in Form Description and Custom HTML elements: standard formatting tags only; `<script>`, `<style>`, `<input>` are stripped.
- Query parameters pre-populate field defaults — production mode only; percent-encode special characters.
- **Ignore Bots** option filters crawlers and link previewers.
- **Use Workflow Timezone** affects `submittedAt` timestamp in output (default is UTC).
- Add multi-page forms with subsequent `n8n-nodes-base.form` nodes.

**Source:** n8n-nodes-base.formtrigger.md  [doc-verified]
