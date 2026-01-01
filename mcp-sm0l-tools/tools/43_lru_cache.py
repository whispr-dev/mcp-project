#!/usr/bin/env python3
"""Optimization 8: Cache with lru_cache"""
from functools import lru_cache
import timeit

# WITHOUT cache (slow on recursion)
def fib_slow(n):
    if n < 2:
        return n
    return fib_slow(n-1) + fib_slow(n-2)

# WITH cache (fast)
@lru_cache(maxsize=None)
def fib_fast(n):
    if n < 2:
        return n
    return fib_fast(n-1) + fib_fast(n-2)

# Test small values to avoid long wait
result = fib_fast(30)
print(f"fib(30) = {result}")
print(f"✓ lru_cache: Hundreds of times faster on recursive functions")
