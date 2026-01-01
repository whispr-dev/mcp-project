from __future__ import annotations

try:
    from flask import Flask
except ImportError:
    print("Missing dependency: flask. Install with: pip install flask")
    raise SystemExit(0)

app = Flask(__name__)

@app.get("/ping")
def ping():
    return "pong"

if __name__ == "__main__":
    app.run(port=5000)
