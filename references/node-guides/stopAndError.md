# Stop And Error — `n8n-nodes-base.stopAndError`
**Type** `n8n-nodes-base.stopAndError` · **core**

**What:** Halts workflow execution and throws a custom error message or error object, useful for validation gates and error workflow integration.

**Credentials:** none.

**Resources / Operations:**
| Error Type | Param |
|-----------|-------|
| Error Message | Error Message (string) |
| Error Object | Error Object (JSON object with arbitrary error properties) |

**Key params & gotchas:**
- Causes the execution to fail — downstream nodes do not run.
- The thrown error is catchable by an [Error Trigger](/integrations/builtin/core-nodes/n8n-nodes-base.errortrigger.md) node in a separate error workflow.
- Use **Error Object** when you need structured error data (e.g., code, details) passed to the error workflow.
- Common pattern: place after an If node to enforce data validation contracts.

**Source:** n8n-nodes-base.stopanderror.md  [doc-verified]
