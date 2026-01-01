"""prefect 2/3 minimal flow demo"""

def main():
    try:
        from prefect import flow, task
    except Exception as e:
        print("Missing dependency or import failed:", e)
        return
    @task
    def add(a,b): return a+b
    @flow
    def main_flow():
        return add(2,3)
    print("result", main_flow())

if __name__ == "__main__":
    main()
