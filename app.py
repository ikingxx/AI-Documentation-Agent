import streamlit as st
import os
from src.extract import extract_text
from src.summarize import summarize_text
from src.generate_report import generate_report

# Set up output directories
os.makedirs("data", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

st.set_page_config(page_title="Document Automation Agent", layout="centered")

# Title of the app
st.title("📄 Document Automation Agent")
st.markdown("Upload a document, extract its content, summarize it, and generate a report!")

# File uploader
uploaded_file = st.file_uploader("Upload your document (PDF or DOCX)", type=["pdf", "docx"])

if uploaded_file is not None:
    with st.spinner('Processing...'):
        # Save uploaded file to disk
        file_path = os.path.join("data", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success(f"File `{uploaded_file.name}` uploaded successfully!")

        # Step 1: Extract text
        extracted_text = extract_text(file_path)
        if not extracted_text:
            st.error("❌ Failed to extract text from the document.")
        else:
            st.subheader("📜 Extracted Text")
            st.text_area("Extracted Content", extracted_text, height=250)

            # Step 2: Summarize text
            summary = summarize_text(extracted_text)
            if not summary:
                st.error("❌ Failed to summarize the extracted text.")
            else:
                st.subheader("📝 Summary")
                st.text_area("Summary", summary, height=200)

                # Step 3: Generate report
                report_output_path = os.path.join("outputs", f"{uploaded_file.name}_report.txt")
                generate_report(extracted_text, summary, report_output_path)

                with open(report_output_path, "r") as file:
                    report_content = file.read()

                st.subheader("📑 Generated Report")
                st.text_area("Report Content", report_content, height=200)

                # Download button for report
                with open(report_output_path, "rb") as file:
                    btn = st.download_button(
                        label="📥 Download Report",
                        data=file,
                        file_name=f"{uploaded_file.name}_report.txt",
                        mime="text/plain"
                    )

st.markdown("---")
st.caption("🚀 Built with Streamlit | Document Automation Agent")
