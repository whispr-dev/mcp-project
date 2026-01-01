"""youtube-search-python quick search demo"""

def main():
    try:
        from youtubesearchpython import VideosSearch
    except Exception as e:
        print("Missing dependency or import failed:", e)
        return
    s = VideosSearch("lofi", limit=1)
    r = s.result()
    print(r["result"][0]["title"])

if __name__ == "__main__":
    main()
