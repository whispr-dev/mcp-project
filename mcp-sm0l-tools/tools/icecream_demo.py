from __future__ import annotations

try:
    from icecream import ic
except ImportError:
    print("Missing dependency: icecream. Install with: pip install icecream")
    raise SystemExit(0)

if __name__ == "__main__":
    x = 3
    ic(x, x ** 2, {"ok": True})
