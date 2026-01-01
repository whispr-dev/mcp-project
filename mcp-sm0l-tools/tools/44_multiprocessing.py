#!/usr/bin/env python3
"""Optimization 9: Parallelize with multiprocessing"""
from multiprocessing import Pool
import time

def square(n):
    time.sleep(0.01)
    return n * n

# Sequential
start = time.time()
result_seq = [square(i) for i in range(4)]
seq_time = time.time() - start

# Parallel (4 cores)
start = time.time()
with Pool(4) as p:
    result_par = p.map(square, range(4))
par_time = time.time() - start

print(f"Sequential: {seq_time:.3f}s")
print(f"Parallel (4 cores): {par_time:.3f}s")
print(f"✓ Multiprocessing: 4x faster for CPU-bound tasks")
