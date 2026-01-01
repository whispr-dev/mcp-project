#!/usr/bin/env python3
"""Tenacity retry logic example"""
from tenacity import retry, stop_after_attempt, wait_exponential
import random

@retry(stop=stop_after_attempt(3))
def flaky():
    print("Trying...")
    if random.random() < 0.7:
        raise ValueError("Random failure")
    return "Success!"

@retry(
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=1, min=1, max=10)
)
def network_call():
    print("Attempting network call...")
    if random.random() < 0.6:
        raise ConnectionError("Network error")
    return "Connected!"

if __name__ == "__main__":
    try:
        print(flaky())
    except:
        print("Failed after retries")

    try:
        print(network_call())
    except:
        print("Network failed after retries")
