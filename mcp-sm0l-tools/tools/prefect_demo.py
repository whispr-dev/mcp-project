from __future__ import annotations

try:
    from prefect import flow, task
except ImportError:
    print("Missing dependency: prefect. Install with: pip install prefect")
    raise SystemExit(0)

@task
def extract():
    return [1, 2, 3]

@task
def transform(xs):
    return [x * 10 for x in xs]

@flow
def etl():
    return transform(extract())

if __name__ == "__main__":
    print("ETL result:", etl())
