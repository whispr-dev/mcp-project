#!/usr/bin/env python3
"""Pydantic: Data validation"""
from pydantic import BaseModel, Field
class User(BaseModel):
    id: int
    email: str
    age: int = Field(..., ge=0, le=150)
user = User(id=1, email="a@b.com", age=30)
print(f"Valid user: {user}")
print("✓ pydantic: Type checking + validation")
