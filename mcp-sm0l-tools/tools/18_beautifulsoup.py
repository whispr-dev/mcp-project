#!/usr/bin/env python3
"""BeautifulSoup: Defensive web scraping"""
from bs4 import BeautifulSoup
html = '<span class="price">$99</span>'
soup = BeautifulSoup(html, 'html.parser')
price = soup.select_one(".price").text
print("✓ BeautifulSoup: Always have fallback selectors")
