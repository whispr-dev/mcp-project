from __future__ import annotations

try:
    import httpx
except ImportError:
    print("Missing dependency: httpx. Install with: pip install httpx")
    raise SystemExit(0)

if __name__ == "__main__":
    url = "https://httpbin.org/get"
    try:
        r = httpx.get(url, timeout=3.0)
        print("status:", r.status_code)
        print("origin:", r.json().get("origin"))
    except Exception as e:
        print("Request failed (maybe offline):", e)
