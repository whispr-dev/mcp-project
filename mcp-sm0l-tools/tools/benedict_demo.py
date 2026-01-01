from __future__ import annotations

try:
    from benedict import benedict
except ImportError:
    print("Missing dependency: python-benedict. Install with: pip install python-benedict")
    raise SystemExit(0)

if __name__ == "__main__":
    d = benedict({"a": {"b": 1}})
    d["a.b"] = 2
    print(d)
    print("a.b =", d["a.b"])
