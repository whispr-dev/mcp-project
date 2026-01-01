from __future__ import annotations

try:
    from rich.console import Console
    from rich.table import Table
except ImportError:
    print("Missing dependency: rich. Install with: pip install rich")
    raise SystemExit(0)

if __name__ == "__main__":
    c = Console()
    t = Table(title="Rich mini demo")
    for col in ("thing", "value"):
        t.add_column(col)
    t.add_row("status", "[green]ok[/green]")
    t.add_row("answer", "42")
    c.print(t)
