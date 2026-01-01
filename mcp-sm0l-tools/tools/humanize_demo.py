from __future__ import annotations
import datetime as dt

try:
    import humanize
except ImportError:
    print("Missing dependency: humanize. Install with: pip install humanize")
    raise SystemExit(0)

if __name__ == "__main__":
    print("Size:", humanize.naturalsize(12345678))
    print("Time:", humanize.naturaltime(dt.datetime.now() - dt.timedelta(hours=5)))
