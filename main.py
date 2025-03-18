from fastapi import FastAPI, UploadFile, File
import shutil
from src.extract import extract_text
from src.summarize import summarize_text
from src.generate_report import generate_report

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Document Automation Agent API"}

@app.post("/process/")
async def process_document(file: UploadFile = File(...)):
    # Step 1: Save the uploaded file to disk
    file_location = f"data/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Step 2: Extract text
    extracted_text = extract_text(file_location)
    if not extracted_text:
        return {"error": "Failed to extract text from the document."}

    # Step 3: Summarize
    summary = summarize_text(extracted_text)
    if not summary:
        return {"error": "Failed to summarize the extracted text."}

    # Step 4: Generate report (optional return path or report content)
    report_output_path = f"outputs/{file.filename}_report.txt"
    generate_report(extracted_text, summary, report_output_path)

    return {
        "message": "Document processed successfully!",
        "summary": summary,
        "report_path": report_output_path
    }
