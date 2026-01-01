#!/usr/bin/env python3
"""PyWhatKit automation example"""
import pywhatkit

# Note: These require proper setup/dependencies
# Image to ASCII art (requires Pillow)
try:
    pywhatkit.image_to_ascii_art("logo.png", "ascii.txt")
    print("ASCII art created")
except Exception as e:
    print(f"Image conversion skipped: {e}")

# QR code generation
try:
    pywhatkit.qr_code("https://github.com")
    print("QR code generated")
except Exception as e:
    print(f"QR generation skipped: {e}")

# Search on Google
try:
    pywhatkit.search("Python automation")
    print("Web search initiated")
except Exception as e:
    print(f"Search skipped: {e}")
