#!/usr/bin/env python3
"""Tiny win 7: dataclass.replace for immutable objects"""
from dataclasses import dataclass, replace

@dataclass(frozen=True)
class Config:
    host: str
    port: int

cfg1 = Config("localhost", 8080)
cfg2 = replace(cfg1, port=9090)

print(f"Config 1: {cfg1}")
print(f"Config 2: {cfg2}")
print("✓ replace(): Clone + modify without side effects")
