from __future__ import annotations
import sys

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("Missing dependency: playwright. Install with: pip install playwright")
    print("Then install browsers: playwright install")
    raise SystemExit(0)

if __name__ == "__main__":
    url = "https://example.com"
    with sync_playwright() as p:
        b = p.chromium.launch(headless=True)
        page = b.new_page()
        try:
            page.goto(url, timeout=5000)
            print("Title:", page.title())
        except Exception as e:
            print("Navigation failed:", e)
        finally:
            b.close()
