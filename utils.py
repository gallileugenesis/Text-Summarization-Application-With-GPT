import streamlit as st
import docx
import PyPDF2


def text_extractor(uploaded_file):
    with st.spinner("Extraindo conteúdo do arquivo..."):
        text = None
        file_extension = uploaded_file.name.split('.')[-1].lower()

        if file_extension == "txt":
            # For plain text files
            text = uploaded_file.read().decode('utf-8')
        elif file_extension == "pdf":
            # For PDF files
            pdf_reader = PyPDF2.PdfFileReader(uploaded_file)
            text = ""
            for page_num in range(pdf_reader.numPages):
                text += pdf_reader.getPage(page_num).extractText()
        elif file_extension == "docx":
            # For Word documents
            doc = docx.Document(uploaded_file)
            text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
        else:
            st.error("Arquivo não suportado!", icon=None)

        if text is not None:
            st.success('Texto extraído com sucesso!', icon="✅")

    return text