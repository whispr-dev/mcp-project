from __future__ import annotations

try:
    import datashader as ds
    import datashader.transfer_functions as tf
    import pandas as pd
    import numpy as np
except ImportError:
    print("Missing dependency: datashader (and pandas/numpy). Install with: pip install datashader pandas numpy")
    raise SystemExit(0)

if __name__ == "__main__":
    n = 100_000
    df = pd.DataFrame({"x": np.random.randn(n), "y": np.random.randn(n)})
    canvas = ds.Canvas(plot_width=200, plot_height=200)
    agg = canvas.points(df, "x", "y")
    img = tf.shade(agg)
    print("Datashader image type:", type(img))
    try:
        img.to_pil().save("datashader_demo.png")
        print("Wrote datashader_demo.png")
    except Exception:
        pass
