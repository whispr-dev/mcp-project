#!/usr/bin/env python3
"""IceCream debug printing example"""
from icecream import ic

# Basic debugging
x = 42
name = "Bob"
ic(x)
ic(name)

# Collections
ic([1, 2, 3])
ic({"key": "value", "count": 99})

# In expressions
result = ic(5 + 3)

# Function calls
def calculate(a, b):
    return a * b + a / b

ic(calculate(10, 5))
