"""requests + BeautifulSoup HTML parse demo"""

def main():
    try:
        import requests
    from bs4 import BeautifulSoup
    except Exception as e:
        print("Missing dependency or import failed:", e)
        return
    html = requests.get("https://httpbin.org/html", timeout=5).text
    soup = BeautifulSoup(html, "html.parser")
    print("h1:", soup.find("h1").get_text(strip=True))

if __name__ == "__main__":
    main()
