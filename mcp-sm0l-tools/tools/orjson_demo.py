from __future__ import annotations

try:
    import orjson
except ImportError:
    print("Missing dependency: orjson. Install with: pip install orjson")
    raise SystemExit(0)

if __name__ == "__main__":
    data = {"n": 1, "items": [1, 2, 3], "ok": True}
    b = orjson.dumps(data)
    print("bytes:", b)
    print("roundtrip:", orjson.loads(b))
