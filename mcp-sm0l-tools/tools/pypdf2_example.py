#!/usr/bin/env python3
"""PyPDF2 PDF manipulation example"""
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
import os

# Merge PDFs
def merge_pdfs():
    merger = PdfMerger()

    if os.path.exists("a.pdf") and os.path.exists("b.pdf"):
        merger.append("a.pdf")
        merger.append("b.pdf")
        merger.write("merged.pdf")
        print("✓ PDFs merged")
    else:
        print("Sample PDFs not found")

# Extract pages
def extract_pages(input_file, start, end):
    if not os.path.exists(input_file):
        print(f"File {input_file} not found")
        return

    reader = PdfReader(input_file)
    writer = PdfWriter()

    for i in range(start, min(end, len(reader.pages))):
        writer.add_page(reader.pages[i])

    output = f"extracted_{start}_{end}.pdf"
    with open(output, 'wb') as f:
        writer.write(f)
    print(f"✓ Extracted pages {start}-{end}")

# Rotate pages
def rotate_pdf(input_file, rotation=90):
    if not os.path.exists(input_file):
        print(f"File {input_file} not found")
        return

    reader = PdfReader(input_file)
    writer = PdfWriter()

    for page in reader.pages:
        page.rotate(rotation)
        writer.add_page(page)

    output = f"rotated_{rotation}_{os.path.basename(input_file)}"
    with open(output, 'wb') as f:
        writer.write(f)
    print(f"✓ Rotated PDF by {rotation}°")

if __name__ == "__main__":
    print("PDF operations available - provide actual PDF files to test")
