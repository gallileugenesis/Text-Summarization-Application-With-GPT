import streamlit as st
from summarizer_model import generate_summarizer
from utils import text_extractor

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Carregar e exibir a imagem
image_path = 'images/header_image.png'  # Caminho para a imagem
st.image(image_path, use_column_width=True)

# Set the application title
st.title("Sumarizador de texto")

resume = """
Bem-vindo ao nosso Sumarizador de Texto alimentado por modelos ChatGPT!
Esta ferramenta foi desenvolvida para simplificar e agilizar o processo de resumir textos extensos. 
"""
st.markdown(f"<p style='text-align: justify;'>{resume}</p>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

#Selection box to select the summarization style
with col1:
    model = st.selectbox(
        "Escolha o modelo",
        (
            "gpt-3.5-turbo",
            "gpt-4",
            
        ),
    )

#Showing the current parameter used for the model 
with col2:
    person_type = st.selectbox(
        "Quem você gostaria que fizesse o resumo?",
        (   
            "Cientista",
            "Estudante universitário",
            "Aluno de ensino médio",
            "Dona de casa",
            "Aposentado",
            'Outro',
        ),
    )

    if person_type == 'Outro':
        person_type = st.text_input("Digite o tipo de pessoa:", "")

st.markdown("<h1 style='font-size: 20px;'>Ajuste os hiperparâmetros</h1>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    token = st.slider("Max Tokes", min_value=0.0, max_value=200.0, value=50.0, step=1.0)
    top_p = st.slider("Nucleus Sampling", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
with col2:
    f_pen = st.slider("Frequency Penalty", min_value=-1.0, max_value=1.0, value=0.0, step=0.01)
    temp = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.0, step=0.01)

col1, col2 = st.columns(2)

# Provide the input area for text to be summarized
input_text = st.text_area("Digite o texto que deseja resumir:", height=200)

# file upload area
uploaded_file = st.file_uploader("Ou, escolha um arquivo:", type=["txt", "pdf", "docx"])

# Creating button for execute the text summarization
if st.button("Sumarizar"):
    if uploaded_file is not None:
        input_text = text_extractor(uploaded_file)

    with st.spinner('Por favor, aguarde...'):
        st.write(generate_summarizer(model, token, temp, top_p, f_pen, input_text, person_type))
 