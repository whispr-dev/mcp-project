#!/usr/bin/env python3
"""Tiny win 4: dataclass InitVar for init-only params"""
from dataclasses import dataclass, field, InitVar

def hash_password(p):
    return f"hashed-{p}"

@dataclass
class User:
    name: str
    raw_password: InitVar[str]
    hashed: str = field(init=False)

    def __post_init__(self, raw_password):
        self.hashed = hash_password(raw_password)

u = User("alice", "mysecret")
print(f"User: {u.name}")
print(f"Hashed password stored, raw password gone")
print("✓ InitVar: Secure, clean initialization")
