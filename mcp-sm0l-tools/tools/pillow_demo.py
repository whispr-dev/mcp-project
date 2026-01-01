from __future__ import annotations
import io

try:
    from PIL import Image, ImageDraw
except ImportError:
    print("Missing dependency: pillow. Install with: pip install pillow")
    raise SystemExit(0)

if __name__ == "__main__":
    img = Image.new("RGB", (120, 80), "white")
    d = ImageDraw.Draw(img)
    d.rectangle([10,10,110,70], outline="black")
    d.text((20,30), "hi", fill="black")
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    print("Created in-memory PNG:", len(buf.getvalue()), "bytes")
