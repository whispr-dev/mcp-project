import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def fetch_subset(url, selector, limit=20, user_agent="Mozilla/5.0 (Automation-Secrets)"):
    """Fetches a URL, extracts a subset of elements, and returns (text, href) tuples."""
    
    r = requests.get(url, timeout=25, headers={"User-Agent": user_agent})
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    out = []
    
    for el in soup.select(selector)[:limit]:
        text = " ".join(el.get_text(strip=True).split())
        href = el.get("href")
        href = urljoin(url, href) if href else url
        out.append((text, href))
        
    return out