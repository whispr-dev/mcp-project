#!/usr/bin/env python3
"""Tiny win 3: contextlib.suppress for clean error handling"""
from contextlib import suppress
import os
import tempfile

# Instead of try/except: pass
with tempfile.TemporaryDirectory() as tmpdir:
    filepath = os.path.join(tmpdir, "temp.txt")
    open(filepath, 'w').close()

    with suppress(FileNotFoundError):
        os.remove(filepath)
        print("File removed")

    with suppress(FileNotFoundError):
        os.remove(filepath)  # Already gone, no error

    print("✓ suppress(): Clean, readable intent")
