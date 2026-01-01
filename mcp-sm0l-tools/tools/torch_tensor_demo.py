from __future__ import annotations

try:
    import torch
except ImportError:
    print("Missing dependency: torch. Install with: pip install torch")
    raise SystemExit(0)

if __name__ == "__main__":
    a = torch.tensor([[1., 2.],[3., 4.]])
    b = torch.ones_like(a)
    c = a @ b
    print("a:", a)
    print("c:", c)
    c.sum().backward() if c.requires_grad else None
