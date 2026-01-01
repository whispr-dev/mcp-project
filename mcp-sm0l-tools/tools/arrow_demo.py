from __future__ import annotations

try:
    import arrow
except ImportError:
    print("Missing dependency: arrow. Install with: pip install arrow")
    raise SystemExit(0)

if __name__ == "__main__":
    now = arrow.now("Asia/Tokyo")
    print("Now:", now)
    print("In 90 min:", now.shift(minutes=90).humanize(now))
