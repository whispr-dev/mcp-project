from __future__ import annotations
import logging

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")
    log = logging.getLogger("demo")
    log.info("hello")
    log.warning("this is a warning")
