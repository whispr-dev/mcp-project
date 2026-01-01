#!/usr/bin/env python3
"""httpx: Modern HTTP client"""
import httpx
print("Sync: with httpx.Client() as c: c.get(url)")
print("Async: async with httpx.AsyncClient() as c: await c.get(url)")
print("✓ httpx: requests + async support")
