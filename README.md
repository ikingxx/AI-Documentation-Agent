# 📄 Document Automation Agent

An AI-powered tool that extracts text from documents, summarizes the content, and generates structured reports automatically.

## Table of Contents
1. [About](#about)
2. [Features](#features)
3. [Technologies](#technologies)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Project Structure](#project-structure)
7. [License](#license)

## About

Document Automation Agent is designed to:
- Extract text from PDF documents.
- Summarize long documents into concise content.
- Generate reports in `.txt` format.

It's built as a backend service using FastAPI.

## Technologies Used

- Python
- FastAPI (backend framework)
- PyMuPDF (text extraction from PDF)
- NLTK (summarization)
- Uvicorn (server)



## Installation

### 1. Clone the repository:
https://github.com/ikingxx/AI-Documentation-Agent


### 2. Create a virtual environment:
- If you're using `conda`:
- conda create -n doc-agent python=3.9 conda activate doc-agent


### 3. Install dependencies:
- pip install -r requirements.txt
---

### 4. **How to Run the Project**
- uvicorn app:app --reload

### Access the API:
Go to your browser: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

There you can:
- Upload documents
- Get extracted text, summary, and reports
