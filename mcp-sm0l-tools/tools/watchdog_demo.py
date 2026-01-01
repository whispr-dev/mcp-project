from __future__ import annotations
import tempfile, time, pathlib

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
except ImportError:
    print("Missing dependency: watchdog. Install with: pip install watchdog")
    raise SystemExit(0)

class H(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            print("Modified:", event.src_path)

if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as d:
        p = pathlib.Path(d) / "demo.txt"
        p.write_text("hi")
        obs = Observer()
        h = H()
        obs.schedule(h, d, recursive=False)
        obs.start()
        try:
            for i in range(3):
                time.sleep(0.2)
                p.write_text(f"tick {i}")
            time.sleep(0.5)
        finally:
            obs.stop()
            obs.join()
