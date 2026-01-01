"""self-healing server monitor (one-shot core)"""

def main():
    try:
        import psutil, requests
    except Exception as e:
        print("Missing dependency or import failed:", e)
        return
    url = "https://httpbin.org/status/200"
ok = requests.get(url, timeout=5).status_code == 200
cpu = psutil.cpu_percent(interval=0.1)
print("http_ok", ok, "cpu%", cpu)


if __name__ == "__main__":
    main()
