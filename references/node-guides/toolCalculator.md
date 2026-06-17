# Calculator — `@n8n/n8n-nodes-langchain.toolCalculator`
**Type** `@n8n/n8n-nodes-langchain.toolCalculator` · **typeVersion** 1 · **ai (sub-node / tool)**
**What:** Sub-node that gives an AI agent the ability to perform safe mathematical calculations, avoiding LLM arithmetic hallucinations.
**Credentials:** None.
**Resources / Operations:** Tool provider — connects to Tools Agent root nodes via `ai_tool` connection type.

**Key params & gotchas:**
- No configuration required — attach to any Tools Agent and the agent will call it automatically when math is needed.
- Evaluates expressions using mathjs — supports arithmetic, algebra, trig, unit conversion, and matrix operations.
- Use this whenever an agent workflow involves numerical computation — LLMs are unreliable at arithmetic without a calculator tool.

**Minimal example (wiring):**
```
[Tools Agent] ─── [OpenAI Chat Model]
              └── [Calculator]         ← attach as tool
```

**Source:** n8n-nodes-langchain.toolcalculator.md  [doc-verified]
