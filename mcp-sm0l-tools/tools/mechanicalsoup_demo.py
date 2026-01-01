"""MechanicalSoup basic fetch demo"""

def main():
    try:
        import mechanicalsoup
    except Exception as e:
        print("Missing dependency or import failed:", e)
        return
    b = mechanicalsoup.StatefulBrowser()
    b.open("https://httpbin.org/forms/post")
    print("page title:", (b.get_current_page().title.string if b.get_current_page().title else "n/a"))

if __name__ == "__main__":
    main()
