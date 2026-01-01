from __future__ import annotations

try:
    from pywhat import identifier
except ImportError:
    print("Missing dependency: pywhat. Install with: pip install pywhat")
    raise SystemExit(0)

if __name__ == "__main__":
    samples = [
        "test@example.com",
        "550e8400-e29b-41d4-a716-446655440000",
        "1BoatSLRHtKNngkdXEeobR76b53LETtpyT",
    ]
    for s in samples:
        print(s, "->", identifier(s)[:1])
