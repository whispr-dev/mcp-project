from __future__ import annotations
from dataclasses import dataclass, field

@dataclass
class Point:
    x: float
    y: float
    meta: dict = field(default_factory=dict)

if __name__ == "__main__":
    p = Point(1, 2, {"tag": "demo"})
    print(p)
