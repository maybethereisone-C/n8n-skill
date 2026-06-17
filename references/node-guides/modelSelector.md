# Model Selector — `n8n-nodes-langchain.modelSelector`
**Type** `n8n-nodes-langchain.modelSelector` · **typeVersion** 1 · **ai**
**What:** Sub-node that dynamically selects one of several connected LLMs at runtime based on conditional rules.
**Credentials:** none
**Resources / Operations:** No discrete operations — routes to one of N attached LLM sub-nodes.
**Key params & gotchas:**
- **Number of Inputs**: Sets how many LLM sub-nodes can be attached (each maps to an input slot).
- **Rules**: Evaluated sequentially — first matching rule wins. Order matters; place most specific rules first.
- Use cases: cost-based routing (cheap model for simple tasks, expensive for complex), fallback on error, A/B model testing within a workflow.
- Does not retry failed models automatically — pair with error handling nodes for resilience.
**Source:** n8n-nodes-langchain.modelselector.md  [doc-verified]
