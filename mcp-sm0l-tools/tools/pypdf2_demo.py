"""PyPDF2 create + read"""

def main():
    try:
        import tempfile, pathlib
        from PyPDF2 import PdfWriter, PdfReader
    except Exception as e:
        print("Missing dependency or import failed:", e)
        return
    p = pathlib.Path(tempfile.gettempdir()) / "sm0l_pypdf2.pdf"
w = PdfWriter()
w.add_blank_page(width=72*8.5, height=72*11)
with open(p, "wb") as f:
    w.write(f)

r = PdfReader(str(p))
print("pages", len(r.pages), "path", p)


if __name__ == "__main__":
    main()
