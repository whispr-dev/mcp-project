#!/usr/bin/env python3
"""Optimization 3: List comprehensions vs loops"""
import timeit

# SLOW: append loop
squares_slow = []
for i in range(10_000):
    squares_slow.append(i * i)

# FAST: comprehension
squares_fast = [i * i for i in range(10_000)]

time_loop = timeit.timeit(lambda: [i**2 for i in range(1000)], number=10000)
print(f"✓ List comprehensions: Pre-allocates memory ({time_loop:.4f}s)")
print(f"Lengths match: {len(squares_slow)} == {len(squares_fast)}")
