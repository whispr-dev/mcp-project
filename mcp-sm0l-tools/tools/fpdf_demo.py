"""fpdf2 minimal PDF generation demo"""

def main():
    try:
        import tempfile, pathlib
    from fpdf import FPDF
    except Exception as e:
        print("Missing dependency or import failed:", e)
        return
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=14)
    pdf.cell(0, 10, "sm0l pdf", ln=1)
    p = pathlib.Path(tempfile.gettempdir())/"sm0l_demo.pdf"
    pdf.output(str(p))
    print("wrote", p)

if __name__ == "__main__":
    main()
