# src/extract.py

import fitz  # PyMuPDF for PDF
import docx  # python-docx for DOCX
import os

def extract_text(file_path):
    """
    Main function to detect file type and extract text.
    Supports PDF, DOCX, and TXT files.
    """
    _, file_extension = os.path.splitext(file_path)

    if file_extension.lower() == '.pdf':
        return extract_pdf(file_path)
    elif file_extension.lower() == '.docx':
        return extract_docx(file_path)
    elif file_extension.lower() == '.txt':
        return extract_txt(file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_extension}")

def extract_pdf(file_path):
    """
    Extract text from a PDF file using PyMuPDF
    """
    try:
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        print(f"Error extracting PDF: {e}")
        return ""

def extract_docx(file_path):
    """
    Extract text from a DOCX file using python-docx
    """
    try:
        doc = docx.Document(file_path)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text
    except Exception as e:
        print(f"Error extracting DOCX: {e}")
        return ""

def extract_txt(file_path):
    """
    Extract text from a TXT file
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except Exception as e:
        print(f"Error extracting TXT: {e}")
        return ""

if __name__ == "__main__":
    file_path = input("Enter the file path: ")
    extracted_text = extract_text(file_path)
    print(extracted_text)