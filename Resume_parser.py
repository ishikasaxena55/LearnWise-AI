import streamlit as st
import fitz  # PyMuPDF

st.set_page_config(page_title="Resume Parser", page_icon="📄")

st.title("📄 Resume Parser")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    try:
        pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")

        text = ""

        for page in pdf:
            text += page.get_text()

        if text.strip():
            st.success("✅ Resume Parsed Successfully!")
            st.text_area("Extracted Resume Text", text, height=350)
        else:
            st.warning("⚠️ No text found. This PDF may be scanned.")

    except Exception as e:
        st.error(f"Error: {e}")