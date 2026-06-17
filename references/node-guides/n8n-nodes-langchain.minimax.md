# MiniMax — `n8n-nodes-langchain.minimax`
**Type** `n8n-nodes-langchain.minimax` · **typeVersion** 1 · **action/ai**
**What:** Call MiniMax AI models for text-to-speech synthesis, image generation, LLM chat, and video generation (text-to-video and image-to-video).
**Credentials:** `minimaxApi` (API key from platform.minimax.io).

## Resources / Operations
| Resource | Operations |
|---|---|
| Audio | Text to Speech |
| Image | Generate an Image |
| Text | Message a Model |
| Video | Generate Video from Text, Generate Video from Image |

## Key params & gotchas
- **Text to Speech**: max 10,000 characters; supports pitch (–12 to 12), speed (0.5–2), volume (0.1–10), emotion, and language boost. WAV output only available in non-streaming mode.
- **Image Generation**: up to 9 images per request; aspect ratio options include 1:1, 16:9, 9:16, 4:3, and 21:9. `promptOptimizer` is off by default.
- **Message a Model**: `hideThinking: true` strips chain-of-thought from response by default. `maxToolsIterations` defaults to 15; set to 0 for unlimited.
- **Video from Image**: supports first-and-last-frame generation (`lastFrameImageUrl`/`lastFrameBinaryPropertyName`) and subject-reference face photo for facial consistency — MiniMax-Hailuo-2.3 only.
- Camera movements use `[command]` syntax in video prompts (e.g., `[Push in]`, `[Zoom in]`).
- `downloadVideo: true` / `downloadImage: true` (default) returns binary data; disable to get URL only.

**Source:** n8n-nodes-langchain.minimax.md  [doc-verified]
