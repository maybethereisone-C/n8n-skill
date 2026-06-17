# n8n Form — `n8n-nodes-base.form`
**Type** `n8n-nodes-base.form` · **core**

**What:** Adds pages to a multi-step form started by the n8n Form Trigger node; also used to end the form with a completion screen, redirect, or custom HTML.

**Credentials:** none.

**Resources / Operations:** Single operation — render a form page or form ending.

**Key params & gotchas:**
- Must be preceded by `n8n-nodes-base.formTrigger` in the workflow.
- **Page Type: Form Ending** terminates the form; only one Form Ending executes per run even with multiple branches.
- **On n8n Form Submission** options: Show Completion Screen, Redirect to URL, Show Text (full HTML/CSS/JS allowed here), Return Binary File.
- **Define Form → Using JSON** accepts a JSON array of field objects; supports `checkbox`, `date`, `dropdown`, `email`, `file`, `hiddenField`, `html`, `number`, `password`, `radio`, `text`, `textarea`.
- Query parameters (from the trigger URL) pre-populate fields on any page — production mode only.
- Custom HTML fields (`<script>`, `<style>`, `<input>` blocked except in Show Text ending).
- With mutually exclusive branches only one branch executes; with Switch sending to multiple branches, n8n runs them sequentially and only the last Form Ending page is shown.

**Source:** n8n-nodes-base.form.md  [doc-verified]
