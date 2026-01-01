from __future__ import annotations
import sys, pathlib

try:
    import pdfplumber
except ImportError:
    print("Missing dependency: pdfplumber. Install with: pip install pdfplumber")
    raise SystemExit(0)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pdfplumber_demo.py <file.pdf>")
        raise SystemExit(0)
    path = pathlib.Path(sys.argv[1])
    with pdfplumber.open(str(path)) as pdf:
        page = pdf.pages[0]
        print("Pages:", len(pdf.pages))
        print("First page text (first 200 chars):")
        print((page.extract_text() or "")[:200])
