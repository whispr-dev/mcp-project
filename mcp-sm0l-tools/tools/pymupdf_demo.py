from __future__ import annotations
import sys, pathlib

try:
    import fitz  # PyMuPDF
except ImportError:
    print("Missing dependency: pymupdf. Install with: pip install pymupdf")
    raise SystemExit(0)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pymupdf_demo.py <file.pdf>")
        raise SystemExit(0)
    doc = fitz.open(sys.argv[1])
    print("Pages:", doc.page_count)
    page = doc[0]
    print("First page text (first 200 chars):")
    print(page.get_text()[:200])
    doc.close()
