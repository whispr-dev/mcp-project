"""pyppeteer minimal headless launch"""

def main():
    try:
        import asyncio
    from pyppeteer import launch
    except Exception as e:
        print("Missing dependency or import failed:", e)
        return
    async def run():
        browser = await launch(headless=True, args=["--no-sandbox"])
        page = await browser.newPage()
        await page.goto("about:blank")
        print("ok")
        await browser.close()
    asyncio.run(run())

if __name__ == "__main__":
    main()
