"""schedule-based demo cleanup (safe temp sandbox)."""

import tempfile, pathlib, time

def main():
    try:
        import schedule
    except Exception as e:
        print("Missing dependency or import failed:", e); return

    base = pathlib.Path(tempfile.mkdtemp())
    old = base/"old.tmp"; new = base/"new.tmp"
    old.write_text("x", encoding="utf-8")
    new.write_text("y", encoding="utf-8")

    # simulate 'old' by backdating mtime
    old_m = time.time() - 3600
    os_utime = getattr(os, "utime", None)
    if os_utime:
        os.utime(old, (old_m, old_m))

    def run_cleanup():
        cutoff = time.time() - 60  # 1 minute
        removed = 0
        for p in base.glob("*.tmp"):
            if p.stat().st_mtime < cutoff:
                p.unlink(); removed += 1
        print("removed", removed)

    schedule.every(0.1).seconds.do(run_cleanup)
    ticks = 0
    while ticks < 3:
        schedule.run_pending()
        time.sleep(0.05)
        ticks += 1

    print("remaining", [p.name for p in base.glob("*.tmp")])

if __name__ == "__main__":
    import os
    main()
