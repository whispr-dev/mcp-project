#!/usr/bin/env python3
"""Loguru: Simple logging"""
try:
    from loguru import logger
    logger.info("Start")
    logger.warning("Caution")
    logger.error("Failed")
except:
    print("pip install loguru")
print("✓ loguru: No config, handles rotation automatically")
