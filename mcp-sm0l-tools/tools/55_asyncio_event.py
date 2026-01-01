#!/usr/bin/env python3
"""Tiny win 5: asyncio.Event for task coordination"""
import asyncio

async def worker(done_event):
    print("Worker: Starting...")
    await asyncio.sleep(1)
    print("Worker: Done, signaling...")
    done_event.set()

async def main():
    done = asyncio.Event()
    asyncio.create_task(worker(done))
    await done.wait()
    print("Main: Resumed after signal")

print("asyncio.Event pattern:")
print("- No shared variables")
print("- No polling")
print("✓ Elegant async coordination")

# asyncio.run(main())  # Uncomment to run
