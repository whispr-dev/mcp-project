#!/usr/bin/env python3
"""Tiny win 8: sched.scheduler for portable scheduling"""
import sched, time

scheduler = sched.scheduler(time.time, time.sleep)

def task():
    print("Running scheduled task")
    scheduler.enter(5, 1, task)  # Reschedule

scheduler.enter(5, 1, task)

print("sched.scheduler:")
print("- No cron required")
print("- Cross-platform")
print("✓ Single file scheduling")

# scheduler.run()  # Uncomment to run
