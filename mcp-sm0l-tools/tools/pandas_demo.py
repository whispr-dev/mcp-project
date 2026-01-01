from __future__ import annotations

try:
    import pandas as pd
except ImportError:
    print("Missing dependency: pandas. Install with: pip install pandas")
    raise SystemExit(0)

if __name__ == "__main__":
    df = pd.DataFrame({"x": [1,2,3], "y": [10,20,30]})
    print(df.assign(z=df.x * df.y).to_string(index=False))
