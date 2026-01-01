"""asyncer asyncify demo"""

def main():
    try:
        import asyncio
    from asyncer import asyncify
    except Exception as e:
        print("Missing dependency or import failed:", e)
        return
    def cpu(x): return x*x
    async def run():
        f = asyncify(cpu)
        print(await f(5))
    asyncio.run(run())

if __name__ == "__main__":
    main()
