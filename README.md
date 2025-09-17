# pdf2text_ai

Convert scanned/image-based PDFs into plain text using OCR.

## Features
- GPU-accelerated OCR with [Surya](https://github.com/datalab-to/surya-ocr)
- Handles two-page spreads or single pages
- Filters out footnotes (bottom margin)
- Outputs clean `output.txt`

## Setup
1. Create a virtual environment (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate   # or venv\Scripts\activate on Windows
