# Edit Image — `n8n-nodes-base.editImage`

**Type** `n8n-nodes-base.editImage` · **typeVersion** 1 · **core**

**What:** Manipulates binary image data — blur, border, composite, create, crop, draw, resize, rotate, shear, add text, make color transparent, or chain multiple ops.

**Credentials:** None.

**Resources / Operations:**

| Operation | Key Params |
|-----------|-----------|
| Blur | Property Name, Blur (0-1000), Sigma (0-1000) |
| Border | Property Name, Width, Height, Color |
| Composite | Property Name (base), Composite Image Property (overlay), Operator, Position X/Y |
| Create | Property Name, Background Color, Width, Height |
| Crop | Property Name, Width, Height, Position X/Y |
| Draw | Property Name, Primitive (Circle/Line/Rectangle), Color, Start/End X/Y, Corner Radius |
| Get Information | Property Name → returns metadata |
| Multi Step | Property Name + ordered list of sub-operations |
| Resize | Property Name, Width, Height, Option (aspect ratio handling) |
| Rotate | Property Name, Degrees (-360 to 360), Background Color |
| Shear | Property Name, Degrees X, Degrees Y |
| Text | Property Name, Text, Font Size, Font Color, Position X/Y, Max Line Length |
| Transparent | Property Name, Color to make transparent |

**Key params & gotchas:**
- **Requires GraphicsMagick** installed on the host if not running on Docker (n8n's official Docker image includes it).
- Image must arrive as binary data via **Property Name** — upstream node (HTTP Request, Read File, etc.) must put the image in a binary property first.
- **Multi Step**: use this to chain multiple operations in sequence without multiple Edit Image nodes — avoids multiple binary decode/encode cycles.
- **Composite → Operator**: "Over" is the standard alpha compositing; other operators (Multiply, Difference, etc.) produce blending effects.
- **Resize → Option**: "Maximum Area" and "Minimum Area" respect aspect ratio within bounds; "Percent" uses width/height as percentage multipliers.
- **Node options → Format**: output as bmp, gif, jpeg, png, tiff, or WebP — set explicitly when format conversion is needed.
- **Text operation** also has a **Font Name or ID** option in node options.

**Source:** n8n-nodes-base.editimage.md  [doc-verified]
