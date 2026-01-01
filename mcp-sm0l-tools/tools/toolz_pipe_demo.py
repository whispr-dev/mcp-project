"""toolz.pipe demo"""

def main():
    try:
        from toolz import pipe
    except Exception as e:
        print("Missing dependency or import failed:", e)
        return
    print(pipe(3, lambda x: x+2, lambda x: x*10))

if __name__ == "__main__":
    main()
