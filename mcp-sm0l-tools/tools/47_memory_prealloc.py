#!/usr/bin/env python3
"""Optimization 12: Preallocate lists"""
import timeit

# SLOW: Growing list
def append_slow():
    result = []
    for i in range(10000):
        result.append(i * 2)
    return result

# FAST: Preallocated
def append_fast():
    result = [0] * 10000
    for i in range(10000):
        result[i] = i * 2
    return result

time_slow = timeit.timeit(append_slow, number=100)
time_fast = timeit.timeit(append_fast, number=100)

print(f"Append loop: {time_slow:.4f}s")
print(f"Preallocated: {time_fast:.4f}s")
print("✓ Preallocation: Avoids repeated memory resizing")
