from __future__ import annotations

try:
    from pywaffle import Waffle
    import matplotlib.pyplot as plt
except ImportError:
    print("Missing dependencies: pywaffle, matplotlib. Install with: pip install pywaffle matplotlib")
    raise SystemExit(0)

if __name__ == "__main__":
    fig = plt.figure(
        FigureClass=Waffle,
        rows=5,
        values={"Python": 50, "JS": 30, "C++": 20},
        legend={"loc": "upper left", "bbox_to_anchor": (1, 1)},
    )
    fig.suptitle("PyWaffle demo")
    plt.tight_layout()
    plt.show()
