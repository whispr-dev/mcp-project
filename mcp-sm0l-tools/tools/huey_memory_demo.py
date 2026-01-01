"""huey MemoryHuey task demo"""

def main():
    try:
        from huey import MemoryHuey
    except Exception as e:
        print("Missing dependency or import failed:", e)
        return
    h = MemoryHuey()
    @h.task()
    def add(a,b): return a+b
    r = add(2,3)
    print("result", r())

if __name__ == "__main__":
    main()
