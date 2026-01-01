#!/usr/bin/env python3
"""Fire CLI generation example"""
import fire

def greet(name="World"):
    return f"Hello {name}"

def calculate(operation, a, b):
    if operation == "add":
        return a + b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b if b != 0 else "Error: div by zero"
    return "Unknown operation"

class TextTools:
    def uppercase(self, text):
        return text.upper()

    def lowercase(self, text):
        return text.lower()

    def reverse(self, text):
        return text[::-1]

    def count_words(self, text):
        return len(text.split())

if __name__ == "__main__":
    fire.Fire({
        'greet': greet,
        'calc': calculate,
        'text': TextTools,
    })

# Usage: python fire_example.py greet --name=Alice
# Usage: python fire_example.py calc add 5 3
# Usage: python fire_example.py text uppercase "hello world"
