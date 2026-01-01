from __future__ import annotations

try:
    from shapely.geometry import Point, Polygon
except ImportError:
    print("Missing dependency: shapely. Install with: pip install shapely")
    raise SystemExit(0)

if __name__ == "__main__":
    tri = Polygon([(0,0), (2,0), (1,2)])
    p = Point(1, 0.5)
    print("area:", tri.area)
    print("contains point:", tri.contains(p))
