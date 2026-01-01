from __future__ import annotations

try:
    from faker import Faker
except ImportError:
    print("Missing dependency: faker. Install with: pip install faker")
    raise SystemExit(0)

if __name__ == "__main__":
    f = Faker()
    print(f.name(), "|", f.email(), "|", f.address().splitlines()[0])
