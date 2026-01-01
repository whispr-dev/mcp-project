from __future__ import annotations

try:
    import typer
except ImportError:
    print("Missing dependency: typer. Install with: pip install typer")
    raise SystemExit(0)

app = typer.Typer(add_completion=False)

@app.command()
def greet(name: str = "world"):
    typer.echo(f"hello {name}")

if __name__ == "__main__":
    app()
