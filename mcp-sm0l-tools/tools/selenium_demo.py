from __future__ import annotations
import sys

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
except ImportError:
    print("Missing dependency: selenium. Install with: pip install selenium")
    raise SystemExit(0)

if __name__ == "__main__":
    opts = Options()
    opts.add_argument("--headless=new")
    try:
        d = webdriver.Chrome(options=opts)
    except Exception as e:
        print("Chrome driver not available:", e)
        print("Install a compatible driver or use Selenium Manager.")
        raise SystemExit(0)
    try:
        d.get("https://example.com")
        print("title:", d.title)
    finally:
        d.quit()
