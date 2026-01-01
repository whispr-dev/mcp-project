#!/usr/bin/env python3
"""Optimization 1: Use built-in functions (C-speed)"""
import timeit

# SLOW: Manual loop
nums = list(range(1_000_000))
total_slow = 0
for n in nums:
    total_slow += n

# FAST: Built-in sum()
total_fast = sum(nums)

print(f"Manual loop: {total_slow}")
print(f"sum(): {total_fast}")

# Benchmark
slow_time = timeit.timeit(lambda: sum([n for n in range(100000)]), number=10)
print(f"✓ Built-in functions: C-speed execution ({slow_time:.4f}s)")
