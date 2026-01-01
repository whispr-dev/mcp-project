#!/usr/bin/env python3
"""Tiny win 1: toolz.pipe for readable pipelines"""
try:
    from toolz import pipe

    def clean(data):
        return [x.strip() for x in data]

    def filter_out(data):
        return [x for x in data if x]

    def to_int(data):
        return list(map(int, data))

    raw = [" 1 ", "", " 2 ", "3"]
    result = pipe(raw, clean, filter_out, to_int)
    print(f"✓ Pipe result: {result}")
    print("Reads like English, no nested calls")
except ImportError:
    print("pip install toolz")
