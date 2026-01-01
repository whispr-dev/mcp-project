from __future__ import annotations

try:
    import pytesseract
    from PIL import Image
except ImportError:
    print("Missing dependencies: pytesseract, pillow. Install with: pip install pytesseract pillow")
    raise SystemExit(0)

if __name__ == "__main__":
    print("pytesseract version:", getattr(pytesseract, "__version__", "unknown"))
    print("This library also requires the Tesseract OCR engine installed on your system.")
