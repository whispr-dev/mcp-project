from __future__ import annotations

try:
    from fuzzywuzzy import fuzz, process
except ImportError:
    print("Missing dependency: fuzzywuzzy. Install with: pip install fuzzywuzzy")
    print("Optional speedup: pip install python-Levenshtein")
    raise SystemExit(0)

choices = ["kitten", "sitting", "knitting", "bitten"]

if __name__ == "__main__":
    print("ratio(kitten,sitting):", fuzz.ratio("kitten", "sitting"))
    print("best for 'kittn':", process.extractOne("kittn", choices))
