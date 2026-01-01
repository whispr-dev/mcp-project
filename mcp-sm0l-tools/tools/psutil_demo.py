"""psutil quick system stats"""

def main():
    try:
        import psutil
    except Exception as e:
        print("Missing dependency or import failed:", e)
        return
    print("cpu%", psutil.cpu_percent(interval=0.1))
print("mem%", psutil.virtual_memory().percent)


if __name__ == "__main__":
    main()
