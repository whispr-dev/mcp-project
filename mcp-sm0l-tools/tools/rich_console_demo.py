"""rich console output demo"""

def main():
    try:
        from rich.console import Console
    from rich.table import Table
    except Exception as e:
        print("Missing dependency or import failed:", e)
        return
    c = Console()
    t = Table(title="sm0l table")
    t.add_column("k"); t.add_column("v")
    for k,v in {"a":1,"b":2}.items():
        t.add_row(k, str(v))
    c.print(t)

if __name__ == "__main__":
    main()
