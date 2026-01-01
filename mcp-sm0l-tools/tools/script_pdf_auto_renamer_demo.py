"""PDF auto-renamer core idea"""

def main():
    try:
        import pathlib, re
        from PyPDF2 import PdfReader
    except Exception as e:
        print("Missing dependency or import failed:", e)
        return
    p = pathlib.Path("sample.pdf")
if not p.exists():
    print("Place a PDF named sample.pdf next to this script.")
    return

r = PdfReader(str(p))
txt = (r.pages[0].extract_text() or "") if r.pages else ""
head = txt.strip().splitlines()[0][:40] if txt.strip() else "document"
key = re.sub(r"\W+", "_", head).strip("_") or "document"
print("suggested", f"{key}.pdf")


if __name__ == "__main__":
    main()
