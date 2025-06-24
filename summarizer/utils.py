
import PyPDF2
import docx
from langdetect import detect

def extract_text_from_pdf(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ''
    for page in reader.pages:
        text += page.extract_text() or ''
    return text.strip()

def extract_text_from_txt(uploaded_file):
    return uploaded_file.read().decode('utf-8')

def extract_text_from_docx(uploaded_file):
    doc = docx.Document(uploaded_file)
    return '\n'.join([p.text for p in doc.paragraphs])

def detect_language(text):
    try:
        return detect(text)
    except:
        return "unknown"
