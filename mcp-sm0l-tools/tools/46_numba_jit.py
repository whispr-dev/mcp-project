#!/usr/bin/env python3
"""Optimization 11: Compile with Numba"""
try:
    from numba import jit
    import timeit

    @jit(nopython=True)
    def compute_sum(n):
        total = 0
        for i in range(n):
            total += i * i
        return total

    result = compute_sum(10_000_000)
    print(f"Result: {result}")
    print("✓ Numba JIT: 50-100x faster for numerical code")
except ImportError:
    print("pip install numba")
    print("✓ Numba: Compile Python to machine code")
