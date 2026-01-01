"""Guardian pattern: runtime interface guard (stdlib-only)."""

EXPECT = {"foo", "bar"}

class API:
    def foo(self): return 1
    def bar(self): return 2

def guard(cls, expect):
    have = {n for n in dir(cls) if not n.startswith("_")}
    missing = expect - have
    extra = have - expect
    if missing or extra:
        raise RuntimeError({"missing": sorted(missing), "extra": sorted(extra)})

def main():
    guard(API, EXPECT)
    print("ok")

if __name__ == "__main__":
    main()
