#!/usr/bin/env python3
"""Tiny win 2: coloredlogs for beautiful logs"""
import logging
try:
    import coloredlogs

    logger = logging.getLogger('myapp')
    coloredlogs.install(level='DEBUG', logger=logger,
                       fmt='%(asctime)s %(levelname)s %(message)s')

    logger.info("Application started")
    logger.warning("Something needs attention")
    logger.error("An error occurred")

    print("✓ Colored logs with timestamps, no config needed")
except ImportError:
    print("pip install coloredlogs")
