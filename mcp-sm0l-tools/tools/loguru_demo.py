from __future__ import annotations

try:
    from loguru import logger
except ImportError:
    print("Missing dependency: loguru. Install with: pip install loguru")
    raise SystemExit(0)

if __name__ == "__main__":
    logger.add("loguru_demo.log", rotation="10 KB")
    logger.info("hello from loguru")
    logger.warning("something to notice")
    print("Wrote loguru_demo.log")
