import streamlit as st
from summarizer.extractive import extractive_summary
from summarizer.abstractive import abstractive_summary
import PyPDF2

st.set_page_config(page_title="SmartDocSum", layout="centered")
st.title("📄 Smart Document Summarizer")
st.markdown("Supports both **Extractive** and **Abstractive** methods.")

uploaded_file = st.file_uploader("Upload a .txt or .pdf file", type=["txt", "pdf"])
method = st.radio("Select summarization method", ["Extractive", "Abstractive"])
num_sentences = st.slider("Extractive: Number of sentences", 1, 20, 5)

text = ""

if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = " ".join([page.extract_text() or "" for page in pdf_reader.pages])
    elif uploaded_file.type == "text/plain":
        text = uploaded_file.read().decode("utf-8")

if text:
    st.subheader("📑 Original Document")
    st.text_area("Document Content", text, height=300)

    if st.button("Generate Summary"):
        with st.spinner("Summarizing..."):
            if method == "Extractive":
                summary = extractive_summary(text, num_sentences=num_sentences)
            else:
                summary = abstractive_summary(text)

        st.success("✅ Summary Ready!")
        st.subheader("🧠 Summary")
        st.text_area("Summary", summary, height=200)
