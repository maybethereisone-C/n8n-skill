# Evals — behavioral regression tests for the n8n skill

Format borrowed from `czlonkowski/n8n-skills` (Evaluation-Driven Development): each file is one real user query + a checklist of `expected_behavior` assertions the skill's answer must satisfy. These are **not** unit tests — there's no LLM call in the runner. An agent (or you) answers the `query` using this skill, then self-checks the answer against the checklist. They catch regressions when the skill's references drift.

## Run

```bash
python3 scripts/run-evals.py list                 # list all evals (id + query)
python3 scripts/run-evals.py show node-selection  # print one eval's full checklist
python3 scripts/run-evals.py --category security   # filter by category
python3 scripts/run-evals.py validate              # schema-check every eval file (CI gate; exit 1 on malformed)
```

## Schema

```jsonc
{
  "id": "kebab-case-id",
  "category": "node-selection | data-contract | credentials | resilience | errors | security | code | ai",
  "query": "the user prompt to answer with this skill",
  "ref": "references/<file>.md",          // where the skill encodes the answer
  "expected_behavior": [                   // measurable assertions; ALL must hold
    "Recommends the dedicated WhatsApp node, not HTTP Request",
    "Cites references/node-selection.md"
  ]
}
```

Add an eval whenever you add a gotcha to a reference — the eval is the proof the skill now teaches it.
