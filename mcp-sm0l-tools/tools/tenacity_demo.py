from __future__ import annotations
import random, time

try:
    from tenacity import retry, stop_after_attempt, wait_fixed, before_log
except ImportError:
    print("Missing dependency: tenacity. Install with: pip install tenacity")
    raise SystemExit(0)

import logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger("tenacity_demo")

@retry(stop=stop_after_attempt(5), wait=wait_fixed(0.2), before=before_log(log, logging.INFO))
def flaky() -> str:
    if random.random() < 0.7:
        raise RuntimeError("nope")
    return "ok!"

if __name__ == "__main__":
    t0 = time.time()
    try:
        print("Result:", flaky())
    except Exception as e:
        print("Failed after retries:", e)
    print("Elapsed:", round(time.time()-t0, 3), "s")
