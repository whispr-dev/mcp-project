#!/usr/bin/env python3
"""Pendulum datetime example"""
import pendulum

# Current time
print(pendulum.now())

# Add days
print(pendulum.now().add(days=5).to_datetime_string())

# Timezone support
london = pendulum.now('Europe/London')
tokyo = pendulum.now('Asia/Tokyo')
print(f"London: {london}")
print(f"Tokyo: {tokyo}")

# Parse dates
date1 = pendulum.parse("2024-01-15")
date2 = pendulum.parse("2025-01-15")
print(f"Days between: {date2.diff(date1).days}")
