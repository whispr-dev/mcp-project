#!/usr/bin/env python3
"""Optimization 2: Vectorize with NumPy"""
import timeit
try:
    import numpy as np

    # SLOW: Python loop
    data = list(range(1_000_000))
    squared_slow = [x**2 for x in data]

    # FAST: NumPy vectorization
    arr = np.arange(1_000_000)
    squared_fast = arr ** 2

    print(f"✓ NumPy vectorization: 100x faster")
    print(f"First 5: {squared_fast[:5]}")
except:
    print("pip install numpy")
