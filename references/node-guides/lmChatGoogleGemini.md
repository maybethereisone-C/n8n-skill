# Google Gemini Chat Model — `n8n-nodes-langchain.lmChatGoogleGemini`
**Type** `n8n-nodes-langchain.lmChatGoogleGemini` · **typeVersion** 1 · **ai**
**What:** Sub-node that provides Google Gemini chat models (via Google AI API) for AI Agents and chains.
**Credentials:** `googlePalmApi` (Google AI / Gemini API key)
**Resources / Operations:** No discrete operations — exposes a chat LLM connection point.
**Key params & gotchas:**
- **Model**: Dynamically loaded from Google Gemini API.
- **Safety Settings**: Gemini exposes adjustable content filters per harm category; adjust if the model over-refuses legitimate prompts.
- **No proxy support**: The node uses Google's SDK which ignores standard proxy env vars. Workaround: set a reverse proxy and change the **Host** in credentials to point at it.
- **Top K / Top P**: Both available; using both simultaneously is discouraged — pick one sampling strategy.
**Source:** n8n-nodes-langchain.lmchatgooglegemini.md  [doc-verified]
