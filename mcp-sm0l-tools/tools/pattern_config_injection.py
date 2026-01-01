"""Configuration injection pattern (stdlib-only)."""

from dataclasses import dataclass

@dataclass(frozen=True)
class Cfg:
    scale: float = 1.0

def compute(x: float, cfg: Cfg) -> float:
    return x * cfg.scale

def main():
    print(compute(3, Cfg(scale=2.5)))

if __name__ == "__main__":
    main()
