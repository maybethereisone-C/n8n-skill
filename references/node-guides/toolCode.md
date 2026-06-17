# Custom Code Tool — `@n8n/n8n-nodes-langchain.toolCode`
**Type** `@n8n/n8n-nodes-langchain.toolCode` · **typeVersion** 1 · **ai (sub-node / tool)**
**What:** Sub-node that lets you write arbitrary JavaScript or Python code that an AI agent can invoke as a tool.
**Credentials:** None.
**Resources / Operations:** Tool provider — connects to Tools Agent root nodes via `ai_tool` connection type.

**Key params & gotchas:**
- **Description**: tells the agent when and how to call this tool — include what input format it expects (e.g., "comma-separated color names to exclude").
- **Language**: JavaScript or Python.
- **Code box**: the agent's input is available as the variable `query` (a string). Return the result value directly.
- The agent decides the value of `query` based on the Description — write the description to match how you parse `query` in code.
- For structured input (JSON), instruct the agent in the Description to pass JSON, then `JSON.parse(query)` in the code.
- Code runs in n8n's sandboxed VM — no filesystem access, no external network calls (use HTTP Request node for that), limited built-ins.

**Minimal example:**
```js
// Description: "Returns the lowercase version of the input string"
let myString = query;
return myString.toLowerCase();
```

**Source:** n8n-nodes-langchain.toolcode.md  [doc-verified]
