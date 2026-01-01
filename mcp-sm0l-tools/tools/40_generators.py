#!/usr/bin/env python3
"""Optimization 5: Generators for memory efficiency"""
import sys

# MEMORY HOG: Full list
nums_list = [i for i in range(10_000_000)]
print(f"List memory: {sys.getsizeof(nums_list) / 1024:.1f} KB (estimated)")

# MEMORY EFFICIENT: Generator
nums_gen = (i for i in range(10_000_000))
print(f"Generator memory: {sys.getsizeof(nums_gen) / 1024:.1f} KB")

# Generators yield one at a time
for i, val in enumerate(nums_gen):
    if i >= 5:
        break
    print(f"  {val}")

print("✓ Generators: Lower RAM, faster on large inputs")
