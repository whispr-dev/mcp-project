#!/usr/bin/env python3
"""PyDeck: GPU maps with deck.gl"""
import numpy as np, pandas as pd
try:
    import pydeck as pdk
    gps = pd.DataFrame({
        'lon': np.random.uniform(-74, -73, 100),
        'lat': np.random.uniform(40, 41, 100),
    })
    layer = pdk.Layer("HexagonLayer", gps, get_position=["lon","lat"], radius=200)
    view = pdk.ViewState(latitude=40.71, longitude=-74, zoom=12)
    r = pdk.Deck(layers=[layer], initial_view_state=view)
    r.to_html("map.html")
except:
    print("Install: pip install pydeck")
print("✓ Geospatial hexbin maps")
