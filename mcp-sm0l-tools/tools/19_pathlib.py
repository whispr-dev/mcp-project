#!/usr/bin/env python3
"""pathlib: Modern file operations"""
from pathlib import Path
p = Path('.')
csv_files = list(p.glob('**/*.csv'))
print(f"Found {len(csv_files)} CSV files")
print("✓ pathlib: Cross-platform, chainable, readable")
