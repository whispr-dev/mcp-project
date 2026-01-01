from __future__ import annotations

try:
    import pyinputplus as pyip
except ImportError:
    print("Missing dependency: pyinputplus. Install with: pip install pyinputplus")
    raise SystemExit(0)

if __name__ == "__main__":
    n = pyip.inputInt("Enter a small int (0-9): ", min=0, max=9)
    print("You entered:", n)
