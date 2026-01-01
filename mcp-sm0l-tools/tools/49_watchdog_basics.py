#!/usr/bin/env python3
"""Watchdog: File system event monitoring"""
try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
    import time

    class Handler(FileSystemEventHandler):
        def on_created(self, event):
            if not event.is_directory:
                print(f"✓ New file: {event.src_path}")

        def on_modified(self, event):
            if not event.is_directory:
                print(f"✓ Modified: {event.src_path}")

        def on_deleted(self, event):
            if not event.is_directory:
                print(f"✓ Deleted: {event.src_path}")

    print("Watchdog ready - watching current directory")
    print("Uncomment to run:")
    print("""
    observer = Observer()
    observer.schedule(Handler(), ".", recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    """)
except ImportError:
    print("pip install watchdog")
