from __future__ import annotations

try:
    import plotext as plt
except ImportError:
    print("Missing dependency: plotext. Install with: pip install plotext")
    raise SystemExit(0)

if __name__ == "__main__":
    plt.clear_figure()
    plt.plot([1,2,3], [1,4,9], marker="dot")
    plt.title("Plotext demo")
    plt.show()
