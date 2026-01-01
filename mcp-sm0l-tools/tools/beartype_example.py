#!/usr/bin/env python3
"""Beartype runtime type checking example"""
from beartype import beartype

@beartype
def add(a: int, b: int) -> int:
    return a + b

@beartype
def greet(name: str, age: int) -> str:
    return f"Hello {name}, you are {age} years old"

@beartype
def process_list(items: list[int]) -> int:
    return sum(items)

if __name__ == "__main__":
    # Valid calls
    print("✓", add(5, 3))
    print("✓", greet("Alice", 30))
    print("✓", process_list([1, 2, 3, 4, 5]))

    # This will catch type error
    try:
        print(add(1, "2"))
    except Exception as e:
        print(f"✗ Caught: {type(e).__name__}")
