"""Transaction wrapper pattern (stdlib-only)."""

from contextlib import contextmanager

@contextmanager
def transaction(state: dict):
    snap = state.copy()
    try:
        yield state
    except Exception:
        state.clear(); state.update(snap)
        raise

def main():
    s = {"balance": 10}
    try:
        with transaction(s) as st:
            st["balance"] -= 5
            raise RuntimeError("fail")
    except RuntimeError:
        pass
    print(s)

if __name__ == "__main__":
    main()
