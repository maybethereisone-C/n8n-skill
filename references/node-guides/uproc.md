# uProc — `n8n-nodes-base.uproc`
**Type** `n8n-nodes-base.uproc` · **typeVersion** 1 · **action**
**What:** Run any of uProc's 700+ data-processing tools across audio, communication, company, finance, geography, image, internet, personal, product, security, and text categories.
**Credentials:** `uprocApi` (email + API key from uProc dashboard).
**Resources / Operations:**
| Resource | Key tool examples |
|----------|-------------------|
| Audio | TTS audio file generation |
| Communication | Email validation, phone validation/HLR, LinkedIn extraction, SMS send |
| Company | Enrich by domain/email/name/IP, find decision makers |
| Finance | IBAN/BIC/currency validation, VAT lookup, currency conversion |
| Geographical | Geocoding, reverse geocoding, distance calculation, IP geolocation |
| Image | QR encode/decode, OCR, screenshot, barcode |
| Internet | Domain/URL checks, WHOIS, SSL, DNS, tech detection |
| Personal | Age/gender/name enrichment, LinkedIn URI lookup, fake data gen |
| Product | ISBN/EAN/ASIN/UPC/VIN lookups and validation |
| Security | Password strength, Luhn, UUID, domain/IP blacklists |
| Text | String manipulation, sentiment analysis, translate, MD5/SHA/Base64 |

**Key params & gotchas:**
- Each tool call is a separate API request; high-volume workflows will accumulate credits fast.
- Spanish-specific tools (Robinson list, CIF/NIF/DNI validation, ZIP codes) only work for Spain.
- LinkedIn automation tools (profile extract, connection send) operate via uProc's own session — may be subject to LinkedIn ToS.
- The node presents a flat tool selector; search by category + keyword in the UI.

**Source:** n8n-nodes-base.uproc.md  [doc-verified]
