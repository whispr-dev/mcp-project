"""logfire minimal setup demo"""

def main():
    try:
        import logfire
    except Exception as e:
        print("Missing dependency or import failed:", e)
        return

    try:
        logfire.configure()
        logfire.info("hello from logfire")
        print("ok")
    except Exception as e:
        print("logfire runtime error:", e)

if __name__ == "__main__":
    main()
