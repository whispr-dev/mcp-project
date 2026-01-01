#!/usr/bin/env python3
"""Optimization 4: Profile before optimizing"""
import timeit
import cProfile
import pstats
from io import StringIO

def slow_function():
    total = 0
    for i in range(100_000):
        total += i ** 2
    return total

# Using timeit
time_taken = timeit.timeit(slow_function, number=100)
print(f"Function time: {time_taken:.4f}s per 100 runs")

# Using cProfile (uncomment to profile a script)
# cProfile.run('slow_function()')

print("✓ Profiling tools: timeit for snippets, cProfile for full programs")
