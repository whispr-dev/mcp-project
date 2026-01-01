#!/usr/bin/env python3
"""Optimization 10: Choose efficient data structures"""

# SLOW: O(n) lookup in list
nums_list = list(range(10000))
result = 9999 in nums_list  # Checks all items

# FAST: O(1) lookup in set
nums_set = set(nums_list)
result = 9999 in nums_set  # Instant lookup

import timeit

time_list = timeit.timeit(lambda: 9999 in nums_list, number=100000)
time_set = timeit.timeit(lambda: 9999 in nums_set, number=100000)

print(f"List lookup: {time_list:.4f}s")
print(f"Set lookup: {time_set:.4f}s")
print("✓ Sets: O(1) vs lists O(n) for membership tests")
