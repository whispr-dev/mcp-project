#!/usr/bin/env python3
"""Datashader: Render billions of points"""
import numpy as np, pandas as pd
try:
    import holoviews as hv
    from holoviews.operation.datashader import rasterize
    hv.extension('bokeh')
    data = pd.DataFrame({'x': np.random.randn(100000), 'y': np.random.randn(100000)})
    points = hv.Points(data, ['x','y'])
    agg = rasterize(points)
    hv.output(agg)
except:
    print("Install: pip install holoviews datashader bokeh")
print("✓ Datashader for massive point clouds")
