from __future__ import annotations
import time

try:
    import schedule
except ImportError:
    print("Missing dependency: schedule. Install with: pip install schedule")
    raise SystemExit(0)

count = 0

def job():
    global count
    count += 1
    print("tick", count)

if __name__ == "__main__":
    schedule.every(1).seconds.do(job)
    while count < 3:
        schedule.run_pending()
        time.sleep(0.1)
