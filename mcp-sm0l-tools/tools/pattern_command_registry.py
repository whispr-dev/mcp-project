"""Command registry pattern (stdlib-only)."""

def main():
    reg = {"ping": lambda: "pong", "add": lambda a=2, b=3: a + b}
    print(reg["ping"](), reg["add"]())

if __name__ == "__main__":
    main()
