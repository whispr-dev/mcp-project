#!/usr/bin/env python3
"""Tiny win 10: functools.cached_property for lazy loading"""
from functools import cached_property

class BigData:
    def __init__(self, source):
        self.source = source
        self.load_count = 0

    @cached_property
    def data(self):
        self.load_count += 1
        print(f"Loading heavy data... (load #{self.load_count})")
        return list(range(1_000_000))

b = BigData("file.csv")
print(f"Object created, no data loaded")
print(f"Accessing data first time...")
len(b.data)
print(f"Accessing data second time (no load)...")
len(b.data)
print("✓ cached_property: Lazy load, compute once")
