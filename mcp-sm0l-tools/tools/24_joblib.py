#!/usr/bin/env python3
"""joblib: Parallel computing"""
from joblib import Parallel, delayed
def task(n):
    return n*2
results = Parallel(n_jobs=4)(delayed(task)(i) for i in range(10))
print(f"Results: {results}")
print("✓ joblib: Multiprocessing without complexity")
