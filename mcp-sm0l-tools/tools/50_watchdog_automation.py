#!/usr/bin/env python3
"""Watchdog: File processing automation"""
try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
    import os, time, shutil

    class AutoProcessor(FileSystemEventHandler):
        def on_created(self, event):
            if event.src_path.endswith('.csv'):
                self.process_csv(event.src_path)

        def process_csv(self, filepath):
            print(f"Processing CSV: {filepath}")
            # Your logic here
            dest = filepath.replace('.csv', '_processed.csv')
            shutil.copy(filepath, dest)
            print(f"✓ Saved to {dest}")

    print("✓ Watchdog automation: Instant file reactions")
    print("Real-time instead of scheduled polling")

except ImportError:
    print("pip install watchdog")
