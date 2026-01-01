from __future__ import annotations

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Missing dependency: beautifulsoup4. Install with: pip install beautifulsoup4")
    raise SystemExit(0)

html = "<html><body><h1>Hello</h1><ul><li>a</li><li>b</li></ul></body></html>"

if __name__ == "__main__":
    soup = BeautifulSoup(html, "html.parser")
    print("h1:", soup.h1.text)
    print("items:", [li.text for li in soup.select("li")])
