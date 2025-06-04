import streamlit as st
import tempfile
import os
from extractPDF import getText, getImages

def process_pdf(uploaded_file):
    if uploaded_file is None:
        st.info("Upload a PDF to see extraction.")
        return None

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_pdf_path = os.path.join(temp_dir, uploaded_file.name)
        with open(temp_pdf_path, "wb") as f:
            f.write(uploaded_file.getvalue())

        st.write("Starting content extraction...")

        pdfText = getText(temp_pdf_path)
        pdfImages = getImages(temp_pdf_path, temp_dir)

        st.success("Extraction complete. Analyzing elements...")
        st.write(f"Extracted counts: Text={len(pdfText['text'])}, Images={len(pdfImages['images'])}")

        st.subheader("Extracted Content:")
        st.text_area("Sample Text", pdfText['text'], height=150)
        if len(pdfImages['images']):
            st.image(pdfImages['images'][0], caption="First extracted image")

        return {
            **pdfText,
            **pdfImages,
        } 