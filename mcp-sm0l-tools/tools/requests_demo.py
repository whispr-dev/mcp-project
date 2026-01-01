from __future__ import annotations

try:
    import requests
except ImportError:
    print("Missing dependency: requests. Install with: pip install requests")
    raise SystemExit(0)

if __name__ == "__main__":
    try:
        r = requests.get("https://httpbin.org/ip", timeout=3)
        print("status:", r.status_code)
        print("json:", r.json())
    except Exception as e:
        print("Request failed (maybe offline):", e)
