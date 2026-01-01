#!/usr/bin/env python3
"""Optimization 6: Keep variables local"""
import timeit

x = 10

def compute_global():
    return [x * i for i in range(10_000)]

def compute_local():
    x = 10
    return [x * i for i in range(10_000)]

time_global = timeit.timeit(compute_global, number=10000)
time_local = timeit.timeit(compute_local, number=10000)

print(f"Global lookup: {time_global:.4f}s")
print(f"Local lookup: {time_local:.4f}s")
print(f"✓ Local variables: Faster (fixed array vs dict lookup)")
