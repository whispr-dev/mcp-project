#!/usr/bin/env python3
"""Schedule job scheduling example"""
import schedule
import time

def job():
    print("Running task...")

def hourly_report():
    print("Hourly report generated")

def daily_backup():
    print("Daily backup completed")

if __name__ == "__main__":
    # Schedule jobs
    schedule.every(10).seconds.do(job)
    schedule.every().minute.do(hourly_report)
    schedule.every().day.at("10:30").do(daily_backup)

    print("Scheduler started - running for 60 seconds...")

    start = time.time()
    while time.time() - start < 60:
        schedule.run_pending()
        time.sleep(1)

    print("Scheduler stopped")
