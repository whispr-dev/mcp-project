#!/usr/bin/env python3
"""Tiny win 6: Check dependency versions at runtime"""
from importlib.metadata import version, PackageNotFoundError

try:
    v = version("requests")
    print(f"requests version: {v}")
    if v < "2.25.0":
        print("⚠ Warning: requests too old, upgrade recommended")
    else:
        print("✓ Version OK")
except PackageNotFoundError:
    print("⚠ requests not installed")
