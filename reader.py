import PyPDF2

def pdf_chunk(pdf_file, limit=4000, overlap=10):
    chunks = []
    chunk = ""
    with open(pdf_file, "rb") as f:
        pdf = PyPDF2.PdfReader(f)
        for page in pdf.pages:
            text = page.extract_text()