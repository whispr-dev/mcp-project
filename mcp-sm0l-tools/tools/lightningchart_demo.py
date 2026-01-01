from __future__ import annotations
import os

try:
    import lightningchart as lc
except ImportError:
    print("Missing dependency: lightningchart. Install with: pip install lightningchart")
    raise SystemExit(0)

if __name__ == "__main__":
    print("LightningChart imported:", lc.__name__)
    if not os.getenv("LIGHTNINGCHART_LICENSE"):
        print("This library may require a license key to fully render charts.")
