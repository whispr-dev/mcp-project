"""fastapi minimal app object"""

def main():
    try:
        from fastapi import FastAPI
    except Exception as e:
        print("Missing dependency or import failed:", e)
        return
    app = FastAPI()
    @app.get("/")
    def root(): return {"ok": True}
    print("FastAPI app ready. Run: uvicorn fastapi_app_demo:app --reload")

if __name__ == "__main__":
    main()
