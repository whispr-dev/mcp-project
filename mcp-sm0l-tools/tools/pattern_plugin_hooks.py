"""Dynamic plugin hooks pattern (stdlib-only)."""

def main():
    hooks = []

    def register(fn):
        hooks.append(fn)
        return fn

    @register
    def h1(x): return x + 1

    @register
    def h2(x): return x * 10

    x = 3
    for h in hooks:
        x = h(x)
    print(x)

if __name__ == "__main__":
    main()
