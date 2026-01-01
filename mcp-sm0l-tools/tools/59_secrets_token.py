#!/usr/bin/env python3
"""Tiny win 9: secrets for cryptographically random tokens"""
import secrets
import string

def gen_secure_token(length=16):
    alphabet = string.ascii_letters + string.digits + "-_"
    return ''.join(secrets.choice(alphabet) for _ in range(length))

token = gen_secure_token(32)
print(f"Secure token: {token}")
print("✓ secrets: Unpredictable, better than random")
