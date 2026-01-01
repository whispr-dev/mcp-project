from __future__ import annotations

try:
    from fastapi import FastAPI
except ImportError:
    print("Missing dependency: fastapi. Install with: pip install fastapi")
    raise SystemExit(0)

app = FastAPI(title="fastapi demo")

@app.get("/ping")
def ping():
    return {"ping": "pong"}

if __name__ == "__main__":
    print("App ready. Run with:")
    print("  uvicorn fastapi_demo:app --reload")
