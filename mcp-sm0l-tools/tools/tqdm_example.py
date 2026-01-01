#!/usr/bin/env python3
"""Tqdm progress bar example"""
from tqdm import tqdm
import time

# Simple iteration with progress
for i in tqdm(range(1000000)):
    pass

# With description
for item in tqdm(['a', 'b', 'c', 'd'], desc="Processing"):
    time.sleep(0.5)

# With custom bar
print("\nCustom progress bar:")
for i in tqdm(range(100), ncols=80, colour='green'):
    time.sleep(0.05)
