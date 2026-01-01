from __future__ import annotations

try:
    import holoviews as hv
except ImportError:
    print("Missing dependency: holoviews. Install with: pip install holoviews")
    raise SystemExit(0)

if __name__ == "__main__":
    hv.extension("bokeh")
    curve = hv.Curve([(0,0), (1,1), (2,0)])
    print("HoloViews object:", curve)
    print("In notebooks, just display `curve`.")
