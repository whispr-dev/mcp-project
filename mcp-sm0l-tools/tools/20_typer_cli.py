#!/usr/bin/env python3
"""Typer: Build CLIs from functions"""
import typer
app = typer.Typer()
@app.command()
def hello(name: str):
    typer.echo(f"Hello {name}")
if __name__ == "__main__":
    app()
print("✓ typer: CLI with zero boilerplate")
