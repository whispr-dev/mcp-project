#!/usr/bin/env python3
"""Rich: Beautiful terminal output"""
try:
    from rich.console import Console
    from rich.table import Table
    c = Console()
    t = Table(title="Metrics")
    t.add_column("name"), t.add_column("value")
    t.add_row("requests/s", "2453")
    t.add_row("errors", "[red]0.3%[/red]")
    c.print(t)
except:
    print("Install: pip install rich")
print("✓ Rich: Terminal dashboards")
