"""APScheduler interval job (3 ticks)"""

def main():
    try:
        from apscheduler.schedulers.background import BackgroundScheduler
        import time
    except Exception as e:
        print("Missing dependency or import failed:", e)
        return
    n = {"c": 0}
def job():
    n["c"] += 1
    print("tick", n["c"])

s = BackgroundScheduler()
s.add_job(job, "interval", seconds=0.1)
s.start()
while n["c"] < 3:
    time.sleep(0.05)
s.shutdown()


if __name__ == "__main__":
    main()
