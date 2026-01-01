"""dagster minimal in-process job demo"""

def main():
    try:
        from dagster import op, job
    except Exception as e:
        print("Missing dependency or import failed:", e)
        return

    @op
    def answer():
        return 42

    @job
    def demo_job():
        answer()

    res = demo_job.execute_in_process()
    print("success", res.success)

if __name__ == "__main__":
    main()
