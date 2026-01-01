#!/usr/bin/env python3
"""Requests: Production HTTP with retries"""
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
def session():
    s = requests.Session()
    r = Retry(total=3, backoff_factor=0.3, status_forcelist=(500,502,504))
    a = HTTPAdapter(max_retries=r)
    s.mount('http://', a)
    s.mount('https://', a)
    return s
print("✓ requests with exponential backoff")
