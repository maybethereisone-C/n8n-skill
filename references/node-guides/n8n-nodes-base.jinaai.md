# Jina AI — `n8n-nodes-base.jinaai`
**Type** `n8n-nodes-base.jinaai` · **typeVersion** 1 · **action**
**What:** Fetch and convert web content to LLM-friendly markdown, perform web searches, and run deep research reports using Jina AI's Reader/Search/Research APIs.
**Credentials:** `jinaAiApi` (API key).

## Resources / Operations
| Resource | Operations |
|---|---|
| Reader | Read (URL → clean markdown), Search (web search → clean results) |
| Research | Deep Research (topic → structured research report) |

## Key params & gotchas
- **Reader→Read** calls `r.jina.ai/<url>` and returns clean markdown — ideal for feeding web pages into LLM nodes without HTML noise.
- **Reader→Search** calls `s.jina.ai` and returns top web results as LLM-friendly text — similar to a Tavily search but returns Jina-processed content.
- **Research→Deep Research** generates a full multi-source research report on a topic — can take significant time (tens of seconds); set workflow timeout accordingly.
- All operations consume Jina AI API credits; free tier has rate limits.
- Output is text/markdown — connect directly to AI Agent or LLM nodes.

**Source:** n8n-nodes-base.jinaai.md  [doc-verified]
