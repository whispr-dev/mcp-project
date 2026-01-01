#!/usr/bin/env python3
"""schedule: Simple task scheduling"""
import schedule, time
schedule.every().day.at("09:00").do(task)
schedule.every(10).minutes.do(task)
while True:
    schedule.run_pending()
    time.sleep(1)
print("✓ schedule: Cron-like without cron")
