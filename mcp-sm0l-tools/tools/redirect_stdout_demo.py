from __future__ import annotations
import io
from contextlib import redirect_stdout

def noisy():
    print("alpha")
    print("beta")

if __name__ == "__main__":
    buf = io.StringIO()
    with redirect_stdout(buf):
        noisy()
    print("captured:", buf.getvalue().strip().replace("\n", "|"))
