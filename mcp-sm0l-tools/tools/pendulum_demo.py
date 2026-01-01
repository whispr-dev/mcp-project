from __future__ import annotations

try:
    import pendulum
except ImportError:
    print("Missing dependency: pendulum. Install with: pip install pendulum")
    raise SystemExit(0)

if __name__ == "__main__":
    now = pendulum.now("Asia/Tokyo")
    then = now.add(days=3, hours=5)
    print("Now :", now.to_iso8601_string())
    print("Then:", then.to_iso8601_string())
    print("Human:", now.diff_for_humans(then))
