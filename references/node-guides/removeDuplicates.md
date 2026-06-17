# Remove Duplicates — `n8n-nodes-base.removeDuplicates`
**Type** `n8n-nodes-base.removeDuplicates` · **core**

**What:** Removes duplicate items from the input based on field values or across executions.

**Credentials:** none.

**Resources / Operations:** Single operation — deduplicate items.

**Key params & gotchas:** [schema-only — templates doc skipped, no detailed param doc in batch]
- Can deduplicate within a single execution (compare item fields) or across executions (using persisted state).
- Cross-execution deduplication requires a database/storage backend to track seen values.

**Source:** n8n-nodes-base.removeduplicates/templates-and-examples.md  [schema-only]
