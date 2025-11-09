"""
PDFParserAgent: Extracts text from PDF files.
Stub for assignment structure.
"""


import pdfplumber

class PDFParserAgent:
    def __init__(self):
        pass

    def parse_pdf(self, pdf_path):
        """
        Extract text from a PDF file at pdf_path using pdfplumber.
        Returns the extracted text as a string.
        """
        try:
            with pdfplumber.open(pdf_path) as pdf:
                text = "\n".join(page.extract_text() or "" for page in pdf.pages)
            return text
        except Exception as e:
            print(f"Error parsing {pdf_path}: {e}")
            return ""
