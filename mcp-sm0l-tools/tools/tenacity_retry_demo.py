"""tenacity retry demo"""

def main():
    try:
        from tenacity import retry, stop_after_attempt, wait_fixed
    except Exception as e:
        print("Missing dependency or import failed:", e)
        return
    state = {"n":0}
    @retry(stop=stop_after_attempt(3), wait=wait_fixed(0.1))
    def flaky():
        state["n"] += 1
        if state["n"] < 3:
            raise RuntimeError("nope")
        return "ok"
    print(flaky())

if __name__ == "__main__":
    main()
