# Alibaba Cloud Model Studio — `n8n-nodes-langchain.alibabacloud`
**Type** `n8n-nodes-langchain.alibabacloud` · **typeVersion** 1 · **action/ai**
**What:** Call Alibaba Cloud Qwen models for text completions, image analysis/generation, and video generation (text-to-video and image-to-video).
**Credentials:** `alibabaCloudApi` (API key from Alibaba Cloud Model Studio).

## Resources / Operations
| Resource | Operations |
|---|---|
| Text | Message a model (chat completion with Qwen) |
| Image | Analyze Image (vision-language), Generate an Image |
| Video | Generate Video from Text, Generate Video from Image |

## Key params & gotchas
- **Text → Message a model** supports optional web search (`enableSearch`), tool-calling iterations (`maxToolsIterations`), seed, stop sequences, and all standard sampling params.
- **Video generation** is async; the node polls until the video is ready or times out. Set `downloadVideo: true` to receive binary data; otherwise only the URL is returned.
- **Generate Video from Image** supports a "last frame" image (first-and-last-frame video) and a subject-reference face photo for facial consistency — model-specific features.
- Camera movements in video prompts use `[command]` syntax (e.g., `[Push in]`, `[Pan left]`).
- Resolution tiers for video: 720P or 1080P; duration 2–15 seconds.
- `promptExtend: true` auto-enhances prompts — disable if you need exact prompt adherence.
- `simplify: true` (default off) strips raw API envelope from response.

**Source:** n8n-nodes-langchain.alibabacloud.md  [doc-verified]
